import logging
import redis
from typing import Optional

def get_redis_connection(host: str, port: int, db: int = 0) -> Optional[redis.Redis]:
    try:
        return redis.Redis(host=host, port=port, db=db)
    except redis.ConnectionError as e:
        logging.error(f"Failed to connect to Redis: {e}")
        return None

def set_config_key(redis_client: redis.Redis, key: str, value: str) -> bool:
    try:
        redis_client.set(key, value)
        return True
    except redis.RedisError as e:
        logging.error(f"Failed to set config key: {e}")
        return False

def get_config_key(redis_client: redis.Redis, key: str) -> Optional[str]:
    try:
        return redis_client.get(key)
    except redis.RedisError as e:
        logging.error(f"Failed to get config key: {e}")
        return None

def delete_config_key(redis_client: redis.Redis, key: str) -> bool:
    try:
        redis_client.delete(key)
        return True
    except redis.RedisError as e:
        logging.error(f"Failed to delete config key: {e}")
        return False