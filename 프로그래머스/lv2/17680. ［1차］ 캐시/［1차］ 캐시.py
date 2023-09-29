def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    cache = []
    time = 0
    for city in cities:
        if city.lower() in cache:
            cache.remove(city.lower())
            cache.append(city.lower())
            time += 1
        else:
            time += 5
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city.lower())
    return time
