<?php
$fp = fopen('wipeFlag.txt', 'r');
if ($fp) {
    fclose($fp);
    unlink('LetsWipe.php');
    echo 'Congratulations! Your device succese recieve wipe signal!';
}
else {
    # refresh after 3 seconds
    header('Refresh: 3; URL=wipedChk.php');
    echo 'Your device is not recieved wipe signal yet.';
}