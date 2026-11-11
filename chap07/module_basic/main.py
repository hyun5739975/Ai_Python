# main.py 파일
# 모듈 가져오기 (from절 미사용)
# import test_module as test 
# raduis = test.number_input()
# print(test.get_circle_area(raduis))
# print(test.get_circumference(raduis))


# 모듈 가져오기(from절 사용)
from test_module import * # 전체함수 사용
# from test_module import get_circle_area, get_circumference, number_input # 특정함수 사용

raduis = number_input()
print(get_circle_area(raduis))
print(get_circumference(raduis))


