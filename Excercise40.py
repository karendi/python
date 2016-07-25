#working with classes
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
happy_bday = Song(["Happy birhday to you.happy birthday to you"])
bulls_on_parade = Song(["they will rally around the family with a packet"])
from_the_inside_out = Song(["Who am i?not becuase of who iam but because of You"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
from_the_inside_out.sing_me_a_song()
