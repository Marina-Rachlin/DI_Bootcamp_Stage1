from  game import Game

def get_user_menu_choice():
    user_choice = input('Menu: \n (g) Play a new game \n (s) Show scores \n (x) exit \n : ')
    if user_choice.lower() in ['g', 's', 'x']:
        return user_choice.lower()
    
def print_results(results): 
    print("Game Results:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}") 
    
def main():
    results = {'win': 0,  'loss' : 0, 'draw': 0}
    while True:
        user_choice = get_user_menu_choice()
        if user_choice == 'g':
            new_game = Game()
            result = new_game.play()
            if result == 'win':
                results['win'] += 1
            elif result == 'loss':
                results['loss'] += 1
            else:
                results['draw'] += 1
        elif user_choice == 's' :
            print_results(results) 
        else:
            print_results(results)
            print("Thank you for playing!")  
            break      

    

# print(get_user_menu_choice())
new_game = main()

