# 841. Keys and Rooms 로 배우는 DFS와 BFS

2026-10-03, LeetCode [Graph Theory study plan](https://leetcode.com/studyplan/graph-theory/)의 첫 단원 Standard Traversal을 시작하면서 공부한 내용입니다.
그래프를 처음 보는 사람에게 설명한다고 생각하고 처음부터 순서대로 적었습니다.

## 1. 문제를 풀기 전에 알아야 할 것

### 그래프 용어

그래프는 점과 점을 잇는 선으로 이루어집니다.
점을 vertex(또는 node), 선을 edge라고 부릅니다.
edge에 방향이 있으면 directed graph, 방향이 없으면 undirected graph입니다.
출발한 곳으로 다시 돌아오는 경로는 cycle, 서로 이어져 있는 vertex 묶음 하나는 connected component라고 합니다.

### 그래프를 코드로 나타내는 방법

가장 많이 쓰는 형태는 adjacency list입니다.
vertex마다 이웃 vertex 목록을 들고 있는 구조이고 `graph[0] = [1, 2]`라면 0번에서 1번과 2번으로 갈 수 있다는 뜻입니다.
adjacency는 "인접"이라는 뜻이고 읽을 때는 d를 따로 소리 내지 않고 "어제이선시"에 가깝게 읽습니다.

LeetCode는 문제마다 그래프를 다른 모양으로 줘서 대부분의 문제는 입력을 adjacency list로 바꾸는 데서 시작합니다.

| 입력 모양 | 예시 | Standard Traversal 단원에서 나오는 문제 |
|---|---|---|
| adjacency matrix | `isConnected[i][j]` | 547 |
| adjacency list | `graph`, `rooms` | 797, 802, 841 |
| edge list | `[[a, b], ...]` | 1129, 1466, 1192 |
| 부모 배열 | `manager[i]` | 1376 |

### 그래프를 다 둘러보는 두 가지 방법

DFS와 BFS는 시작점에서 갈 수 있는 곳을 빠짐없이 한 번씩 방문하는 방법입니다.
둘의 차이는 방문하는 순서뿐입니다.
자세한 설명은 5장에서 841을 풀면서 합니다.
두 방법 모두 vertex와 edge를 한 번씩 보기 때문에 시간복잡도는 O(V+E)입니다.

### 단원 문제를 푸는 순서

이 단원은 문제가 8개입니다.
페이지에 나온 순서대로 풀면 두 번째에 802가 나오는데, directed graph에서 cycle을 찾아야 해서 처음에는 막히기 쉽습니다.
개념이 하나씩 늘어나도록 아래 순서로 풀기로 했습니다.

841 → 547 → 797 → 1376 → 1466 → 1129 → 802 → 1192

802는 topological sort를 쓰고 1192는 Tarjan의 bridge 알고리즘이 필요한 Hard 문제입니다.
두 문제는 같은 플랜의 Topological Sort 단원을 먼저 풀고 돌아와도 됩니다.

## 2. 841. Keys and Rooms

방이 n개 있고 0번 방만 열려 있습니다.
방에 들어가면 다른 방 열쇠가 몇 개 있고 열쇠 번호가 곧 열 수 있는 방 번호입니다.
`rooms[i]`는 i번 방에서 얻는 열쇠 목록입니다.
모든 방에 들어갈 수 있으면 `true`, 아니면 `false`를 반환합니다.

제약 조건은 방 개수가 2~1000개, 모든 방의 열쇠를 합친 개수가 최대 3000개입니다.

그래프로 바꿔 보면 방은 vertex, 열쇠는 directed edge입니다.
0번 방에 1번 열쇠가 있으면 0에서 1로 가는 edge가 있는 셈입니다.
결국 0번 vertex에서 출발해서 모든 vertex에 도달할 수 있는지 묻는 문제입니다.

### 첫 번째 풀이: 재귀

처음에는 이렇게 생각했습니다.
0번 방에 가서 열쇠를 가져온다.
가져온 열쇠로 방에 들어가고 방문했다고 기록한다.
들어간 방에서 또 열쇠가 나오니까 같은 일을 반복한다.
이미 방문한 방의 열쇠를 받으면 거기서 멈춘다.

같은 일을 반복하니 함수가 자기 자신을 부르는 재귀로 짰습니다.

```python
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
```

LeetCode에서는 0 ms로 통과했습니다.
이 생각의 흐름이 바로 DFS인데, 그건 5장에서 다시 보겠습니다.

## 3. 재귀가 터지는 입력

방 1000개가 0 → 1 → 2 → … → 999로 일렬로 이어진 입력을 넣어 보았습니다.

```python
rooms = [[i + 1] for i in range(999)] + [[]]
```

로컬 Python(3.9.6, 기본 설정)에서는 `RecursionError`가 났습니다.
왜 그런지 알려면 호출 횟수와 쌓인 깊이를 구분해야 합니다.

### 호출 횟수

`checkVisit`는 새 방에 들어갈 때마다 한 번 호출됩니다.
`[[1], [2], [3], []]`처럼 방이 4개면 4번입니다.
마지막 방의 열쇠 목록이 `[]`여도 그 방에 들어갈 때 `checkVisit(rooms, [])`가 한 번 불리기 때문에 3번이 아니라 4번입니다.
같은 규칙으로 방이 1000개면 1000번입니다.

### 쌓인 깊이

호출 횟수가 많다고 해서 바로 에러가 나지는 않습니다.
하나 부르고 끝내고 또 부르는 식이라면 call stack은 한 칸이면 충분합니다.
문제는 앞에서 부른 함수가 끝나지 않고 안쪽 호출이 돌아오기를 기다린다는 데 있습니다.

```
canVisitAllRooms
└ checkVisit(keys=[1])        ← 기다리는 중
  └ checkVisit(keys=[2])      ← 기다리는 중
    └ checkVisit(keys=[3])    ← 기다리는 중
      └ checkVisit(keys=[])   ← 지금 실행 중
```

일렬 입력에서는 모든 호출이 이렇게 겹겹이 쌓이므로 호출 횟수와 깊이가 같아집니다.
Python은 call stack에 frame을 기본 1000개까지만 허용합니다.
이 1000에는 `checkVisit`뿐 아니라 스크립트 자체와 `canVisitAllRooms`의 frame도 들어가서 실제로는 `checkVisit`가 998번째로 호출될 때 에러가 납니다.

```
스크립트 자체           1
canVisitAllRooms        1
checkVisit            998
----------------------------
합계                 1000  ← 한도
```

### 횟수와 깊이는 다르다

`[[1, 2, 3], [], [], []]`을 넣으면 0번 방의 `for` 문이 1번, 2번, 3번 방을 차례로 부릅니다.
1번 방의 호출은 2번 방을 부르기 전에 끝납니다.
그래서 호출은 4번이지만 동시에 쌓이는 깊이는 2입니다.

```
checkVisit(keys=[1, 2, 3])  # 호출 1번째, 깊이 1
  checkVisit(keys=[])       # 호출 2번째, 깊이 2
  checkVisit(keys=[])       # 호출 3번째, 깊이 2
  checkVisit(keys=[])       # 호출 4번째, 깊이 2
```

정리하면 호출 횟수는 방 개수가 정하고 깊이는 그래프 모양이 정합니다.
길게 이어진 그래프일수록 깊어집니다.
vertex가 수천 개를 넘는 문제에서는 재귀 대신 반복문으로 짜는 편이 안전합니다.

## 4. 두 번째 풀이: 재귀 없이

재귀는 "나중에 돌아와서 마저 볼 열쇠"를 call stack에 대신 기억해 줍니다.
그 목록을 list 하나로 직접 들고 있으면 재귀가 필요 없습니다.

```python
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
```

일렬로 이어진 방 1000개 입력도 `True`를 반환합니다.
다만 이 코드에는 문제가 두 가지 있었고 그 전에 DFS와 BFS를 먼저 짚고 넘어가겠습니다.

## 5. DFS와 BFS

아래 그래프로 설명하겠습니다.

```
        A
       / \
      B   C
     / \   \
    D   E   F
```

DFS(Depth-First Search, 깊이 우선 탐색)는 한 갈래를 막다른 곳까지 들어갔다가, 막히면 바로 전 갈림길로 돌아가 다음 갈래로 갑니다.
미로에서 벽에 닿을 때까지 한 길로 가 보고 막히면 되돌아오는 것과 같습니다.
방문 순서는 A B D E C F입니다.

BFS(Breadth-First Search, 너비 우선 탐색)는 시작점에서 가까운 곳부터 방문합니다.
거리 1인 곳을 다 본 다음에 거리 2로 넘어가는 식이라, 물결이 퍼지는 모양을 떠올리면 됩니다.
방문 순서는 A B C D E F입니다.
가까운 곳부터 방문하기 때문에 BFS로 처음 도착한 순간의 거리가 곧 최단 거리입니다.

여기에 자료구조 두 개가 짝을 이룹니다.
stack은 마지막에 넣은 것을 먼저 꺼내고 list의 뒤에서 꺼내는 것과 같습니다.
queue는 먼저 넣은 것을 먼저 꺼내고 list의 앞에서 꺼내는 것과 같습니다.

### 꺼내는 쪽만 바꿔 보기

`rooms = [[1, 2], [3], [4], [], []]`는 그림으로 그리면 이렇습니다.

```
        0
       / \
      1   2
      |   |
      3   4
```

같은 입력을 세 가지 방식으로 돌려서 방문 순서를 비교했습니다.

| 방식 | 방문 순서 | 이름 |
|---|---|---|
| list 앞에서 꺼냄 (queue) | 0 → 1 → 2 → 3 → 4 | BFS |
| list 뒤에서 꺼냄 (stack) | 0 → 2 → 4 → 1 → 3 | DFS |
| 재귀 | 0 → 1 → 3 → 2 → 4 | DFS |

같은 반복문이라도 queue를 쓰면 BFS, stack을 쓰면 DFS가 됩니다.
4장의 두 번째 풀이는 앞에서 꺼내므로 BFS입니다.

재귀가 DFS인 이유는 함수 호출이 call stack에 쌓이기 때문입니다.
가장 나중에 부른 함수가 가장 먼저 끝나니, 마지막에 넣은 것을 먼저 꺼내는 stack과 같은 일을 합니다.

stack 방식과 재귀는 둘 다 DFS인데 방문 순서가 다릅니다.
stack 방식은 0번 방의 열쇠 `[1, 2]`를 한꺼번에 넣고 뒤에서 꺼내므로 2가 먼저 나옵니다.
재귀는 `for key in keys`가 앞에서부터 돌아서 1번 방 쪽 갈래부터 끝까지 들어갑니다.
어느 갈래부터 들어가느냐만 다를 뿐입니다.
이 문제는 몇 개를 방문했는지만 보니까 순서가 달라도 답은 같습니다.

## 6. 두 번째 풀이의 문제 두 가지

### `keys = keys[1:]`는 비싸다

`keys[1:]`는 첫 원소를 뺀 나머지 전부를 새 list에 복사합니다.
한 번 실행에 남은 원소 수만큼 일을 하고 이 줄이 `while` 문 안에서 열쇠마다 한 번씩 실행됩니다.
열쇠가 K개면 전체 비용은 O(K²)이 됩니다.

Python list는 뒤에서 꺼내는 것은 싸고 앞에서 꺼내는 것은 비쌉니다.
앞에서 싸게 꺼내야 할 때는 `collections.deque`를 씁니다.
`popleft()`는 한 번에 O(1)이라 전체 비용이 O(K)로 줄어듭니다.

LeetHub 기록에도 차이가 그대로 남았는데 `keys[1:]` 버전은 6 ms(하위 5%), `deque` 버전은 0 ms였습니다.

### 입력이 바뀐다

`rooms = [[1, 2], [3], [4], [], []]`로 두 번째 풀이를 돌리고 나니 `rooms[0]`이 `[1, 2, 3]`으로 바뀌어 있었습니다.

Python에서 `=`는 값을 복사하지 않고 이미 있는 객체에 이름을 하나 더 붙일 뿐입니다.

```python
a = [1, 2]
b = a
b.append(3)
print(a)      # [1, 2, 3]  a와 b는 같은 list

b = b[1:]
b.append(4)
print(a)      # [1, 2, 3]  슬라이싱이 새 list를 만들어서 이제 둘은 따로
print(b)      # [2, 3, 4]
```

두 번째 풀이의 `keys = rooms[0]`도 `b = a`와 똑같아서 첫 번째 반복에서 `keys.append(3)`을 하면 `rooms[0]`에 3이 붙습니다.
첫 번째 반복이 끝날 때 `keys = keys[1:]`이 새 list를 만들기 때문에, 두 번째 반복부터는 `rooms[0]`이 바뀌지 않고 4도 붙지 않습니다.

### 그 밖에 손본 것

`visited`에는 값으로 늘 `True`만 넣었습니다.
있는지 없는지만 알면 되니 dict보다 set이 맞습니다.

`visited = {}`를 class 바로 아래에 두면 그 dict 하나를 모든 인스턴스가 같이 씁니다.
`canVisitAllRooms` 첫 줄의 `self.visited = {}`가 매번 새 dict를 만들어 줘서 겨우 문제가 없었던 것입니다.
그 줄을 지우면 앞 테스트에서 방문한 기록이 다음 테스트에 남습니다.
실제로 그 줄을 지우고 예제 두 개를 연달아 돌리면, `false`가 나와야 할 두 번째 예제가 `true`를 반환합니다.
첫 번째 예제에서 방문한 2번 방이 기록에 남아 있기 때문입니다.
앞에서 본 "같은 객체에 이름이 여러 개 붙는" 문제와 같은 이야기입니다.
함수 안 지역 변수로 두면 이런 걱정이 없습니다.

## 7. 최종 풀이

```python
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
```

`deque(rooms[0])`이 새 객체를 만들기 때문에 입력이 바뀌지 않습니다.
`popleft()`로 앞에서 싸게 꺼내고 `visited`는 함수 안의 set입니다.
LeetCode에서 0 ms로 통과했습니다.
`popleft()`를 `pop()`으로 바꾸면 뒤에서 꺼내게 되어 같은 코드가 DFS가 됩니다.

### visited는 넣을 때 검사하자

위 코드는 queue에서 꺼낼 때 방문 여부를 검사합니다.
넣을 때 검사하면 이미 방문한 방은 아예 queue에 넣지 않습니다.
`rooms = [[1, 2, 3], [2, 3], [3], []]`로 세어 보면, 꺼낼 때 검사하는 방식은 queue에 6개가 들어가고 넣을 때 검사하는 방식은 3개만 들어갑니다.

넣을 때 검사하면 vertex 하나가 queue에 최대 한 번만 들어가서 queue 크기가 V를 넘지 않습니다.
841에서는 답이 같지만 격자 문제나 최단 거리 문제에서는 이 차이가 커집니다.
BFS에서는 넣을 때 `visited`를 표시하는 것을 기본으로 기억해 둡니다.

## 8. 오늘 배운 것

재귀 DFS는 그래프가 길게 이어지면 call stack 한도에 걸립니다.
호출 횟수는 vertex 개수가 정하고 깊이는 그래프 모양이 정합니다.

재귀는 stack입니다.
stack을 쓰면 DFS, queue를 쓰면 BFS가 됩니다.

Python의 `=`는 복사가 아닙니다.
입력 list를 그대로 받아 쓰면 원본이 바뀔 수 있습니다.

list 앞에서 꺼내기(`keys[1:]`, `pop(0)`)는 비쌉니다.
queue는 `deque`로 씁니다.

BFS에서 `visited`는 queue에 넣을 때 표시합니다.

841을 그래프 용어로 바꾸면 방이 V, 열쇠가 E입니다.
최종 풀이의 시간복잡도는 DFS·BFS의 기본 비용인 O(V+E) 그대로입니다.

다음 문제는 547 Number of Provinces입니다.
841은 0번 방에서 한 번만 탐색을 시작하면 됐지만 547은 탐색을 여러 번 시작해야 합니다.
