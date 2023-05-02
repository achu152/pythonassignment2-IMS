import re
from user import User
from unit import Unit

class UserTeacher(User):
    def __init__(self, user_id=None, username=None, user_password=None, user_role='TA', user_status='enabled', teach_units=[]):
        super().__init__(user_id, username, user_password, user_role, user_status)
        self.teach_units = teach_units
        
    def __str__(self):
        return super().__str__() + ', ' + ', '.join(self.teach_units)
    
    def teacher_menu(self):
        print("Teacher Menu Options")
        print("1. List all units taught by this teacher")
        print("2. Add a new unit")
        print("3. Delete a unit")
        print("4. List enrolled students for a unit")
        print("5. Show unit's average, maximum, and minimum score")
        print("6. Logout")
        
    def list_teach_units(self):
        with open("data/user.txt", "r") as f: 
            lines = f.readlines() 
            for line in lines:         
                if re.search(f"^{self.username},", line):
                    user_info = line.split(",")
                    teach_units = user_info[-1].strip()
                    if teach_units:
                        unit_codes = teach_units.split(";")
                        for unit_code in unit_codes:
                            with open("data/unit.txt", "r") as u:
                                unit_lines = u.readlines()
                                for unit_line in unit_lines:
                                    if re.search(f"^{unit_code},", unit_line):
                                        print(unit_line.strip())
                    else:
                        print("No units taught by this teacher are found in the system.")
                    break
                    
    def delete_teach_unit(self, unit_code):
    with open("data/user.txt", "r") as file:
        lines = file.readlines()
    with open("data/user.txt", "w") as file:
        for line in lines:
            user_data = re.split(",", line)
            if user_data[1] == self.username:
                teach_units = user_data[5].split(";")
                if unit_code in teach_units:
                    teach_units.remove(unit_code)
                    user_data[5] = ";".join(teach_units)
                    file.write(",".join(user_data) + "\n")
                else:
                    print("The unit is not taught by the teacher.")
            else:
                # Check for enrollment units for student and update user.txt
                if user_data[3] == "ST":
                    student_units = user_data[5].split(";")
                    if unit_code in student_units:
                        student_units.remove(unit_code)
                        user_data[5] = ";".join(student_units)
                        file.write(",".join(user_data) + "\n")
                        print("Student's enrollment for the unit has been removed.")
                file.write(line)
                
    def list_enrol_students(self, unit_code):
    with open("data/user.txt", "r") as file:
        lines = file.readlines()
        found = False
        for line in lines:
            user_data = re.split(",", line)
            if user_data[3] == "ST" and unit_code in user_data[5]:
                found = True
                print(user_data[0], user_data[1])
        if not found:
            print("No students are enrolled in the unit.")


    def show_unit_avg_max_min_score(self, unit_code):
        # get all the enrolled units for the specified unit code
        enrolled_units = []
        with open("user.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                fields = line.strip().split(",")
                username = fields[0]
                user_role = fields[2]
                if user_role == "ST":
                    enrolled_units = [tuple(unit.split(":")) for unit in fields[3].split(";") if unit]
                    enrolled_units = [(unit[0], int(unit[1])) if unit[1] != '' else (unit[0], -1) for unit in enrolled_units]
                    if username == self.username:
                        break
                        
        # filter the enrolled units to get the one with the specified unit code
        unit_scores = [unit[1] for unit in enrolled_units if unit[0] == unit_code]
        
        if not unit_scores:
            print(f"No student has enrolled in unit {unit_code}.")
            return
        
        # calculate the average, maximum and minimum scores for the unit
        unit_avg_score = sum(unit_scores) / len(unit_scores)
        unit_max_score = max(unit_scores)
        unit_min_score = min(unit_scores)
        
        # display the unit's average, maximum and minimum scores
        print(f"Unit code: {unit_code}")
        print(f"Average score: {unit_avg_score:.2f}")
        print(f"Maximum score: {unit_max_score}")
        print(f"Minimum score: {unit_min_score}")

        
	pass