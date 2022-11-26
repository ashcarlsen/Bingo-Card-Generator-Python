# Bingo! User Manual  	         	  

1. Run Program
2. Main Menu will appear:
	*	Type C to create a deck
	*	Type X to close the program
3. Deck Created "C command"
	*	Size prompt will appear:
		*	must be between 3 and 16
		*	Prompt shows range and format of cards N x N
	*	Input desired size
	*	Number of cards prompt will appear:
		*	Menu will show range from 0 - 100 cards
	*	Input desired number of cards
	*	Max card value prompt will appear
		*	Menu will ask the maximum value to appear on cards
		*	0-999 range will be shown
		*	Example that 100 would allow 1-100 to be allowed on cards
	*	Input desired maximum value
	*	DECK CREATED
		*	Deck main menu appears
			*	Deck main menu will repeat until "X" is pressed
			*	Pushing "P" will allow you to print a single card
				*	prompt will ask for a position in the deck starting at 1
				*	will only allow valid range between 1 and the last card in the deck
			*	Pushing "D" will print the entire deck to the screen
			*	Pushing "S" will allow you to save the deck to a file
				*	prompt will run for file name
				*	deck will be saved into the current directory under that file name
			*	Pushing "X" will allow you to return to the main menu
			***Once pressing X the current deck will be forgotten unless saved to a file***