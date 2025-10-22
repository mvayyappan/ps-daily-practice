                                      #  Easy Level Python Problems

a=int(input("enter a number:"))
if a%10==2 or a%5==-2:
    print("2")
else:
    print("not 2")




a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
else:
    print(c)


n=int(input("enter a number:"))
if n>=500:
    print("your delivery cast is free")
else:
    print(n+50)



colors=(input("red/yellow/green:"))
if colors=="red":
    print("Stop")
elif colors=="yellow":
    print("Get ready")
elif colors=="green":
    print("Go")



a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if a>=40 and b>=40 and c>=40:
    print("promoted")
else:
    print("not promoted")


weather_condition=input("weather/sunny:")
if weather_condition=="sunny":
    print("umbrella")
else:
    print("no umbrella")



tamil=int(input("enter tamil mark:"))
eng=int(input("enter eng mark:"))
max=int(input("enter max mark:"))
science=int(input("enter science marK:"))
s_s=int(input("enter s_s mark:"))
if tamil>=35:
    print("Pass")
else:
    print("Fail")
if eng>=35:
    print("Pass")
else:
    print("Fail")
if max>=35:
    print("Pass")
else:
    print("Fail")
if science>=35:
    print("Pass")
else:
    print("Fail")
if s_s>=35:
    print("Pass")
else:
    print("Fail")


a=int(input("enter tamil subject mark:"))
b=int(input("enter English subject mark:"))
c=int(input("enter Maths subject mark:"))
average=(a+b+c)/3
print(average)
if average>=90:
    print("A")
elif average>=75 and average<90:
    print("B")
elif average>=50 and average<75:
    print("C")
else:
    print("fail")

x=int(input("enter a value:"))
if x<=100:
    print("bill:" "free")
elif x>=100 and x<=200:
    print("bill",x*5)
elif x>=200:
    print("bill",x*10)


a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
d=int(input("enter d value:"))
if a>b and a>c and a>d:
    print(a)
elif b>a and b>c and b>d:
    print(b)
elif c>a and c>b and c>d:
    print(c)
else:
    print(d)


a=int(input("enter a value:"))
if a%2==0 and a<0:
    print("negative even")
elif a%2==0 and a>0:
    print("positive even")
elif a%2==1 and a>0:
    print("positive odd")
elif a%2==1 and a<0:
    print("negative odd")



a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if(a > b and a > c):
    print(a)
elif (b > a and b > c):
    print(b)
else:
    print(c)

num = int(input("Enter a number: "))
if num < 0:
    print(-num)  
else:
    print(num)
    

n=int(input("enter n value:"))
m=int(input("enter m value:"))
add=n+m
if add%2==0:
    print("even")
else:
    print("odd")

a=int(input("enter a number:"))
b=int(input("enter a number:"))
total=0

while a<=b:
    if a%2==0:
        total=total+a
    a=a+1
print(total) 

a=int(input("enter a KG:"))
if a<=5:
    cost=10
    tax=(5/100)*cost
    print("total:",cost+tax)
elif a>5 and a<=20:
    cost=20
    tax=(5/100)*cost
    print("total:",cost+tax)
else:
    print("cost:",50*0.05+50)


file=input(".csv/.jpg/.doc/.pdf/.py:")
if file==".csv":
    print("This is an Excel File")
elif file==".jpg":
    print("This is an JPEG File")
elif file==".doc":
    print("This is an Word File")
elif file==".pdf":
    print("This is an PDF File")
elif file==".py":
    print("This is an Python File")
else:
    print("Unknown File Type")

n=int(input("enter a chocolate:"))
a=0
b=1
while n>a:
    chocolate=n-1
    print("day:",b,"= left",chocolate)
    n=n-1
    b=b+1





#             "                          # Medium  Level Python Problem

a=int(input("Enter the a value:"))
if ((a%4==0 and a%100!=0) or a%400==0):
    print("Y")
else:
    print("N")

a=int(input("enter a number:"))
if a%10==5 or a%5==-5:
    print("5")
else:
    print("not 5")

a=int(input("Enter the number x:"))
b=int(input("Enter the number y:"))
c=int(input("Enter the number z:"))
if a+b+c==180:
  print("valid triangle")
  if a==b==c:
    print("Equilateral")
  elif a==b!=c or a==c!=b or b==c!=a:
    print("iso")
  else:
    print("scalene")
else:
  print("invalid triangle")

a=int(input("enter a number:"))
total=a
if a>=0:
    total=a//5
    print("No of Buckets:",total)
    a=a%10
    print("left:",a)



a=int(input("enter a value:"))
if a<=12:
    cast=50
    print("cast:",cast)
    if a%2==0:
        print("Total_amount:",cast-5)
elif a>12 and a<=59:
    cast=100
    print("cast:",cast)
    if a%2==0:
        print("Total_amount:",cast-5)
elif a>=60:
    cast=150
    print("cast:",cast)
    if a%2==0:
        print("Total_amount:",cast-5)
else:
    print("invalid age")


height=float(input("Enter your height:"))
weight=float(input("enter your weight:"))
BMI=weight/(height**2)
print(BMI)
if BMI<=18:
    print("under_weight")
elif BMI>18 and BMI<=25:
    print("normal")
elif BMI>25 and BMI<=29:
    print("overweight")
elif BMI>=30:
    print("Obese")


a=int(input("enter a number:"))
if a<=9 and a>=-9:
    print("one digit")
elif a<=99 and a>=-99:
    print("two digit")
elif a<=999 and a>=-999:
    print("three digit")
elif a<=9999 and a>=-9999:
    print("four digit")
elif a<=99999 and a>=-99999:
    print("five digit")

a=input("username:")
b=input("password:")
username=("Ayyappan_M_V")
password=("An@2007") 
if username==a and b==password:
    print("Login Successful")
else:
    print("Access Denied")


num = int(input("Enter a number: "))
n = abs(num)  
while n >= 10:
    n = n // 10  
if n == 1:
    print("First digit is 1")
else:
    print("First digit is not 1")




a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
print(a," ",b," ",c)


                            
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
d=b**2-4*a*c
print(d)
if d>0:
    print("two real roots")
elif d==0:
    print("one real root")
elif d<0:
    print("Imaginary roots")


a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
add=a+b+c
d=add
if d==180:
    print("Triangle is valid")
    if a==90 or b==90 or c==90:
        print("Right angled triangle")
    elif a<90 or b<90 or c<90:
        print("Acute angled triangle")
    else:
        print("Obtuse-angled Triangle")
else:
    ("Not a valid Triangle")  

what_is_today=input("sunday/Monday/Tuesday/Wednesday/thursday/Friday/saturday:")
if what_is_today=="Monday" or what_is_today=="Tuesday" or what_is_today=="Wednesday" or what_is_today=="Thursday" or what_is_today=="friday":
    print("Working day")
elif what_is_today=="Saturday"  or what_is_today=="Sunday":
    print("Holiday")
else:
    print("Invalid day")

x=int(input("enter a number:"))
if x>=50000:
    discount=x*10/100
    print("salary:",discount+x)
else:
    discount=x*5/100
    print("salary:",x+discount)

n=int(input("enter a time:"))
if n>9 and n<12:
    print("Morning Show")
elif n>12 and n<16:
    print("Matinee Show")
elif n>16 and n<20:
    print("Evening Show ")
elif n>20:
    print("night Show ")





n=int(input("enter value:"))
if  n%3==0 and n%5==0:
    print("FizzBuzz if the number is divisible by both 3 and 5")
elif n%3==0:
    print("Fizz if the number is divisible by 3")
elif n%5==0:
    print("Buzz if the number is divisible by 5")
else:
    print("The number itself if it is divisible by neither 3 nor 5")




ola=50
n=int(input("enter a km:"))
if n<=5:
    print("cast:",ola+n*10)
elif n>=6 and n<=15:
    print("cast:",ola+n*8)
elif n>15:
    print("cast:",ola+n*6)



                                      # Hard Level Python Problems 

year=int(input("enter a year:"))
if ((year%4==0 and year%100!=0) or year%400==0 ):
    print("this year is leap year")
else:
    print("this year is not leap year")

x=int(input("enter x value:"))
y=int(input("enter y value:"))
if x>0 and y>0:
    print("1")
elif x<0 and y>0:
    print("2")
elif x<0 and y<0:
    print("3")
elif x>0 and y<0:
    print("4")
elif x==0 and y==0:
    print("point")
elif x==0 and y<0:
    print("Y")
elif x==0 and y>0:
    print("Y")
elif x>0 and y==0:
    print("X")
elif x<0 and y==0:
    print("X")

    
z=input("Residential/commercial:")
unit=int(input("enter a unit:"))
if z=="Residential":
    if unit>0 and unit<100:
        print("cast:",unit*3)
    elif unit>100 and unit<200:
        print("cast:",unit*5)
    elif unit>200:
        print("cast:",unit*7)
    else:
        print("out of unit")
elif z=="commercial":
    if unit>0 and unit<100:
        print("cast:",unit*5)
    elif unit>100 and unit<200:
        print("cast:",unit*7)
    elif unit>200:
        print("cast:",unit*10)
    else:
        print("out of unit")


amount = int(input("Enter amount: "))

if amount >= 500:
    n500 = amount // 500
    amount = amount % 500
else:
    n500 = 0

if amount >= 200:
    n200 = amount // 200
    amount = amount % 200
else:
    n200 = 0

if amount >= 100:
    n100 = amount // 100
    amount = amount % 100
else:
    n100 = 0

if amount >= 50:
    n50 = amount // 50
    amount = amount % 50
else:
    n50 = 0

if amount >= 10:
    n10 = amount // 10
    amount = amount % 10
else:
    n10 = 0

if amount >= 5:
    n5 = amount // 5
    amount = amount % 5
else:
    n5 = 0

if amount >= 1:
    n1 = amount // 1
    amount = amount % 1
else:
    n1 = 0

print("500:", n500)
print("200:", n200)
print("100:", n100)
print("50 :", n50)
print("10 :", n10)
print("5  :", n5)
print("1  :", n1)


f=input("pizza/burger/sandwich:")
n=int(input("enter a number:"))
if f=="pizza":
    cast=200
    tax=(5/100)*cast
    print("amount:",cast*n+tax*n)
elif f=="burger":
    cast=100
    tax=(5/100)*cast
    print("amount:",cast*n+tax*n)
elif f=="sandwich":
    cast=50
    tax=(5/100)*cast
    print("amount:",cast*n+tax*n)

    




























