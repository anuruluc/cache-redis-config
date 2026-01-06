import logging
import os
import json
from typing import Dict, Any

logger = logging.getLogger(__name__)

def load_config(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"Config file not found: {file_path}")
        return {}
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse config file: {file_path}, error: {e}")
        return {}

def save_config(file_path: str, config: Dict[str, Any]) -> None:
    try:
        with open(file_path, 'w') as file:
            json.dump(config, file, indent=4)
    except Exception as e:
        logger.error(f"Failed to save config file: {file_path}, error: {e}")

def get_redis_config(config: Dict[str, Any]) -> Dict[str, Any]:
    return config.get('redis', {})

def get_cache_config(config: Dict[str, Any]) -> Dict[str, Any]:
    return config.get('cache', {})

def merge_configs(base_config: Dict[str, Any], override_config: Dict[str, Any]) -> Dict[str, Any]:
    merged_config = base_config.copy()
    merged_config.update(override_config)
    return merged_config

def main():
    config_file = os.environ.get('CONFIG_FILE', 'config.json')
    config = load_config(config_file)
    redis_config = get_redis_config(config)
    cache_config = get_cache_config(config)
    logger.info(f"Redis config: {redis_config}")
    logger.info(f"Cache config: {cache_config}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()