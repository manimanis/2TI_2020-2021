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

function update_data($db, $cle, $valeur)
{
  $query = "UPDATE saves 
            SET
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
// $PWD = '';
$PWD = 'abdouda';
$DB = 'pages_contents';
$db = mysqli_connect($HOST, $USER, $PWD, $DB);
$request_method = $_SERVER['REQUEST_METHOD'];

if ($request_method === 'POST') {
  $has_keys = isset($_POST['key']) && $_POST['key'] != '';
  if (isset($_POST['value'])) {
    $value = $_POST['value'];
    if (!$has_keys) {
      $key = generate_unique_key($db, 10);
      $user_name = $key;
      $ok = insert_data($db, $user_name, $key, $value);
    } else {
      $key = $_POST['key'];
      if (!has_key($db, $key)) {
        echo json_encode(array(
          'resultat' => 'error', 
          'message' => 'Clé invalide'
        ));
        die();
      }
    }
    $data = get_data_bykey($db, $key);
    // Cannot save over readonly data
    // Generate a new key and use the new one
    if ($data['can_save'] == 0) {
      $key = generate_unique_key($db, 10);
      $user_name = $key;
      $ok = insert_data($db, $user_name, $key, $value);
      $data = get_data_bykey($db, $key);
    } else if ($has_keys) {
      update_data($db, $key, $value);
      $data = get_data_bykey($db, $key);
    }
    echo json_encode(array(
      'resultat' => 'ok', 
      'data' => $data
    ));
  } else {
    echo json_encode(array(
      'resultat' => 'error', 
      'message' => 'valeur à insérer manquante'
    ));
  }
} else if ($request_method === 'GET') {
  if (isset($_GET['key'])) {
    $key = $_GET['key'];
    if (has_key($db, $key)) {
      $data = get_data_bykey($db, $key);
      echo json_encode(array(
        'resultat' => 'ok', 
        'data' => $data
      ));
    } else {
      echo json_encode(array(
        'resultat' => 'error', 
        'message' => 'Clé invalide'
      ));
    }
  } else {
    echo json_encode(array(
      'resultat' => 'error', 
      'message' => 'Indiquer une clé'
    ));
  }
}
