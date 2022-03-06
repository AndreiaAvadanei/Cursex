# 1.Remove all occurrences of a specific item from a list.
# 2.Check if all items in the tuple are the same
# 3.Convert the following Vehicle Object into JSON
# import json
# class Vehicle:
#   def __init__(self, name, engine, price):
#        self.name = name
#        self.price = price
# vehicle = Vehicle(“Toyota Rav4”, “2.5L”, 32000)
# 4.Create new config.json file
# Parse the following JSON to get all the values of a key ‘name’ within an array
# [
#   {
#     “id”:1,
#     “name”:“name1”,
#      “color”:[
#         “red”,
#         “green”
#      ]
#   },
#   {
#      “id”:2,
#      “name”:“name2”,
#      “color”:[
#         “pink”,
#         “yellow”
#      ]
#   }
# ]

#  1st exercise
# Self- tine locul instantei
# Remove all occurrences of a specific item from a list.
# tema = set instead of list
class Students:
    def __init__(self):  # self tine locul instantei
        self.list_of_names = []
        self.student_atributes = ('diligent', 'tired', ' lost', 'curious')

    def add_student(self, name):
        self.list_of_names.append(name)


    def print_first_atribute(self):
        print(self.student_atributes[0])

    def get_unigue_list_of_names(self):
        temp_list = []
        for name in self.list_of_names:
            if name not in temp_list:  # nu este foarte optim sa folosim acesta functie cu liste
                temp_list.append(name)  # este optim sa folosim seturi sau dictionare
        return temp_list  # listele se folosesc cand facem indexari, adica cand stim indexul


student_obj = Students()

student_obj.add_student('John')
student_obj.add_student('Mary')
student_obj.add_student('John')
student_obj.add_student('Steven')

student_obj.print_first_atribute()
print(student_obj.list_of_names)
print(student_obj.get_unigue_list_of_names())