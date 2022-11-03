from random import randint

print("Welcome to Python Casino")
pc_choice = randint(1,100)

playing = True

while playing:
  user_choice = int(input("Choose number(1-100):\n"));
  if user_choice==pc_choice:
    print("You Win!")
    playing = False
  elif user_choice>pc_choice:
    print("Lower!")
  else:
    print("Higher!")