# - 재귀 호출은 "나중에 돌아와서 마저 볼 key"를 call stack에 대신 기억해 주는 것 이다. 그 목록을 내가 직접 list 하나로 들고 있으면 재귀가 꼭 필요할까?
class Solution:
    visited = {}

    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        self.visited = {}
        keys = rooms[0]
        self.visited[0] = True
        while len(keys) != 0:
            room_key = keys[0]
            if not self.visited.get(room_key):
                self.visited[room_key] = True
                for rk in rooms[room_key]:
                    keys.append(rk)
            keys = keys[1:]

        return len(self.visited) == len(rooms)
                


            
