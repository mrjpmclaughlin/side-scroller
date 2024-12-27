import pygame

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 20

            screen.blit(enemy_surface, enemy_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > 0]
        return obstacle_list
    else: return []
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('THE GAME')
clock = pygame.time.Clock()
running = True
game_active = False

#score details
s_font = pygame.font.Font(None, 36)
score_surface = s_font.render('Eat it', False, 'Black')
score_rect = score_surface.get_rect(topright=(1260, 0))
# background picture details
background_surface = pygame.image.load('bg1.jpeg').convert()
bg_refit = pygame.transform.scale(background_surface, (1280, 620))

# ocean picture details the ocean will serve as the floor
test_surface = pygame.image.load('oceanShot.jpeg').convert()
ocean_refit = pygame.transform.scale(test_surface, (1280, 100))

# obstacle details
enemy_surface = pygame.image.load('crab.png').convert_alpha()
enemy_small = pygame.transform.scale(enemy_surface, (100,50))
enemy_rect = enemy_small.get_rect(bottomright = (1280, 645))

obstacle_rect_list = []

# player details
psurf = pygame.image.load('boatkid.png').convert_alpha()
prefit = pygame.transform.scale(psurf, (250, 150))
prect = prefit.get_rect(midbottom=(175, 625))
player_grav = 0

# game over surface
game_over_font = pygame.font.Font(None, 50)
game_over_surface = game_over_font.render('Lily''s Voyage', False, 'Black')
game_over_rect = score_surface.get_rect(topleft=(500, 100))

# timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1000)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and prect.bottom >= 625:
                    player_grav = -20

            if event.type == obstacle_timer:
                obstacle_rect_list.append(enemy_small.get_rect(bottomright = (1280, 645)))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                enemy_rect.left = 1280

    if game_active:
        screen.blit(bg_refit, (0, 0))
        screen.blit(ocean_refit, (0, 620))
        screen.blit(score_surface, score_rect)
        #enemy_rect.x -= 1
        #screen.blit(enemy_small, enemy_rect)

        player_grav += 1
        prect.y += player_grav
        if prect.bottom >=625:
            prect.bottom = 625
        screen.blit(prefit, prect)

        # obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
    #collision
        if enemy_rect.colliderect(prect):
            game_active = False

    # game over screen---need to make better
    else:
        screen.fill(('Blue'))
        screen.blit(game_over_surface, game_over_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()



#1:56 he talks about time. i don't know that I care right now