# DataStructures_Crazy8game

# Game Rules
This practical work consists of the implementation of a simulation of part of Crazy Eights Countdown, which is a variant of the card
game Crazy Eights ( the eight). A game of Crazy Eights is played as follows: each player starts with 8 cards. The first card of the deck is
exposed and forms the discard stack. The first player must then play on the heel a card of the same suit (suit) or the same rank (rank)
that is in his hand. It is now the next player's turn to get rid of a card of the same sign or of the same rank as the previous player
(therefore the card that is on top of the heel) and so on. If a player cannot play a valid card, he must draw a card from the top of the
deck (without playing it). When there are no cards left in the deck, all cards in the stack except the first are shuffled and become the new
deck. The object of the game is to get rid of all the cards from our hand as quickly as possible. When a player has only one card, that
player must knock on the table to warn the other players.

Some cards have special effects on the course of the game:
- A ♠, A r , A q , A ♣: Reverses the order in which the players take their turns.
- J ♠, J r , J q , J ♣: The next player does not play and it is up to the next player to play.
- 8 ♠, 8 r , 8 q , 8 ♣: It's about a show off ( wildcard). The player playing a show declares the sign of the card the next player is to
play. This declaration is in effect until a player has played a card of that sign or another show. Show off can be played on any
card (except the following cards).
- 2 ♠, 2 r , 2 q , 2 ♣: The next player must draw two cards from the deck (without playing afterwards). The only way to escape is to
play another two, which will imply that the next player will have to draw 4 cards. It is possible to stack both until a player cannot
play one. This player must therefore draw a number of cards equal to the sum of this stack of two. It is not possible to use a
show on a two to avoid drawing cards.
- Q ♠: Same as a two, but involves a draw of 5 cards.

A part of Crazy Eights Countdown starts out exactly like a game of Crazy Eights. The difference is that when a player gets rid of all his
cards, he now draws 7 and the 7 becomes showy instead of the 8. Once that same player has finished playing all his cards for a second
time, he gets some. pin 6 and 6 becomes wild instead of 7, etc. To deal with the fact that several players play different frills
simultaneously, a score is associated with each player. The score is equal to the show a player uses, which implies that each player
starts with a score of 8. The first player with a score of 1 (the ace is the show in this case) who gets rid of the cards of his hand and who
therefore obtains a score of zero wins the game. The game is then continued to determine the player who finishes in 2nd, 3rd and 4th
place.

# Special cases
If the first card that forms the heel at the start of a game is a special card, it has no effect on the player starting the game since it has not
been played by a player. In the event that a card played is both a show and a special card, both effects of that card are in effect. It is
important to note that since the effect of a show is in effect until a player has played a card of that sign or another show, the following
scenario is not allowed:
player A with a score of 7 plays 7 ♣ and declares ♡ as a sign. Player B with a score of 8 plays 7 q . In this scenario, player B must play
either an 8 or a hearts card. Finally, if a player ends the game by playing an ace (his show off), he does not have to declare an ensign.

# Functions
- Deck.shuffle (): This function simulates a “riffle shuffle”. The package is first split into two. The index of the card of the original
deck that will become the first card of the second deck is determined by the variable k. The two lists are then merged so that the
header of the original packet is followed by the header of the second packet (found at index k previously), which is then followed
by the second card of the original packet, etc. To allow that the head of the result is not always the head of the original packet,
the head pointer of the original packet and the node pointer to the index k are interchanged once in two before the merger of the
two packages. The additional memory space used by this function must be in O ( 1).
- Player.play (): This function contains a player's strategy. Since it takes as input the object Game, the player has access to the
heel, his hand and attributes declared_suit and draw_count
to play a card. The naive strategy is this: if you are forced to draw cards, play a two or queen of spades to avoid having to do so.
Otherwise, play the first card of the same suit from our hand without wasting any frills. If we don't have cards of the same suit,
play a card of the same rank. As a last resort, play a show and declare the most frequent card suit in your hand. If we can play a
card, this is where the player's hand and heel have to be changed. Otherwise, we do nothing and the loop while
of Game is responsible for making the player draw a card. The order of precedence of the signs is as
follows: ♠ > ♡ > ♢ > ♣.

# Language 
Python 

# Results
result_debug.txt

# Data structures
- linked list 
- Circular linked list
- class
