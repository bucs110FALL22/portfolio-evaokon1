import random
import pygame
import math

#Part A
#Drawing Dart board
pygame.init()
window = pygame.display.set_mode((300, 300))
window.fill("blue")
screen_size = pygame.display.get_window_size()
pygame.draw.circle(window, "red", (screen_size[0] / 2, screen_size[1] / 2), screen_size[0] / 2)

pygame.display.flip()

pygame.draw.line(window, "black", (screen_size[0] / 2, 0), (screen_size[0] / 2, screen_size[1]))
pygame.display.flip()
pygame.draw.line(window, "black", (0, screen_size[1] / 2),
                 (screen_size[0], screen_size[1] / 2))
pygame.display.flip()
#Part B
for i in range(11):
    x3 = random.randrange(0, 300)
    y4 = random.randrange(0, 300)
    coordiantes = (x3, y4)
    # pygame.draw.circle(window,"Black",coordiantes,4)
    # pygame.display.flip()
    x = screen_size[0] / 2
    y = screen_size[1] / 2
    distance_from_center = math.hypot(x3 - x, y4 - y)
    is_in_circle = distance_from_center <= 300 / 2
    print(is_in_circle)
    if is_in_circle == True:
        pygame.draw.circle(window, "Green", coordiantes, 4)
        pygame.display.flip()
        pygame.time.wait(200)
    if is_in_circle == False:
        pygame.draw.circle(window, "Red", coordiantes, 4)
        pygame.display.flip()
        pygame.time.wait(200)

#Part C
window.fill("white")
window = pygame.display.set_mode((100, 100))

while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    red_button = pygame.draw.rect(window, "red", (200, 150, 100, 50))
    pygame.display.flip()
    blue_button = pygame.draw.rect(window, "blue", (200, 100, 200, 50))
    pygame.display.flip()
    pygame.time.wait(500)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if blue_button.collidepoint(mouse_x, mouse_y):
                teams = 'blue'
            else:
                teams = 'red'
            print(teams)

for i in range(11):
    x3 = random.randrange(0, 100)
    y4 = random.randrange(0, 100)
    coordiantes = (x3, y4)
    # pygame.draw.circle(window,"Black",coordiantes,4)
    # pygame.display.flip()
    x = screen_size[0] / 2
    y = screen_size[1] / 2
    distance_from_center = math.hypot(x3 - x, y4 - y)
    is_in_circle = distance_from_center <= 300 / 2
    print(is_in_circle)
    if is_in_circle == True:
        pygame.draw.circle(window, "black", coordiantes, 4)
        pygame.display.flip()
        pygame.time.wait(200)
# if is_in_circle == False:
#  pygame.draw.circle(window,"Red",coordiantes,4)
#  pygame.display.flip()
#  pygame.time.wait(200)

#Player
player1 = print("Who do you think will win the match today?")
player1 = input()

# player2 = print("Who do you think will win the match today?")
# player2 = input()

# player1_selection
# player2_selection