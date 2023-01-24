<?php
// Imitating Writing version
// With the purpose of Emulate DragaliaLost.com/api/index.php functions
// --時無_ShiWu

// receive parameters
// priority: type > action > lang > article_id > priority_lower_than
$type=$_GET['type'];
$category_id = $_GET['category_id'];
$priority_lower_than = $_GET['priority_lower_than'];
$action = $_GET['action'];
$article_id = $_GET['article_id'];
$lang = $_GET['lang'];
$td = $_GET['td'];

// Return data
header('Content-Type:application/json');
$jsoncallback=htmlspecialchars($_REQUEST['jsoncallback']);
echo $jsoncallback . $json_data ;
?>