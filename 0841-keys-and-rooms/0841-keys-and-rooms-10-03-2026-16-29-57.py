# BFS 개선
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()
        keys = deque(rooms[0])
        visited.add(0)
        while len(keys) > 0:
            room_key = keys.popleft() 
            if room_key not in visited:
                visited.add(room_key)
                for rk in rooms[room_key]:
                    keys.append(rk)

        return len(visited) == len(rooms)
                


            
