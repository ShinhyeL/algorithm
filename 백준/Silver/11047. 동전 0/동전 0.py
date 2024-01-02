N, K = map(int, input().split())

cnt = 0
coin_list = list()
for i in range(N):
    coin_list.append(int(input()))

for i in reversed(range(N)):
    cnt += K//coin_list[i]
    K = K%coin_list[i]

print(cnt)