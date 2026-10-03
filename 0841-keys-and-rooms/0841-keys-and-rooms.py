# 841 Keys and Rooms 풀어볼게 풀어보고 있는데..
#   일단 생각의 흐름
#   1. 0번째 room에 가서 열쇠를 가져온다.
#   2. 그 가져온 key들을 가지고 방을 방문 한다. (기록)
#   3. 방문한 방들에 있는 key를 가지고 다시 2번 반복

#   그러면 ..
#   2번을 할려면 dict같은걸 하나두고
#   가져온 key를 받으면 dict에 0번방 방문 같은걸 기록하는 함수를 하나 둘 것 같고 그 함수를 내부적으로 또 호출해서, 왜냠 방문한곳에서 key가 있을거니까. 종료조건은 이미 방문 했던곳의 key를 받으면 종료
#   이렇게 되어야 겠네.
class Solution:
    visited = {}
    def checkVisit(self, rooms: list[list[int]], keys: list[int]) -> list[int]:
        for key in keys:
            if self.visited.get(key) is None:
                self.visited[key] = True
                self.checkVisit(rooms, rooms[key])
                
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        self.visited = {}
        keys = rooms[0]
        self.visited[0] = True
        self.checkVisit(rooms, keys)
        return len(self.visited) == len(rooms)
                


            
