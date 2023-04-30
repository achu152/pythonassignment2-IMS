import random


class User:
    
    def  __init__(self, user_id=1, user_name="admin", user_password="password", user_role="AD", user_status="enabled")
        self.user_id = generate_user_id()
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role
        self.user_status = user_status
        
    def __str__()
      return f"{self.user_id}, {self.user_name}, {self.user_password}, {self.user_role}, {self.user_status}"
    
    def generate_user_id(self)
    # Assume no of users exist in the system is not more than 100 
        user_id = random.randint(1, 100)
        
        
    def check_username_exist(self, user_name):
        # Open the user file and check if the username exists
        with open("data/user.txt", "r") as file:
            for line in file:
                fields = line.strip().split(", ")
                if fields[1] == user_name:
                    return True
        return False
    
str_1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
str_2 = "!#$%&()*+-./:;<=>?@\^_`{|}~"
       
    def encrypt(self, user_password):
        # Algorithm to encrypt the user_password 
        #encrypted_password = "^^^"
        for letter in user_password:
            ascii_code = ord(letter)
            remainder1 = ascii_code % len(self.str_1)
            char1 = self.str_1[remainder1]
            remainder2 = (user_password.index(letter) % len(self.str_2))
            char2 = self.str_2[remainder2]
            encrypted_password = "^^^"+ char_1 + char_2 + "$$$"
            #encrypted_password += char_1 + char_2
        #encrypted_password += "$$$"
        return encrypted_password
       
        
    def login(self, user_name, user_password):
        # Open the user file and check if the user exists and is enabled
        with open("data/user.txt", "r") as file:
            for line in file:
                fields = line.strip().split(", ")
                if fields[1] == user_name and fields[4] == "enabled":
                    # Decrypt the user password and check if it matches the provided password
                    decrypted_password = ""
                    encrypted_password = fields[2][3:-3]
                    for i in range(0, len(encrypted_password), 2):
                        index_1 = self.str_1.index(encrypted_password[i])
                        index_2 = self.str_2.index(encrypted_password[i+1])
                        ascii_code = (index_1 + index_2) % 128
                        decrypted_password += chr(ascii_code)
                    if decrypted_password == user_password:
                        # If the user is authenticated, return their information
                        return str(self)
        # If the user is not authenticated, return None
        return None
	pass