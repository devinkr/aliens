class GameStats:
    """track statistics for alien invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

        # High score should never be reset
        try:
            with open('high_score.txt', 'r') as f:
                score = f.readline()
                if score:
                    self.high_score = int(score)
                else:
                    self.high_score = 0
        except:
            self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that change during game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        with open('high_score.txt', 'w') as f:
            f.write(str(self.high_score))
    