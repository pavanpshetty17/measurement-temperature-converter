i=1
while(i>0):
    choice=input("--------------------\nChoose the conversion u want to perform:\nFor temperature conversion, press 'T'.\nFor measurement conversion, press 'M'\nTo exit, press 'E'\nEnter your choice: ").upper()
    if choice=="T":
        convert=input("To convert from celsius to fahrenheit, press 'F'\nTo convert from fahrenheit to celsius, press 'C'\nEnter 'F' or 'C': ").upper()
        if convert=="F":
            celcius = float(input("Enter the celcius temperature: "))
            fahrenheit=((9*celcius)/5+32)
            print("Equivalent fahrenheit temperature is",fahrenheit,"\n--------------------\n")
        elif convert=="C":
            fahrenheit= float(input("Enter the fahrenheit temperature: "))
            celcius=((fahrenheit-32)* 5/9)
            print("Equivalent celcius temperature is",celcius,"\n--------------------\n")
        else :
            print("Invalid input\n--------------------\n")
    elif choice=="M":
        convert = input("To convert from inches to centimeters, press 'C'\nTo convert from centimeters to inches, press 'I'\nEnter 'C' or 'I': ").upper()
        if  convert== "C":
            inches = float(input("Enter length in inches: "))
            centimeters = (inches*2.54)
            print(f"{inches:.2f}in is {centimeters:.2f}cm\n--------------------\n")
        elif convert == 'I':
            centimeters = float(input("Enter length in centimeters: "))
            inches = (centimeters /2.54)
            print(f"{centimeters:.2f}cm is {inches:.2f}in\n--------------------\n")
        else:
            print("Invalid input!\n--------------------\n")
    elif(choice=="E"):
        exit()
    else:
        print("Invalid choice! Please enter correctly.\n--------------------\n")
    i=i+1