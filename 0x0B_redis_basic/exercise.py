#!/usr/bin/env python3
"""Writing strings to Redis, Reading from Redis and recovering original type,
   Incrementing values, Storing lists, Retrieving lists"""
from typing import Union, Callable, Optional, Any
import redis
import uuid
from functools import wraps


def call_history(method: Callable) -> Callable:
    """Store the history of inputs and outputs for a particular function."""
    key = method.__qualname__
    inputs = f"{key}:inputs"
    outputs = f"{key}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Wrapped function to record inputs and outputs."""
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return result

    return wrapper


def count_calls(method: Callable) -> Callable:
    """Count how many times methods of the Cache class are called."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Wrapped function to increment the call count."""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """Cache class to interact with Redis."""

    def __init__(self) -> None:
        """Constructor - store an instance of the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key, store the input data in Redis, and return the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable[[bytes], Any]] = None
    ) -> Union[str, bytes, int, float, None]:
        """Retrieve data from Redis using a key and optionally apply a conversion function."""
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve and decode data from Redis as a string."""
        data = self._redis.get(key)
        return data.decode("utf-8") if data else None

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve and decode data from Redis as an integer."""
        data = self._redis.get(key)
        if data is None:
            return None
        try:
            return int(data.decode("utf-8"))
        except (ValueError, AttributeError):
            return 0


def replay(method: Callable) -> None:
    """Display the history of calls of a particular function."""
    key = method.__qualname__
    inputs = f"{key}:inputs"
    outputs = f"{key}:outputs"
    redis_instance = method.__self__._redis

    count = redis_instance.get(key).decode("utf-8")

    print(f"{key} was called {count} times:")

    input_list = redis_instance.lrange(inputs, 0, -1)
    output_list = redis_instance.lrange(outputs, 0, -1)
    redis_zipped = list(zip(input_list, output_list))

    for input_args, output_data in redis_zipped:
        args, data = input_args.decode("utf-8"), output_data.decode("utf-8")
        print(f"{key}(*{args}) -> {data}")
