<?php
$HOST = '127.0.0.1';
$USER = 'root';
// $PWD = '';
if (file_exists('sentinel.txt')) {
    $PWD = 'mysqlroot';
} else {
    $PWD = 'abdouda';
}
$DB = 'pages_contents';