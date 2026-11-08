class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 1. isConnected(adjacency matrix)를 graph(adjacency list)로 바꾸기
        n = 0
        graph = dict()
        for i in isConnected:
            for index, connection in enumerate(i):
                if not graph.get(n):
                    graph[n] = set()
                if connection == 1:
                    graph[n].add(index)
            n += 1
        
        visted = set()
        count = 0
        for city in range(len(isConnected)):
            if city in visted:
                continue
            visted.add(city)
            dq = deque([city])
            while dq:
                c = dq.popleft()
                for i in graph[c]:
                    if i in visted:
                        continue
                    visted.add(i)
                    dq.append(i)
            count += 1
        return count
                    
        

        


            
        
        


