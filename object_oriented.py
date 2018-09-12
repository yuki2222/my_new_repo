
"""
class Data:
    def __init__(self, a, b):
        self.nums = [a, b]

class Avatar(Data):
    def area(self):
        return self.nums[0] * self.nums[1]

d2 = Avatar(3, 2)
print(d2.area())


d1 = Data(5, 6)

# 一度オブジェクトを介さないと変数へアクセスできない
# オブジェクトの中に変数やメソッドがあるイメージ
d1.nums[1] = 9

# 変数へ直接アクセス可能
data1 = [3, 4]
data2 = [1, 6]
data1[1] = 9
"""

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
        
class Person:
    def __init__(self, name):
        self.name = name
        
stan = Dog("Stanley", "Bulldog", "Mick")
mick = Person(stan)
print(mick.name.breed)
