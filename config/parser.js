const config = require('config');
const redis = require('redis');
const fs = require('fs');

class Parser {
  constructor() {
    this.config = config;
    this.redisClient = redis.createClient();
    this.configFile = 'config.json';
  }

  readConfig() {
    return new Promise((resolve, reject) => {
      fs.readFile(this.configFile, (err, data) => {
        if (err) {
          reject(err);
        } else {
          try {
            resolve(JSON.parse(data));
          } catch (e) {
            reject(e);
          }
        }
      });
    });
  }

  readRedisConfig() {
    return new Promise((resolve, reject) => {
      this.redisClient.get('config', (err, data) => {
        if (err) {
          reject(err);
        } else {
          try {
            resolve(JSON.parse(data));
          } catch (e) {
            reject(e);
          }
        }
      });
    });
  }

  parseConfig() {
    return Promise.all([this.readConfig(), this.readRedisConfig()])
     .then(([localConfig, redisConfig]) => {
        return { local: localConfig, redis: redisConfig };
      })
     .catch((err) => {
        throw err;
      });
  }
}

module.exports = Parser;