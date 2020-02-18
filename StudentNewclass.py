class Student:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def display(self,address):

    print("Hello my name and age is {}".format(address))

p1 = Student("anu",21)

p1.display("tvm")
# p2=Student("remya",14)
# p2.display()