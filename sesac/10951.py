while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

#테스트 케이스 개수가 정해지지 않았을 때는 try, except를 이용하여 while문을 멈춘다.
#try: try안의 코드를 실행해라.
#except: try 코드가 안될 경우 except안의 명령어를 수행해라.
    