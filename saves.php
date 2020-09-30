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

function insert_data($db, $user_name, $classname, $key, $value)
{
  // host_addr 	creation_date 	user_name 	update_date 	visible
  $query = "INSERT INTO saves (cle, valeur, can_save, host_addr, creation_date, user_name, classname, update_date, visible) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
  $stmt = $db->prepare($query);
  $can_save = TRUE;
  $host_addr = $_SERVER['REMOTE_ADDR'];
  $creation_date = date('Y-m-d H:i:s');
  $visible = TRUE;
  $stmt->bind_param(
    'ssisssssi',
    $key,
    $value,
    $can_save,
    $host_addr,
    $creation_date,
    $user_name,
    $classname,
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

function update_data($db, $cle, $valeur, $user_name = "", $classname = "")
{
  $host_addr = $_SERVER['REMOTE_ADDR'];
  $update_date = date('Y-m-d H:i:s');
  $data = array(
    'valeur' => $valeur,
    'host_addr' => $host_addr,
    'update_date' => $update_date
  );
  if ($user_name != "") {
    $data['user_name'] = $user_name;
  }
  if ($classname != "") {
    $data['classname'] = $classname;
  }
 
  $fields = "";
  foreach ($data as $key => $value) {
    if ($fields != "") $fields .= ", ";
    $fields .= "`".$key."` = '".mysqli_real_escape_string($db, $value)."'";
  }
  $query = "UPDATE saves SET $fields WHERE cle = '".mysqli_real_escape_string($db, $cle)."'";
  //echo $query;
  $res = $db->query($query) or die($db->error);
  return $res;
}

function extract_data($data)
{
  try {
    $arr = json_decode($data, TRUE);
    if (!$arr) {
      return array("");
    }
    return $arr;
  } catch (Exception $e) {
    return array("");
  }
}

function get_username($arr)
{
  if (key_exists('data', $arr) && key_exists('save-content-0', $arr['data'])) {
    return $arr['data']['save-content-0'];
  }
  return "";
}

function get_classname($arr)
{
  if (key_exists('data', $arr) && key_exists('save-content-1', $arr['data'])) {
    return $arr['data']['save-content-1'];
  }
  return "";
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
    $arr = extract_data($value);
    $user_name = get_username($arr);
    $classname = get_classname($arr);
    if ($has_keys) {
      $key = $_POST['key'];
      $has_keys = has_key($db, $key);
    } else {
      $key = generate_unique_key($db, 10);
      $user_name = ($user_name == "") ? $key : $user_name;
      $classname = ($classname == "") ? $key : $classname;
      $ok = insert_data($db, $user_name, $classname, $key, $value);
    }
    $data = get_data_bykey($db, $key);
    // Cannot save over readonly data
    // Generate a new key and use the new one
    if ($data['can_save'] == 0) {
      $key = generate_unique_key($db, 10);
      $user_name = $key;
      $ok = insert_data($db, $user_name, $classname, $key, $value);
      $data = get_data_bykey($db, $key);
    } else if ($has_keys) {
      update_data($db, $key, $value, $user_name, $classname);
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
