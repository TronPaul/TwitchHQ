import rest
class BaseJustin(object):
    def __init__(self):
        self._r = rest.RestRequester('https://api.justin.tv/api')

class ChannelMixin(object):
    def channel_summary(self, channel_name):
        return self._r.get('stream/summary.json', args={'channel':channel_name})

class JustinAPI(BaseJustin, ChannelMixin):
    pass
