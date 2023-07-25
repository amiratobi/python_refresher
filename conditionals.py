age = int(input('How old are you?\n'))
if age <= 40:
  print('You are young')
else:
  print('You are not young')

score = int(input('What was your score?\n'))
if score >= 80:
  print('You did very well!')
elif score >= 60:
  print('You did okay')
else:
  print('You can do better!')

gender = input('What is your gender?\nType M for Male\nType F for Female\n')
if gender == 'M':
  print('Thanks for coming')
elif gender == 'F':
  is_pregnant = input('Are you pregnant?\nType Y for Yes\nType N for No\n')
  if is_pregnant == 'Y':
    print('Hope you deliver safely')
  elif is_pregnant == 'N':
    print('Okay. No further checks')
  else:
    print('Wrong input start again')
else:
  print('Wrong input, start again')