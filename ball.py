import pygame
import math

class Ball:
    def __init__(self, x_ball, y_ball):
        self.x_ball = x_ball
        self.y_ball = y_ball
        self.image = pygame.image.load("ball.png")
        self.original_image = self.image.copy()  # Store a copy of the original image
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x_ball, self.y_ball, self.image_size[0], self.image_size[1])
        self.is_shooting = False
        self.target_pos = (0, 0)
        self.speed = 30
        self.shoot_timer = None
        self.minimum_size_ratio = 0.5  # The minimum size ratio (80% of the original size)

    def shoot(self, target_x, target_y):
        if not self.is_shooting and self.shoot_timer is None:
            self.is_shooting = True
            self.target_pos = (target_x, target_y)
            self.shoot_timer = pygame.time.get_ticks() + 1000  # Set the timer for 1 second (1000 milliseconds)

    def update(self):
        if self.is_shooting:
            if self.shoot_timer is not None and pygame.time.get_ticks() >= self.shoot_timer:
                target_x, target_y = self.target_pos
                distance = math.sqrt((target_x - self.x_ball) ** 2 + (target_y - self.y_ball) ** 2)
                if distance > self.speed:
                    ratio = self.speed / distance
                    dx = (target_x - self.x_ball) * ratio
                    dy = (target_y - self.y_ball) * ratio
                    self.x_ball += dx
                    self.y_ball += dy
                else:
                    self.x_ball = target_x
                    self.y_ball = target_y
                    self.is_shooting = False
                    self.shoot_timer = None  # Reset the timer

                # Calculate the new size based on the remaining distance
                remaining_distance = math.sqrt((target_x - self.x_ball) ** 2 + (target_y - self.y_ball) ** 2)
                size_ratio = remaining_distance / distance

                if size_ratio <= self.minimum_size_ratio:
                    # Calculate the size at the minimum ratio
                    new_width = int(self.image_size[0] * self.minimum_size_ratio)
                    new_height = int(self.image_size[1] * self.minimum_size_ratio)

                    # Resize the image using the calculated size
                    self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
                    self.rect = pygame.Rect(self.x_ball, self.y_ball, new_width, new_height)

    def shoot_to_mouse(self, mouse_x, mouse_y):
        self.shoot(mouse_x, mouse_y)
