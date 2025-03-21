#check whether the given number is odd or even
num=int(input("enter any number"))
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")

#check whether the given two numbers are equal or not
x=int(input("enter the first number"))
y=int(input("enter the second number"))
if x==y:
    print("x is equal to y")
else:
    print("x is not equal to y")

#check whether given number is pisitive or negative
x=int(input("enter the number"))
if x>0:
    print("x is positive")
elif x<0:
    print("x is negative")
else:
    print("x is 0")

#check whether eligible to vote or not
age=int(input("enter age"))
if age>18:
    print("eligible to vote")
else:
    print("not eligible to vote")

#check whether to pass or fail
a=int(input("enter student marks out of 100"))
if a>=40:
    print("pass")
else:
    print("fail")
