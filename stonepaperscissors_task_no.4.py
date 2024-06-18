import random
class StonePaperScissors:
    def __init__(self) :
       self.user_score=0
       self.computer_score=0
    def get_user_choice(self):
        while True:
            user_choice=input("Choose one:stone,paper or scissors:").strip().lower()
            if user_choice in['stone','paper','scissors']:
                return user_choice
            else:
                print("Invaild choice!Please choose again.")
    def get_computer_choice(self):
        choices=['stone','paper','scissors']
        return random.choice(choices)
    def determine_winner(self,user_choice,computer_choice):
        if user_choice==computer_choice:
            return"It is a tie!",0,0
        elif (user_choice=='stone' and computer_choice=='scissors') or\
             (user_choice=='paper' and computer_choice=='stone') or \
             (user_choice=='scissors' and computer_choice=='paper'):
            return"You win!",1,0
        else:
            return"Computer wins!",0,1    
    def play_game(self):
        print("Welcome to the Stone,Paper,Scissors game!")
        while True:
            start_game=input("Do you want to start the game?(yes \\ no):").strip().lower()
            if start_game!='yes':
                print("Goodbye!")
                return
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(f"You chose:{user_choice}")
            print(f"Computer chose:{computer_choice}")
            result, user_point, computer_point=self.determine_winner(user_choice,computer_choice)
            print(f"Before updating scores: User Score= {self.user_score}, Computer Score= {self.computer_score}")
            self.user_score+=user_point
            self.computer_score+=computer_point
            print(f"After updating scores:User Score= {self.user_score},Computer Score= {self.computer_score}") 
            print(result)
            print(f"score-You: {self.user_score},Computer:{self.computer_score}")
            play_again=input("Do you want to play again?(yes \\ no):").strip().lower()
            if play_again !='yes':
                 break
        print("Final Score:")
        print(f"You:{self.user_score},Computer:{self.computer_score}")
        print("Thanks for playing")
if __name__ == "__main__":        
   game=StonePaperScissors()
   game.play_game()
