
import random



class Player:
    def __init__(self):
        self.hand = []
        self.money = 1000

    def draw_card(self,card):
        self.hand.append(card)

    def hand_value(self):
        card_values = {"A": 11, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "J": 10, "Q": 10, "K": 10}
        hand_total = 0
        ones_in_hand = 0

        for i in self.hand:
            hand_total += card_values[i]

            if i == "A":
                ones_in_hand += 1

        while ones_in_hand > 0 and hand_total > 21:
            hand_total -= 10
            ones_in_hand -= 1

        return hand_total

    def busted(self):
        if self.hand_value() > 21:
            return True
        return False

    def amount_betting(self,amount):
        self.amount_in_bet = amount

class Deck:
    def __init__(self,number_decks):
        self.deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] * 4 * number_decks
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Game:
    def __init__(self,deck,players):
        self.players = players
        self.deck = deck

        for i in range((len(players)) *2):
            self.players[i % (len(players))].draw_card(self.deck.deal())


    def hit_or_stand(self, player_number):
        while (h_o_s := input("player" + str(player_number) + " Do you want to hit or stand h/s\n")) != "h" and (h_o_s != "s"):
            print("type h or s")

        if (h_o_s == "h"):
            self.players[player_number].draw_card(self.deck.deal())
            return True                        #True == hit, False == stand
        else:
            return False

    def crupier(self):
        while self.players[-1].hand_value() < 17:
            self.players[-1].draw_card(self.deck.deal())

    def winner(self, player_number):
        player = self.players[player_number].hand_value()
        crupier = self.players[-1].hand_value()

        if player > 21:
            return False
        elif crupier > 21:
            return True
        elif player > crupier:
            return True
        elif crupier > player:
            return False
        else:
            return True                                         #True == player wins

def play():
    number_of_players = 1
    number_of_decks = 2
    deck = Deck(number_of_decks)
    playing = True

    players = [Player() for _ in range(number_of_players + 1)]  # last player is the house

    while playing:
        if (start_game := input("Do you want to play y/n\n")) == "y":
            game = Game(deck,players)

            for i in range(number_of_players):
                while (amount_to_bet := int(input("player" + str(i)  + " place your bet:\n"))) > players[i].money:
                    print("you have " + str(players[i].money) + "USD place a lower bet\n")

                players[i].amount_betting(amount_to_bet)

            for i in range(number_of_players):
                player_turn = True

                while player_turn:
                    print("\nplayer" + str(i) + " Your hand is", *players[i].hand, sep=" ",end="\n")
                    print("crupier's hand is " + str(players[-1].hand[0]) + " ? ", end="\n")


                    if game.hit_or_stand(i) == False:
                        player_turn = False

                    if players[i].busted():
                        print("player" + str(i) + " Your hand is", *players[i].hand,"\nyou busted" ,sep=" ", end="\n")
                        player_turn = False

            game.crupier()

            print("\ncrupier's hand is ", *players[-1].hand, sep=" ", end="\n")

            for i in range(number_of_players):
                if game.winner(i):
                    print("player" + str(i) + " wins")

                    players[i].money += players[i].amount_in_bet
                else:
                    print("player" + str(i) + " loses")

                    players[i].money -= players[i].amount_in_bet

        elif start_game == "n":
            playing = False
        else:
            print("type y or n \n")

play()









