# redisns

Requires [redis-py](http://github.com/andymccurdy/redis-py) module.

Inspired by [redis-namespace](http://github.com/defunkt/redis-namespace/) from Chris Wanstrath.

    >>> from redisns import Redisns
    >>> db = Redisns('MyApp::v1', host="127.0.0.1", port=6379)

    >>> db.set("user1", "John Doe")
    'OK'
    >>> print db.get("user1")
    u'John Doe'

Would be translated into:

    >>> db.set("MyApp::v1:user1", "John Doe")
    'OK'
    >>> print db.get("MyApp::v1:user")
    u'John Doe'

# author

Rafael Valverde, rafacvo@gmail.com