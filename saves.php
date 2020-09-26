<?php
srand(time());
function generate_key($length)
{
  $dict = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
  $l = strlen($dict);
  $s = '';
  for ($i = 0; $i < $length; $i++) {
    $s .= $dict[rand() % $l];
  }
  return $s;
}

function has_key($db, $key)
{
  $query = "SELECT COUNT(cle) AS nbr FROM saves WHERE cle = ?";
  $stmt = $db->prepare($query);
  $stmt->bind_param('s', $key);
  $stmt->execute();
  $res = $stmt->get_result();
  $row = $res->fetch_assoc();
  $stmt->close();
  return $row['nbr'] == 1;
}

function generate_unique_key($db, $length)
{
  do {
    $key = generate_key($length);
  } while (has_key($db, $key));
  return $key;
}

function insert_data($db, $user_name, $key, $value)
{
  // host_addr 	creation_date 	user_name 	update_date 	visible
  $query = "INSERT INTO saves (cle, valeur, can_save, host_addr, creation_date, user_name, update_date, visible) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
  $stmt = $db->prepare($query);
  $can_save = TRUE;
  $host_addr = $_SERVER['REMOTE_ADDR'];
  $creation_date = date('Y-m-d H:i:s');
  $visible = TRUE;
  $stmt->bind_param(
    'ssissssi',
    $key,
    $value,
    $can_save,
    $host_addr,
    $creation_date,
    $user_name,
    $creation_date,
    $visible
  );
  $stmt->execute();
  $aff_rows = $stmt->affected_rows;
  $stmt->close();
  return $aff_rows > 0;
}

function get_data_bykey($db, $key)
{
  $query = "SELECT * FROM saves WHERE cle = ?";
  $stmt = $db->prepare($query);
  $stmt->bind_param('s', $key);
  $stmt->execute();
  $res = $stmt->get_result();
  $row = $res->fetch_assoc();
  $stmt->close();
  return $row;
}

function update_data($db, $cle, $valeur) {
  $query = "UPDATE saves 
              valeur = ?, 
              host_addr = ?, 
              update_date = ? 
            WHERE cle = ?";
  $stmt = $db->prepare($query);
  $host_addr = $_SERVER['REMOTE_ADDR'];
  $update_date = date('Y-m-d H:i:s');
  $stmt->bind_param(
    'ssss',
    $valeur,
    $host_addr,
    $update_date,
    $cle
  );
  $stmt->execute();
  $aff_rows = $stmt->affected_rows;
  $stmt->close();
  return $aff_rows > 0;
}

/******************************************************************************/
date_default_timezone_set('Africa/Tunis');

$HOST = '127.0.0.1';
$USER = 'root';
$PWD = ''; // 'abdouda';
$DB = 'pages_contents';
$db = mysqli_connect($HOST, $USER, $PWD, $DB);
$request_method = $_SERVER['REQUEST_METHOD'];

if ($request_method === 'POST') {
  if (isset($_POST['user_name']) && isset($_POST['save'])) {
    $user_name = $_POST['user_name'];
    $value = $_POST['save'];
    $key = generate_unique_key($db, 10);
    $ok = insert_data($db, $user_name, $key, $value);
    echo json_encode(array('resultat' => 'ok', 'cle' => $key));
  } else {
    echo json_encode(array('resultat' => 'error', 'message' => 'user_name or save fields empty'));
  }
} else if ($request_method === 'GET') {
  if (isset($_GET['key'])) {
    $key = $_GET['key'];
    if (has_key($db, $key)) {
      $data = get_data_bykey($db, $key);
      if ($data['can_save'] == 0) {
        if (isset($_GET['user_name'])) {
          $key = generate_unique_key($db, 10);
          $user_name = $_GET['user_name'];
          $ok = insert_data($db, $user_name, $key, $data['valeur']);
          $data = get_data_bykey($db, $key);
        } else {
          echo json_encode(array('resultat' => 'error', 'message' => 'Indiquer le nom d\'utilisateur'));
          die();
        }
      }
      echo json_encode(array('resultat' => 'ok', 'data' => $data));
    }
  } else {
    echo json_encode(array('resultat' => 'error', 'message' => 'Indiquer une clé'));
  }
} else if ($request_method === 'PUT') {
  parse_str(file_get_contents('php://input'), $_PUT);
  if (isset($_PUT['cle']) && isset($_PUT['valeur'])) {
    $cle = $_PUT['cle'];
    $valeur = $_PUT['valeur'];
    if (has_key($db, $key)) {
      $data = get_data_bykey($db, $key);
    }
    if ($data['can_save'] == 0) {
      echo json_encode(array('resultat' => 'error', 'message' => 'Indiquer une clé valide'));
      return;
    }
    $ok = update_data($db, $cle, $valeur);
    echo json_encode(array('resultat' => 'ok', 'data' => 'Données mise à jour'));
  } else {
    echo json_encode(array('resultat' => 'error', 'message' => 'Indiquer une clé et une valeur'));
  }
}
