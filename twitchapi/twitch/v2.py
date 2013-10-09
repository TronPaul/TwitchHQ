import twitchapi.rest as rest
import twitchapi.twitch.base as base

class TwitchToken(object):
    def __init__(self, access_token, scopes):
        self.access_token = access_token
        self.scopes = scopes

class UnauthorizedError(Exception):
    pass

class ChannelMixin(object):
    def channel(self, channel):
        return self._r.get('channels/%s' % channel)

    def my_channel(self):
        if not self.token or 'channel_read' not in self.token.scopes:
            raise UnauthorizedError('channel_read scope required')
        return self._r.get('channel', headers=self.auth_headers)

    def update_channel(self, channel, status=None, game=None):
        if not self.token or 'channel_editor' not in self.token.scopes:
            raise UnauthorizedError('channel_editor scope required')
        args = {}
        if status:
            args['channel[status]'] = status
        if game:
            args['channel[game]'] = game
        return self._r.put('channels/%s' % channel,
                args=args,
                headers=self.auth_headers)

    def run_commercial(self, length=None):
        if not self.token or 'channel_commercial' not in self.token.scopes:
            raise UnauthorizedError('channel_commercial scope required')
        args = None if not length else {}
        if length:
            args['length'] = length
        return self._r.post('channels/%s/commercial' % channel, args=args,
                headers=self.auth_headers)

class GamesMixin(object):
    def top_games(self, limit=None, offset=None):
        args = None if not limit and not offset else {}
        if limit:
            args['limit'] = limit
        if offset:
            args['offset'] = offset
        return self._r.get('games/top', args=args)

class IngestsMixin(object):
    def ingests(self):
        return self._r.get('ingests')

class SearchMixin(object):
    def search_streams(self, queury, limit=None, offset=None):
        args = {'query':query}
        if limit:
            args['limit'] = limit
        if offset:
            args['offset'] = offset
        return self._r.get('search/streams', args=args)

    def search_games(self, query, live=None):
        args = {'query':query, 'type':suggest}
        if live:
            args['live'] = live
        return self._r.get('search/games', args=args)

class TeamsMixin(object):
    def teams(self, limit=None, offset=None):
        args = None if not limit and not offset else {}
        if limit:
            args['limit'] = limit
        if offset:
            args['offset'] = offset
        return self._r.get('teams', args=args)

    def team(self, team):
        return self._r.get('teams/%s' % team)

class UserMixin(object):
    def user(self, user):
        return self._r.get('users/%s' % user)

    def my_user(self):
        if not self.token or 'user_read' not in self.token.scopes:
            raise UnauthorizedError('user_read scope required')
        return self._r.get('user', headers=self.auth_headers)

class VideosMixin(object):
    def video(self, video_id):
        return self._r.get('videos/%s' % video_id)

    def channel_videos(self, channel, limit=None, offset=None):
        args = None if not limit and not offset else {}
        if limit:
            args['limit'] = limit
        if offset:
            args['offset'] = offset
        return self._r.get('channels/%s/videos' % channel, args=args)

class TwitchAPI(base.BaseTwitch, ChannelMixin, GamesMixin, IngestsMixin,
        SearchMixin, TeamsMixin, UserMixin, VideosMixin):
    pass
