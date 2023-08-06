from redis import Redis

r: Redis = Redis(host='redis', port=6379, db=0)
