x = 70
print(x)
# y = input("What is your name:")
# print("My name is", end=" ")
# print(y)


name, age, height = "Tobi Amira", 30, 180.0
print(name)
print(age)
print(height)

greeting = "Hello World!"
print(greeting[0]) #expecting g
print(greeting[0:5]) #expecting hello
print(greeting[6:11]) #expecting world

# lists are arrays and can contain multiple data types
class_mates = ['John', 'Jane', 'Jimmy', 'Joseph', 'Jasmine']
new_class_mates = ['James', 'Joan']
print(class_mates[0:2])
print(class_mates + new_class_mates)

# tuples are arrays but are read only
scores = (89, 91, 78, 82, 90)
new_scores = (87, 88)
print(scores)
print(scores + new_scores)
print(scores[2:4])

# dictionaries are like objects
bio_data = {}
bio_data['name'] = 'James Smith'
bio_data[2] = 25
print(bio_data)

book_info = {'author': 'Ryan Kenoly', 'title': 'Learning Python', 'released': 1992, 'price':10.99}
print(book_info)
print(book_info['price'])
print(book_info.values())
print(book_info.keys())