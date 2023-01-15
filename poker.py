import deck as dk

class Poker (object):
    def __init__ (self, nr_players):
        self.deck = dk.Deck()
        self.deck.shuffle ()
        self.hands = []
        self.tlist=[]               #create a list to store total_point
        self.multiple_games_list = []    #create a list for points during the whole game  
        numCards_in_Hand = 5

        for i in range (nr_players):
            hand = []
            for j in range (numCards_in_Hand):
                hand.append (self.deck.deal())
            self.hands.append (hand)


    def play (self):
        for i in range (len(self.hands)):
            sorted_hand = sorted(self.hands[i], reverse = True)
            hand = ''
            for card in sorted_hand:
                hand = hand + str(card) + ' '
            print ('Player ' + str(i + 1) + ': ' + hand)

    def point(self,hand): #partial score
        sortedHand = sorted(hand, reverse=True)
        c_sum=0
        ranklist=[]
        for card in sortedHand:
            ranklist.append(card.rank)
        c_sum=ranklist[0]*10**4+ranklist[1]*10**3+ranklist[2]*10**2+ranklist[3]*10+ranklist[4]
        return c_sum

      
    def isRoyal (self, hand):       
        sorted_hand = sorted(hand, reverse=True)
        flag=True
        h=10
        current_suit=sorted_hand[0].suit
        current_rank=14
        total_point=h*10**5+self.point(sorted_hand)
        for card in sorted_hand:
            if card.suit!=current_suit or card.rank!=current_rank:
                flag=False
                break
            else:
                current_rank-=1
        if flag:
            print('Royal Flush')
            self.tlist.append(total_point)
            self.multiple_games_list.append(55)    
        else:
            self.isStraightFlush(sorted_hand)
    

    def isStraightFlush (self, hand):    
        sorted_hand = sorted(hand, reverse=True)
        flag=True
        h=9
        current_suit=sorted_hand[0].suit
        current_rank=sorted_hand[0].rank
        total_point=h*10**5+self.point(sorted_hand)
        for card in sorted_hand:
            if card.suit!=current_suit or card.rank!=current_rank:
                flag=False
                break
            else:
                current_rank-=1
        if flag:
            print ('Straight Flush')
            self.tlist.append(total_point)
            self.multiple_games_list.append(35)
        else:
            self.isFour(sorted_hand)

    def isFour (self, hand): 
        sorted_hand = sorted(hand,reverse=True)
        flag = True
        h=8
        current_rank=sorted_hand[1].rank     
        count=0
        total_point=h*10**5+self.point(sorted_hand)
        for card in sorted_hand:
            if card.rank == current_rank:
                count+=1
        if not count<4:
            flag = True
            print('Four of a Kind')
            self.tlist.append(total_point)
            self.multiple_games_list.append(25)

        else:
            self.isFull(sorted_hand)
    
    def isFull (self, hand):                
        sorted_hand = sorted(hand, reverse=True)
        flag=True
        h=7
        total_point=h*10**5+self.point(sorted_hand)
        mylist=[]                                 
        for card in sorted_hand:
            mylist.append(card.rank)
        rank1 = sorted_hand[0].rank                  
        rank2 = sorted_hand[-1].rank
        num_rank1 = mylist.count(rank1)
        num_rank2 = mylist.count(rank2)
        if (num_rank1 == 2 and num_rank2 == 3)or (num_rank1 == 3 and num_rank2 == 2):
            flag=True
            print ('Full House')
            self.tlist.append(total_point)
            self.multiple_games_list.append(20)
      
        else:
            flag=False
            self.isFlush(sorted_hand)

    def isFlush (self, hand):                         
        sorted_hand = sorted(hand,reverse=True)
        flag=True
        h=6
        total_point=h*10**5+self.point(sorted_hand)
        current_suit=sorted_hand[0].suit
        for card in sorted_hand:
            if not(card.suit == current_suit):
                flag=False
                break
        if flag:
            print ('Flush')
            self.tlist.append(total_point)
            self.multiple_games_list.append(15)
      
        else:
            self.isStraight(sorted_hand)

    def isStraight (self, hand):
        sorted_hand = sorted(hand,reverse=True)
        flag=True
        h=5
        total_point=h*10**5+self.point(sorted_hand)
        current_rank = sorted_hand[0].rank
        for card in sorted_hand:
            if card.rank != current_rank:
                flag=False
                break
            else:
                current_rank-=1
        if flag:
            print('Straight')
            self.tlist.append(total_point)
            self.multiple_games_list.append(12)
      
        else:
            self.isThree(sorted_hand)
        
    def isThree (self, hand):
        sorted_hand = sorted(hand, reverse=True)
        flag=True
        h=4
        total_point=h*10**5+self.point(sorted_hand)
        current_rank = sorted_hand[2].rank
        mylist=[]
        for card in sorted_hand:
            mylist.append(card.rank)
        if mylist.count(current_rank) == 3:
            flag=True
            print ("Three of a Kind")
            self.tlist.append(total_point)
            self.multiple_games_list.append(8)
      
        else:
            flag=False
            self.isTwo(sorted_hand)
        
    def isTwo (self, hand):                           
        sorted_hand = sorted(hand, reverse=True)
        flag=True
        h=3
        total_point=h*10**5+self.point(sorted_hand)
        rank1=sorted_hand[1].rank                      
        rank2=sorted_hand[3].rank
        mylist=[]
        for card in sorted_hand:
            mylist.append(card.rank)
        if mylist.count(rank1)==2 and mylist.count(rank2)==2:
            flag=True
            print ("Two Pair")
            self.tlist.append(total_point)
            self.multiple_games_list.append(4)
      
        else:
            flag=False
            self.isOne(sorted_hand)
  
    def isOne (self, hand):                         
        sorted_hand = sorted(hand,reverse=True)
        flag=True
        h=2
        total_point=h*10**5+self.point(sorted_hand)
        mylist=[]                                       
        mycount=[]                                    
        for card in sorted_hand:
            mylist.append(card.rank)
        for each in mylist:
            count=mylist.count(each)
            mycount.append(count)
        if mycount.count(2)==2 and mycount.count(1)==3:  
            flag=True
            print ("One Pair")
            self.tlist.append(total_point)
            self.multiple_games_list.append(2)
      
        else:
            flag=False
            self.isHigh(sorted_hand)

    def isHigh (self, hand):                
        sorted_hand = sorted(hand, reverse=True)
        flag=True
        h=1
        total_point=h*10**5+self.point(sorted_hand)
        mylist=[]                                     
        for card in sorted_hand:
            mylist.append(card.rank)
        print ("High Card")
        self.tlist.append(total_point)
        self.multiple_games_list.append(1)
