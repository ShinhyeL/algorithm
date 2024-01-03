import sys

N = int(sys.stdin.readline())
Nlist = list(map(int, sys.stdin.readline().split()))
Nlist.sort()#이분탐색이니까 정렬해주어야 한다.

M = int(sys.stdin.readline())
Mlist = list(map(int, sys.stdin.readline().split()))

for m in Mlist :
    left = 0
    right = N-1
    
    while left <= right:
        mid = (left+right)//2
        if m < Nlist[mid]:
            right = mid - 1
        elif m > Nlist[mid]:
            left = mid + 1
        else:
            left = mid
            right = mid
            break
    if left == mid and right == mid:
        print(1)
    else : 
        print(0)