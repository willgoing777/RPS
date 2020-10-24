import pygame
import button
import dungeon
from itertools import cycle
import random as rand
from enum import Enum

# The game is split into 4 scene
# The first scene is the start window, waiting for player to click button to start a game
# The second scene is the difficulty choose window, player can choose different mode of the game
# The third scene is the main playing window, player can make choice of RPS, try to beat the monsters in the dungeon
# The fourth scene is the end window, congrats for a win or show GG for the lose

# text flash event
BLINK_EVENT = pygame.USEREVENT+0

# Enum of game status
class Status(int, Enum):
    GAMELOSE = 0   # The total game lose
    RPSLOSE = 1    # The player loses in a single RPS compare
    DRAW = 2       # Draw of a single RPS compare
    RPSWIN = 3     # The player wins in a single RPS compare
    LEVELWIN = 4   # The player has beat the monster of current level
    GAMEWIN = 5    # The player beats all the monsters in all the levels, wins the total game

# pygame initialization
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.time.set_timer(BLINK_EVENT, 500)
pygame.display.set_caption("RPS")
icon = pygame.image.load("assets/icon.jpg")
pygame.display.set_icon(icon)

# First scene initialize
init_bg = pygame.image.load("assets/init_bg.jpg")
init_bg = pygame.transform.scale(init_bg, (800, 600))
screen.blit(init_bg, (0, 0))
welcome_font = pygame.font.Font("font.ttf", 40)
hint_font = pygame.font.Font("font.ttf", 20)
text = welcome_font.render("Welcome to RPS Dungeon", True, (0, 0, 0))
w, h = text.get_size()
screen.blit(text, (400 - w / 2, 100))
start_button = button.Button("START", 50, 275, 350, (0, 0, 0))
start_button.draw(screen)
pygame.draw.rect(screen, (255, 255, 255), (start_button.x, start_button.y, start_button.width, start_button.height),
                 2)
hint = hint_font.render("Click to start", True, (60, 60, 60))
off_hint = hint_font.render("Click to start", True, (0, 0, 0))
blink_surfaces = cycle([hint, off_hint])
blink_surface = next(blink_surfaces)

screen.blit(hint, (255, 420))
pygame.display.flip()

# four flags to control the main loop of four scenes
init = True
start = True
choose_difficult = True
end = True
# The main loop of the first scene
while init:

    for event in pygame.event.get():
        # Quit event
        if event.type == pygame.QUIT:
            init = False
            start = False
            choose_difficult = False
            end = False
        # Text flash event
        if event.type == BLINK_EVENT:
            blink_surface = next(blink_surfaces)

            screen.blit(blink_surface, (255 , 420))
        # User clicks somewhere(mouse down)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            # Change the border color of start button if it is clicked
            if start_button.click(x,y):
                pygame.draw.rect(screen, (100, 100, 100),
                                 (start_button.x , start_button.y , start_button.width , start_button.height ), 2)
        # User clicks somewhere(mouse up)
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = event.pos
            # Start a game if the start button is clicked
            # End first scene
            if start_button.click(x,y):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (start_button.x, start_button.y, start_button.width, start_button.height), 2)
                screen.fill((0,0,0))
                init = False
        clock.tick(60)
    pygame.display.update()

# Second scene intialize
easy_button = button.Button("EASY", 50, 275, 150, (255, 255, 255))
easy_button.draw(screen)
pygame.draw.rect(screen, (255, 255, 255), (easy_button.x, easy_button.y, easy_button.width, easy_button.height),
                 2)

medium_button = button.Button("MEDIUM", 50, 275, 300, (255, 255, 255))
medium_button.draw(screen)
pygame.draw.rect(screen, (255, 255, 255), (medium_button.x, medium_button.y, medium_button.width, medium_button.height),
                 2)

hard_button = button.Button("HARD", 50, 275, 450, (255, 255, 255))
hard_button.draw(screen)
pygame.draw.rect(screen, (255, 255, 255), (hard_button.x, hard_button.y, hard_button.width, hard_button.height),
                 2)


choosed_difficult = 1
# The main loop of the second scene
while choose_difficult:
    for event in pygame.event.get():
        # Quit event
        if event.type == pygame.QUIT:
            init = False
            start = False
            choose_difficult = False
            end = False
        # user clicks event (mouse down)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            # Change the border color of button if it is clicked
            if easy_button.click(x,y):
                pygame.draw.rect(screen, (100, 100, 100),
                                 (easy_button.x , easy_button.y , easy_button.width , easy_button.height ), 2)
            if medium_button.click(x,y):
                pygame.draw.rect(screen, (100, 100, 100),
                                 (medium_button.x , medium_button.y , medium_button.width , medium_button.height ), 2)
            if hard_button.click(x,y):
                pygame.draw.rect(screen, (100, 100, 100),
                                 (hard_button.x , hard_button.y , hard_button.width , hard_button.height ), 2)
        # user clicks event (mouse up)
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = event.pos
            # If user clicks one of the button, and chooses the difficulty
            # set the difficulty base on player choice and end the second scene
            if easy_button.click(x,y):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (easy_button.x, easy_button.y, easy_button.width, easy_button.height), 2)
                screen.fill((0,0,0))
                choosed_difficult = 1
                choose_difficult = False
            if medium_button.click(x,y):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (medium_button.x, medium_button.y, medium_button.width, medium_button.height), 2)
                screen.fill((0,0,0))
                choosed_difficult = 2
                choose_difficult = False
            if hard_button.click(x,y):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (hard_button.x, hard_button.y, hard_button.width, hard_button.height), 2)
                screen.fill((0,0,0))
                choosed_difficult = 3
                choose_difficult = False
    pygame.display.update()

# Second scene intialize
# Construct a player of dungeon base on the chosen difficulty
if choosed_difficult == 1:
    player = dungeon.Player(100)
elif choosed_difficult == 2:
    player = dungeon.Player(60)
elif choosed_difficult == 3:
    player = dungeon.Player(30)
else:
    player = dungeon.Player(999)


new_dungeon = dungeon.Dungeon(0)
info_font = pygame.font.Font("font.ttf", 20)
warn_font = pygame.font.Font("font.ttf", 40)
hp_text = info_font.render("HP: {0}".format(player.HP), True, (255, 255, 255))
attack_text = info_font.render("Attack: {0}".format(player.Weapon.attack), True, (255, 255, 255))
armor_text = info_font.render("Armor: {0}".format(player.Plate.armor), True, (255, 255, 255))
level_text = info_font.render("level: {0}".format(new_dungeon.level), True, (255, 255, 255))
top_hint = warn_font.render("PREPARE", True, (255, 255, 255))
w, h = top_hint.get_size()
mid_hint = info_font.render("Click and beat the monster!", True, (20, 20, 20))
off_mid_hint = info_font.render("Click and beat the monster!", True, (200, 200, 200))
blink_surfaces = cycle([mid_hint, off_mid_hint])
blink_surface = next(blink_surfaces)
dungeon_bg = pygame.image.load("assets/ground.png")
dungeon_bg = pygame.transform.scale(dungeon_bg, (800, 500))
champion_img = pygame.image.load("assets/champion.png")
champion_img = pygame.transform.scale(champion_img, (200, 200))
monster_img = pygame.image.load("assets/monster1.png")
monster_img = pygame.transform.scale(monster_img, (200, 200))
rock_img = pygame.image.load("assets/rock.png")
rock_img = pygame.transform.scale(rock_img, (100, 100))
paper_img = pygame.image.load("assets/paper.png")
paper_img = pygame.transform.scale(paper_img, (100, 100))
scissor_img = pygame.image.load("assets/scissor.png")
scissor_img = pygame.transform.scale(scissor_img, (100, 100))
qm_img = pygame.image.load("assets/question_mark.png")
qm_img = pygame.transform.scale(qm_img, (100, 100))
next_img = pygame.image.load("assets/next.png")
next_img = pygame.transform.scale(next_img, (200, 100))
choosed_RPS = None

# draw of redraw the main window of scene base on the type parameter(different game process)
# -1 for initialize
# and others are related to the Status Enum
def start_bg_init(type):
    screen.blit(mid_hint, (190, 120))
    screen.blit(dungeon_bg, (0, 100))
    screen.blit(champion_img, (100, 400))
    screen.blit(monster_img, (500, 400))
    if type == -1:
        screen.blit(top_hint, (400 - w / 2, 10))
        screen.blit(paper_img, (355, 200))
        screen.blit(hp_text, (10, 10))
        screen.blit(attack_text, (10, 40))
        screen.blit(armor_text, (10, 70))
        screen.blit(level_text, (640, 10))
        screen.blit(rock_img, (82, 200))
        screen.blit(scissor_img, (620, 200))
    if type == 0:
        screen.blit(hp_text, (10, 10))
        screen.blit(attack_text, (10, 40))
        screen.blit(armor_text, (10, 70))
        screen.blit(level_text, (640, 10))
    if type == 1:
        screen.blit(attack_text, (10, 40))
        screen.blit(armor_text, (10, 70))
        screen.blit(level_text, (640, 10))
    if type == 2:
        screen.blit(hp_text, (10, 10))
        screen.blit(attack_text, (10, 40))
        screen.blit(armor_text, (10, 70))
        screen.blit(level_text, (640, 10))
    if type == 3:
        screen.blit(hp_text, (10, 10))
        screen.blit(attack_text, (10, 40))
        screen.blit(armor_text, (10, 70))
        screen.blit(level_text, (640, 10))
    if type == 4:
        screen.blit(hp_text, (10, 10))
    if type == 5:
        screen.blit(hp_text, (10, 10))
        screen.blit(attack_text, (10, 40))
        screen.blit(armor_text, (10, 70))
        screen.blit(level_text, (640, 10))


# player compete with the monster (using RPS compare)
# base on the current hp of player and monster, return different status: Status Enum,
# delta if not draw (player or monster should be attaced if lose)
# monster choice for visualization
def compete(player_choice):
    monster_choice = dungeon.RPS(rand.randrange(3))
    if player_choice.compare(monster_choice) == -1:
        temp = max(new_dungeon.attack - player.Plate.armor, 0)
        if player.HP <= temp:
            return {"status": Status.GAMELOSE, "delta": temp, "m": monster_choice}
        else:
            return {"status": Status.RPSLOSE, "delta": temp, "m": monster_choice}
    elif player_choice.compare(monster_choice) == 0:
        return {"status": Status.DRAW, "m": monster_choice}
    else:
        temp = player.Weapon.attack
        if new_dungeon.Monster_HP <= temp:
            # The maximum dungeon level is based on the game difficulty, hard for more levels and easy for less levels
            if new_dungeon.level == choosed_difficult:
                return {"status": Status.GAMEWIN, "delta": temp, "m": monster_choice}
            else:

                return {"status": Status.LEVELWIN, "delta": temp, "m": monster_choice}
        else:
            return {"status": Status.RPSWIN, "delta": temp, "m": monster_choice}


start_bg_init(-1)


win_flag = 0
next_step = False
result = None
# Main loop of the third scene
while start:
    for event in pygame.event.get():
        # Quit event
        if event.type == pygame.QUIT:
            init = False
            start = False
            choose_difficult = False
            end = False
        # Text flash event
        if event.type == BLINK_EVENT:
            blink_surface = next(blink_surfaces)

            screen.blit(blink_surface, (190, 120))

        # user click event
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            # Rock clicked
            if 82 <= x <= 182 and 100 <= y <= 300 and not next_step:
                screen.blit(qm_img, (82, 200))
                screen.blit(qm_img, (355, 200))
                screen.blit(qm_img, (620, 200))
                choosed_RPS = dungeon.RPS(0)
                result = compete(choosed_RPS)

            # Paper clicked
            if 355 <= x <= 455 and 100 <= y <= 300 and not next_step:
                screen.blit(qm_img, (82, 200))
                screen.blit(qm_img, (355, 200))
                screen.blit(qm_img, (620, 200))
                choosed_RPS = dungeon.RPS(1)
                result = compete(choosed_RPS)

            # Scissor clicked
            if 620 <= x <= 720 and 100 <= y <= 300 and not next_step:
                screen.blit(qm_img, (82, 200))
                screen.blit(qm_img, (355, 200))
                screen.blit(qm_img, (620, 200))
                choosed_RPS = dungeon.RPS(2)
                result = compete(choosed_RPS)

            # Next step clicked
            # Lead to next RPS or next level or next scene base on the game status
            if 300 <= x <= 500 and 200 <= y <= 300 and next_step:
                pygame.time.delay(300)
                next_step = False
                result = None
                screen.fill((0, 0, 0))
                if win_flag == 0:
                    top_hint = warn_font.render("PREPARE", True, (255, 255, 255))
                    start_bg_init(-1)
                # End the third scene loop is the game lose or win
                else:
                    start = False


            pygame.display.update()
            pygame.time.delay(500)
            if result:
                screen.fill((0, 0, 0))
                monster_RPS = None
                # Deal with the result of competition
                # Game lose, winflag = -1, enable next_step button
                if result["status"] == Status.GAMELOSE:
                    start_bg_init(0)
                    monster_RPS = result["m"]
                    delta = result["delta"]

                    top_hint = warn_font.render("YOU LOSE!", True, (255, 255, 255))
                    delta_text = info_font.render("hp: -{}".format(delta), True, (255, 255, 255))
                    w2, h2 = delta_text.get_size()
                    screen.blit(delta_text, (400 - w2 / 2, 50))

                    start = False
                    win_flag = -1
                    next_step = True
                # RPS lose, player is attacked, enable next_step button
                if result["status"] == Status.RPSLOSE:
                    start_bg_init(1)
                    monster_RPS = result["m"]
                    delta = result["delta"]
                    player.HP -= delta

                    hp_text = info_font.render("HP: {0}".format(player.HP), True, (255, 255, 255))
                    screen.blit(hp_text, (10, 10))
                    top_hint = warn_font.render("YOU LOOSE!", True, (255, 255, 255))
                    delta_text = info_font.render("hp: -{}".format(delta), True, (255, 255, 255))
                    w2, h2 = delta_text.get_size()
                    screen.blit(delta_text, (400 - w2 / 2, 50))

                    next_step = True

                # Draw, blit and do nothing
                if result["status"] == Status.DRAW:
                    start_bg_init(2)
                    monster_RPS = result["m"]

                    top_hint = warn_font.render("DRAW!", True, (255, 255, 255))

                    next_step = True
                # RPS win, monster is attacked, enable next_step button
                if result["status"] == Status.RPSWIN:
                    start_bg_init(3)
                    monster_RPS = result["m"]
                    delta = result["delta"]
                    new_dungeon.Monster_HP -= delta
                    top_hint = warn_font.render("YOU WIN!", True, (255, 255, 255))
                    delta_text = info_font.render("Monster: -{}".format(delta), True, (255, 255, 255))
                    w2, h2 = delta_text.get_size()
                    screen.blit(delta_text, (400 - w2 / 2, 50))
                    print(new_dungeon.Monster_HP)
                    next_step = True
                # Level win, player gets new loot(randomly pick one from the loot chest),
                # create a new level of dungeon, enable next_step button
                if result["status"] == Status.LEVELWIN:
                    start_bg_init(4)
                    monster_RPS = result["m"]
                    delta = result["delta"]

                    new_loot = rand.sample(new_dungeon.Loots, 1)
                    new_loot = new_loot[0]
                    if isinstance(new_loot, dungeon.Weapon):
                        player.Weapon = new_loot

                    else:
                        player.Plate = new_loot
                    attack_text = info_font.render("Attack: {0}".format(player.Weapon.attack), True, (255, 255, 255))
                    armor_text = info_font.render("Armor: {0}".format(player.Plate.armor), True, (255, 255, 255))
                    screen.blit(attack_text, (10, 40))
                    screen.blit(armor_text, (10, 70))

                    new_level = new_dungeon.level + 1
                    new_dungeon = dungeon.Dungeon(new_level)
                    level_text = info_font.render("level: {0}".format(new_dungeon.level), True, (255, 255, 255))

                    screen.blit(level_text, (640, 10))
                    top_hint = warn_font.render("YOU WIN!", True, (255, 255, 255))
                    delta_text = info_font.render("Monster: -{}".format(delta), True, (255, 255, 255))
                    w2, h2 = delta_text.get_size()
                    screen.blit(delta_text, (400 - w2 / 2, 50))

                    next_step = True
                # Game win, winflag = 1, enable next_step button
                if result["status"] == Status.GAMEWIN:
                    start_bg_init(5)
                    monster_RPS = result["m"]
                    delta = result["delta"]

                    top_hint = warn_font.render("YOU WIN!", True, (255, 255, 255))
                    delta_text = info_font.render("Monster: -{}".format(delta), True, (255, 255, 255))
                    w2, h2 = delta_text.get_size()
                    screen.blit(delta_text, (400 - w2 / 2, 50))

                    win_flag = 1
                    start = False
                    next_step = True

                screen.blit(next_img, (300, 200))
                if choosed_RPS.value == 0:
                    screen.blit(rock_img, (82, 200))
                elif choosed_RPS.value == 1:
                    screen.blit(paper_img, (82, 200))
                else:
                    screen.blit(scissor_img, (82, 200))
                w1, h1 = top_hint.get_size()
                screen.blit(top_hint, (400 - w1 / 2, 10))
                if monster_RPS.value == 0:
                    screen.blit(rock_img, (620, 200))
                elif choosed_RPS.value == 1:
                    screen.blit(paper_img, (620, 200))
                else:
                    screen.blit(scissor_img, (620, 200))
        clock.tick(60)

    pygame.display.update()

# Fourth scene initialize
screen.fill((0, 0, 0))
# Show different base on win_flag
# -1 for lose, GGWP
# 1 for win, save the princess
if win_flag == -1:
    defeated_text = warn_font.render("GGWP, YOU LOSE!", True, (255, 255, 255))
    w,h = defeated_text.get_size()
    screen.blit(defeated_text, (400 - w/2, 200))
if win_flag == 1:
    win_text = warn_font.render("YOU SAVED THE PRINCESS!", True, (255, 255, 255))
    w, h = win_text.get_size()
    screen.blit(win_text, (400 - w / 2, 100))
    princess_img = pygame.image.load("assets/princess.png")
    princess_img = pygame.transform.scale(princess_img, (200, 200))
    screen.blit(princess_img, (300 , 200))
    grats_text = warn_font.render("CONGRATULATIONS!", True, (255, 255, 255))
    w, h = grats_text.get_size()
    screen.blit(grats_text, (400 - w / 2, 450))


# The main loop of the fourth scene
while end:
    for event in pygame.event.get():
        # Quit event
        if event.type == pygame.QUIT:
            init = False
            start = False
            choose_difficult = False
            end = False
    pygame.display.update()