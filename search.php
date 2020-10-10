<?php

date_default_timezone_set('Africa/Tunis');

require_once 'config.php';

$db = mysqli_connect($HOST, $USER, $PWD, $DB);
$request_method = $_SERVER['REQUEST_METHOD'];
$pagename = isset($_GET['pagename']) ? $_GET['pagename'] : '';
$pagename = isset($_POST['pagename']) ? $_POST['pagename'] : $pagename;
$classname = isset($_POST['classname']) ? $_POST['classname'] : '';

function get_pagenames($db)
{
  $query = "SELECT DISTINCT(pagename) AS pagename FROM saves WHERE pagename <> '' AND pagename IS NOT NULL ORDER BY 1";
  $res = $db->query($query) or die($db->error);
  $arr = array();
  while ($row = $res->fetch_assoc()) {
    $arr[] = $row['pagename'];
  }
  return $arr;
}

function get_classnames($db)
{
  $query = "SELECT DISTINCT(classname) AS classname FROM saves WHERE classname <> '' AND pagename IS NOT NULL ORDER BY 1";
  $res = $db->query($query) or die($db->error);
  $arr = array();
  while ($row = $res->fetch_assoc()) {
    $arr[] = $row['classname'];
  }
  return $arr;
}

function find($db, $pagename, $classname)
{
  $query = "SELECT cle, user_name, creation_date, update_date 
            FROM saves
            WHERE pagename = '" . mysqli_real_escape_string($db, $pagename) . "' 
              AND classname = '" . mysqli_real_escape_string($db, $classname) . "'
            ORDER BY update_date DESC";
  $res = $db->query($query) or die($db->error);
  $arr = array();
  while ($row = $res->fetch_assoc()) {
    $arr[] = $row;
  }
  return $arr;
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Recherche</title>
  <link rel="stylesheet" href="styles/bootstrap.min.css">
</head>

<body>
  <main class="container">
    <h1>Recherche</h1>
    <form id="search" method="post">
      <div class="my-2">
        <label for="pagename">Projet</label>
        <select name="pagename" id="pagename" class="form-control">
          <?php
          $pagenames = get_pagenames($db);
          foreach ($pagenames as $page) {
            echo "<option" . (($pagename == $page) ? ' selected' : '') . ">$page</option>";
          }
          ?>
        </select>
      </div>
      <div class="my-2">
        <label for="classname">Classe</label>
        <select name="classname" id="classname" class="form-control">
          <?php
          $classnames = get_classnames($db);
          foreach ($classnames as $class) {
            echo "<option" . (($classname == $class) ? ' selected' : '') . ">$class</option>";
          }
          ?>
        </select>
      </div>
      <div class="my-2"><button class="btn btn-primary">Rechercher</button></div>
    </form>
    <?php
    if ($request_method == 'POST') :
    ?>
      <table class="table my-2">
        <thead>
          <tr>
            <th>Clé</th>
            <th>Utilisateur</th>
            <th>Création</th>
            <th>Mise à jour</th>
          </tr>
        </thead>
        <tbody>
          <?php
          $data = find($db, $_POST['pagename'], $_POST['classname']);
          foreach ($data as $row) :
          ?>
            <tr>
              <td><?= $row['cle'] ?></td>
              <td><?= $row['user_name'] ?></td>
              <td><?= $row['creation_date'] ?></td>
              <td><?= $row['update_date'] ?></td>
            </tr>
          <?php
          endforeach; // foreach($data as $row)
          ?>
        </tbody>
      </table>
    <?php
    endif; // if ($request_method == 'POST')
    ?>
  </main>
</body>

</html>