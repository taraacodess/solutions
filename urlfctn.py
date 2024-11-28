import webbrowser

print('''
       I am your robot.
       enter g to open google.
       enter y to open youtube.
       enter s to open  game.
       ''')

def open_utube():
    webbrowser.open("https://www.youtube.com/")

def open_google():
    webbrowser.open("https://www.google.com/")  

def open_game():
    webbrowser.open("https://www.microsoft.com/en-us/edge/surf?form=MA13E3")

ask=input("enter what you want to open ")    

if ask=="y":
    webbrowser.open(open_utube())

elif ask=="g":
    webbrowser.open(open_google()) 

elif ask=="s":
    webbrowser.open(open_game())     

else:
    print("invalid")    