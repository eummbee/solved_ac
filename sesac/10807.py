N =  int(input())
n = list(map(int, input().split()))
v = int(input())
count = 0
for i in n:
    if v == i:
        count += 1
print(count)        

#정답 코드
N =  int(input())
n = list(map(int, input().split()))
v = int(input())

print(n.count(v)) #한 줄로 출력할 수 있다.