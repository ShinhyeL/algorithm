
N = int(input())
#key에 튜플로 여러 인자를 주고
##전체를 시작 시간의 오름차순으로 정렬 한 뒤, 정렬된 리스트를 다시 끝나는 시간으로 오름차순 정렬 해주기
time = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x:(x[1], x[0]))
answer = 0
end = 0

for s, e in time:
    if s >= end:
        answer += 1
        end = e
print(answer)
