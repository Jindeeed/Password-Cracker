import hashlib
import time
import getpass
import itertools
import string
import random


file = "pass_crack.txt"

symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
                  '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '.',
                  '<', '>', '/', '?', '|', '\\', '`', '~']


lowercase = [chr(i) for i in range(97,123)]
uppercase = [chr(i) for i in range (65,91)]

def improve_pass(word):
    ## teach how to improve password 
    
    print(f"Your password {word} was cracked in under a second. We will now give you methods of improving this password.")
    
    if len(word) < 13:
        print("For your password to be considered close to impossible to crack - It must be from 12 - 16 characters")

    randsymbol = random.randint(0,31)
    randindex = random.randint(0,len(word))
    randiter = random.randint(5,10)
    
    word_add = list(word)

    word_add[randindex] = symbol[randsymbol - 1]
    print(word_add)
    
   
    for i in range(0,randiter):
        pick = random.choice([uppercase,lowercase,symbol])
        word_add.append(random.choice(pick))
        new_pass = "".join(word_add)
    
    print(f"Your new and improved password is below \n {new_pass}")
   


def hash_password(phold):
    return hashlib.sha256(phold.encode()).hexdigest() # hash password using sha-256 ## built in library to hash







def dict_attack(file,hashed_pass):
    flag = False
    line_num = 0
    try:
        with open(file, "r", encoding="utf-8") as f:  ## important as many characters use special characters and python default language may not pickup
            for line in f:
                line_num +=1
                word = line.strip()
                if hash_password(word) == hashed_pass:
                    print(f"Password found in {line_num - 1} passes : {word}")
                    flag = True
                    improve_pass(word)
                    break


     
            if not flag:
                print(f"{pass_inp} is a safe password - Not found")            
            

    except FileNotFoundError:
        print(f"UNABLE TO LOCATE FILE : {file}")



'''def check_result(word):
    if flag:        
        print(f"Password found in {line_num - 1} passes : {word}")
        improve_pass(word)   
    else
        print(f"{word} not flag")'''

        
        


pass_inp = getpass.getpass("Enter a password: ")
hashed_pass = hash_password(pass_inp)




dict_attack(file,hashed_pass)





