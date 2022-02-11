from secret_word import SecretWord
from parachuter import Parachuter


class Jumper: 
    
    def __init__(self):
        self.parachuter = Parachuter()  # We obtain the the picture of parachuter
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
            
            self.print_jumper()
            self.input_user()
            self.mistakes_counter()  
            self.guess_letters()
            self.print_letters()
            self.winner()
            
        self.loser()      
                
        
    def hide_letters (self): #Get a random word from a list and hide the letters with underscores 
        self.word = self.secret_word.get_random_word()  #We get a random word 
        
        #print(self.word)
        
        for i in self.word:
            self.list_letters.append(i)
            self.list_underscore.append("_")

    def input_user (self):   #Ask the user enter a guess letter and 1save them into self.list_user_letters 
        print()
        self.input_user_letter = input(" Guess a letter (a-z): ")
        self.list_user_letters.append(self.input_user_letter)  #Save the letters choosen in a list to avoid to choose the same later 
        
    
        return self.list_user_letters
    
    def guess_letters(self):
            
        self.counter = self.word.count(self.input_user_letter)
        #print(self.counter)
     
        for i in range (self.counter):
            for i in self.list_letters:
                if i == self.input_user_letter:
                    index = self.list_letters.index(i)
                    self.list_letters[index] = " _ "
                    self.list_underscore[index] = i
        print()
    
    def mistakes_counter(self):
        if self.input_user_letter not in self.list_letters:
            self.mistakes = self.mistakes + 1   
        return self.mistakes 
    
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
    
    def print_jumper(self):
        
        if self.mistakes == 0:
            self.parachuter.draw_0()
        elif self.mistakes == 1:
            self.parachuter.draw_1()
        elif self.mistakes == 2: 
            self.parachuter.draw_2()
        elif self.mistakes == 3: 
            self.parachuter.draw_3()
        elif self.mistakes == 4: 
            self.parachuter.draw_4()        
      
    def loser(self):
        if self.mistakes == 4:
            print("________________________________")
            print()
            print("** Sorry, you lose :(, try again **")
            print()
            print("________________________________")          

prove1 = Jumper()
prove1.start_game()
