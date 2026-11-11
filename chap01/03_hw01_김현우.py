#10월 27일 과제
#print 함수를 이용한 자기소개 문자열 출력 
print("성함        : 김현우")
print("전공        : 인터넷정보과 / 자바 및 정산 프로그램 유지보수")
print("지원동기    : AI를 이용한 프로그램 분석 및 개발에 대한 흥미")
print("하고 싶은말 : 잘부탁드립니다.")

iflags = ["성함","전공","지원동기","하고 싶은말"]
jflags = ["김현우","인터넷정보과 / 자바 및 정산 프로그램 유지보수","AI를 이용한 프로그램 분석 및 개발에 대한 흥미","잘부탁드립니다"]

for key, value in zip(iflags,jflags) :
  print (f"{key} : {value}")

strtest1 ="""
      안녕하세요 
      \"철수\"가 놀러 왔어요.
      기쁜 마음에 반갑습니다.
      인사를 했어요 
      """

print(strtest1)


for strtest in range(3) :
  print(strtest1)

  