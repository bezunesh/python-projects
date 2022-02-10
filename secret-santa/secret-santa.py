from random import choice

class SecretSanta:
    players = ["Bezu", "Jhon", "Alexis", "Tom", "Barney"]
    out = []

    def pickSanta(self, player):
        santas = self.players.copy()
        # avoid self
        santas.remove(player)
        # avoid getting more than one present
        [santas.remove(p) for p in self.out if self.out and p in santas]
        # avoid being the last one in turn and the only one yet not has received a present
        if len(self.out) == len(self.players) - 2 and self.players[-1] not in self.out:
            # pick the last person
            mysanta = self.players[-1]
        else:    
            # randomly pick one
            mysanta = choice(santas)
        self.out.append(mysanta)

        return mysanta


if __name__ == '__main__':
    game = SecretSanta()      
    print([[p, game.pickSanta(p)] for p in game.players])
   