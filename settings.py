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
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 is right, -1 is left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase dynamic speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        