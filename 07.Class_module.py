#opp란?
#클래스, 인스턴스
#self 개념
#인스턴스 메소드
#클래스, 인스턴스 변수

#class 를 이용하면 코드 재사용이 가능하다
#하지만 객체지향 프로그램이 빠른건 아니다

##예제1##-------------------------------

class Dog(object): #object 상속
  species = 'firstdog'

  #초기화/인스턴스 속성
  def __init__(self, name, age):
    self.name = name
    self.age =age


#인스턴스는 객체에 포함된다고 보면된다.

#클래스 정보
print(Dog)



#네임스페이스: 객체를 인스턴스화 할때 저장된 공간
#클래스변수 : 직접 접근 가능
#인스턴스 변수: 객체마다 별도 존재 (self가 붙은것들)

#인스턴스화 
a=Dog('micky', 2) #각각 다른 변수를 입력해서 인스턴스화 한다
b=Dog('baby',3)
c=Dog('micky',2)

print(a.name)

print(a==b)

print('dog1', a.__dict__) #namespace 확인가능 
print('dog2', b.__dict__)

#인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))


if a.species == "firstdog":
  print('{0} is a {1}'.format (a.name, a.species))

print(Dog.species) #클래스로도 접근 가능
print(a.species) #인스턴스화 된 형태로도 접근가능

##예제2##---------------------------------
#self의 이해

class SelfTest:
  def func1():
    print('Func1 called')
  def func2(self):
    print(id(self))
    print('Func2 called')


f = SelfTest() #self라는 메쏘드가 있는 경우만 넘어간다

print(dir(f)) #namespce안에 요소를 확인가능

print(id(f))
#f.func1() #예외

f.func2()

SelfTest.func1()#self가 없어서 바로 class로 직접호출
#SelfTest.func2() #예외 : func2는 하나의 매개변수를 요구하나 들어가지 않아서 에러발생
SelfTest.func2(f) #self가 있는 인스턴스 
#SelfTest.func2() #예외


##예제3##--------------------------------------
#클래스 변수, 인스턴스 변수

class Warehouse:
  #클래스 변수 = 0
  stock_num = 0 #재고
  def __init__(self, name):
    #인스턴스 변수
    self.name = name
    Warehouse.stock_num += 1

  def __del__(self):
    Warehouse.stock_num -= 1


user1 = Warehouse('Lee')
print(Warehouse.stock_num)
user2 = Warehouse('Cho')


print(user1.name)
print(user2.name)
print(Warehouse.__dict__)
print(user1.stock_num)

del user1

print('after', Warehouse.__dict__)


##예제4##---------------------------------------

class Dog:
  species = 'firstdog'
  def __init__(self, name, age, color):
    self.name = name
    self.age = age
    self.color =color
  def info(self):
    return '{} is {} years old'.format(self.name, self.age)
  def speak(self, sound):
    return '{} says {}!'.format(self.name, sound)

#인스턴스 생성
c=Dog('koko',12, 'red')
d=Dog('bell', 10, 'brown')
print(c.speak('hoho'))
print(c.info())

print(d.info())
print(d.speak('mung mung'))
