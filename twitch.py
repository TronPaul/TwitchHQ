import rest

class TwitchToken(object):
    def __init__(self, access_token, scopes):
        self.access_token = access_token
        self.scopes = scopes

class UnauthorizedError(Exception):
    pass

class BaseTwitch(object):
    def __init__(self):
        self.token = None
        self.r = rest.RestRequester('https://api.twitch.tv/kraken')

    @property
    def auth_headers(self):
        return {'Authorization':'OAuth %s' % self.token.access_token}

class ChannelMixin(object):
    def channel(self, channel):
        return self.r.get('channels/%s' % channel)

    def my_channel(self):
        if not self.token or 'channel_read' not in self.token.scopes:
            raise UnauthorizedError('channel_read scope required')
        self.r.get('channel', headers=self.auth_header)

    def update_channel(self, channel, status=None, game=None):
        if not self.token or 'channel_editor' not in self.token.scopes:
            raise UnauthorizedError('channel_editor scope required')
        args = {}
        if status:
            args['status'] = status
        if game:
            args['game'] = game
        return self.r.put('channels/%s' % channel, args={'channel':args}, headers=self.auth_header)

    def run_commercial(self, length=None):
        if not self.token or 'channel_commercial' not in self.token.scopes:
            raise UnauthorizedError('channel_commercial scope required')
        args = None if not length else {}
        if length:
            args['length'] = length
        return self.r.post('channels/%s/commercial' % channel, args=args, headers=self.auth_header)

class GamesMixin(object):
    def top_games(self, limit=None, offset=None):
        args = None if not limit and not offset else {}
        if limit:
            args['limit'] = limit
        if offset:
            args['offset'] = offset
        return self.r.get('games/top', args=args)

class IngestsMixin(object):
    def ingests(self):
        return self.r.get('ingests')

class SearchMixin(object):
    def search_streams(self, queury, limit=None, offset=None):
        args = {'query':query}
        if limit:
            args['limit'] = limit
        if offset:
            args['offset'] = offset
        return self.r.get('search/streams', args=args)

    def search_games(self, query, live=None):
        args = {'query':query, 'type':suggest}
        if live:
            args['live'] = live
        return self.r.get('search/games', args=args)

class TeamsMixin(object):
    def teams(self, limit=None, offset=None):
        args = None if not limit and not offset else {}
        if limit:
            args['limit'] = limit
        if offset:
            args['offset'] = offset
        return self.r.get('teams', args=args)

    def team(self, team):
        return self.r.get('teams/%s' % team)

class UserMixin(object):
    def user(self, user):
        return self.r.get('users/%s' % user)

    def my_user(self):
        if not self.token or 'user_read' not in self.token.scopes:
            raise UnauthorizedError('user_read scope required')
        return self.r.get('user', headers=self.auth_header)

class VideosMixin(object):
    def video(self, video_id):
        return self.r.get('videos/%s' % video_id)

    def channel_videos(self, channel, limit=None, offset=None):
        args = None if not limit and not offset else {}
        if limit:
            args['limit'] = limit
        if offset:
            args['offset'] = offset
        return self.r.get('channels/%s/videos' % channel, args=args)

class TwitchAPI(BaseTwitch, ChannelMixin, GamesMixin, IngestsMixin,
        SearchMixin, TeamsMixin, UserMixin, VideosMixin):
    pass
