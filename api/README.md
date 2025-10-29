# cache-redis-config

A simple library for managing Redis cache configurations.

## Installation

```bash
npm install cache-redis-config
```

## Usage

```javascript
const { RedisConfigManager } = require('cache-redis-config');

async function main() {
  const configManager = new RedisConfigManager({
    host: 'localhost',
    port: 6379,
    password: 'your_redis_password', // Optional
    db: 0, // Optional
    defaultExpiration: 60, // Default expiration in seconds (optional)
  });

  try {
    await configManager.connect();
    console.log('Connected to Redis!');

    // Set a value with default expiration
    await configManager.set('myKey', 'myValue');

    // Set a value with custom expiration
    await configManager.set('anotherKey', 'anotherValue', 120);

    // Get a value
    const value = await configManager.get('myKey');
    console.log('Value for myKey:', value);

    // Check if a key exists
    const exists = await configManager.exists('myKey');
    console.log('myKey exists:', exists);

    // Delete a key
    await configManager.delete('myKey');

    // Get a value after deletion
    const valueAfterDeletion = await configManager.get('myKey');
    console.log('Value for myKey after deletion:', valueAfterDeletion);

    // Close the connection
    await configManager.disconnect();
    console.log('Disconnected from Redis.');

  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```

## API

### `RedisConfigManager(options)`

Constructor for the `RedisConfigManager` class.

**Options:**

*   `host` (string, required): Redis host.
*   `port` (number, required): Redis port.
*   `password` (string, optional): Redis password. Defaults to no password.
*   `db` (number, optional): Redis database. Defaults to 0.
*   `defaultExpiration` (number, optional): Default expiration time in seconds for cached items. Defaults to no expiration.

### `connect()`

Establishes a connection to the Redis server. Returns a Promise.

### `disconnect()`

Closes the connection to the Redis server. Returns a Promise.

### `set(key, value, expiration)`

Sets a key-value pair in Redis with optional expiration. Returns a Promise.

**Parameters:**

*   `key` (string, required): The key to set.
*   `value` (any, required): The value to set.  Will be serialized as JSON.
*   `expiration` (number, optional): Expiration time in seconds. If not provided, uses the `defaultExpiration` from the constructor. If `defaultExpiration` is also not set, the key will not expire.

### `get(key)`

Gets the value associated with a key from Redis. Returns a Promise that resolves with the value or `null` if the key does not exist.  Deserializes the value from JSON.

**Parameters:**

*   `key` (string, required): The key to retrieve.

### `exists(key)`

Checks if a key exists in Redis. Returns a Promise that resolves with a boolean.

**Parameters:**

*   `key` (string, required): The key to check.

### `delete(key)`

Deletes a key from Redis. Returns a Promise.

**Parameters:**

*   `key` (string, required): The key to delete.

## Error Handling

The methods `connect`, `set`, `get`, `exists`, and `delete` return Promises that reject if an error occurs during the Redis operation.

## Contributing

Contributions are welcome! Please submit a pull request.

## License

MIT