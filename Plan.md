# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

*	The program will provide a user manual showing how to use this program. It will use a User Interface to interact
*	with the user. The user will input what needs to be done with the program. Once the user has specified what needs to be done
*	the program will either create, save, or delete a bingo card. 

## Phase 1: System Analysis *(10%)*

*	This program will take user input as data. The user will use the UI to input what needs to be done throughout the program
*	The output will be printed either to the screen or input into a file if the user wants the deck saved
*	The algorithms needed for this program is a random number generator in a range
*	There will also need to be an algorithm to save output to a file
*	Also will need an algorithm to loop through the UI until exiting


## Phase 2: Design *(30%)*

**Deliver:**

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.

### Functions

#### RandNumberSet

	*	init(self, nSize, nMax):
		set the size
		check that the size if valid
		check that the max number is at least the size squared #if not then there won't be enough numbers to fill the whole board
		use int division to create the segment size.
		for the range from 1 to number of rows
			add a list of numbers in order to segments list
			increment the range to keep adding up segments to the segments
		set the self.segments once finished
		
	*	len(self)
		return the size of the number set
	
	*	getitem(self, n)
			if in index range
				return the n'th row of Bingo numbers 
			else 
				throw index error
				
	*	shuffle(self)
			for each segment
				shuffle the numbers in the segment (using random)
			reset row position
	
	*	next_row(self)
			if row position is out of bounds
				return None
			for each segment
				add that row to temp list
			increment position
			return row

	*	str(self)
			for each segment
				add the segment (cast as a string) to a list
			return the string list
	
#### Card 

	*	init(self, idnum, ns):
	
		initialize idnum and the number set
		for size of number set
			add segment to columns of card
			
	*	id(self)
			return id number
		
	*	number_at(self,row,col)
			return the row index of the card column selected
	
	*	len(self)
			return numberSet size
			
	*	str(self)
			return a formatted string with columns and 
			
#### Deck

	*	init(self, card_size, num_cards, max_num)
			initialize list of cards
			for num of cards
				initialize numberset with max_num and card_size
				initialize card using index as card id
	
	*	len__car(self)
			return size of the deck (size of cardSet list)
			
	*	card(self, n)
			return n index of cardSet list
			
	*	str(self)
			for each card in deck
				add card string to a fomrmatted string 
			return formatted string
			
#### UserInterface

	*	init(self)
			initialize current working deck
			initialze menu
			add 2 menu options to the menu
	
	*	run(self)
			print welcome statement
			loop until break
				run menu prompt and get correct input
				if command is a C
					create a deck
				elif the command is an X
					exit the program
	*	deck_menu(self)
			create a new menu
			add print option
			add display for entire deck option
			add save option
			add exit to main menu option
			
	*	get_str(self, prompt)
			print prompt
			get input
			while input is not empty
				print prompt
			return input
			
	*	get_int(self, prompt, lo, hi)
			print prompt 
			get input
			while input is less than lo or higher than hi
				print prompt
				get input
			return input
			
	*	create_deck(self)
		print prompt to get a string name of deck
		store input 
		print prompt to get a number of cards 
		store input
		print prompt to get a size of cards
		store input 
		print prompt to get a max size 
		for num of cards
			create number set with max size
			create card with number set setting id to index number
		store deck into currentDeck
		
	*	print_card(self)
			run get_int to store an int inside the index of currentDeck
			print the string representation of that card in the deck
			
	*	save_deck(self)
			run get_str to prompt for a file name
			open the file in current working directory
			for each card in deck
				output formatted string to file
		
			
## Phase 3: Implementation *(15%)*

**Deliver:**

*	The implementation went smoothly.
*	I didn't have to change any class methods
*	Changed a few names around in order to clarify for myself.

### Interesting Things

*	I struggled at first to grasp what the number set was doing
*	Once I realized how it worked the code was easily written and tested.
*	Had a few issues with the Free! square on odd cards.
*	I forgot that // is for integer division in python.
*	I took awhile to format the Card string; however, it turned out very nicely
*	I had to update the range of the maximum number taken into the cards. Anything lower than 2 * max^2 would have an access violation
*	I forgot to add self. before accessing a member inside the RandNumberSet class.


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.

### Test Cases

*	I wrote some source code to print out the number set after being created. It helped to see exactly which numbers were in which locations.
*	I then wrote print statements that showed me the 2d array of rows and columns within the card class. This made sure I was getting the correct implementation from the number set.
*	I then ran the runTests.py script in order to check for several different things. Originally I had 3 main errors. My free square was not showing up. However, when printed, the cards did have the free square.
*	I had a bug within the method that returned a specific location of the card. This was causing the test to fail.
*	I also had to fix a bug that would allow me to access cards within a deck. I forgot to bound the upper and lower indexes of the deck. Therefore, I was trying to access cards that were not there.
*	The last bug I encountered was in the main menu. The functions that would get a string or int would continually loop forever. I had to make sure the input was the right type before returning it.


## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.

*	Pushed repo and made sure the program runs from command line

## Phase 6: Maintenance


*	I feel like the program is neatly written. The hardest part for me to understand was the RandNumberSet class that was given. However, after doing some testing with this class.
*	I was able to understand how the  class generated and stored it's variables.
*	I believe that I would be able to find a bug inside of this program fairly easily once reported. Now that I understand the basic structure, I would be able to quickly see where it was going wrong.
*	I think my documentation will make sense to most people. The design is fairly straight forward. 
*	I think that in 6 months I would be able to jump right back into this program and add to it. It's fairly straight forward and has a basic class structure.
*	I believe I can add things in with other classes very easily. 
*	This program should work on every piece of hardware or OS used. Nothing should change once the next version of python is added. 




