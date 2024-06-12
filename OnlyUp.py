import pygame
import random
import json
import os
#Quellen: Chatgpt, Tutorial: https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=8862s
#Texturen aaus dem Video und selbst gemacht
pygame.init()
screen = pygame.display.set_mode((1728, 972))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 50)
Level_Up_Font = pygame.font.Font('Pixeltype.ttf', 200)
Only_Up_Font = pygame.font.Font('Pixeltype.ttf',100)

# Lade oder initialisiere das Scoreboard
def load_scoreboard():
    if os.path.exists('scoreboard.json'):
        with open('scoreboard.json', 'r') as f:
            return json.load(f)
    else:
        return []

def save_scoreboard(scoreboard):
    with open('scoreboard.json', 'w') as f:
        json.dump(scoreboard, f)

scoreboard = load_scoreboard()

# Funktion zur Anzeige des Scoreboards
def display_scoreboard():
    screen.fill((0, 0, 0))
    title_surf = test_font.render('Scoreboard:', False, 'White')
    title_rect = title_surf.get_rect(center=(864, 100))
    screen.blit(title_surf, title_rect)

    for index, entry in enumerate(scoreboard):
        entry_surf = test_font.render(f"{entry['name']}: {entry['score']}", False, 'White')
        entry_rect = entry_surf.get_rect(center=(864, 150 + index * 50))
        screen.blit(entry_surf, entry_rect)

    pygame.display.update()
    pygame.time.wait(3000)  # Zeige das Scoreboard für 3 Sekunden an

# Funktion zur Abfrage des Spielernamens
def prompt_name():
    input_active = True
    name = ""
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode

        screen.fill((0, 0, 0))
        prompt_surf = test_font.render('Enter your name:', False, 'White')
        prompt_rect = prompt_surf.get_rect(center=(864, 200))
        screen.blit(prompt_surf, prompt_rect)
        
        name_surf = test_font.render(name, False, 'White')
        name_rect = name_surf.get_rect(center=(864, 300))
        screen.blit(name_surf, name_rect)
        
        pygame.display.update()
        clock.tick(30)
    
    return name

# Funktion zur Anzeige des Punktestands
def display_score(score):
    score_surf = test_font.render(f'Score: {score}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(864, 100))
    screen.blit(score_surf, score_rect)

# Funktion zur Erstellung von Plattformen
def generate_platforms():
    platforms = []
    small_islands = []
    for i in range(16):
        x = random.randint(-100, 3000)
        y = 1000 - i * 125
        platforms.append(pygame.Rect(x, y, ile_surface.get_width(), ile_surface.get_height()))
        
        # Füge kleine Inseln hinzu
        if i % 2 == 0:  # Füge eine kleine Insel für jede zweite Plattform hinzu
            x_klein = random.randint(-100, 3000)
            y_klein = y - random.randint(300, 700)  # Platziere kleine Inseln über den Plattformen
            small_islands.append(pygame.Rect(x_klein, y_klein, insel_klein_surface.get_width(), insel_klein_surface.get_height()))
    
    return platforms, small_islands

# Funktion zur Erstellung neuer Plattformen
def add_new_platform(platforms, snails, small_islands):
    last_platform = platforms[-1]
    x = random.randint(max(last_platform.x - 800, 0), min(last_platform.x + 400, 2000 - ile_surface.get_width()))
    min_y_distance = 350
    max_y_distance = 500
    y = last_platform.top - random.randint(min_y_distance, max_y_distance)
    # Erstelle eine normale Plattform
    platform = pygame.Rect(x, y, ile_surface.get_width(), ile_surface.get_height())
    platforms.append(platform)
    if random.random() < 0.3:
        # Erstelle eine Schnecke auf der Plattform
        snail_rect = snail_surf.get_rect(midbottom=(platform.x + platform.width // 2, platform.top))
        snails.append({'rect': snail_rect, 'speed': 4.5, 'direction': 1, 'platform': platform})
    if random.random() < 0.4:  # 30% Chance, eine kleine Insel hinzuzufügen
        x_klein = random.randint(-100, 3000)
        y_klein = platform.top - random.randint(350, 500)
        small_island = pygame.Rect(x_klein, y_klein, insel_klein_surface.get_width(), insel_klein_surface.get_height())
        small_islands.append(small_island)

# Timer für Hindernisse und Bewegung
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

Movement_timer = pygame.USEREVENT + 1
pygame.time.set_timer(Movement_timer, 250)

# Stage 1 Assets
sky_surface_stage1 = pygame.image.load('skystage1.png').convert()
ground_surface_stage1 = pygame.image.load('groundultragig.png').convert()
ile_surface_stage1 = pygame.image.load('PlattformsStage1.1.png')
ile_small_surface_stage1 = pygame.image.load('PlattformKlein.png')

# Stage 1.1 Assets
sky_surface_stage1_1 = pygame.image.load('Night_Sky.png').convert()

# Stage 1.2 Assets
sky_surface_stage1_2 = pygame.image.load('Night_Sky_Dark.png').convert()

# Stage 2 Assets
sky_surface_stage2 = pygame.image.load('SkyStage2Snowy.png').convert()
ground_surface_stage2 = pygame.image.load('groundultragig.png').convert()
ile_surface_stage2 = pygame.image.load('PlatformSnow.png')
ile_small_surface_stage2 = pygame.image.load('PlatformKleinSnow.png')

# Stage 3 Assets
sky_surface_stage3 = pygame.image.load('Red_Sky.png').convert()
ile_surface_stage3 = pygame.image.load('Plattformsstage_Red.png')
ile_small_surface_stage3 = pygame.image.load('Plattformklein_Red.png')


# Stage 4 Assets
sky_surface_stage4 = pygame.image.load('Red_Sky_Dark.png').convert()
ile_surface_stage4 = pygame.image.load('Plattformsstage_Red_2.png')
ile_small_surface_stage4 = pygame.image.load('Plattformklein_Red_2.png')

# Stage 5 Assets
sky_surface_stage5 = pygame.image.load('Violet_Sky.png').convert()
ile_small_surface_stage5 = pygame.image.load('Plattformlkein_Violette.png')
ile_surface_stage5 = pygame.image.load('Plattformsstage_Violette.png')
# Stage 6 Assets
sky_surface_stage6 = pygame.image.load('Violette_Sky_2.png').convert()
ile_surface_stage6 = pygame.image.load('Plattformsstage_Violette_2.png')
ile_small_surface_stage6 = pygame.image.load('Plattformklein_Violette_2.png')

# Stage 7 Assets
sky_surface_stage7 = pygame.image.load('Night_Sky_Midnight.png').convert()

# Stage 8 Assets
sky_surface_stage8 = pygame.image.load('Eye_Sky.png').convert()

# Stage End of the Game Assets
sky_surface_stage9 = pygame.image.load('Endgame.png').convert()

# Aktuelle Stage Assets
sky_surface = sky_surface_stage1
ground_surface = ground_surface_stage1
ile_surface = ile_surface_stage1

text_surface = test_font.render('My Game', False, 'Green')

snail_surf = pygame.image.load('snail1.png').convert_alpha()
ile_surface = pygame.image.load('PlattformsStage1.1.png')
ile_rect = ile_surface.get_rect(bottomright=(720, 720))
insel_klein_surface = pygame.image.load('PlattformKlein.png').convert_alpha()

player_walk_right_surf = pygame.image.load('player_walk_1.png').convert_alpha()
player_walk_left_surf = pygame.image.load('player_walk_Left.png').convert_alpha()
player_stand_surf = pygame.image.load('player_stand.png').convert_alpha()
player_rect = player_stand_surf.get_rect(midbottom=(864, 720))

player_gravity = 0
player_speed = 5
sprint_multiplier = 2

# Musik laden und Lautstärke einstellen
pygame.mixer.music.load('Refreshing Elevator music.mp3') # Quelle: https://www.youtube.com/watch?v=9v9-Nw4nAZg
pygame.mixer.music.set_volume(0.3)  # Setze die Lautstärke auf 30%
pygame.mixer.music.play(-1)  # Spiele die Musik in einer Schleife ab

# Sprungsound laden
jump_sound = pygame.mixer.Sound('Jumpsound.mp3')

jump_count = 0
max_jumps = 2
camera_x = 0
camera_y = 0

platforms, small_islands = generate_platforms()
snails = []
start_time = 0
game_active = False
name = ""
fall_start_y = player_rect.y
level_up_display_time = 0

# Definiere Grenzen
left_border = -100
right_border = 3000

# Funktion zur Bewegung der Schnecken
def move_snails(snails):
    for snail in snails:
        snail['rect'].x += snail['speed'] * snail['direction']
        if snail['rect'].left <= snail['platform'].left or snail['rect'].right >= snail['platform'].right:
            snail['direction'] *= -1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w) and jump_count < max_jumps:
                player_gravity = -23.5
                jump_count += 1
                if jump_count == 1: 
                    jump_sound.play()  # Spiele den Sprungsound ab
        else:
            screen.fill(("Cyan"))
            player_rect.midbottom = (864, 720)  # Setze die Spielerposition auf die Mitte unten
            screen.blit(player_stand_surf, player_rect)
            game_title_surf = Only_Up_Font.render('Only Up', True, 'White') 
            game_title_rect = game_title_surf.get_rect(center=(864, 100)) 
            screen.blit(game_title_surf, game_title_rect)
            start_surf = test_font.render('Press Space to Start', False, (255, 255, 255))
            start_rect = start_surf.get_rect(center=(864, 350))
            screen.blit(start_surf, start_rect)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                name = prompt_name()
                start_time = int(pygame.time.get_ticks() / 1000)
                fall_start_y = player_rect.y
                player_rect.midbottom = (80, 1000)  # Setze die Spielerposition auf die Startposition zurück

    if game_active:
        keys = pygame.key.get_pressed()
        current_speed = player_speed * sprint_multiplier if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] else player_speed

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player_rect.x -= current_speed
            player_surf = player_walk_left_surf
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player_rect.x += current_speed
            player_surf = player_walk_right_surf
        else:
            player_surf = player_stand_surf

        player_gravity += 1
        player_rect.y += player_gravity

        if player_gravity > 0 and player_rect.bottom >= 1000:
            player_rect.bottom = 1000
            player_gravity = 0
            jump_count = 0
            fall_start_y = player_rect.y

        for platform in platforms:
            if player_rect.colliderect(platform) and player_gravity > 0 and player_rect.bottom - player_gravity <= platform.top:
                player_rect.bottom = platform.top
                player_gravity = 0
                jump_count = 0
                fall_start_y = player_rect.y
        for small_island in small_islands:
            if player_rect.colliderect(small_island) and player_gravity > 0 and player_rect.bottom - player_gravity <= small_island.top:
                player_rect.bottom = small_island.top
                player_gravity = 0
                jump_count = 0
                fall_start_y = player_rect.y
        
        if player_rect.left < left_border:
            player_rect.left = left_border
        elif player_rect.right > right_border:
            player_rect.right = right_border

        camera_x += (player_rect.x - camera_x - 864) * 0.1
        camera_y += (player_rect.y - camera_y - 486) * 0.1

        screen.fill((135, 206, 235))

        # Ändere die Stage basierend auf dem Punktestand
        score = int((320 - player_rect.bottom + 700) * 0.005)
        if score >= 50 and score <= 99:
            if sky_surface != sky_surface_stage1:
                level_up_disyplay_time = pygame.time.get_ticks()
            sky_surface = sky_surface_stage1_2
            pygame.mixer.music.set_volume(0.65)  
            snail_surf = pygame.image.load('snail2.png').convert_alpha()

        elif score >= 100 and score <= 149:
            sky_surface = sky_surface_stage1_1
            pygame.mixer.music.set_volume(0.55)  
            snail_surf = pygame.image.load('snail3.png').convert_alpha()

        elif score >=150 and score <=199:
            sky_surface = sky_surface_stage7
            snail_surf = pygame.image.load('snail4.png').convert_alpha()
            pygame.mixer.music.set_volume(0.45)

        elif score >= 200 and score <= 299:
            sky_surface = sky_surface_stage2
            ground_surface = ground_surface_stage2
            ile_surface = ile_surface_stage2
            insel_klein_surface = ile_small_surface_stage2
            snail_surf = pygame.image.load('snail10.png').convert_alpha()
            pygame.mixer.music.set_volume(0.35)
        elif score >= 300 and score <= 399:
            sky_surface = sky_surface_stage5
            ile_surface = ile_surface_stage5
            insel_klein_surface = ile_small_surface_stage5
            snail_surf = pygame.image.load('snail5.png').convert_alpha()
            pygame.mixer.music.set_volume(0.25)

        elif score >=400 and score <=499:
            sky_surface = sky_surface_stage6
            ile_surface = ile_surface_stage6
            insel_klein_surface = ile_small_surface_stage6
            snail_surf = pygame.image.load('snail7.png').convert_alpha()
            pygame.mixer.music.set_volume(0.15)

        elif score >=500 and score <=599:
            sky_surface = sky_surface_stage3
            ile_surface = ile_surface_stage3
            insel_klein_surface = ile_small_surface_stage3
            snail_surf = pygame.image.load('snail6.png').convert_alpha()
            pygame.mixer.music.set_volume(0.05)

        elif score >=600 and score <=699:
            sky_surface = sky_surface_stage4
            ile_surface = ile_surface_stage4
            insel_klein_surface = ile_small_surface_stage4
            snail_surf = pygame.image.load('snail8.png').convert_alpha()
            pygame.mixer.music.set_volume(0.02)

        elif score >=700 and score <= 999:
            sky_surface = sky_surface_stage8
            snail_surf = pygame.image.load('snail9.png').convert_alpha()
            pygame.mixer.music.set_volume(0)

        elif score >=1000 and score <= 1004:
            sky_surface = sky_surface_stage9
            pygame.mixer.music.set_volume(0.5)
            ground_surface = ground_surface_stage1
            ile_surface = ile_surface_stage1
            insel_klein_surface = ile_small_surface_stage1
            snail_surf = pygame.image.load('snail1.png').convert_alpha()
        
        elif score >= 1005:
            pygame.time.wait(100)
            pygame.quit()
        else:
            sky_surface = sky_surface_stage1
            ground_surface = ground_surface_stage1
            ile_surface = ile_surface_stage1
            insel_klein_surface = ile_small_surface_stage1
            snail_surf = pygame.image.load('snail1.png').convert_alpha()
            pygame.mixer.music.set_volume(0.7)
        for i in range(-1, (screen.get_height() // sky_surface.get_height()) + 2):
            for j in range(-1, (screen.get_width() // sky_surface.get_width()) + 2):
                screen.blit(sky_surface, (j * sky_surface.get_width() - (camera_x % sky_surface.get_width()), i * sky_surface.get_height() - (camera_y % sky_surface.get_height())))

        for i in range(-1, (screen.get_width() // ground_surface.get_width()) + 2):
            screen.blit(ground_surface, (i * ground_surface.get_width() - (camera_x % ground_surface.get_width()), 1000 - camera_y))

        display_score(score)

        for platform in platforms:
            screen.blit(ile_surface, (platform.x - camera_x, platform.y - camera_y))

        # Bewege und zeichne Schnecken
        move_snails(snails)
        for snail in snails:
            screen.blit(snail_surf, (snail['rect'].x - camera_x, snail['rect'].y - camera_y))

        # Zeichne kleine Inseln
        for small_island in small_islands:
            screen.blit(insel_klein_surface, (small_island.x - camera_x, small_island.y - camera_y))

        screen.blit(player_surf, (player_rect.x - camera_x, player_rect.y - camera_y))

        if platforms[-1].top > player_rect.top - 400:
            add_new_platform(platforms, snails, small_islands)

        # Zeige "Level Up" für eine kurze Dauer an
        if level_up_display_time and pygame.time.get_ticks() - level_up_display_time < 2000:  # 2000 ms (2 Sekunden)
            level_up_surf = Level_Up_Font.render('Level Up!', False, 'Cyan')
            level_up_rect = level_up_surf.get_rect(center=(864, 200))
            screen.blit(level_up_surf, level_up_rect)

        # Überprüfe Fallstrecke und Spielende-Bedingungen
        fall_distance = player_rect.y - fall_start_y
        for snail in snails:
            if fall_distance > 1000 or player_rect.colliderect(snail['rect']):
                game_active = False
                scoreboard.append({'name': name, 'score': score})
                scoreboard = sorted(scoreboard, key=lambda x: x['score'], reverse=True)[:10]
                save_scoreboard(scoreboard)
                display_scoreboard()

    pygame.display.update()
    clock.tick(60)
