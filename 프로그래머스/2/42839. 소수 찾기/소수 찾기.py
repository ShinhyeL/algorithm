from itertools import permutations

#소수 판별
def prime_num(x): 
    if x<2:
        return False
    
    for i in range(2,x):
        if x%i == 0:
            return False
    
    return True


def solution(numbers):
    answer = 0
    num = []
    
    #permutations(iterable, r)은 iterable요소들을 길이 r인 순열로 반환함
    #즉, 여기서는 numbers의 요소들을 길이 i인 순열로 반환함
    #list : 순서가 있으며, 데이터 중복 허용
    #set : 순서가 없으며, 데이터 중복 허용x
    #map : key&value구조, key는 중복을 허용하지 않으며, value는 중복을 허용
    for i in range(1, len(numbers)+1) :
        num.append(list(set(map(''.join, permutations(numbers, i)))))
    #sum함수로 리스트끼리 덧셈. 중복을 없애기 위해set함수를 사용. num이라는 빈 리스트에 넣기 위해 다시 list로 바꾸어줌.
    per = list(set(map(int, set(sum(num, [])))))

    #이렇게 만들어진 per리스트가 소수라면 answer+=1
    for p in per :
        if prime_num(p) == True :
            answer += 1

    return answer
