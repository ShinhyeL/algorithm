import sys
input = sys.stdin.readline

m,n = map(int, input().split())
snack = list(map(int, input().split()))

start = 1
end = int(1e9)
answer = 0

while start <= end:
    mid = (start+end)//2
    count = 0
    for s in snack:
        count += s//mid
    if count >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(answer)            