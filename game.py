from deck import Deck
from player import Player
from card import Card

class Game():
    def __init__(self):
        name1 = input("Player1's name:")
        name2 = input("Player2's name:")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def print_winner(self, winner):
        print("{} wins this round\n".format(winner.name))

    def print_draw(self, p1, p2):
        print("{} draws {}, {} draws {}".format(p1.name, p1.card, p2.name, p2.card))

    def play_game(self):
        cards = self.deck.cards
        print("Start War!")
        while len(cards) >= 2:
            m = "Please press q(quit) or the other(start):"
            response = input(m)
            if response == "q":
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            self.print_draw(self.p1, self.p2)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.print_winner(self.p1)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2)

        win = self.winner(self.p1, self.p2)

    def winner(self, p1, p2):
        print("Finish game.")
        if p1.wins != p2.wins:
            if p1.wins > p2.wins:
                  print("{} is winner!".format(p1.name))
            else:
                  print("{} is winner!".format(p2.name))
        else:
            print("Draw!")

if __name__ == "__main__":
    game = Game()
    game.play_game()
            
