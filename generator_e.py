"""
Yield
*****

Inside a program, when you call a function that has a yield statement, as soon as a yield is encountered, the execution of the function stops and returns an object of the generator to the function caller. In simpler words, the yield keyword will convert an expression that is specified along with it to a generator object and return it to the caller. Hence, if you want to get the values stored inside the generator object, you need to iterate over it.

It will not destroy the local variables’ states. Whenever a function is called, the execution will start from the last yield expression. Please note that a function that contains a yield keyword is known as a generator function. 

When you use a function with a return value, every time you call the function, it starts with a new set of variables. In contrast, if you use a generator function instead of a normal function, the execution will start right from where it left last.
"""

def fib_gen(n):
    fib_0 = 1
    yield fib_0
    fib_1 = 1
    yield fib_1

    for i in range(n-2):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1    


[print(num) for num in fib_gen(10)]

# Making iterator from generator

class Squares:
    def __init__(self, n):
        self.n = n
        
    @staticmethod
    def squares_gen(n):
        for i in range(n):
            yield i ** 2
        
    def __iter__(self):
        return Squares.squares_gen(self.n)

sq = Squares(5)

[print(num) for num in sq]

# Use with other generator

def Squares2(n):
    for i in range(n):
        yield i ** 2

sq = Squares2(10)
enum_sq = enumerate(sq)

print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(enum_sq))

from collections import namedtuple

Card = namedtuple('Card', 'rank, suit')
SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
RANKS = tuple(range(2, 11)) + tuple('JQKA')

class CardDeck:
    SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    RANKS = tuple(range(2, 11)) + tuple('JQKA')
        
    def __iter__(self):
        return CardDeck.card_gen()
    
    def __reversed__(self):
        return CardDeck.reversed_card_gen()
    
    @staticmethod
    def card_gen():
        for suit in CardDeck.SUITS:
            for rank in CardDeck.RANKS:
                card = Card(rank, suit)
                yield card
        
    @staticmethod
    def reversed_card_gen():
        for suit in reversed(CardDeck.SUITS):
            for rank in reversed(CardDeck.RANKS):
                card = Card(rank, suit)
                yield card

deck = CardDeck()
[print(card) for card in deck]

rev = reversed(CardDeck())
[print(card) for card in rev]
