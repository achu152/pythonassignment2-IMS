class UserAdmin(User):
    def __init__(self, user_id=1, user_name="admin", user_password="password", user_role="AD", user_status="enabled"):
        super().__init__(user_id, user_name, self.encrypt(user_password), user_role, user_status)
        
    def __str__(self):
        return super().__str__()
    
    def admin_menu(self):
        print("1. Search user information")
        print("2. List all users’ information")
        print("3. List all units’ information")
        print("4. Enable/Disable user")
        print("5. Add User")
        print("6. Delete User")
    
    def search_user(self, user_name):
        with open("data/user.txt", "r") as file:
            for line in file:
                fields = line.strip().split(", ")
                if fields[1] == user_name:
                    print("User found:")
                    print(line)
                    return
        print("User not found.")
        
    def list_all_users(self, user_name):
        with open("data/user.txt", "r") as file:
            for line in file:
                print(line.strip())
                
    def list_all_units(self):
        with open("data/unit.txt", "r") as file:
            for line in file:
                print(line.strip())
                
    def enable_disable_user(self, user_name):
        with open("data/user.txt", "r") as file:
            lines = file.readlines()
        with open("data/user.txt", "w") as file:
            for line in lines:
                fields = line.strip().split(", ")
                if fields[1] == user_name:
                    if fields[4] == "enabled":
                        fields[4] = "disabled"
                    else:
                        fields[4] = "enabled"
                    line = ", ".join(fields) + "\n"
                file.write(line)
        print("User status updated.Current status: {current_status}, New status: {fields[4]}")
     
     def add_user(self, user_obj):
        with open("data/user.txt", "a") as file:
            file.write(str(user_obj) + "\n")
        print("User added.")
    
    def delete_user(self, user_name):
    with open("data/user.txt", "r") as file:
        lines = file.readlines()
    with open("data/user.txt", "w") as file:
        user_found = False
        new_lines = []
        for line in lines:
            fields = line.strip().split(", ")
            if fields[1] == user_name:
                user_found = True
            else:
                new_lines.append(line)
        if user_found:
            file.writelines(new_lines)
            print("User deleted.")
        else:
            print("User not found.")
      
	pass