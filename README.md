
# AdServer Bot

A bot made to advertise in some servers, it will send the message you want, in multiple servers, or channels, with whatever cooldown you want.

# Setup

```
git clone https://github.com/Wikileas/AdServerBot/
pip install -r requirements.txt
cd AdServer
python3 AdServer.py
```

To stop the bot, you can either do a `KeyboardInterrupt` action (e.g CTRL+C) or write `:stop` in any server or channel.

# Commands

`start` - Starts the advertising.

`build` - Build the JSON structure, usage: `:build {channel_id} {cooldown} {message}`

`stop` - Stops the bot from advertising.
# Requirements

Python 3.8.0 or higher.


