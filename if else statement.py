
# Question-1 Write a progarm to calculate the electricity bill using only if statement.

unit=int(input("Enter the electricity unit:"))
Rupey=0
bill=0
if unit<=100:
    print("Free electricity No need to pay")
if unit>100 and unit<=200:
    Rupey=(unit-100)*5
    print("Your Electricity bill is:", Rupey)
if unit>200 :
    Rupey=(unit-100)*10
    print("Your Electricity bill is :",Rupey)
    

# question-2  write a program to accept the percantage from the user and display the grade according to the following criteria:
Marks=int(input("Enter the marks:"))
if Marks>90:
    print("Grade A")
elif Marks>80 and Marks<=90:
    print("Grade B")
elif Marks>=60 and Marks<=80:
    print("Grade C")
elif Marks<60:
    print("Grade D")  


# Question-3 accept the age of 4 people and display the youngest one...
mohan=int(input("Enter the age of Mohan:"))
rahul=int(input("Enter the age of Rahul:"))
sohan=int(input("Enter the age of Sohan:"))
vishal=int(input("Enter the age of vishal:"))
if mohan<rahul and mohan<sohan and mohan<vishal:
    print("Mohan is youngest person")
elif rahul<mohan and rahul<sohan and rahul<vishal:
    print("Rahul  is youngest person" )    
elif sohan<mohan and sohan<rahul and sohan<vishal:
    print("Sohan is youngest person")
else:
    print("Vishal is youngest person") 



# Question-5 Accept three number from the user and display second largest number...
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if num1>num2 and num1>num3:
    if num2>3:
        print("The second largest number:",num2)
    else:
        print("The second largest number:", num3)

elif num2>num3 and num2>num1:
    if num1>num3:
        print("The second largest number is:", num1)
    else:
        print("The second largest number is:", num3)                
elif num3>2 and num2>1:
    if num1>num2:
        print("The second largest number is:",num1)
    else:
        print("the second largest number is:",num2)  



# Question-6 Accept the marked price from the user and calculatethe net amount as (marked price-discount) to pay according to following criteria...
marked_price=int(input("Enter the marked_ price:"))
discount=0
netamount=0
if marked_price>10000:
    discount=(20/100)*marked_price
elif marked_price>7000 and marked_price<=10000:
    discount=(15/100)*marked_price
elif marked_price<=7000:
    discount=(10/100)*marked_price 
netamount=marked_price-discount
print("netamount:",netamount) 





# Question-8 Write a program to display Hello" if a number entered by user is a multiple of five,otherwise print "Bye"...
num=int(input("Enter the number:"))
if num%5==0:
    print("Hello")
else:
    print("Bye")  



# Question-9 Write a program to check whether the last digit of a number (entered by user) is divisible by 3 or not..

num=int(input("Enter any number:"))
last_digit=num%10
print("Last digit of number:",last_digit)
if last_digit%3==0:
    print("Last digit of number is divisible by 3")
else:
    print("Last digit of number is not divisible by 3") 

    


# Question-10 Write a program to check whether a number entered is three-digit number or not.
num=int(input("Enter a number:"))
if num>=100 and num<=999:
    print("The number is three digit number")
else:
    print("The number is not three digit number")
































   
   





         
                   
            

        












