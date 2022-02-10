from secret_word import SecretWord
from parachuter import Parachuter


class Jumper: 
    
    def __init__(self):
        #self.parachuter = Parachuter()  # We obtain the the picture of parachuter
        self.secret_word = SecretWord() #We obtain a random word 
        self.list_letters = [] 
        self.list_underscore = []
        self.list_user_letters = []
        self.validate_responses = False
        self.mistakes = 0
        self.counter_winner =  10
        
    def start_game(self):
        
        self.secret_word.type_word()
        self.hide_letters()
        self.print_letters()
        while self.mistakes !=4 and self.counter_winner != 0:
            self.draw()
            self.input_user() 
            self.guess_letters()
            self.print_letters()
            self.winner()
        self.draw()    
                
        
    def hide_letters (self): #Get a random word from a list and hide the letters with underscores 
        self.word = self.secret_word.get_random_word()  #We get a random word 
        
        print(self.word)
        
        for i in self.word:
            self.list_letters.append(i)
            self.list_underscore.append("_")

        print(self.list_letters)
        print(self.list_underscore)

    def input_user (self):   #Ask the user enter a guess letter and save them into self.list_user_letters 
        print()
        self.input_user_letter = input(" Guess a letter (a-z): ")
        self.list_user_letters.append(self.input_user_letter)  #Save the letters choosen in a list to avoid to choose the same later 
        
    
        return self.list_user_letters
    
    def guess_letters(self):
            
        self.counter = self.word.count(self.input_user_letter)
        #print(self.counter)
        
        if self.input_user_letter not in self.list_letters:
            self.mistakes = self.mistakes + 1   
            
        for i in range (self.counter):
            for i in self.list_letters:
                if i == self.input_user_letter:
                    index = self.list_letters.index(i)
                    self.list_letters[index] = " _ "
                    self.list_underscore[index] = i
        
        print()
    
    def winner (self):
        
        self.counter_winner = self.list_underscore.count("_")
        
        if self.counter_winner == 0:
            print("________________________________")
            print()
            print("** Congratulations!! You win **")
            print()
            print("________________________________")    
    
    def print_letters(self):
        
        for i in self.list_underscore:
            print(f" {i} ", end="")            

        print()
    
    def draw(self):
        if self.mistakes == 0:        
            print("      _____   ")
            print("    / _____ \ ")
            print("    \       / ")
            print("     \     / ")
            print("       😀    ")
            print("      / | \  ")
            print("       / \  ")
            print()
            print("   ^^^^^^^^^^  ")
        
        if self.mistakes == 1:
            print()
            print("    / ____  \ ")
            print("    \       / ")
            print("     \     / ")
            print("       😕    ")
            print("      / | \  ")
            print("       / \  ")
            print()
            print("   ^^^^^^^^^^  ")
        elif self.mistakes == 2:
            print()
            print("             ")
            print("    \       / ")
            print("     \     / ")
            print("       😬    ")
            print("      / | \  ")
            print("       / \  ")
            print()
            print("   ^^^^^^^^^^  ")
           
        elif self.mistakes == 3: 
            print()
            print("             ")
            print("             ")
            print("     \     / ")
            print("       😩   ")
            print("      / | \  ")
            print("       / \  ")
            print()
            print("   ^^^^^^^^^^  ")
        
        elif self.mistakes == 4: 
            print()
            print("             ")
            print("    Game Over")
            print("             ")
            print("       💀    ")
            print("      / | \  ")
            print("       / \  ")
            print()
            print("   ^^^^^^^^^^  ")
        return self.mistakes      
              
prove1 = Jumper()
prove1.start_game()