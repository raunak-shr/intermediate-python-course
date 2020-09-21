import random
def main():

 dice_rolls = 2
 dice_sum = 0


 for i in range(0, dice_rolls):                                      
 
  
  roll = random.randint(1,6)                      
  dice_sum = dice_sum + roll 
                       
  print(f'You rolled a {roll}')                     

 print(f'You rolled a total of {dice_sum}')

if __name__== "__main__":
  main()


#EXPLANATION OF THE CODE 

#dice_rolls-->no. of times dice will be rolled
#dice_sum-->variable for finally adding the outcome of every roll

#roll = 3
#dice_sum(0) = dice_sum(0) + roll(3) = 3
#print roll(3)
#go up
#roll = 4
#dice_sum(3) = dice_sum(3) + roll( now 4) = 7
#print roll(4)
#2 times done-->exit loop
#print dice_sum(now 7)
  