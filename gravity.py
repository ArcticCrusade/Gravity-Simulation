import pygame
from gravityutil import *
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
total_time = 0
x_velocity = 120
y_velocity = -50
mass = 1000000
font = pygame.font.Font('freesansbold.ttf', 28)
center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
planets = []
s_pressed = False
mouse_down = False

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    left, middle, right = pygame.mouse.get_pressed()

    if left and not mouse_down:
        planets.append(Planet(pygame.Vector2(pygame.mouse.get_pos()), mass, keys[pygame.K_s]))
        mouse_down = True
    elif not left:
        mouse_down = False

    

    if keys[pygame.K_PLUS] or keys[pygame.K_EQUALS]:
        mass += 100000
    if keys[pygame.K_p]:
        mass += 1000000
    if keys[pygame.K_r]:
        planets = []
    if keys[pygame.K_1]:
        mass = 100000
    elif keys[pygame.K_9]:
        mass = 100000000
    if (keys[pygame.K_MINUS] or keys[pygame.K_UNDERSCORE]) and mass > 200000:
        mass -= 100000
    if keys[pygame.K_m] and mass > 1000000:
        mass -= 1000000
    

    screen.fill("black")
    text = font.render("Mass: " + str(mass / 1000000) + " Million", True, (255, 255, 255), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (screen.get_width() - 125, 20)
    screen.blit(text, text_rect)

    for planet1 in planets:
        planet1.x_accel = 0
        planet1.y_accel = 0
        for planet2 in planets:
            accel = calculate_accel(planet1, planet2)
            planet1.x_accel += accel[0]
            planet1.y_accel += accel[1]
        planet1.x_velocity += planet1.x_accel * dt
        planet1.y_velocity += planet1.y_accel * dt
        planet1.x_pos += planet1.x_velocity * dt
        planet1.y_pos += planet1.y_velocity * dt


    for planet in planets:
        pygame.draw.circle(screen, planet.color, planet.get_pos(), planet.radius)


    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
