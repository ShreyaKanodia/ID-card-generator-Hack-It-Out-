<?php
include('phpqrcode/qrlib.php');


header("content-type: image/jpg");
$file_name='gd-template.jpg';
require 'config-pdo.php';
$sql="SELECT * FROM registration";
foreach($dbo->query($sql) as $row ){
  //echo "$row[name]<br>";
$x=250; // Horizontal postion to add name
$y=330; // vertical
$img_source=imagecreatefromjpeg($file_name);
/// adding name ///
$text_color=imagecolorallocate($img_source,0,0,255);
ImageString($img_source,5,$x,$y,$row['name'],$text_color);
// adding class ///
$y=390; // vertical
ImageString($img_source,5,$x,$y,$row['email'],$text_color);
// adding mark ///
$y=425; // vertical
ImageString($img_source,5,$x,$y,$row['contact'],$text_color);
$y=455; // vertical
ImageString($img_source,5,$x,$y,$row['gender'],$text_color);
$y=425;
$x=700;
ImageString($img_source,5,$x,$y,$row['id_number'],$text_color);


// $text=$row->id_number;
$text=$row['id_number'];


$path='images/';

$file= $path.$text.".png";

QRcode::png($text,$file);



$str=imagecreatefrompng("$file");
imagecopy($img_source,$str,500,390,0,0,200,200);

//end ///
imagejpeg($img_source,"outputs/$row[id_number].jpg");
// imagedestroy($img_source);
}
?>
