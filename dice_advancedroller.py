import random
def main():

 dice_rolls = int(input('How many die you want to roll?'))
 dice_sum = 0
 dice_size = int(input('How many sides you want on your dice?'))

 for i in range(0, dice_rolls):                                      
 
  
  roll = random.randint(1,dice_size)                      
  dice_sum = dice_sum + roll 
  if roll == 1:
    print(f'You rolled a {roll}! Critical Fail')
  elif roll == dice_size:
    print(f'You rolled a {roll}! Critical Success!')
  else:                     
    print(f'You rolled a {roll}')                  

 print(f'You rolled a total of {dice_sum}')

if __name__== "__main__":
  main()