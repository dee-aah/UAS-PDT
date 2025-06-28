import redis

r = redis.Redis(host='redis_perpus', port=6379, decode_responses=True)

r.set("book:1:available", 3)
r.set("book:2:available", 2)

print("Redis sudah diisi.")
