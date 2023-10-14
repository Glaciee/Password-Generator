import random
import string

def generate_password(length):

    all_combinations = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
  
    password = ''.join(random.choice(all_combinations) for i in range(length))
    return password

length = int(input("Enter the length of password to generate: "))
print(f"Generated password: {generate_password(length)}")
