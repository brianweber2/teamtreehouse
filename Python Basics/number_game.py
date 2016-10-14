import random


rand_num = random.randint(1, 10)
guessed_nums = []
allowed_guesses = 5

while len(guessed_nums) < allowed_guesses:
  guess = input("\nGuess a number between 1 and 10: ")
  
  try:
    player_num = int(guess)
  except:
    print("That's not a whole number!")
    break
    
  if not player_num > 0 or not player_num < 11:
    print("That number isn't between 1 and 10!")
    break
    
  guessed_nums.append(player_num)
  
  if player_num == rand_num:
    print("You win! My number was {}.".format(rand_num))
    print("It took you {} tries.".format(len(guessed_nums)))
    break
  else:
    if rand_num > player_num:
      print("Nope! My number is higher than {}. Guess #{}".format(
        player_num, len(guessed_nums)))
    else:
      print("Nope! My number is lower than {}. Guess #{}".format(
          player_num, len(guessed_nums)))
    continue
    
if not rand_num in guessed_nums:
  print("\nSorry! My number was {}.".format(rand_num))