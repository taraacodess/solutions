#ask user for number
#convert it into string
#reverse string
#convert reversed string into no
#check if it's palindrome

#ask user for number
num=int(input("enter a number"))

#convert it into string
str_num=str(num)

#reverse string
reversed_string= ''.join(reversed(str_num))

#convert reversed string into no
reversed_num=int(reversed_string)

#convert reversed string into no
if num==reversed_num:
    print("palindrome")
else:
    print("not palindrome")    