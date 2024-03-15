#A journey through the solar system

print('''Welcome to your journey to a foreign planet. 
\nIn this journey, you will face many different decisions that will directly affect your outcome.
\nCan you survive?
\n(Answer all multiple choice questions with the corresponding number)\n''')

start = int(input('Type 1 to start. --> '))
if start == 1:
  print('\nAh, I see you have decided to proceed with your adventure. Good luck!')
  print('\nLets name your spacecraft.\n')
else:
  print('\nToo bad.')
  exit()
  
ship = input('--> The ')

print('\nNow we can leave in the', ship ,'and explore the night sky.')

print('\nYour first decision will be to decide where we are going.')
print('1) Jupiter\n2) Mars\n3) Venus\n4) Saturn')
c1 = int(input('--> '))
if c1 == 1:
  ch = "Jupiter"
  print('\nAh the gas giant Jupiter. Great Choice.')
elif c1 == 2:
  ch = "Mars"
  print('\nMars, the red planet. Our closest neighbour.')
elif c1 == 3:
  ch = "Venus"
  print('\nVenus. Interesting choice.')
elif c1 == 4:
  ch = "Saturn"
  print('Saturn. The planet with many rings.')
else:
  print('Wrong input.')
  exit()

key = 0

print('\nOn your way to', ch ,'you encounter a strange vehicle. Do you investigate?')
print('1) Yes\n2) No')
c2 = int(input('--> '))
if c1 == 3 and c2 == 2:
  print('''\nThe vehicle was full of beings from''',ch+'''.
They saw you avoid them so they chased after you and blew up the''',ship+'''. You died.''')
  exit()
elif c1 > 1 and c2 == 1:
  print('\nThe vehicle was empty. Keep moving')
elif c1 <= 2 and c2 == 2:
  print('\nYou drive right past the vehicle. Boring!')
elif c2 > 2:
  print('Wrong input.')
  exit()
elif c1 > 1 and c2 == 2:
  print('\nYou drive straight past the vehicle. Boring!')
else:
  print('\nYou find a key in a box. This could come in useful later.')
  key = 1

fb = 0
al = 0
kl = 0
stf = 0
ckey = 0

print('\nYou land on', ch,'and it looks uninhabited. Do you...')
print('1) Explore a cave\n2) Explore the surface\n3) Explore the ocean')
c3 = int(input('--> '))
if c1 >= 3 and c3 <=2:
  print('\nYou find nothing yet but keep searching in hopes of finding something.')
  stf = 1
elif c1 == 1 and c3 == 1:
  print('\nYou find a dead body in here. The air around you becomes colder. Best if you leave now.')
  fb = 1
elif c1 == 3 and c3 == 2:
  print('\nYou find aliens roaming the surface. Keep a safe distance.')
  al = 1
elif c3 > 3:
  print('\nWrong input.')
  exit()
elif key == 1:
  print('\nYou find a box with a keyhole that fits the key you found on the vehicle. Do you open it?')
  print('1) Yes\n2) No')
  ckey = int(input('--> '))
else:
  print('\nYou find nothing so far but keep looking.')
  kl = 1

east = 0

if ckey == 1:
  print('\nYou found the Easter Egg. Congratulations.')
  east = 1
elif ckey == 2:
  print('''\nWho would find the key and not open the chest. Disappointing.
  \nI am sending you back to Earth for that.''')
  exit()


print('\nYou hear noises in the distance. Do you leave or do you investigate further...')
print('1) Investigate further \n2) Leave')

c4 = int(input('--> '))

egg = 0
tc = 0 

if fb == 1 and c4 == 1:
  print('\nIt was a trap. You were eaten by a strange creature.')
  exit()
elif fb == 1 and c4 == 2:
  print('\nYou left. This was the right choice. You fly back to Earth on the',ship+'.')
  exit()
elif al == 1 and c4 == 1:
  print('\nYou find a weird egg, taking it might have consequences...')
  egg = 1
elif al == 1 and c4 == 2:
  print('\nYou fly back to Earth on the',ship+'.')
  exit()
elif kl == 1 and c4 == 1:
  print('\nYou find a terrifying creature and it starts to chase you.')
  tc = 1
elif kl == 1 and c4 == 2:
  print('\nYou fly back to Earth on the',ship+'.')
  exit()
elif stf == 1 and c4 == 1:
  print('\nYou find the nesting ground of aliens. They eat you alive.')
  exit()
elif stf == 1 and c4 == 2:
  print('\nRight choice. It isnt safe on this planet. You fly back to Earth on the',ship+'.')
  exit()
elif east == 1:
  print('''\nWith the Easter Egg there isnt really much point in playing anymore.\n
You head back to Earth with your head held high.''')
  exit()

egg2 = 0
tc2 = 0

if egg == 1:
  print('''\nYou make it back to the''',ship+'''but the egg starts to hatch.
  \nDo you leave it here or take it with you?''')
  print('1) Leave it here\n2) Take it with you')
  egg2 = int(input('--> '))
elif tc == 1:
  print('''\nYou try to run back to the''',ship+'''. Its surrounded by creatures.
  \nDo you make a break for it or stay and fight''')
  print('1) Make a break for it\n2) Stay and fight.')
  tc2 = int(input('--> '))

if egg2 == 1:
  print('\nLeaving it here was the right choice. You would have been eaten otherwise.')
  print('\nYou fly back to Earth on the',ship+'.')
  exit()
elif egg2 == 2:
  print('\nThe creature hatched and ate you.')
  exit()


if tc2 == 1:
  print('\nYou somehow avoid all of the creatures. You survived and fly back to Earth.')
  exit()
if tc2 == 2:
  print('\nWho would stay and fight💀. You were decimated.')
  exit()