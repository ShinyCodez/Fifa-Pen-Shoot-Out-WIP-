import pygame

class Goal:
    def __init__(self, x, y):
        self.goal_image = pygame.image.load("goal.png")
        self.rect_goal = self.goal_image.get_rect(topleft=(x, y))