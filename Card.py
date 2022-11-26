class Card():  	         	  
    COLUMN_NAMES = list("BINGODARLYZEMPUX")  	         	  

    def __init__(self, idnum, ns):  	         	  
        """  	         	  
        Initialize a Bingo! card  	         	  
        """ 
        self.size = ns.card_Size
        self.__m_idnum = idnum
        self.__m_numberSet = ns
        self.rows = []
        vector = ns.next_row()
        while vector != None:
            self.rows.append(vector)
            vector = ns.next_row()
        if self.size % 2 != 0:
            middle = self.size // 2
            self.rows[middle][middle] = "Free!"
            
            
    def id(self):  	         	  
        """  	         	  
        Return an integer: the ID number of the card  	         	  
        """ 
        return self.__m_idnum 	         	  

    def number_at(self, row, col):  	         	  
        """  	         	  
        Return an integer or a string: the value in the Bingo square at (row, col)  	         	  
        """
        return self.rows[row][col]  	         	  

    def __len__(self):  	         	  
        """  	         	  
        Return an integer: the length of one dimension of the card.  	         	  
        For a 3x3 card return 3, for a 5x5 return 5, etc.  	         	  
        """  
        return self.size      	  

    def __str__(self):  	         	  
        """  	         	  
        Return a string: a neatly formatted, square bingo card  	         	  
        """
        string = "Card #" + str(self.__m_idnum+1) + '\n'
        string += "   "
        for num in range(0,self.size):
            string += self.COLUMN_NAMES[num]
            string += '     '
        string +='\n'
        for num in range(0, self.size):
            string += "+-----"
        string += "+\n"
        for column in range(0, self.size):
            for num in range(0, self.size):
                if self.rows[column][num] != "Free!":
                    temp = "|" + "{:3}".format(self.rows[column][num]) + "  "
                else:
                    temp = "|" + "{:2}".format(self.rows[column][num])
                string +=temp
            string += "|\n"
            for num in range(0, self.size):
                string += "+-----"
            string += "+\n"
        return string  	         	  
