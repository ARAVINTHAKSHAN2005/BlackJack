#Importing Random Library 
import random

#Defining Variables 
Suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
Ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
Values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

#Creating Card Class
class Card():
    def __init__(self,suit,rank):
        # Suit 
        self.suit = suit 
        # Rank
        self.rank = rank 
        # Corresponding Value  by indexing
        self.value = Values[rank]
    
    #returns rank of suit if printed 
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    #Creates an empty list to which all cards are appended to
    def __init__(self):
        self.all_cards = []
        #The double for loop creates 13 ranks for each Suit
        for suit in Suits:
            for rank in Ranks:
                #Create the Card Object
                created_card = Card(suit,rank)
                #Appends the created cards one by one to the list.
                self.all_cards.append(created_card)
                
    def __str__(self):
        deck_comp = ''
        for card in self.all_cards:
            deck_comp += '\n' + card.__str__()
        return "The deck has:  " + deck_comp
            
    def shuffle(self):
        #Shuffles the list containing the cards
        random.shuffle(self.all_cards)
   
    def deal(self):
        #pops the item of a list based on the index specified
        single_card = self.all_cards.pop()
        return single_card 

#Creating Hand Class that refers to the cards in Player and Dealer's Hand
class Hand():
    def __init__(self):
        self.cards = []  # starting with an empty list
        self.value = 0   # starting  with zero value
        self.aces = 0    # adding an attribute to keep track of aces
    
    def add_card(self,card):
        #After appending cards to Hand, Value of Hand is also modified.
        self.cards.append(card)
        self.value = self.value + card.value
        
        if card.rank == 'Ace':
            self.aces += 1
            
    def adjust_for_ace(self):
        #If the value of hand exceeds 21 because ace value is taken as 11, subtract 10 from the total value. 
        while self.value > 21 and self.aces:
            self.value -= 10 
            self.aces -= 1 

#Creating a Chips Class 
class Chips():
    #Default chips is 100 
    def __init__(self, total = 100):
        self.total = total  # This can be set to a default value or supplied by a user input later on if required 
        self.bet = 0
    
    #Tp add chips if won 
    def win_bet(self):
        self.total += self.bet 
    
    #To subtract chips if lost 
    def lose_bet(self):
        self.total -= self.bet

#Function that asks users for how much he is willing to bet
def take_bet(chips):
    
    while True:
        
        try:
            chips.bet = int(input("\nHow many chips would you like to bet? :"))
        except:
            print("Sorry please provide an integer !")
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you do not have enough chips! You have: {chips.total}')
            else:
                break
#Function that draws cards to hand of PLayer or Dealer while adusting for ace value
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

#Asks user if he is going to stand or hit 
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop, global variable can be changed.
    
    while True:
        print('\n')
        x = input("Hit or Stay? Enter 'h' or 's' :")
        
        if x[0].lower() =='h':
            hit(deck,hand)
            print("\nPlayer Hits !")
            
        elif x[0].lower() == 's':
            print("\nPlayer Stands, Dealer's Turn")
            playing = False
            
        else:
            print("\nSorry, I did not understand that, enter h or s")
            continue

        break

#Function that shows some of the cards in hand 
def show_some(player,dealer):
    print("\nCURRENT CARDS IN HAND:")
    print("\nDealer's Hand: ")
    print("  <Hidden Card!>")
    print(f"  {dealer.cards[1]}")
    
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(f"  {card}")

#Function that shows all cards in hand 
def show_all(player,dealer):

    print("\nFINAL RESULT :")
    print("\nDealer's Hand: ")
    for card in dealer.cards:
        print(f"  {card}")
       
    print(f"  Value of Dealer's hand is {dealer.value}")
    
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(f"  {card}")
        
    print(f"  Value of Player's hand is {player.value}")

#Function for when Player is busted
def player_busts(player,dealer,chips):
    print("\nPLAYER BUSTS! DEALER WINS !!")
    chips.lose_bet()

#Function for when Player WINS 
def player_wins(player,dealer,chips):
    print("\nPLAYER WINS !!")
    chips.win_bet()

#Function for when Player WINS cause Dealer is Busted 
def dealer_busts(player,dealer,chips):
    print("\nDEALER BUSTS! PLAYER WINS !!!")
    chips.win_bet()

#Function for when Dealer WINS 
def dealer_wins(player,dealer,chips):
    print("\nDEALER WINS !!")
    chips.lose_bet()

#When it is a tie.
def push():
    print("\nDealer and Player tie ! Push")

while True:
    
    # Printing an opening statement
    print("\nWelcome to BLACKJACK!,\nGet as close to 21 as you can without being busted,\nDealer will keep hitting unitl he/she reaches 17,\nNOTE:Aces count as 1 or 11 ")
    
    # Creating & shuffling the deck, dealing two cards to each player
    New_Deck = Deck()
    New_Deck.shuffle()
    
    Dealer_hand = Hand()
    Player_hand = Hand()
        
    Player_hand.add_card(New_Deck.deal())
    Dealer_hand.add_card(New_Deck.deal())
    Player_hand.add_card(New_Deck.deal())
    Dealer_hand.add_card(New_Deck.deal())
    
    # Setting up the Player's chips 
    Player_Chips = Chips()

    # Prompting the Player for their bet
    take_bet(Player_Chips)

    # Shows cards (but keeps one dealer card hidden)
    show_some(Player_hand,Dealer_hand)
    
    while playing:  #variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(New_Deck,Player_hand)
        
        # Shows cards (but keeps one dealer card hidden)
        show_some(Player_hand,Dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if Player_hand.value > 21:
            show_all(Player_hand,Dealer_hand)
            player_busts(Player_hand,Dealer_hand,Player_Chips) 
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if Player_hand.value <= 21:
        
        while Dealer_hand.value < 17:
            hit(New_Deck,Dealer_hand)
            continue
            
        
        # Test different winning scenarios
            # Run different winning scenarios
        if Dealer_hand.value > 21:
            dealer_busts(Player_hand,Dealer_hand,Player_Chips)
        
        elif Dealer_hand.value > Player_hand.value:
            dealer_wins(Player_hand,Dealer_hand,Player_Chips)

        elif Dealer_hand.value < Player_hand.value:
            player_wins(Player_hand,Dealer_hand,Player_Chips)

        else:
            push()
    
        # Show all cards
        show_all(Player_hand,Dealer_hand)
        
    # Inform Player of their chips total 
    print(f"\nPlayer's Chips currently stands at {Player_Chips.total}")
    
    # Ask to play again
   
    play_again = input("\nWould you like to play again ? Enter y for yes and n for no: ")
    
    if play_again[0].lower() == 'y':
        playing = True 
        continue 
    elif play_again[0].lower() == 'n':
        playing = False 
        #End Message
        print("\nThank You for Playing BLACKJACK !!")
        break
    else:
        print("You have not enetered a Valid Input, Game Ends !")
        break
#End of Game Code 

