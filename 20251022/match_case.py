                                        ## easy level questions\

menu_card=int(input("enter a number:"))
match menu_card:
    case 1:
        print("pizza")
    case 2:
        print("burger")
    case 3:
        print("pasta")

a=input("enter a letter:")
match a:
    case "a" |  "A" | "e" | "E" | "i" | "I" | "o" | "O" | "U" | "u":
        print("vowel")
    case _:
        print("Consonant")

    
month_number=int(input("enter a number:"))
match month_number:
    case 1:
        print("january")
    case 2:
        print("february")
    case 3:
        print("march")
    case 4:
        print("april")
    case 5:
        print("may")
    case 6:
        print("june")
    case 7:
        print("july")
    case 8:
        print("August")
    case 9:
        print("september")
    case 10:
        print("october")
    case 11:
        print("november")
    case 12:
       print("december")
    case _:
        print("invalid month number")


color=input("enter a color:")
match color:
    case "red":
        print("stop")
    case "yellow":
        print("wait")
    case "green":
        print("go")
    case _:
        print("invalid color")

a=int(input("enter a value:"))
match a:
    case 1:
        print("sunday")
    case 2:
        print("monday")
    case 3:
        print("tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("thursday")
    case 6:
        print("friday")
    case 7:
        print("saturday")
    case 8:
        print("invalid number")


                                        ##  Medium level question
      
marks=int(input("enter yours marks:"))
match marks:
    case n if n>=90:
      print("grade a")
    case n if n>=50:
      print("grade b")
    case n if n>=40:
      print("grade c")
    case n if n>=0 and n<=35:
      print("fail") 
    case _:
      print("invalid mark")



age=int(input("enter your age:"))
match age:
    case n if age<=5:
        print("Your ticket is free")
    case n if age>5 and age<12:
        print("your ticket cost is 10")
    case n if age>13 and age<64:
        print("your ticket cost is 20")
    case n if age>=65:
        print("your ticket cost is 20")


a=int(input("enter a number:"))
match a%2==0:
    case True:
        print("even")
    case False:
        print("odd")


            
payment=input("UPI/Card/Net banking/COD:")
match payment:
    case "UPI":
        print("You selected UPI payment")
    case "Card":
        print("You selected Debit/Credit Card payment")
    case "NetBanking":
        print("You selected Net Banking")
    case "COD":
        print("You selected Cash on Delivery")
    case _:
        print("Invalid Payment Mode")


a=int(input("enter a value:"))
b=int(input("enter a value:"))
operator=input("add/sub/mul/div:")
match operator:
    case "add":
        print(a+b)
    case "sub":
        print(a-b)
    case "mul":
        print(a*b)
    case "div":
        print(a/b)
    case _:
        print("invalid operator")



                                        ## Hard level questions



shape=input("circle/square/rectangle:")
match shape:
    case "square":
        a=int(input("enter meeter:"))
        result=a**2
        print(result)
    case "rectangle":
        l=int(input("enter length meeter:"))
        b=int(input("enter meeter:"))
        result=l*b
        print(result)
    case "circle":
        r=int(input("enter radius meeter:"))
        result=22/7*r*r
        print(result)
    case _:
        print("invalid operator")

    

categories=input("electronics/fashion/groceries/books:")
price=int(input("enter the price:"))
match categories:
    case "electronics":
        discount=price*10/100
        print("discount:",discount)
        print("price:",price-discount)
    case "fashion":
        discount=price*20/100
        print("discount:",discount)
        print("price:",price-discount)
    case "groceries":
        discount=price*5/100
        print("discount:",discount)
        print("price:",price-discount)
    case"books":
        discount=("no discount:",price)
        print(discount)
    case _:
        print("invalid product:")


balance=int(input("enter a balance:"))
bank=input("withdraw/deposit:")
match bank:
    case "withdraw":
        amount=int(input("enter amount"))
        print(balance-amount)
    case "deposit":
        deposit=int(input("enter a deposit"))
        print(balance+deposit)

n=int(input("enter 2 digit positive number:"))
a=n//10
b=n%10
m=a+b
j=a*b
result=m+j
match result:
    case x if result==n:
        print("great")
    case _:
        print("Not")


a=int(input("Enter a value:"))
convert=input("Meters/centimeters/millimeters/mile:")
match convert:
    case "Meters":
        result=a*1000
        print(result,"meters")
    case "centimeters":
        result=a*100000
        print(result,"centimeters")
    case "millimeters":
        result=a*1000000
        print(result,"millimeters")
    case "mile":
        result=a/1.609
        print(result,"mile")
    case _:
        print("Invalid Conversion")


    



   
    
    
    
    
    

    



