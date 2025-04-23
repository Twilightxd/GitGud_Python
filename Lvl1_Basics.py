'''
consists of Super basic python programming codes
- to get a clear understanding of python syntax
- indents given for clarification; consider using proper indenattion during actual codes
- uploaded a notepad file under .py extension
'''

# print name and age
  name = "iTwili8"
  age = 22
  num = 10
  
  print("Hello Twilight!  Welcome to GitGud Series - Python")
  print(name, age, num)

# swapping numbers with temp var
  num1 = 10
  num2 = 50
  print(num1, num2)
  temp = num1
  num1 = num2
  num2 = temp
  print(num1, num2)

#swapping numbers without temp var
  a = 5
  b = 10
  print(a, b)
  a = a+b
  b = a-b
  a = a-b
  print(a, b)

#adding of numbers
  num1 = 10
  num2 = 20
  print(num1 + num2)

#even_odd number
  num = 10
  if num%2==0:
    print("even")
  else:
    print("odd")

#square_cube number
  num = 10
  sq_num = num * num
  cu_num = num * num * num
  print(sq_num, cu_num)

#positive, negative, zero
  num = 10
  if num>0:
    print("positive")
  elif num<0:
    print("negative")
  else:
    print("zero")
