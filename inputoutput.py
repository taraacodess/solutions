name=input("what's your name?")

file = open("name.txt","w")
file.write(name)
file.close()