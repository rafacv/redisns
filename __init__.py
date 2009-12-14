from redis import *

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
        def missing_method(*args, **kwargs):
            args = list(args)
            if attr in Redisns.key_commands:
                args[0] = "{0}{1}".format(self.namespace, args[0])
            elif attr in Redisns.mkeys_commands:
                for arg in range(len(args)):
                    args[arg] = "{0}{1}".format(self.namespace, args[arg])
            return self._db.__getattribute__(attr)(*args, **kwargs)
        missing_method.__doc__ = self._db.__getattribute__(attr).__doc__
        missing_method.__name__ = self._db.__getattribute__(attr).__name__
        missing_method.__dict__ = self._db.__getattribute__(attr).__dict__
        return missing_method
