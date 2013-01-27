TwitchHQ
========

Python library for Twitch.tv

Library
-------

`TwitchAPI` at this time has a method for all of twitch.tv's endpoints apart from chat.

Command Line Tool
-----------------

To see available commands run `python twitch.py`.  For use with authentciation you must
[register the application](http://www.twitch.tv/settings?section=applications) on twitch.tv.
Then fill out the `.auth_settings` file with your settings (client\_id, client\_secret, etc).
See auth\_settings\_example for an example settings file.

Run `python twitch.py auth` to begin the authentication process.

Run `python twitch.py check` to check that your authentication is valid.

To update your channel run `python twitch.py update --status STATUS --game GAME CHANNEL`.
You do not need to specifiy both status and game, just one.  You must specify the channel
you are editing.
