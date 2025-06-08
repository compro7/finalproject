import random
import pandas as pd

def get_rand_name():
    first_names = [
        "James", "Mary", "John", "Patricia", "Robert", "Jennifer",
        "Michael", "Linda", "William", "Elizabeth", "David", "Barbara",
        "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah",
        "Charles", "Karen"
    ]

    last_names = [
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
        "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez",
        "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore",
        "Jackson", "Martin"
    ]

    last_name = random.choice(last_names) # Last name 
    first_name = "".join(random.sample(first_names, 2)) # First name 
    full_name = last_name + " " + first_name # Full name 
    
    return full_name

def get_rand_phone_number():
    numbers = "0123456789"
    num1 = "".join(random.sample(numbers, 4))
    num2 = "".join(random.sample(numbers, 4))
    
    phone_num = "021-{0}-{1}".format(num1, num2)
    
    return phone_num

def get_rand_member_ID():
    alphabet_numbes = "abcdefghizklmnopqrstuvwxyz0123456789"
    digit = random.randint(4,10)
    
    while(True):
        member_ID = "".join(random.sample(alphabet_numbes, digit))
        if(member_ID[0] not in '0123456789'): 
            break                             
    
    return member_ID

def main():
    user_infos = []

    for k in range(1000):
        name = get_rand_name()
        phone_number = get_rand_phone_number()
        member_ID = get_rand_member_ID()
        
        user_infos.append([name, phone_number, member_ID])

        columns_name = ['Fullname', 'Phone', 'UserID']
        df = pd.DataFrame(user_infos, columns =columns_name)

if __name__ == "__main__":

    main()
            