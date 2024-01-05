#q.pop대신 import deque. 시간 복잡도 낮은 popleft()사용
from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]#초기값을 false로 만들어 그래프 선언

#연결된 정점을 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

#방문 유무를 담는 리스트 visited. N+1사용 이유는 0번째 인덱스를 사용하지 않기 위해서    
visited1 = [False] * (N + 1)  # dfs의 방문기록
visited2 = [False] * (N + 1)  # bfs의 방문기록


def dfs(V):
    visited1[V] = True  # 해당 V값 방문처리
    print(V, end=" ") #방문 후 정점 출력
    for i in range(1, N + 1):
        if not visited1[i] and graph[V][i]:  # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
            dfs(i)  # 해당 i 값으로 dfs를 돈다.(더 깊이 탐색)
     
def bfs(V):
    q = deque([V])  # pop메서드의 시간복잡도가 낮은 덱 내장 메서드를 이용한다
    visited2[V] = True  # 해당 V 값을 방문처리
    while q:  # q가 빌때까지 돈다.
        V = q.popleft()  # 큐에 있는 첫번째 값 꺼낸다.
        print(V, end=" ")  # 해당 값 출력
        for i in range(1, N + 1):  # 1부터 N까지 돈다
            if not visited2[i] and graph[V][i]:  # 만약 해당 i값을 방문하지 않았고 V와 연결이 되어 있다면
                q.append(i)  # 그 i 값을 추가
                visited2[i] = True  # i 값을 방문처리

dfs(V)
print()
bfs(V)
