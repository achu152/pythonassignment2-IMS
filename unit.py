import random

class Unit:
    def __str__(self,unit_id=1111111,unit_code='FIT9136',unit_name='default-unit',unit_capacity=2)
    self.unit_id = generate_unit_id()
    self.unit_code = unit_code
    self.unit_name = unit_name
    unit_capacity = unit_capacity
    
    def __str__(self)
       return f"{self.unit_id}, {self.unit_code}, {self.unit_name}, {unit_capacity}"
    
    def generate_unit_id(self)
       return random.randint(1111111, 9999999)
	pass


# should we create a method to generate unique unit code?