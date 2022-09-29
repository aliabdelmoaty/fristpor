from secrets import choice
print("1=+ \n2=-\n3=*\n4=/\n")
while True: 
    num1 = input("first number:  ")
    num2 = input("second number:  ")
    choice=input("your choice:  ")

    if choice in ('1', '2', '3', '4'):
        if choice =='1':
            result = float(num1)+float(num2)
            print(result)
        elif choice =='2' :
            result = float(num1)-float(num2)
            print(result)
        elif choice =='3' :
            result = float(num1)*float(num2)
            print(result)
        elif choice =='4' :
            result = float(num1)/float(num2)
            print(result)
        next_calculation=input("next calculation? yes  or no")
    
        if next_calculation == 'no':
            print("thank you")
            break
    #else: ينفع نستخدم دى برضوا عشان يطلع شكرا بدل الدالة اللى فوقها
        #print("thank you")