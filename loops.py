valid_input = False
while valid_input == False:
  gender = input('What is your gender?\nType M for Male\nType F for Female\n').upper()
  if gender == 'M':
    print('Hello son of Adam')
    valid_input = True
  elif gender == 'F':
    print('Hello daughter of Eve')
    valid_input = True
  else:
    print('Wrong input, try again!')
else:
  print('Thanks for providing your gender')


# using break to get out of a loop
valid_number = False
while valid_number == False:
  user_num = int(input('Pick a number from 1 to 6\n'))
  if user_num >= 1 and user_num <= 6:
    print("Thank you for playing. Your number is: " + str(user_num))
    print('Displaying all numbers from 0 to ' + str(user_num))
    break
  else:
    print('Please select a number between 1 and 6')

# for loop
for num in list(range(user_num+1)):
  print(num)

print()

# use loop on string
for my_letter in 'Tobi Amira':
  print(my_letter)

print()

class_mates = ['John', 'Jane', 'Jimmy', 'Joseph', 'Jasmine']

# iterate through the classmates themselves
for class_mate in class_mates:
  print(class_mate)

# iterate through the classmates using their indexes
for i in range(len(class_mates)):
  print(class_mates[i])

# using else with loops
numbers = (12, 17, 24, 31, 49)
for number in numbers:
  if number % 5 == 0:
    print('number is divisible by 5')
    break
else:
  print('no number was divisible by 5')