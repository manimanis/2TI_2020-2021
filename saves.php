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

function insert_data($db, $key, $value)
{
  $query = "INSERT INTO saves (cle, valeur, can_save) VALUES (?, ?, ?)";
  $stmt = $db->prepare($query);
  $can_save = TRUE;
  $stmt->bind_param('ssi', $key, $value, $can_save);
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

$HOST = '127.0.0.1';
$USER = 'root';
$PWD = 'abdouda';
$DB = 'pages_contents';
$db = mysqli_connect($HOST, $USER, $PWD, $DB);
$request_method = $_SERVER['REQUEST_METHOD'];

if ($request_method === 'POST' && isset($_POST['save'])) {
  $value = $_POST['save'];
  $key = generate_unique_key($db, 10);
  $ok = insert_data($db, $key, $value);
  echo json_encode(array('resultat' => 'ok', 'cle' => $key));
} else if ($request_method === 'GET' && isset($_GET['key'])) {
  $key = $_GET['key'];
  if (has_key($db, $key)) {
    $data = get_data_bykey($db, $key);
    if ($data['can_save'] == 0) {
      $key = generate_unique_key($db, 10);
      $ok = insert_data($db, $key, $data['valeur']);
      $data = get_data_bykey($db, $key);
    }
    echo json_encode(array('resultat' => 'ok', 'data' => $data));
  } else {
    echo json_encode(array('resultat' => 'error', 'message' => 'Clé introuvable'));
  }
} else if ($request_method === 'PUT') {
  parse_str(file_get_contents('php://input'), $_PUT);
  print_r($_PUT);
}
