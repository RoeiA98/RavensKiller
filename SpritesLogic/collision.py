import pygame # type: ignore


class CollisionsHandler:

    def __init__(self,
                 player,
                 player_health,
                 fly_raven_group,
                 ground_raven_group,
                 deadly_raven_group,
                 all_enemies):

        self.player = player
        self.player_health = player_health
        self.fly_raven_group = fly_raven_group
        self.ground_raven_group = ground_raven_group
        self.deadly_raven_group = deadly_raven_group
        self.all_enemies = all_enemies
        self.fly_raven_damage = 0
        self.ground_raven_damage = 0

    def detect_collision(self):
        # Fly raven hit
        if pygame.sprite.spritecollide(self.player.sprite, self.fly_raven_group, True):
            self.player_health.hp -= self.fly_raven_damage
            if self.player_health.hp <= 0:
                self.all_enemies.empty()
                return False

        # Ground raven hit
        if pygame.sprite.spritecollide(self.player.sprite, self.ground_raven_group, True):
            self.player_health.hp -= self.ground_raven_damage
            if self.player_health.hp <= 0:
                self.all_enemies.empty()
                return False

        # Deadly raven hit
        if pygame.sprite.spritecollide(self.player.sprite, self.deadly_raven_group, True):
            self.all_enemies.empty()
            return False

        return True
