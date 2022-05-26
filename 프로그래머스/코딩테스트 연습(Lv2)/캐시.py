"""
대소문자 구분 없다 -> lower()
캐시 queue 자료형과 유사
cahce안에 있다면 hit 1 , 제거하고 새로 다시 append
miss면 맨 앞 pop(0)하기
"""
def solution(cacheSize, cities):

    cache = []
    answer = 0

    for c in cities:
        c = c.lower()
        if cacheSize == 0:
            return len(cities) * 5

        else:
            if c in cache:
                answer += 1
                cache.remove(c)
                cache.append(c)
            else:
                answer += 5
                if cacheSize <= len(cache):
                    cache.pop(0)
                cache.append(c)







    return answer