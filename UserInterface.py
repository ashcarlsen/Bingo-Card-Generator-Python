from math import floor  	         	  

from Deck import Deck  	         	  
from Menu import Menu  	         	  
from MenuOption import MenuOption  	         	  


class UserInterface():  	         	  
    """  	         	  
    Provide the UserInterface for the program, which consists of the Main menu and the Deck menu  	         	  

    Also provides methods for accepting and validating user input  	         	  
    """  	         	  

    def __init__(self):  	         	  
        self.__m_currentDeck = None  	         	  
        self.__m_menu = Menu("Main")  	         	  
        self.__m_menu += MenuOption("C", "Create a new deck")  	         	  
        self.__m_menu += MenuOption("X", "Exit the program")  	         	  

    def run(self):  	         	  
        """  	         	  
        Return None: present the main menu to the user  	         	  

        Repeatedly prompt for a valid command until good input is given, or the program is exited  	         	  
        """  	         	  
        print("Welcome to the Bingo Deck Generator\n")  	         	  

        while True:  	         	  
            command = self.__m_menu.prompt()  	         	  
            if command.upper() == "C":  	         	  
                self.__create_deck()  	         	  
            elif command.upper() == "X":  	         	  
                break  	         	  

    def __deck_menu(self):  	         	  
        """  	         	  
        Return None  	         	  

        Present the deck menu to user until a valid selection is chosen  	         	  
        """  	         	  
        menu = Menu("Deck")  	         	  
        menu += MenuOption("P", "Print a card to the screen")  	         	  
        menu += MenuOption("D", "Display the whole deck to the screen")  	         	  
        menu += MenuOption("S", "Save the whole deck to a file")  	         	  
        menu += MenuOption("X", "Return to the Main menu")  	         	  

        while True:  	         	  
            command = menu.prompt()  	         	  
            if command.upper() == "P":  	         	  
                self.__print_card()  	         	  
            elif command.upper() == "D":  	         	  
                print(self.__m_currentDeck)  	         	  
            elif command.upper() == "S":  	         	  
                self.__save_deck()  	         	  
            elif command.upper() == "X":  	         	  
                break  	         	  

    def __get_str(self, prompt):  	         	  
        """  	         	  
        Return a string: non-empty input entered by the user  	         	  

        Take a prompt string as input  	         	  
        Repeat the prompt until a non-empty string is provided  	         	  
        """ 
        print(prompt)
        inp = input()
        while inp == None:
            print(prompt)
            inp = input() 
        return inp

    def __get_int(self, prompt, lo, hi):  	         	  
        """  	         	  
        Return an integer: validated integer input by user  	         	  

        Take a prompt string, low and high integers as input  	         	  
        Repeat the prompt until an integer that is in-range is provided  	         	  
        """
        print(prompt)
        inp = input()
        while inp.isdigit() == False:
            print(prompt)
            inp = input()
        inp = int(inp)
        while inp < lo or inp > hi:
            print("Invalid Range")
            print(prompt)
            inp = input()
            inp = int(inp)
        return inp  	         	  

    def __create_deck(self):  	         	  
        """  	         	  
        Return None: Create a new Deck  	         	  

        The Deck is stored in self.__m_currentDeck  	         	  
        """
        low = 3
        hi = 16
        card_Size = self.__get_int("Enter the size of the card (N x N)(Min of 3, Max of 16): ", low, hi)
        numOFcards = self.__get_int("Enter the number of cards in the deck(Min of 2, Max of 8192): ", 2, 8192)
        maxSize = self.__get_int("Enter maximum value to be included onto the cards (100 would allow 1-100 to be used on card)(Min of 1, Max of 999).\nValue must be greater than two times the card size squared or else it will default to that value: ", 1, 999)
        deck = Deck(card_Size, numOFcards, maxSize)
        self.__m_currentDeck = deck
        self.__deck_menu()

    def __print_card(self):  	         	  
        """  	         	  
        Return None: Print one Card from the Deck  	         	  

        Prompt user for a Card ID  	         	  
        """
        cardID = self.__get_int("Enter the position of the card in the deck (starting at 1): ", 1,len(self.__m_currentDeck))
        print(self.__m_currentDeck.card(cardID))
          	         	  

    def __save_deck(self):  	         	  
        """  	         	  
        Return None: Save a Deck to a file  	         	  

        Prompt user for the name of file to write the entire Deck into  	         	  
        """
        tempName = self.__get_str("Enter file name for deck to be saved: ")
        file = open(tempName, "w")
        print(self.__m_currentDeck, file=file)
        file.close()
        


























        
