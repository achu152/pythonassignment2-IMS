import random


class UserStudent(User):
    def __init__(self, user_id=-1, user_name='', user_password='', user_role='ST', user_status='enabled', enrolled_units=[]):
        super().__init__(user_id, user_name, user_password, user_role, user_status)
        self.enrolled_units = enrolled_units

    def __str__(self):
        return super().__str__() + f", {self.enrolled_units}"

    def student_menu(self):
        print("1. List available units")
        print("2. List enrolled units")
        print("3. Enrol unit")
        print("4. Drop unit")
        print("5. Check score")
        print("6. Generate score")
        
    def list_available_units(self):
        # read available units from the 'unit.txt' file and display them
        with open('/data/unit.txt', 'r') as file:
            for line in file:
                unit_data = line.strip().split(',')
                unit_code = unit_data[0]
                unit_name = unit_data[1]
                unit_capacity = int(unit_data[2])
                print(f"{unit_code}: {unit_name} (capacity: {unit_capacity})")
                
    def list_enrolled_units(self):
        # read user data from the 'user.txt' file
        with open('user.txt', 'r') as file:
            for line in file:
                user_data = line.strip().split(',')
                if user_data[1] == self.user_name and user_data[3] == 'ST':
                    # filter the enrolled units based on the username
                    for unit_code, score in self.enrolled_units:
                        print(f"Unit code: {unit_code}, Score: {score}")
                    return  # return after finding the matching user and displaying their enrolled units
        print("User not found")

    def enrol_unit(self, unit_code):
    # check if the student is already enrolled in the unit
    for unit in self.enrolled_units:
        if unit[0] == unit_code:
            print("You are already enrolled in this unit.")
            return

    # check if the student has already enrolled in 3 units
    if len(self.enrolled_units) == 3:
        print("You have already enrolled in 3 units. You cannot enroll in any more units.")
        return

    # check if the unit is available and has capacity
    with open("unit.txt", "r") as f:
        available_units = [line.strip().split(",") for line in f]
    for unit in available_units:
        if unit[0] == unit_code:
            if int(unit[2]) == 0:
                print("This unit has reached its maximum capacity. You cannot enroll in this unit.")
                return
            else:
                # reduce the unit's capacity by 1 and update the 'unit.txt' file
                unit[2] = str(int(unit[2]) - 1)
                with open("unit.txt", "w") as f:
                    for line in available_units:
                        f.write(",".join(line) + "\n")
                # add the unit to the student's list of enrolled units
                self.enrolled_units.append((unit_code, -1))
                # update the 'user.txt' file with the new enrolment information
                with open("user.txt", "r") as f:
                    users = [line.strip().split(",") for line in f]
                for user in users:
                    if user[1] == self.user_name:
                        user[5] += f",{unit_code},-1"
                        break
                with open("user.txt", "w") as f:
                    for line in users:
                        f.write(",".join(line) + "\n")
                print(f"You have successfully enrolled in unit {unit_code}.")
                return

    # if the unit is not found in 'unit.txt', display an appropriate message
    print("This unit does not exist.")
    
    def drop_unit(self, unit_code):
    for i, unit in enumerate(self.enrolled_units):
        if unit[0] == unit_code:
            del self.enrolled_units[i]
            print(f"{unit_code} has been dropped successfully.")
            return
    print(f"You are not currently enrolled in {unit_code}.")


    def check_score(self, unit_code=''):
    if unit_code == '':
        # display scores for all units
        for unit in self.enrolled_units:
            print(f"Unit code: {unit[0]}, Score: {unit[1]}")
    else:
        # display score for specified unit
        for unit in self.enrolled_units:
            if unit[0] == unit_code:
                print(f"Unit code: {unit[0]}, Score: {unit[1]}")
                return
        print("You are not enrolled in this unit.")


    def generate_score(self, unit_code):
    # check if the student is enrolled in the specified unit
    for i, unit in enumerate(self.enrolled_units):
        if unit[0] == unit_code:
            # generate a random score between 0 and 100 (inclusive)
            score = random.randint(0, 100)
            # update the score for the specified unit
            self.enrolled_units[i] = (unit_code, score)
            # update the user.txt file with the new score
            with open('user.txt', 'r') as f:
                lines = f.readlines()
            with open('user.txt', 'w') as f:
                for line in lines:
                    fields = line.strip().split(',')
                    if fields[0] == str(self.user_id) and fields[3] == 'ST':
                        units = []
                        for u in self.enrolled_units:
                            units.append(f"{u[0]}:{u[1]}")
                        fields[5] = ','.join(units)
                    f.write(','.join(fields) + '\n')
            # display a message to confirm the score update
            print(f"Score for unit {unit_code} updated to {score}")
            return
    # if the student is not enrolled in the specified unit, display an appropriate message
    print(f"You are not enrolled in unit {unit_code}.")

	pass