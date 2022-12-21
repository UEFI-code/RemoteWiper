<?php
$magicWord = 'WipeAllDataNow';
$fp = fopen('LetsWipe.html', 'w');
fwrite($fp, $magicWord);
fclose($fp);
echo 'OK';
?>