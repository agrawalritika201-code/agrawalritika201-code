# print("Hello world")
# a= int(input("Enter first number:\n") )
# b= int(input("Enter Second number:\n") )

# print("the value of ", a ,"+",b, "is :", a+b)
# print("the value of ", a ,"-",b, "is :", a-b)
# print("the value of ", a ,"*",b, "is :", a*b)
# print("the value of ", a ,"/",b, "is :", a/b)
# print("the value of ", a ,"%",b, "is :", a%b)
# print("the value of ", a ,"//",b, "is :", a//b)
# print("the value of ", a ,"**",b, "is :", a**b)
# print("the type of a is :",type(a))
# print("the type of b is :",type(b), "\n")

# c = int(input("enter a number:"))
# if c%2==0:
#     print("the number is even\n")
# else:
#     print("the number is odd\n")
  
# d = int(input("enter first number:"))   
# e = int(input("enter second number:"))
# f = int(input("enter third number:"))
# if d>e and d>f:
#     print("the gratest number is: ",d)
# elif e>d and e>f:
#     print("the gratest number is:",e) 
# else:
#     print("the gratest number is: ",f)

# age= int(input("enter age of the person:"))  
# if age>= 18:
#     print("the person is eligible for vote") 
# else:
#     print("the person is not eligible for vote")

d = int(input("enter marks for maths:"))  
e = int(input("enter marks for HV:"))  
f = int(input("enter marks for pfps:"))  
g = int(input("enter marks for BCE:"))
h = int(input("enter marks for physics:")) 

per = (d+e+f+g+h)/5

print("per = ",per)

if per>85 and per<=100:
    print("Grade = A")
elif per>70 and per<=85:
    print("Grade = B")
elif per>55 and per<=70:
    print("Grade = C")
elif per>36 and per<=55:
    print("Grade = D")
else:
    print("Fail")
 

