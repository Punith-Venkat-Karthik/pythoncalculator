first_num=int(input("Enter first number:"))
second_num=int(input("Enter second number:"))
operator=input("Give an operator(+,-,*,/,%):")

if operator=="+":
    print(first_num+second_num)
elif operator=="-":   
    print(first_num-second_num)
elif operator=="*":    
    print(first_num*second_num)
elif operator=="/":
    if second_num==0:
        print("Infinite") 
    else:       
        print(first_num/second_num)
elif operator=="%":
    if second_num==0:
        print("Modulus by zero is not allowed") 
    else:       
        print(first_num%second_num)
else:
    print("Invalid Operator") 

except ValueError:
    print("Error enter a valid number")

