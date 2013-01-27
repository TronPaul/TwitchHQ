TwitchHQ
========

Python library for Twitch.tv

Requirements
------------

* httplib2

Command Line Tool
-----------------

    twitch.py [-h] [--token-file TOKEN_FILE]
    [--auth-settings-file AUTH_SETTINGS_FILE] COMMAND

    commands:
    auth - authenticate with twitch.tv
    check - check that saved twitch.tv authentication is valid
    channel_info - print channel info
    update - update channel information

Currently you must register the application yourself on twitch.tv to use the command line
tool.  Go [here](http://www.twitch.tv/settings?section=applications) to do so.  Once the
application is registered copy the `client_id`, and `client_secret` from your application
settings page on twitch.tv to your `.auth_settings` file.  Follow `auth_settings_example`
for an example `.auth_settings` file.

Example usage:

    $ twitch.py check
    Not authenticated!

    $ twitch.py auth
    Navigate to: https://api.twitch.tv/kraken/oauth2/authorize?response_type=code&scope=channel_editor&scope=channel_read&redirect_uri=http%3A%2F%2Flocalhost&client_id=blahblahblahsecretstuff
    Args (copy the text after the ? in the url): code=blahblahblahblah&scope=channel_read

    $ twitch.py update --status 'TF2 Soap DM - Scout' my_channel

Library
-------

`TwitchAPI` at this time has a method for all of twitch.tv's endpoints apart from chat.
