// types.ts

export interface RedisConfig {
  host: string;
  port: number;
  password?: string;
  db?: number;
}

export interface CacheConfig {
  redis: RedisConfig;
  ttl?: number;
  maxttl?: number;
}

export interface CacheOptions {
  prefix?: string;
  suffix?: string;
}

export type CacheValue = string | number | boolean | object | null;

export type CacheGetCallback = (err: Error | null, value: CacheValue) => void;

export type CacheSetCallback = (err: Error | null) => void;

export type CacheDelCallback = (err: Error | null) => void;