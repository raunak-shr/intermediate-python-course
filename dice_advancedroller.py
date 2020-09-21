import random
def main():

 name1 = str(input('Enter your name'))
 dice_rolls = int(input('How many die you want to roll?'))
 dice_sum1 = 0
 dice_size = int(input('How many sides you want on your dice?'))

 for i in range(0, dice_rolls):                                      
 
  roll = random.randint(1,dice_size)                      
  dice_sum1 = dice_sum1 + roll 
  if roll == 1:
    print(f'You rolled a {roll}! Critical Fail')
  elif roll == dice_size:
    print(f'You rolled a {roll}! Critical Success!')
  else:                     
    print(f'You rolled a {roll}')                  

 print(f'{name1} rolled a total of {dice_sum1}')

# Player 2 Starts

 name2 = str(input('Enter your name'))
 
 dice_sum2 = 0
 

 for i in range(0, dice_rolls):                                      
 
  roll = random.randint(1,dice_size)                      
  dice_sum2 = dice_sum2 + roll 
  if roll == 1:
    print(f'You rolled a {roll}! Critical Fail')
  elif roll == dice_size:
    print(f'You rolled a {roll}! Critical Success!')
  else:                     
    print(f'You rolled a {roll}')                  

 print(f'{name2} rolled a total of {dice_sum2}')

 if dice_sum1>dice_sum2:
  print(f'{name1} wins by a lead of {dice_sum1-dice_sum2}')
 elif dice_sum2>dice_sum1:
  print(f'{name2} wins by a lead of {dice_sum2-dice_sum1}')
 else:
  print(f'Its a draw between {name1} and {name2}') 

if __name__== "__main__":
  main()