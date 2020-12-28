class Game():
    def __init__(self, game):
        self.gameName = game

    def __getGameName(self, game):
        game = game.lower()
        game = game.split()
        
        self.gameName = game

    def output(self):
        self.__getGameName(self.gameName)

        return self.gameName