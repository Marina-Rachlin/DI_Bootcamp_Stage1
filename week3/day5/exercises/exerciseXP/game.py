import random 

class Game():

    def get_user_item(self):
        while True:
            user_item = input("Select (r)ock, (p)aper or (s)cissors): ")
            if user_item.lower() in ['r', 'p', 's']:
                return user_item.lower()
            else:
                print("Invalid input.")

    def get_computer_item(self) :
        computer_item = random.choice(['r', 'p', 's'])   
        return computer_item   

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'draw'
        elif (user_item == 'rock' and computer_item == 'scissors') or \
                (user_item == 'paper' and computer_item == 'rock') or \
                (user_item == 'scissors' and computer_item == 'paper'):
            return 'win'
        else:
            return 'loss'
        

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result( user_item, computer_item)
        print(f"You selected {user_item}. The computer selected {computer_item}. You {result}. ")
        return str(result)
        

                

game = Game()
# game.get_user_item()
# print(game.get_computer_item())
# print(game.get_game_result(game.get_user_item(), game.get_computer_item()))
# game.play()



