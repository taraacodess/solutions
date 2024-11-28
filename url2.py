from urlclass import Robot

print('''
      I am your robot.
      enter 'g' to open google
      enter 'y' to open youtube 
      enter 's'



''')

d=Robot()

ask=input("enter a letter:")


if ask=="y":
    d.open_utube()

elif ask=="g":
    d.open_google()

elif ask=="s":
    d.open_game()    

else:
    print("invalid")    
