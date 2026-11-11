# main.py
import test_module as test

print(__name__)

# 개발자 취향 차이
if __name__ == "__main__" :
  radius = test.number_input()
  print(test.get_circumference(radius))
  print(test.get_circle_area(radius))