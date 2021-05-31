

class Person:
  def __init__(self, name, age):
    self.name = name + "aaa"
    self.age = age + 1
    
if __name__ == '__main__':
    p1 = Person("John", 36)
    print(p1.name)
    print(p1.age)