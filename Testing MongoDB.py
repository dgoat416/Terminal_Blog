__author__ = "DGOAT"

import pymongo

# exactly where on the mongoDB server we are connecting to
uri = "mongodb://127.0.0.1:27017"

# initialize the mongoDB client which has access to all databases in
# mongoDB instance
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

# finds all data in the collection (table)
students = collection.find({})
student_list = []

# prints a pointer to the first element in our collection
# can be used to iterate over all elements
print(students)
print(2 * "\n")

# print all students
for student in students:
    print(student)

# condensed and succinct form of above just get rid of 'grade'
print(3 * "\n")
students = [student['grade'] for student in collection.find({})]
print(students)

# creates a list consisting of digits 0 - 9
digits = [i for i in range(0, 10)]
print(digits)


#create a list of dictionaries with the same key
class1 = [{"name" : "Deron", "grade" : 100}, { "name" : "John", "grade" : 76},
          {"name" : "Otis", "grade" : 59}, {"name" : "Uriah", "grade" : 100}]

class2 = [{"name" : "Jordan", "grade" : 100}, { "name" : "Octeye", "grade" : 76},
          {"name" : "Dummy", "grade" : 59}, {"name" : "Justin", "grade" : 100}]

class3 = [{"name" : "Miles", "grade" : 100}, { "name" : "idioto", "grade" : 76},
          {"name" : "stupid", "grade" : 59}, {"name" : "David", "grade" : 100}]


#collection.delete_many({"name" : "Otis", "grade" : 59})
collection.insert_many([student for student in class1])
students = collection.find({})
for i in students:
    print(i)

# all_classes = [{class1}, {class2}, {class3}]
#
# # print each class individually
# all_classes_list = [a_class for a_class in all_classes]
# print(all_classes_list)
# print(2 * "\n")
#
# # print a list of all the names in the class
# names = [a_class["names"] for a_class in all_classes]
# print(names)
# print(2 * "\n")
#
# # print a list of all names with grade equal to 100
# names_100 = [smart for smart in all_classes if smart["grade"] = 100]