print("Hello World!")

a = 1
b = 2
c = a+b
print(c)

myName = "Lilia"

bed = True

def say_hello():
  print("hello")

say_hello()

def alert(error):
  print("warning",error)

alert("e")

age = int(input("Your age:\n"))
if age<18:
  print("You can't drink!")
elif age>=18 and age<35:
  print("You can drink beer")
else:
  print("Go ahead")
