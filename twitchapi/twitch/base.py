class BaseTwitch(object):
    def __init__(self, token=None):
        self.token = token
        self._r = rest.RestRequester('https://api.twitch.tv/kraken')

    @property
    def auth_headers(self):
        return {'Authorization':'OAuth %s' % self.token.access_token}

    def get(self, *args, **kwargs):
        if self.token:
            if 'headers' in kwargs:
                kwargs['headers'].update(self.auth_headers)
            else:
                kwargs['headers'] = self.auth_headers
        return self._r.get(*args, **kwargs)

    def post(self, *args, **kwargs):
        if self.token:
            if 'headers' in kwargs:
                kwargs['headers'].update(self.auth_headers)
            else:
                kwargs['headers'] = self.auth_headers
        return self._r.post(*args, **kwargs)

    def put(self, *args, **kwargs):
        if self.token:
            if 'headers' in kwargs:
                kwargs['headers'].update(self.auth_headers)
            else:
                kwargs['headers'] = self.auth_headers
        return self._r.put(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.token:
            if 'headers' in kwargs:
                kwargs['headers'].update(self.auth_headers)
            else:
                kwargs['headers'] = self.auth_headers
        return self._r.delete(*args, **kwargs)

    def head(self, *args, **kwargs):
        if self.token:
            if 'headers' in kwargs:
                kwargs['headers'].update(self.auth_headers)
            else:
                kwargs['headers'] = self.auth_headers
        return self._r.head(*args, **kwargs)


