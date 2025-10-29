import random
import string
 
def gen_password():
    length=int(input("Enter the desired password length: ").strip())
    include_uppercase=input("Include uppercase letters? YES or No: ").strip().lower()
    include_special=input("Include special characters? YES or No: ").strip().lower()
    include_digits=input("Include digits? YES or No: ").strip().lower()

    if length < 4:
        print("Password length must be atleast 4 characters.")
        return
    
    lowercase=string.ascii_lowercase #gives all the lowercase letters
    uppercase=string.ascii_uppercase  if include_uppercase =="yes"else ""
    special=string.punctuation  if include_special =="yes"else ""
    digits=string.digits  if include_digits =="yes"else ""
    all_characters=lowercase+uppercase+special+digits

    required_characters=[]
    if include_uppercase=="yes":
        required_characters.append(random.choice(uppercase))
    if include_special=="yes":
        required_characters.append(random.choice(special))
    if include_digits=="yes":
        required_characters.append(random.choice(digits))
    
    remaining_length=length-len(required_characters)
    password=required_characters

    for _ in range(remaining_length):
        character=random.choice(all_characters)
        password.append(character)
    
    random.shuffle(password)

    str_password="".join(password)
    return str_password
  

password=gen_password()
print(password)









