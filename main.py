from employ import Employee


print('''
     press d to display employee information
      Press i to increase employee salary

''')

choice= input("enter a choice:")

c= Employee()


if choice == "d":
    c.display_information()

elif choice=="i":
    c.increase_salary()   

else:
    print("Invalid input")    