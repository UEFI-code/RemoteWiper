# Remote Wiper Client for macOS

## Features

### iCloud Fire Supported

Checkout the ```magicWord``` varible in the code.

You can use another client create a file or folder name as this magicWord, then when you Mac sync it will wipe all data under /Users.

### Private Web Server Supported

Also the ```magicWord``` varible in the code.

Additional you need setup the ```webHooks``` arrays that points to your server.

## How to Build & Run

```bash
pip3 install -r requirement.txt
sudo python3 wiper.py
```

## Notice

There maybe some code Commentted for security reason during develop. Please remove those Comment to make the Wipe Work!