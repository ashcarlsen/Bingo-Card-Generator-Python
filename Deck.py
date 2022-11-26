from Card import Card  	         	  
from RandNumberSet import RandNumberSet  	         	  


class Deck():  	         	  
    def __init__(self, card_size, num_cards, max_num):  	         	  
        """  	         	  
        Deck constructor  	         	  
        """  	     
        self.__cardSet = []
        self.__deckSize = num_cards
        self.__maxNumber = max_num
        for num in range(0, num_cards):
            numbSet = RandNumberSet(card_size, max_num)
            card = Card(num, numbSet)
            self.__cardSet.append(card)

    def __len__(self):  	         	  
        """  	         	  
        Return an integer: the number of cards in this deck  	         	  
        """ 
        return self.__deckSize       	  

    def card(self, n):  	         	  
        """  	         	  
        Retrieve Card N from the deck  	         	  
        """
        if n == 0:
            return None
        if n > len(self.__cardSet):
            return None
        return self.__cardSet[n-1]  	         	  

    def __str__(self):  	         	  
        """  	         	  
        Return None: Display the entire Deck as a string  	         	  
        """
        string = ""
        for card in self.__cardSet:
            string += card.__str__()
            string += "\n"
        return string
