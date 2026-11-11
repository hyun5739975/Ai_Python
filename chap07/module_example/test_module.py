# test_module.py

PI = 3.141592

def number_input():
    output = input("숫자 입력> ")
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius

# 활용 예 테스트 코드 유지한채 배포 할 경우 제 3자에서는 혼동이 옴
# 주석이나 코드문 제거하는 거 아니면 제일 좋은건 if문으로 조건을 걸음
# 변수 __ : 파이썬에서 정의해서 사용하는 식별자 사용이름
# print("module의 __name__ : ", __name__)

if __name__ == "__main__" : 
    print("get_circumference(10):", get_circumference(10))
    print("get_circle_area(10): ", get_circle_area(10))