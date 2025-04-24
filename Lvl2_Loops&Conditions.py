'''
consists of basic loops & conditions python programming codes
- to get a clear understanding of looping and conditionals
- first part: user input syntax
- indents given for clarification; consider using proper indenattion during actual codes
''' 

#test from vscode
#how to user input in python
name = input("Enter your name: ")
num = int(input("Enter your lucky number: "))
f_num = float(input("Enter a floating-point number: "))
num1, num2 = input("Enter two values separated by space: ").split()
print(name)
print(num)
print(f_num)
print(num1, num2)

#first 10 Natural numbers using while loop
N = 1
while N<=10:
    print(N)
    N += 1
    
#first 10 Whole numbers using for loop
for i in range(0,11):
    print(i)
    i += 1

#multiplication table for a given number
num = int(input("Enter a number of your choice: "))
for i in range(1,11):
    print(num, "*", i, "=" ,num * i)

#sum of numbers between 1 to 10
sum = 0
for i in range(1,11):
    sum += i
print(sum)

#sum of all even numbers between 1 to 100
sum = 0
for i in range(1,101):
    if i%2==0:
        sum += i
print(sum)

#prime number or not
num = int(input("Enter a number of your choice: "))
c = 0
for i in range(1, num+1):
    if num%i==0:
        c += 1
if c==2:
    print("prime")
elif c>2:
    print("not prime")
  
#factorial of a number
num = int(input("Enter a number of your choice: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print(fact)