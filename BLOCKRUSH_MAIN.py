#BlockRush - Main Game File
import pygame, sys

from BLOCKRUSH.GAMECLASS import Game
from BLOCKRUSH.colors import Colors

pygame.init()
import pygame
pygame.mixer.init()

# Background music
pygame.mixer.music.load("C:\\Users\\Adeel\\Downloads\\ytmp3free.cc_tetris-mobile-androidios-theme-high-quality-youtubemp3free.org.mp3")
pygame.mixer.music.set_volume(4)
pygame.mixer.music.play(-1)
#sound effects
line_clear_sound = pygame.mixer.Sound("C:\\Users\\Adeel\\Downloads\\tetris-gb-21-line-clear.mp3")
move_sound = pygame.mixer.Sound("C:\\Users\\Adeel\\Downloads\\tetris (1).mp3")
rotate_sound = pygame.mixer.Sound("C:\\Users\\Adeel\\Downloads\\tetris (1).mp3")
game_over_sound = pygame.mixer.Sound("C:\\Users\\Adeel\\Downloads\\game-over.mp3")


game=Game()
# Game over
if game.game_over:
    game_over_sound.play()
# Window and timing
WIDTH, HEIGHT = 675, 785
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("💕BLOCKRUSH💕")
clock = pygame.time.Clock()

# Fonts
title_font = pygame.font.Font("C:\\Users\\Adeel\\OneDrive\\Desktop\\TETRIS\\PressStart2P.ttf", 68)
small_font = pygame.font.Font("C:\\Users\\Adeel\\OneDrive\\Desktop\\TETRIS\\PressStart2P.ttf", 24)
font = pygame.font.Font("C:\\Users\\Adeel\\OneDrive\\Desktop\\TETRIS\\PressStart2P.ttf", 20)

# Backgrounds
menu_background = pygame.image.load("C:\\Users\\Adeel\\OneDrive\\Desktop\\SEMESTER 1\\BLOCKRUSH\\blockrush innn.png")
menu_background = pygame.transform.scale(menu_background, (WIDTH, HEIGHT))

game_background = pygame.image.load("C:\\Users\\Adeel\\OneDrive\\Desktop\\SEMESTER 1\\BLOCKRUSH\\download (4) - Copy.jpg")
game_background = pygame.transform.scale(game_background, (450, HEIGHT))

def draw_menu_bg():
    screen.blit(menu_background, (0, 0))


#Welcome Screen
def welcome_screen():
    percent = 0
    bar_w, bar_h = 500, 20
    bar_x=  WIDTH//2-bar_w//2
    bar_y=HEIGHT-100
    last = pygame.time.get_ticks()


    while percent < 100:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if pygame.time.get_ticks() - last > 400:
            percent = min(100, percent + 10)
            last = pygame.time.get_ticks()

        draw_menu_bg()

        # Loading bar only
        pygame.draw.rect(screen, Colors.sweet_pink, (bar_x, bar_y, bar_w, bar_h), 2)
        pygame.draw.rect(screen, Colors.dark_lavender, (bar_x, bar_y, int(bar_w * percent / 100), bar_h))

        txt = small_font.render(f"GAME LOADING.... {percent}%", True, (251,195,196))
        screen.blit(txt, (WIDTH//2 - txt.get_width()//2, bar_y +bar_h+10))

        pygame.display.flip()
        clock.tick(60)


# Ask Username
def ask_username():
    bg_image = pygame.image.load("C:\\Users\\Adeel\\Downloads\\download (18).jpg")
    name = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return name or "PLAYER"
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    ch = event.unicode
                    if ch and ch.isalnum():
                        name += ch.upper()

        screen.fill((0, 0, 0))
        screen.blit(bg_image, (WIDTH // 2 - bg_image.get_width() // 2,  HEIGHT // 2 - bg_image.get_height() // 2))

        glitter_pink = (229, 103, 155)
        highlight_pink = (255, 182, 193)
        # Glow layers
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            glow = title_font.render("BLOCKRUSH", True, highlight_pink)
            screen.blit(glow, (WIDTH // 2 - glow.get_width() // 2 + dx, 120 + dy))
        title = title_font.render("BLOCKRUSH", True, glitter_pink)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 130))

        prompt = small_font.render("ENTER YOUR NAME:", True, Colors.sweet_pink)
        screen.blit(prompt, (WIDTH//2 - prompt.get_width()//2, 300))

        name_txt = small_font.render(name, True, (224, 33, 138))
        screen.blit(name_txt, (WIDTH//2 - name_txt.get_width()//2, 340))

        tip = small_font.render("Press Enter to continue", True, Colors.white)
        screen.blit(tip, (WIDTH//2 - tip.get_width()//2, 390))

        pygame.display.flip()
        clock.tick(60)


# Option Box (Start / Quit)
def option_screen(username):
    bg_image = pygame.image.load("C:\\Users\\Adeel\\Downloads\\download (16).jpg")
    options = ["CONTINUE", "QUIT"]
    selected = 0
    box_rect = pygame.Rect(WIDTH//2 - 180, 280, 360, 200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    selected = (selected - 1) % len(options)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    selected = (selected + 1) % len(options)
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    if selected == 0:
                        return True
                    else:
                        pygame.quit()
                        sys.exit()
        # Background
        screen.fill((255, 240, 245))
        screen.blit(bg_image, (WIDTH // 2 - bg_image.get_width() // 2, HEIGHT // 2 - bg_image.get_height() // 2))

        # Title
        glitter_pink = (229, 103, 155)
        highlight_pink = (255, 182, 193)
        # Glow layers
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            glow = title_font.render("BLOCKRUSH", True, highlight_pink)
            screen.blit(glow, (WIDTH // 2 - glow.get_width() // 2 + dx, 120 + dy))
        title = title_font.render("BLOCKRUSH", True, (255, 105, 180))  # hot pink
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 130))

        # Greeting
        msg = small_font.render(f"HELLO {username}", True, Colors.white) # lavender
        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, 220))

        # Box with rounded edges
        pygame.draw.rect(screen, (255, 182, 193), box_rect, border_radius=18)  # light pink fill
        pygame.draw.rect(screen, (255, 105, 180), box_rect, 4, border_radius=18)  # darker pink border

        # Options
        for i, text in enumerate(options):
            is_sel = (i == selected)
            row_y = 330 + i * 60
            opt_width = 260
            opt_rect = pygame.Rect(WIDTH // 2 - opt_width // 2, row_y - 6, opt_width, 40)
            if is_sel:
                pygame.draw.rect(screen, (40, 40, 80), opt_rect, border_radius=8)
            color = Colors.chocolate_brown if is_sel else Colors.dark_lavender
            option_surface = small_font.render(text, True, color)
            screen.blit(option_surface, (WIDTH // 2 - option_surface.get_width() // 2, row_y))

        tip = small_font.render("Use ↑/↓ and Enter", True, Colors.white)
        screen.blit(tip, (WIDTH // 2 - tip.get_width() // 2, box_rect.bottom + 20))

        pygame.display.flip()
        clock.tick(60)
def load_high_score():
    try:
        with open("../highscore.txt", "r") as f:
            return int(f.read())
    except:
        return 0   # if file doesn't exist yet

def save_high_score(score):
    with open("../highscore.txt", "w") as f:
        f.write(str(score))

def game_over_screen(final_score,high_score):
    high_score = load_high_score()
    options = ["RESTART", "QUIT"]
    selected = 0

    screen_out = pygame.image.load("C:\\Users\\Adeel\\OneDrive\\Desktop\\SEMESTER 1\\BLOCKRUSH\\ndscc.jpg")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    selected = (selected - 1) % len(options)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    selected = (selected + 1) % len(options)
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    if selected == 0:
                        return "restart"   # exits Game Over screen
                    else:
                        return "quit"

        # NEW: clear the screen so it's a fresh Game Over screen
        screen.fill((0, 0, 0))

        # Draw background
        screen.blit(screen_out, (0, 0))
        # Title
        over_font = pygame.font.Font("C:\\Users\\Adeel\\OneDrive\\Desktop\\TETRIS\\PressStart2P.ttf", 50)
        title = over_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))

        # Final score and highest score
        score_txt = font.render(f"FINAL SCORE: {final_score}", True, Colors.chocolate_brown)
        high_msg = font.render(f"High Score: {high_score}", True, Colors.crimson_red)

        screen.blit(score_txt, (WIDTH//2 - score_txt.get_width()//2, 230))
        screen.blit(high_msg, (WIDTH//2 - score_txt.get_width()//2, 275))

        # Options box
        box = pygame.Rect(WIDTH//2 - 160, 300, 320, 160)
        pygame.draw.rect(screen,Colors.boundary_color, box, 3)

        # Options
        for i, text in enumerate(options):
            y = 340 + i * 60
            rect = pygame.Rect(WIDTH//2 - 120, y - 6, 240, 40)
            if i == selected:
                pygame.draw.rect(screen, (40, 40, 80), rect, border_radius=8)
            color = Colors.orange if i == selected else Colors.dark_lavender
            surf = small_font.render(text, True, color)
            screen.blit(surf, (WIDTH//2 - surf.get_width()//2, y))

        pygame.display.flip()   # update the screen






# Tetris Game Loop
def run_blockrush():
    game = Game()
    high_score = load_high_score()

    score_surface = font.render("SCORE", True, (255, 192, 203))
    title_surface = font.render("NEXT BLOCK", True, (255, 192, 203))
    score_rect = pygame.Rect(480, 100, 170, 60)
    next_rect  = pygame.Rect(480, 240, 170, 150)

    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if game.game_over:
                    if event.key == pygame.K_RETURN:
                        game.reset()
                else:
                    if event.key == pygame.K_LEFT:
                        game.move_left()
                        move_sound.play()
                    elif event.key == pygame.K_RIGHT:
                        game.move_right()
                        move_sound.play()
                    elif event.key == pygame.K_DOWN:
                        game.move_down()
                        move_sound.play()
                        game.update_score(0, 1)
                    elif event.key == pygame.K_UP:
                        game.rotate()
                        rotate_sound.play()
            if event.type == GAME_UPDATE and not game.game_over:
                game.move_down()

        if game.lines_cleared > 0:
            line_clear_sound.play()
            game.lines_cleared = 0


            # Game over check
        if game.game_over:
            game_over_sound.play()
            running = False



        screen.fill((102, 0, 102))
        screen.blit(game_background, (0, 0))
        game.draw(screen)


        if game.game_over:
            if game.score > high_score:
                high_score = game.score
                save_high_score(high_score)

            action = game_over_screen(game.score, high_score)
            if action == "restart":
                game.reset()
            else:
                pygame.quit()
                sys.exit()

        # Score box
        screen.blit(score_surface, (510, 60))
        pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)

        # Render score and level
        score_value_surface = font.render(f"{game.score}", True, Colors.black)
        level_value_surface = font.render(f"Level: {game.level}", True, Colors.deep_pink)

        # Render high score title and value separately
        high_score_title_surface = font.render("HIGH SCORE", True, Colors.crimson_red)
        high_score_value_surface = font.render(str(high_score), True, Colors.crimson_red)

        # Blit score and level
        screen.blit(score_value_surface, (550, 120))
        screen.blit(level_value_surface, (480, 500))

        # Blit high score title and value stacked vertically
        screen.blit(high_score_title_surface, (460, 600))
        screen.blit(high_score_value_surface, (520, 600+ high_score_title_surface.get_height() + 5))
        # Next block box
        screen.blit(title_surface, (460, 190))
        pygame.draw.rect(screen, (173, 216, 230), next_rect, 0, 6)
        game.draw_next_block(screen, next_rect)

        #Game over menu
        if game.game_over:
            options = ["RESTART", "EXIT"]
            selected = 0

            while game.game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key in (pygame.K_UP, pygame.K_w):
                            selected = (selected - 1) % len(options)
                        elif event.key in (pygame.K_DOWN, pygame.K_s):
                            selected = (selected + 1) % len(options)
                        elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                            if selected == 0:  # Restart
                                game.reset()
                            else:  # Exit
                                pygame.quit()
                                sys.exit()

                # Draw background and grid again
                screen.fill((102, 0, 102))
                screen.blit(game_background, (0, 0))
                game.draw(screen)

                # Game Over text
                over_font = pygame.font.SysFont("Times New Roman", 50, bold=True)
                over_surface = over_font.render("GAME OVER", True, (255, 0, 0))
                over_rect = over_surface.get_rect(center=(225, 180))
                screen.blit(over_surface, over_rect)

                # Final score
                score_msg = font.render(f"Final Score: {game.score}", True, Colors.white)
                score_rect = score_msg.get_rect(center=(225, 240))
                screen.blit(score_msg, score_rect)

                # Options box
                box_rect = pygame.Rect(150, 300, 150, 120)
                pygame.draw.rect(screen, Colors.white, box_rect, 3)

                for i, text in enumerate(options):
                    is_sel = (i == selected)
                    row_y = 320 + i * 50
                    opt_rect = pygame.Rect(160, row_y - 6, 130, 40)
                    if is_sel:
                        pygame.draw.rect(screen, (40, 40, 80), opt_rect, border_radius=6)
                    color = Colors.light_blue if is_sel else Colors.olive_green
                    option_surface = small_font.render(text, True, color)
                    screen.blit(option_surface, (225 - option_surface.get_width() // 2, row_y))



        pygame.display.flip()
        clock.tick(60)



# Program flow

def main():
    welcome_screen()        # Show loading bar
    player = ask_username() # Ask for player name
    option_screen(player)
    run_blockrush()
    game_over_screen(final_score=0)

# This ensures the game starts when you run the file
if __name__ == "__main__":
    main()