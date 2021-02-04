

import math
import random
import copy

#linkedlist class
class LinkedList:
    class _Node:
        def __init__(self, v, n):
            self.value = v
            self.next = n

    #initialising the node
    def __init__(self):
        self._head = None
        self._size = 0
    
    #String conversion
    def __str__(self):
        if self.isEmpty():
          return "[]"
        else:
          st="["
          temp=self._head
          while temp.next is not None:
            st+=str(temp.value)+", "
            temp=temp.next
          st+=str(temp.value) + "]"
         
        return st
    
    #length of the node
    def __len__(self):
        return self._size

    #checking for an empty string
    def isEmpty(self):
        if self._head is None:
            return True
        else:
            return False

    # Adds a node of value v to the beginning of the list
    def add(self, v):
      new_v = self._Node(v,None)
      if self.isEmpty():
          self._head = new_v
          self._size+=1
      else:
          new_v.next = self._head
          self._head= new_v
          self._size+=1
      
    # Adds a node of value v to the end of the list
    def append(self,v):
        new_v = self._Node(v,None)
        if self.isEmpty():
           self._head = new_v
           self._size+=1
           return
        temp = self._head
        while temp.next is not None:
            temp= temp.next
        temp.next = new_v;
        self._size+=1

    # Removes and returns the first node of the list
    def pop(self):
        if self.isEmpty():
            return None

        else:
            temp = self._head
            self._head= temp.next
            temp.next = None
            self._size-=1
            return temp.value

    # Returns the value of the first node of the list
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self._head.value

    # Removes the node of the list with value v and return v
    def remove(self, v):
        temp = self._head
        if temp.value == v:
            self._head= self._head.next
            self._size-=1
            return v
        while temp.next:
            if temp.next.value == v:
                temp.next = temp.next.next
                self._size-=1
                return v
            temp = temp.next

#circular linked list 
class CircularLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
    
    #string conversion
    def __str__(self):
        if self.isEmpty():
          return "[]"
        else:
           a = "["
           temp = self._head
           while temp != None:
             a += str(temp.value) + ', ' 
             temp = temp.next
             if temp==self._head:
                break
           a = a[:-2] + ']'  
           return a  
      
    #iterator for using for loops
    def __iter__(self):
        
        temp = self._head
        while temp.next is not self._head:
            yield temp.value
            temp = temp.next
        yield temp.value

    # Moves head pointer to next node in list
    def next(self):
       if not self._head:
         return None
       else:
         temp=self._head
         curr=self._head
         while temp is not None:
            temp=temp.next
            if temp==self._head:
                break
         temp=self._head
         self._head=temp.next
      
        

    # Adds a node of value v to the end of the list
    def append(self, v):
        
        
        if not self._head:
            self._head=self._Node(v,None)
            self._head.next =self._head
         
        else:
           temp=self._head
           new_v=self._Node(v,None)
           while temp.next!=self._head:
             temp=temp.next
           temp.next=new_v
           new_v.next=self._head


    # Reverses the next pointers of all nodes to previous node
    def reverse(self):
       if (self._head == None): 
          return None
  
       prev = None
       current = self._head
       next = current.next
       current.next = prev 
       prev = current 
       current = next
       while (current != self._head): 
          next = current.next
          current.next = prev 
          prev = current 
          current = next
   
       self._head.next = prev 
       
     
  
    # Removes head node and returns its value
    def pop(self):
        if self._head is None:
            return None
        pop_node=self._head
        crnt_node=self._head.next
        pointer_head=self._head.next
        while pointer_head.next.value!=self._head.value:
            pointer_head=pointer_head.next
        pointer_head.next=crnt_node
        self._head=crnt_node
        return pop_node.value


###Class card
class Card:
    def __init__(self, r, s):
        self._rank = r
        self._suit = s
       
        

    suits = {'s': '\U00002660', 'h': '\U00002661', 'd': '\U00002662', 'c': '\U00002663'}
    
    ###String conversion
    def __str__(self):
        return self._rank + self.suits[self._suit]
    
    ###string equal
    def __eq__(self, other):
        if (other is not None):
          if other._rank =='1' or other._rank == 'A':
             rank= 'A'
          else:
             rank=other._rank
          if self._rank == '1' or self._rank == 'A':
             self_rank = 'A'
          else:
             self_rank= self._rank
     
          return self_rank == rank and self._suit == other._suit;

#class Hand
class Hand:
    def __init__(self):
        self.cards = {'s': LinkedList(), 'h': LinkedList(), 'd': LinkedList(), 'c': LinkedList()}

    def __str__(self):
        result = ''
        for suit in self.cards.values():
            result += str(suit)
   
        return result

    def __getitem__(self, item):
        return self.cards[item]

    def __len__(self):
        result = 0
        for suit in list(self.cards):
            result += len(self.cards[suit])

        return result

    def add(self, card):
        self.cards[card._suit].add(card)
        

    def get_most_common_suit(self):
        return max(list(self.cards), key = lambda x: len(self[x]))

    # Returns a card included in the hand according to
    # the criteria contained in *args and None if the card
    # isn't in the hand. The tests show how *args must be used.
    def play(self, *args):
       
        ### if args have 2 arguments
        if (len(args)==2):
          #checking for a suit
          if (args[0]== 's' or args[0] == 'h' or args[0]=='d' or args[0]=='c'):
            cards= self.__getitem__(args[0])
            new_rank=args[1]
          else:
            cards = self.__getitem__(args[1])
            new_rank=args[0]
          if(new_rank=='1'):
            new_rank='A'
          node = cards._head
          while node: 
               if(node.value._rank==new_rank):
                 cards.remove(node.value)
                 return node.value
               node = node.next
        
        ###if args has 1 arguments
        elif (len(args)==1):
           if (args[0]=='1'):
              card='A'
           else:
              card=args[0]
           ##suit check
           if (card== 's' or card== 'h' or card=='d' or card=='c'):
             cards= self.__getitem__(card)
             return cards.pop()
           else:
             for i in (self.cards):
               node=self.cards[i]._head
               while node:
                 if(node.value._rank==card):
                     self.cards[i].remove(node.value)
                     return node.value
                 node = node.next
            
           
      
####Deck class
class Deck(LinkedList):
    def __init__(self, custom=False):
        super().__init__()
        if not custom:
            # for all suits
            for i in range(4):
                # for all ranks
                for j in range(13):
                    s = list(Card.suits)[i]
                    r = ''
                    if j == 0:
                        r = 'A'
                    elif j > 0 and j < 10:
                        r = str(j+1)
                    elif j == 10:
                        r = 'J'
                    elif j== 11:
                        r = 'Q'
                    elif j == 12:
                        r = 'K'
                    self.add(Card(r,s))


    #drawing the card
    def draw(self):
        return self.pop()

    #Shuffling the cards
    def shuffle(self, cut_precision = 0.05):
        
        # Cutting the two decks in two
        center = len(self) / 2
        k = round(random.gauss(center, cut_precision*len(self)))

        # seperating into  two lists
        current=self._head
        i=0
        for i in range(k-1):         
          current = current.next          
       
        first=self._head
        second=current.next
        current.next=None
        
        #for the first instance
        if random.uniform(0,1) < 0.5:
            headone=self._Node(second,None)
            temp=headone
            curr_first= first        
            curr_second=second

             #switch self._head and other_deck pointers
            while (curr_first != None and curr_second !=None):
                  temp.next = curr_second                
                  temp = curr_second
                  curr_second = curr_second.next
                  temp.next=curr_first
                  temp = curr_first
                  curr_first= curr_first.next

            if (curr_first != None):
               temp.next = curr_first      
            if (curr_second != None):
               temp.next = curr_second         
            self._head = headone.next
            return self._head

        #for the second instance    
        else:
            head=self._Node(first,None)
            curr=head
            curr_first= first        
            curr_second=second
            while(curr_first != None and curr_second !=None):
            
                  curr.next=curr_first
                  curr = curr_first
                  curr_first= curr_first.next
                  curr.next = curr_second
                  curr = curr_second
                  curr_second = curr_second.next

            if (curr_first != None):
              curr.next = curr_first
        
            if (curr_second != None):
              curr.next = curr_second
            self._head = head.next
    
            return self._head
            
        
       
##class player
class Player():
    def __init__(self, name, strategy='naive'):
        self.name = name
        self.score = 8
        self.hand = Hand()
        self.strategy = strategy
    
    ###string conversion
    def __str__(self):
        return self.name

    # This function must modify the player's hand,
    # the discard pile, and the game's declared_suit 
    # attribute. No other variables must be changed.
    # The player's strategy can ONLY be based
    # on his own cards, the discard pile, and
    # the number of cards his opponents hold.
    def play(self, game):
        if (self.strategy == 'naive'):
            top_card = game.discard_pile.peek()

  
            ###########Checking the top card in the same suit##############
            for suit in self.hand.cards:
                if (game.declared_suit != ''):
                   suitmatch=game.declared_suit
                else:
                   suitmatch=top_card._suit
                if (suit == suitmatch):
                   suit_list=self.hand.__getitem__(suit)
                   if (len(suit_list)> 0):

                      #if the suit has same suit  and special card... check the rank and the length is 1
                      if (len(suit_list)==1 and suit_list._head.value._rank==str(self.score)):
                         
                         ###Do not use special cards and use normal cards
                         for i in self.hand.cards:
                           node = self.hand.__getitem__(i)._head
                           while node: 
                             if  (node.value._rank== top_card._rank):
                                 if (node.value._rank=='2'):
                                     game.draw_count+=2 # draw 2
                                 if (node.value._rank=='Q' and i=='s'):
                                     game.draw_count+=5 # draw 5
                                 game.discard_pile.add(self.hand.play(node.value._rank,i))  
                                 if (game.declared_suit != ''):
                                     game.declared_suit=''
                                 if (node.value._rank == str(self.score) or (node.value._rank=='A' and str(self.score)=='1')):
                                     game.declared_suit=self.hand.get_most_common_suit()
                                 return game
                             node=node.next
                         
                         ##if normal cards are not available
                         s= suit_list._head.value
                         game.discard_pile.add(self.hand.play(s._rank))
                         game.declared_suit=self.hand.get_most_common_suit()
                         if (s._rank == '2'):
                           game.draw_count +=2
                         print(game.draw_count)
                         return game
                      node=suit_list._head
                      pop_card=suit_list.peek()


                      #IF there are many cards of the given suit
                      if (len(suit_list)>1):

                        #if top card is special card ..drop the next card
                        if (pop_card._rank==str(self.score)or (node.value._rank=='A' and str(self.score)=='1')):
                           pop_card= suit_list._head.next.value
                      if (pop_card._rank=='2'):
                           game.draw_count+=2 #draw 2
                      if (pop_card._rank=='Q' and pop_card._suit=='s'):
                           game.draw_count+=5 #draw 5
                      if (game.declared_suit != ''):
                           game.declared_suit=''
                      game.discard_pile.add(self.hand.play(pop_card._rank,pop_card._suit))
                      return game
                   else :
                     break


            ############checking the top card of same rank##############
            for suit in self.hand.cards:
                node = self.hand.__getitem__(suit)._head

                while node: 
                  if  (node.value._rank== top_card._rank):
                    if (node.value._rank=='2'):
                      game.draw_count+=2 #draw 2
                    if (node.value._rank=='Q' and suit=='s'):
                      game.draw_count+=5# draw 5
                    game.discard_pile.add(self.hand.play(node.value._rank,suit))
                    if (node.value._rank == str(self.score) or (node.value._rank=='A' and str(self.score)=='1')):
                        game.declared_suit=self.hand.get_most_common_suit()                     
                    return game
                  node=node.next


            ############checking the top card as same score card###########
            for suit in self.hand.cards:
                node = self.hand.__getitem__(suit)._head

                while node:   
                  if (node.value._rank == str(self.score) or (node.value._rank=='A' and str(self.score)=='1')):
                    if (node.value._rank=='2'):
                      game.draw_count+=2 #draw 2
                    game.discard_pile.add(self.hand.play(node.value._rank))
                    game.declared_suit=self.hand.get_most_common_suit()
                    return game
                  node = node.next
            
            ###########else draw a card###############
            game.draw_count=1 #draw 1
            return game        

         
        else:
            # TO DO(?): Custom strategy (Bonus)
            pass

class Game:
    def __init__(self):
        self.players = CircularLinkedList()

        for i in range(1,5):
            self.players.append(Player('Player '+ str(i)))

        self.deck = Deck()
        self.discard_pile = LinkedList()

        self.draw_count = 0
        self.declared_suit = ''

    def __str__(self):
        
        result = '--------------------------------------------------\n'
        result += 'Deck: ' + str(self.deck) + '\n'
        result += 'Declared Suit: ' + str(self.declared_suit) + ', '
        result += 'Draw Count: ' + str(self.draw_count) + ', '
        result += 'Top Card: ' + str(self.discard_pile.peek()) + '\n'
        for player in self.players:

            result += str(player) + ': '
            result += 'Score: ' + str(player.score) + ', '
            result += str(player.hand) + '\n'
        
        return result


    # Puts all cards from discard pile except the 
    # top card back into the deck in reverse order
    # and shuffles it 7 times
    def reset_deck(self):
        #######pop the top card########
        if (len(self.discard_pile) !=0):
           top_card=self.discard_pile.pop()

           ########reverse the discardpile########
           prev = None
           current = self.discard_pile._head
           while(current is not None):
               next = current.next
               current.next = prev
               prev = current
               current = next

           #######adding the discard pile to deck#######
           while(prev is not None):
               self.deck.add(prev.value)
               prev = prev.next
           self.discard_pile.pop()
           self.discard_pile.add(top_card)
        
        ##shuffling for 7 times#####
        for i in range(7):
             self.deck.shuffle()
        
        
   

    # Safe way of drawing a card from the deck
    # that resets it if it is empty after card is drawn
    def draw_from_deck(self, num):
       
        l=LinkedList()
        for i in range(num):
           l.append(self.deck.draw())
    
           ###resetting the deck####
           if (len(self.deck)==0):
              self.reset_deck()
        
        return l
 
    def start(self, debug=False):
        print("started")
    
        # Order in which the players win the game
        result = LinkedList()
      
        self.reset_deck()
        
        # Each player draws 8 cards
        for player in self.players:
            
            for i in range(8):
                player.hand.add(self.deck.draw())     
           
        
        self.discard_pile.add(self.deck.draw())
        
        transcript = open('/content/drive/My Drive/Colab Notebooks/result.txt','w')
        if debug:
            transcript = open('/content/drive/My Drive/Colab Notebooks/result_debug.txt','w')
        call=0
        position=0
        while(not self.players.isEmpty()):
            
            if debug:
                transcript.write(str(self))
                

            # player plays turn
            player = self.players.peek()

            old_top_card = self.discard_pile.peek()

            ########if it is first play and all top cards are special cards########
            if (call==0 and (old_top_card._rank=='2' or (old_top_card._rank == 'Q'and old_top_card._suit=='s')or old_top_card._rank==str(player.score))):
               self = player.play(self)
            
            ##########if the previous card has suit declared i.e if previous card is special show card###########
            elif (call !=0 and self.declared_suit != '' ):
                   
                   suit_list=player.hand.__getitem__(self.declared_suit)

                   #draw cards if previous card is a special card#
                   if (self.draw_count != 0):
                      print(self.draw_count)
                  
                   
                   #suit-list length is not empty#
                   elif (len(suit_list)>0):
                      pop_card=suit_list.peek()
                      
                      if (len(suit_list)>1):
                        if (pop_card._rank==str(player.score) or (pop_card._rank=='A' and str(player.score)=='1')):
                          pop_card= suit_list._head.next.value
                      if (pop_card._rank=='Q'and pop_card._suit=='s'):
                        self.draw_count+=5
                      if (pop_card._rank=='2'):
                        self.draw_count+=2
                     
                      self.declared_suit = ''
                      game.discard_pile.add(player.hand.play(pop_card._rank,pop_card._suit))
                      
                  #suit-list is empty # use other normal cards#
                   elif (len(suit_list)==0):
                     c=False
                     for suit in player.hand.cards:
                       node = player.hand.__getitem__(suit)._head
                       while node: 
                  
                           if (node.value._rank == str(player.score) or (node.value._rank=='A' and str(player.score)=='1')):
                              if (node.value._rank=='2'):
                                  self.draw_count+=2
                              self.discard_pile.add(player.hand.play(node.value._rank,suit))
                              self.declared_suit=player.hand.get_most_common_suit()
                              c==True
                              break
                           node=node.next
                       if (c==True):
                           break
                   else:        
                      self.draw_count+=1

            ########## if old top card is a special card with 2 or Qs ###############
            elif (call!=0  and ((old_top_card._rank == 'Q'and old_top_card._suit=='s') or old_top_card._rank=='2' )) :
           
              if (self.draw_count == 0 and old_top_card._rank=='2'):
                self.draw_count+=2
             
              c=False
              #current player special cards check#
              for suit in player.hand.cards:
                node = player.hand.__getitem__(suit)._head
                while node: 
                  
                  if ((node.value._rank == 'Q' and suit== 's') or (node.value._rank=='2')):
                     if (node.value._rank=='Q'):
                       self.draw_count+=5 #draw 5
                     if (node.value._rank=='2'):
                        self.draw_count+=2 # draw  2
                     self.discard_pile.add(player.hand.play(node.value._rank,suit))
                     
                     if (node.value._rank == str(player.score) or (node.value._rank=='A' and str(player.score)=='1')):
                       self.declared_suit=player.hand.get_most_common_suit()
                     c=True
                     break
                  node=node.next
                if (c==True):
                  break
            ###### if not special cards proceed routine way ######
            else:
               self=player.play(self)
            
      
               
            call=call+1
            new_top_card = self.discard_pile.peek()

            ####### Player didn't play a card => must draw from pile
            if new_top_card == old_top_card:
               # if special cards draw more than 1 card#
               if ((new_top_card._rank == 'Q' and new_top_card._suit=='s') or new_top_card._rank == '2' ):
                 if (self.draw_count != 0):
                    transcript.write(""+ str(player)+" draws "+str(self.draw_count)+ " cards \n")
                    l=(self.draw_from_deck(self.draw_count)) # draw cards more than 1 card
                    node=l._head
                    while node:
                      player.hand.add(node.value)
                      node=node.next
                    
                    self.draw_count=0
                    call=0

               #draw single card and update in txt file
               else:
                 self.draw_count=1
                 player.hand.add(self.draw_from_deck(self.draw_count)._head.value) # draw single card
                 transcript.write(""+ str(player)+" draws 1 card \n")
                 self.draw_count=0
                 

            ##########Player played a card
            else:
               transcript.write("\n"+ str(player)+" plays "+ str(new_top_card) +"\n")

               #reverse the players#
               if (call != 0 and new_top_card._rank =='A'):
                  self.players.reverse()

               #skip the player#
               if (call  != 0 and new_top_card._rank == 'J'):
                  self.players.next()

            ######## Player has finished the game#######
            if len(player.hand) == 0 and player.score == 1:
                player.score=0
                position=position+1
                transcript.write("" + str(player)+ " finishes in position "+ str(position) +"\n")

                ##deletion of the circularlinked list node
                head=self.players._head
                if (head == None):
                    return result
              # If the list contains only a single node delete 
                if ((head).value == player and (head).next == head):
                      head = None
                      return result
                last = head
                d = None
                #deletion of the player
                if (head.value == player) :
                     while (last.next != head):
                          last = last.next 
                     last.next = head.next
                     head = last.next      
                while (last.next != head and last.next.value != player) :
                        last = last.next
                if (last.next.value == player) :
                      d = last.next
                      last.next = d.next
                self.players._head=head
                node=self.players._head

                #######losing player
                if (node==node.next):
                   transcript.write("" + str(node.value)+ " finishes in last position \n")
                   return result
            else:
                ####Player is out of cards to play... draw score-1 cards
                if len(player.hand) == 0:
                    player.score = player.score-1
                    
                    transcript.write(""+str(player)+ " is out of cards to play! "+ str(player) + " draws "+str(player.score)+" cards \n" )
                    l=(self.draw_from_deck(player.score)) # drawing the given cards
                    node=l._head
                    while node:
                      player.hand.add(node.value)
                      node=node.next   
                    
                # Player has a single card left to play
                elif len(player.hand) == 1:
                    transcript.write("-*knock, knock*- "+ str(player) + " has a single card left! \n")
                self.players.next()
        return result


if __name__ == '__main__':

    random.seed(420)
    game = Game()
    print(game.start(debug=True))
    
    # TESTS
    # LinkedList
    l = LinkedList()
    l.append('b')
    l.append('c')
    l.add('a')

    assert(str(l) == '[a, b, c]')
    assert(l.pop() == 'a')
    assert(len(l) == 2)
    assert(str(l.remove('c')) == 'c')
    assert(l.remove('d') == None)
    assert(str(l) == '[b]')
    assert(l.peek() == 'b')
    assert(l.pop() == 'b')
    assert(len(l) == 0)
    assert(l.isEmpty())

    # CircularLinkedList
    l = CircularLinkedList()
    l.append('a')
    l.append('b')
    l.append('c')

    assert(str(l) == '[a, b, c]')
    l.next()
    assert(str(l) == '[b, c, a]')
    l.next()
    assert(str(l) == '[c, a, b]')
    l.next()
    assert(str(l) == '[a, b, c]')
    l.reverse()
    assert(str(l) == '[a, c, b]')
    assert(l.pop() == 'a')
    assert(str(l) == '[c, b]')
    
    # Card
    c1 = Card('A','s')
    c2 = Card('A','s')
    # Il est pertinent de traiter le rang 1
    # comme étant l'ace
    c3 = Card('1','s')
    assert(c1 == c2)
    assert(c1 == c3)
    assert(c3 == c2)

    # Hand
    h = Hand()
    h.add(Card('A','s'))
    h.add(Card('8','s'))
    h.add(Card('8','h'))
    h.add(Card('Q','d'))
    h.add(Card('3','d'))
    h.add(Card('3','c'))

    assert(str(h) == '[8♠, A♠][8♡][3♢, Q♢][3♣]')
    assert(str(h['d']) == '[3♢, Q♢]')
    assert(h.play('3','d') == Card('3','d'))
    assert(str(h) == '[8♠, A♠][8♡][Q♢][3♣]')
    assert(str(h.play('c')) == '3♣')
    assert(str(h.play('8')) == '8♠')
    assert(str(h) == '[A♠][8♡][Q♢][]')
    assert(h.play('d','Q') == Card('Q','d'))
    assert(h.play('1') == Card('A','s'))
    assert(h.play('J') == None)

    # Deck
    d = Deck(custom=True)
    d.append(Card('A','s'))
    d.append(Card('2','s'))
    d.append(Card('3','s'))
    d.append(Card('A','h'))
    d.append(Card('2','h'))
    d.append(Card('3','h'))

    random.seed(15)

    temp = copy.deepcopy(d)
    assert(str(temp) == '[A♠, 2♠, 3♠, A♡, 2♡, 3♡]')
    temp.shuffle()
    assert(str(temp) == '[A♠, A♡, 2♠, 2♡, 3♠, 3♡]') 
    temp = copy.deepcopy(d)
    temp.shuffle()
    assert(str(temp) == '[A♡, A♠, 2♡, 2♠, 3♡, 3♠]')
    assert(d.draw() == Card('A','s'))


