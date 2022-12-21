<?php
$magicWord = 'WipeAllDataNow';
$newPHPTxt = '<?php $fp = fopen(\'wipeFlag.txt\', \'w\'); fwrite($fp, \'1\'); fclose($fp); echo \'' . $magicWord . '\'; ?>';
# delete the old flag file
unlink('wipeFlag.txt');

# write the new PHP file that device will receive
$fp = fopen('LetsWipe.php', 'w');
fwrite($fp, $newPHPTxt);
fclose($fp);

# redirect to the status check page
header('Location: wipedChk.php');
?>