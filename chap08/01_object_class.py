# 클래스를 선언합니다.
# 클래스 -> 사용자가 정의해주는 자료형, 테이블을 만들어 주는 거 자료형을 하나 선언
# 파이썬 리스트는 서로 다른 데이터형도 저장이 됨 자바는 안됨 그래서 클래스 지식은 많이 요하지는 않음 환경 때문에 
# 클래스 = 리스트 대체 / 클래스는 첫글자는 대문자
# self = this 자바가 this, self 파이썬 변수명 때문에 번거로움 때문에 self 변수명과 매개변수 변수명은 다르게 함
# 파이썬 자체에서 내부에서는 self 변수 안에 주소값에 저장됨 -> 함수로 호출 -> 데이터가 변수에 담김 내부) self. 으로 메모리에 접근 
# 외부에서는 honkildon. 으로 메모리에 접근
# self(키워드) 할당된 주소값 - > 복귀 -> honkildong로 접근 (할당된 메모리 공간 = 객체 / 인스턴스(self.name 등))
# 함수랑 메소드 차이 => 클래스 안에 함수는 메소드
class Student:
  def __init__(self, name, korean, math, english, science): # __init__약속
    self.name    = name
    self.korean  = korean
    self.math    = math
    self.english = english
    self.science = science

  def get_sum (self): # 총점
    return self.korean + self.english + self.math + self.science

  def get_avg (self): # 평균
    return self.get_sum() / 4

  def to_string(self):
    return f"{self.name}\t{self.get_sum()}\t{self.get_avg()}"
     

# 메모리 할당 요청
# honkildong = 참조변수 할당된 메모리를 참조함 (객체 / 인스턴스)
hongkildong = Student("홍길동", 95, 85, 15, 70) # def __init__(self) 함수 호출 (java = > new)

# 메모리 접근하는 방법 (데이터 저장)
hongkildong.name    = "홍길동"
hongkildong.korean  = 100
hongkildong.math    = 38
hongkildong.english = 100
hongkildong.science = 70

# 메모리 접근 방법(테이터 읽기)
print("이름 :  ", hongkildong.name)
print("국어 :  ", hongkildong.korean)
print("영어 :  ", hongkildong.english)
print("수학 :  ", hongkildong.math)
print("과학 :  ", hongkildong.science)

print("이름", "총점", "평균", sep="\t")
print(hongkildong.name, hongkildong.get_sum(), hongkildong.get_avg(), sep="\t" )


# 학생 리스트를 선언합니다.
students = [
    Student("유재석", 87, 98, 88, 95), # 마지막은 주소값
    Student("신동엽", 92, 98, 96, 98),
    Student("강호동", 76, 96, 94, 90),
    Student("박명수", 98, 92, 96, 92),
    Student("김구라", 95, 98, 98, 98),
    Student("김국진", 64, 88, 92, 92),
    Student("수지", 64, 88, 92, 92),
]

# 학생을 한 명씩 반복합니다.
print("이름", "국어", "영어", "수학", "과학", "총점", "평균", sep="\t")
for i in range(len(students)) :
    print("{}\t {}\t {}\t {}\t {}\t {}\t {}".format(students[i].name
                                                  , students[i].korean
                                                  , students[i].english
                                                  , students[i].math
                                                  , students[i].science
                                                  , students[i].get_sum()
                                                  , students[i].get_avg()))
# 방법2
for student in students:
    print (student.to_string())
    

print()
# 개별적 접근 방법
print("이름", "국어", "영어", "수학", "과학", "총점", "평균", sep="\t")
print("{}\t {}\t {}\t {}\t {}\t {}\t {}".format(students[2].name
                                              , students[2].korean
                                              , students[2].english
                                              , students[2].math
                                              , students[2].science
                                              , students[2].get_sum()
                                              , students[2].get_avg()))

print()