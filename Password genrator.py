import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters=int(input("How many letters would you like to in your password\n"))
nr_number=int(input("How many numbers would you like to in your password\n"))
nr_symbols=int(input("How many symbols would you like to in your password\n"))
#EASY WAY TO GENRATE THE PASSOWORD


#password = ""
#
#for char in range(1, nr_letters + 1):
#  password += random.choice(letters)
#
#for char in range(1, nr_symbols + 1):
#  password += random.choice(symbols)
#
#for char in range(1, nr_number + 1):
#  password += random.choice(numbers)
#
#print(password)

# THIS IS THe HARD ONE
   
password=[]
for char in range (1, nr_letters):
    password.append (random.choice(letters)) 
for char in range (1,nr_number):
    password.append(random.choice(numbers))   
for char in range (1,nr_symbols):     
    password.append(random.choice(symbols))     
#print ( password)
random.shuffle(password)
#print (password)    
password2 =""
for char in password:
    password2+= char


print(password2)

    

