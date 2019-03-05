import random

class Robot(object):

    name_list = []

    def __init__(self):
        self.name = self.get_new_name()

    def get_new_name(self):
        while True:
            name = self.create_name()
            if name not in self.name_list:
                return name

    def create_name(self):
        return chr(random.randint(65, 90)) + \
            chr(random.randint(65,90)) + \
                str(random.randint(0,9)) + \
                    str(random.randint(0,9)) + \
                        str(random.randint(0,9)) 

    def reset(self):
        self.name_list.append(self.name)
        self.name = self.get_new_name()