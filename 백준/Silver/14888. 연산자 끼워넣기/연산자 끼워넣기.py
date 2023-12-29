N = int(input()) #n개
A = list(map(int, input().split())) #n개 길이의 수열
add, sub, mul, div = map(int, input().split())
answer = []

# cal=현재까지 결과값. i=리스트 A의 인덱스
def backtrack(add, sub, mul, div, cal = 0, i = 0):
    
    #add, sub, mul, div가 모두 0이라면, 즉 모든 연산이 끝났다면
    if add==0 and sub==0 and mul==0 and div==0 :
        answer.append(cal) #현재 계산된 값들을 answer에 append
        return
    
    if add>0: #현재까지 결과값인 cal에 A[i]를 더하고 다음 인덱스로 넘어간다.
        backtrack(add-1, sub, mul, div, cal + A[i], i+1) #A[0]에서부터 시작해서 add가 0이 될때까지 i 하나씩 늘려주며 재귀
    if sub>0:
        backtrack(add, sub-1, mul, div, cal - A[i], i+1)
    if mul>0:
        backtrack(add, sub, mul-1, div, cal * A[i], i+1)
    if div>0: #음수 값에 주의하여 계산
        if cal<0:
            backtrack(add, sub, mul, div-1, -int(-cal/A[i]), i+1)
        else:
            backtrack(add, sub, mul, div-1, int(cal/A[i]), i+1)
            
backtrack(add, sub, mul, div, A[0], 1) #리스트의 첫번째 값에서부터 시작
print(max(answer))
print(min(answer))
