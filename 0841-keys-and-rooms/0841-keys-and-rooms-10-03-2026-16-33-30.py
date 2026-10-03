# BFS 개선, 좀 더 python 스러운 버전
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        keys = deque(rooms[0])
        visited = {0}
        while keys:
            room_key = keys.popleft() 
            if room_key not in visited:
                visited.add(room_key)
                keys.extend(rooms[room_key])

        return len(visited) == len(rooms)
                


            
