class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen Settings
        self.fullscreen = False
        self.screen_width = 1024
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed = 1
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = .75
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 is right, -1 is left
        self.fleet_direction = 1
