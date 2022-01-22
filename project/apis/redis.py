from project import cache


def set_redis_object(upload_id, redis_object):
    cache.set(upload_id, redis_object, timeout=86400)


def get_redis_object(upload_id):
    obj = cache.get(upload_id)
    return obj


def delete_redis_object(upload_id):
    cache.delete(upload_id)
