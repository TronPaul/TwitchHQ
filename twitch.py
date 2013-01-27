#! /usr/bin/python
import re
import argparse
import urllib
import json
import os
from twitchapi import TwitchAPI
from twitchapi.twitch import TwitchToken

TOKEN_FILE='.access_token'
AUTH_SETTINGS_FILE='.auth_settings'

args_pattern = re.compile(r'code=(?P<code>.*?)&scope=(?P<scopes>.*?)')

def get_auth_settings(auth_settings_file):
    fp = open(auth_settings_file)
    return json.load(fp)

def auth_url(client_id, redirect_uri, scopes):
    base_url = (u'https://api.twitch.tv/kraken/oauth2/authorize'
        u'?response_type=code')
    return base_url + u'&' + urllib.urlencode({'client_id':client_id,
        'redirect_uri':redirect_uri, 'scope':scopes}, True)

def make_token(token_file):
    if os.path.isfile(token_file):
        json_token = json.load(open(token_file))
        return TwitchToken(json_token['access_token'],
            json_token['scope'])
    return None

def make_client(token_file):
    return TwitchAPI(make_token(token_file))

def clear_token(token_file):
    if os.path.isfile(token_file):
        os.remove(token_file)

def prompt(name, default=None):
    prompt = name + (default and ' [%s]' % default or '')
    prompt += name.endswith('?') and ' ' or ': '
    while True:
        rv = raw_input(prompt)
        if rv:
            return rv
        if default is not None:
            return default

def auth(twitch_client, token_file, auth_settings_file):
    auth_settings = get_auth_settings(auth_settings_file)
    print 'Navigate to: %s' % auth_url(auth_settings['client_id'],
            auth_settings['redirect_uri'], auth_settings['scopes'])
    args = {}
    while not args:
        args_text = urllib.unquote(
                prompt('Args (copy the text after the ? in the url)'))
        m = args_pattern.match(args_text)
        if m:
            args['code'] = m.group('code')
            args['scopes'] = m.group('scopes').split()
    args = {
            'client_id':auth_settings['client_id'],
            'client_secret':auth_settings['client_secret'],
            'grant_type':'authorization_code',
            'redirect_uri':auth_settings['redirect_uri'],
            'code':args['code']
           }
    resp, con = twitch_client.post('oauth2/token', args=args)
    token = json.loads(con)
    clear_token(token_file)
    json.dump(token, open(TOKEN_FILE, 'w'))

def check(twitch_client, token_file):
    if os.path.isfile(token_file):
        resp, con = twitch_client.get('/')
        d = json.loads(con)
        if d['token']['valid']:
            print ('Authenticated! Scopes: %s' %
                d['token']['authorization']['scopes'])
            return
    print 'Not authenticated!'
    clear_token(token_file)

def update(twitch_client, channel, status, game):
    resp, con = twitch_client.update_channel(channel, status, game)
    if resp.status != 200:
        print 'Error occurred!'
        print resp, con
    else:
        print 'Update successful.'

def channel_info(twitch_client):
    print twitch_client.my_channel()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--token-file', default=TOKEN_FILE, dest='token_file')
    parser.add_argument('--auth-settings-file', default=AUTH_SETTINGS_FILE,
            dest='auth_settings_file')
    subparsers = parser.add_subparsers(dest='subparser_name')

    auth_parser = subparsers.add_parser('auth')
    check_parser = subparsers.add_parser('check')
    up_parser = subparsers.add_parser('update')
    up_parser.add_argument('channel', type=str)
    up_parser.add_argument('--status', type=str)
    up_parser.add_argument('--game', type=str)
    channel_info_parser = subparsers.add_parser('channel_info')

    args = parser.parse_args()
    twitch_client = make_client(args.token_file)
    if args.subparser_name == 'auth':
        auth(twitch_client, args.token_file, args.auth_settings_file)
    elif args.subparser_name == 'check':
        check(twitch_client, args.token_file)
    elif args.subparser_name == 'update':
        if args.game or args.status:
            update(twitch_client, args.channel, args.status, args.game)
    elif args.subparser_name == 'channel_info':
        channel_info(twitch_client)
