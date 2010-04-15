from functools import wraps
from redis import Redis

class Redisns(object):
    key_commands = [
                    'set',
                    '__setitem__',
                    'get',
                    '__getitem__',
                    'getset',
                    'incr',
                    'decr',
                    'exists',
                    'delete',
                    'get_type',
                    'keys',
                    'ttl',
                    'expire',
                    'push',
                    'llen',
                    'lrange',
                    'ltrim',
                    'lindex',
                    'pop',
                    'lset',
                    'lrem',
                    'sort',
                    'sadd',
                    'srem',
                    'spop',
                    'scard',
                    'sismember',
                    'smembers',
                    'srandmember',
                    'zadd',
                    'zrem',
                    'zrange',
                    'zrangebyscore',
                    'zcard',
                    'zscore',
                    'move'
                    ]
    mkeys_commands = [
                        'mget',
                        'rename',
                        'poppush',
                        'smove',
                        'sinter',
                        'sinterstore',
                        'sunion',
                        'sunionstore',
                        'sdiff',
                        'sdiffstore',
                    ]
    def __init__(self, namespace=None, *args, **kwargs):
        if namespace and not namespace.endswith(":"):
            namespace += ":"
        self.namespace = namespace
        self._db = Redis(*args, **kwargs)
    def __getattr__(self, attr):
        if not hasattr(self._db):
            raise AttributeError("'Redis' class has no attribute '%s'" % attr)
        @wraps(self._db.__getattribute__(attr))
        def missing_method(*args, **kwargs):
            args = list(args)
            if attr in Redisns.key_commands:
                args[0] = "{0}{1}".format(self.namespace, args[0])
            elif attr in Redisns.mkeys_commands:
                for arg in range(len(args)):
                    args[arg] = "{0}{1}".format(self.namespace, args[arg])
            return self._db.__getattribute__(attr)(*args, **kwargs)
        return missing_method
    def __getitem__(self, attr):
        return self.get(attr)
    def __setitem__(self, attr, value):
        return self.set(attr, value)
    def __delitem__(self, attr):
        return self.delete(attr)
