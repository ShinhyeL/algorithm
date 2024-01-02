def solution(n, lost, reserve):
#set자료형은 중복을 허용하지 않는 집합 자료형
#set은 객체끼리 집합 연산을 지원한다

    set_lost = set(lost)-set(reserve)
    set_reserve = set(reserve)-set(lost)
    
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
            
    return n-len(set_lost)