"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

"""
Hi this is my game I have wasted time debbuging for the past 2 hours so ima write this like i hate the code

Choice_text should work for most things and display over all things if not well bad code lol

pg is just a short way of saying thing

text_object is used for putting text in

Code is a lot so i hope u enjoy there could be things i forgot to remove while debbuging it to look a way i want

Recution is being used for the game to run

if u see death text + return that will pull the death text and return it to death screen also I have of as rn not added a replay option so user might not be able to do that unless i have added it in after

we have a fight with a zombie and there is a fun fight with it user has a random chance of dieing or living also dont run away u will die lol

start menu is not working that explains the game so might remove it or fix the bug im no seeing

ai was used input box and making sure text_object looks good but the base was made by me i just ai for resposiveness so it doesnt look bad and i could skim over making resposive code my self
funny that while reading over ai code i saw that if i wasnt behind i could of learned it or made it my self with some thinking

for input of what user does i did have ai explain to me that i need to use global so it could be used for some things

main() calls recution and there is error checking just in case there is a bug an yoou can bring it back to me to fix also doesnt work 100% of the time
and was great for debbuging the recution at times

the win screens are there own thing but i would love to try making this code smaller and having a win screen like the death screen



"""

# all imports and files for later uses
import pygame as pg
import random
file = open("Blood_Altar_inside.png")
file = open("Death.jpg")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
# start pygame
pg.init()
# Set the width and height of the screen [width, height]
size = (720, 480)
screen = pg.display.set_mode(size)
# display name on header
pg.display.set_caption("Scary Tempol text based game")
# Used to manage how fast the screen updates
clock = pg.time.Clock()
# colors for imput box
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)
# the inpiut box class has a lot of help from ai with getting text to wrap and center the text even tho its not inportant for the game but i want it to look nice and to learn how to do it for future projects
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, BLACK)
        self.active = False
        self.enter_pressed = False
        self.enter_released = True  # Add this flag
        self.lines = [text]  # Store lines of text

    def set_position(self, x, y):
        """Dynamically set the position of the input box."""
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN and self.enter_released:
                    self.enter_pressed = True
                    self.enter_released = False  # Set to False when Enter is pressed
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.update_lines()
        if event.type == pg.KEYUP:
            if event.key == pg.K_RETURN:
                self.enter_released = True  # Set to True when Enter is released

    def update_lines(self):
        words = self.text.split(' ')
        self.lines = []
        current_line = ''
        for word in words:
            test_line = current_line + word + ' '
            if FONT.render(test_line, True, BLACK).get_width() > self.w - 10:  # Adjust width for box edge
                self.lines.append(current_line)
                current_line = word + ' '
            else:
                current_line = test_line
        self.lines.append(current_line)
        self.update_rect_height()

    def update_rect_height(self):
        # Update the height of the rect to fit all lines of text
        self.rect.h = max(self.h, len(self.lines) * FONT.get_height() + 10)

    def update(self):
        # Resize the box based on the longest line
        max_width = max(FONT.render(line, True, BLACK).get_width() for line in self.lines) + 10
        width = min(max(200, max_width), size[0] - 40)
        self.rect.w = width
        self.rect.x = self.x - (width - self.w) // 2  # Adjust x to keep it centered

    def draw(self, screen):
        # Draw a rounded rectangle for the input box background
        bg_rect = pg.Rect(self.rect.x - 10, self.rect.y - 10, self.rect.w + 20, self.rect.h + 20)
        pg.draw.rect(screen, BLACK, bg_rect, border_radius=10)  # Rounded background
        pg.draw.rect(screen, self.color, self.rect, 2, border_radius=10)  # Rounded border

        # Blit the text inside the input box
        for i, line in enumerate(self.lines):
            line_surface = FONT.render(line, True, WHITE)  # Text color is black for better contrast very nice ai comment was needed lol
            screen.blit(line_surface, (self.rect.x + 5, self.rect.y + 5 + i * FONT.get_height()))

    def get_user_name(self):
        return self.text

    def is_enter_pressed(self):
        if self.enter_pressed:
            user_input = self.text.strip()  # Capture the text before clearing
            self.enter_pressed = False  # Reset the flag
            self.text = ''  # Clear the text in the input box
            self.update_lines()  # Update the lines to reflect the cleared text
            return user_input if user_input else None  # Return the captured text or None if empty
        return None  # Return None if Enter is not pressed
            
        return None  # Return None if Enter is not pressed


def text_objects(text, position, center, max_width=size[0] - 40, font_size=24):
    """
    Renders text with word wrapping and optional centering.
    """
    font = pg.font.SysFont('Calibri', font_size, True, False)
    words = text.split(' ')
    lines = []
    current_line = ''
    for word in words:
        test_line = current_line + word + ' '
        if font.render(test_line, True, WHITE).get_width() > max_width:
            lines.append(current_line)
            current_line = word + ' '
        else:
            current_line = test_line
    lines.append(current_line)

    y_offset = 0
    line_spacing = font.get_height() + 10  # Add spacing between lines
    for line in lines:
        text_render = font.render(line, True, WHITE)
        if center:
            center_text = text_render.get_rect(center=(position[0], position[1] + y_offset))
            screen.blit(text_render, center_text)
        else:
            screen.blit(text_render, (position[0], position[1] + y_offset))

# all vars out side the game fuctions
user_choice = None # none is out side state so when user goes out to stuff they can have a choice in the fuctions
death_text = '' # empty tell user dies not sure if i have it refresh after replay
input_box = InputBox((size[0] - 200) // 2, 300, 200, 32)  # Centered position

# -------- Main Program Loop -----------
# death screen shows what killed the user
def death_screan():
    # user will log what killed them and place it on the death screen
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return "exit"  # Return "exit" to handle quitting properly
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    done = True
                elif event.key == pg.K_r:  # Add replay option
                    return "replay"

        try:
            background_image = pg.image.load("Death.jpg")
            background_image = pg.transform.scale(background_image, size)  # Scale the image to match the screen size
            screen.blit(background_image, (0, 0))  # Display the image at the top-left corner
        except FileNotFoundError:
            print("Error: 'Blood_Altar_inside.png' not found. Ensure the file is in the correct directory.")
            screen.fill(BLACK)  # Fill the screen only if the image fails to load
        else:
            screen.blit(background_image, (0, 0))  # Display the image at the top-left corner
        text_objects("You have died!", (360, 150), True)
        text_objects(death_text, (360, 200), True)  # Display the cause of death
        text_objects("Press Enter to exit.", (360, 250), True)
        text_objects("Press R to replay.", (360, 300), True)  # Replay instruction
        pg.display.flip()
        clock.tick(60)
# user name input
def main_menu():
    input_box.text = ''  # Clear input box
    input_box.update()
    screen.fill(BLACK)
    input_box.draw(screen)
    pg.display.flip()
    """
    Displays the main menu and allows the user to enter their name.
    """
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            input_box.handle_event(event)

        input_box.update()
        screen.fill(BLACK)
        text_objects('Welcome to the game', (size[0] // 2, 50), True)  # Centered position
        text_objects('Enter your name:', (size[0] // 2, 150), True)  # Centered position
        input_box.draw(screen)
        pg.display.flip()
        clock.tick(60)

        user_name = input_box.is_enter_pressed()  # Capture the text when Enter is pressed
        if user_name:  # Ensure the user entered a valid name
            user_name = user_name.strip()
            if user_name:  # Validate the name
                done = True
                return user_name
            else:
                text_objects("Please enter a valid name.", (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)
# talks to user and explains how this game works
def start_game(user_name):
    input_box.text = ''  # Clear input box
    input_box.update()
    screen.fill(BLACK)
    input_box.draw(screen)
    pg.display.flip()
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                done = True  # Exit the loop when Enter is pressed

        screen.fill(BLACK)
        text_objects(f'Welcome {user_name}', (360, 50), True)  # Centered position
        text_objects('This is a text-based adventure game.', (360, 100), True)  # Centered position
        text_objects('You are going to be exploring a temple.', (360, 130), True)  # Centered position
        text_objects('You will be given a choice of 2 options.', (360, 160), True)  # Centered position
        text_objects('You will have to type the number of the option you want to choose.', (360, 190), True)  # Centered position
        text_objects('Press Enter to start the game.', (360, 220), True)  # Centered position

        pg.display.flip()
        clock.tick(60)

    return "Game started"
# a mid way point for user
def left_or_right():
    input_box.text = ''  # Clear the input box text
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            input_box.handle_event(event)

        screen.fill(BLACK)  # Clear the screen before rendering text
        text_objects('You have entered the temple', (360, 50), True)
        text_objects('You have two options', (360, 100), True)
        text_objects('1. Go left', (360, 150), True)
        text_objects('2. Go right', (360, 200), True)
        input_box.update()
        input_box.draw(screen)

        user_input = input_box.is_enter_pressed()  # Get the user input
        if user_input:  # Check if Enter was pressed
            user_input = user_input.strip()  # Strip whitespace
            screen.fill(BLACK)
            if user_input == '1':
                text_objects('You have chosen to go left', (360, 250), True)
                pg.display.flip()
                pg.time.wait(2000)
                done = True
                return user_input
            elif user_input == '2':
                text_objects('You have chosen to go right', (360, 250), True)
                pg.display.flip()
                pg.time.wait(2000)
                done = True
                return user_input
            else:
                text_objects('Invalid choice. Please select 1 or 2.', (360, 250), True)
                pg.display.flip()
                pg.time.wait(2000)

        pg.display.flip()
        clock.tick(60)
# right
def user_right_1():
    input_box.text = ''  # Clear input box
    input_box.set_position(size[0] // 2 - 100, 350)
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            input_box.handle_event(event)

        screen.fill(BLACK)
        text_objects("You have chosen to go right", (size[0] // 2, 50), True, font_size=28)
        text_objects("You have entered a hallway that you are not sure is safe of traps", (size[0] // 2, 100), True, font_size=24)
        text_objects("You have two options:", (size[0] // 2, 150), True, font_size=24)
        text_objects("1. Go slow and safe", (size[0] // 2, 200), True, font_size=24)
        text_objects("2. Run through the hallway", (size[0] // 2, 250), True, font_size=24)
        input_box.update()
        input_box.draw(screen)

        user_input = input_box.is_enter_pressed()  # Get the user input
        if user_input:  # Check if Enter was pressed
            user_input = user_input.strip()  # Strip whitespace
            if user_input == '1':
                return "You have chosen to go slow and safe"
            elif user_input == '2':
                return "You have chosen to run through the hallway"
            else:
                text_objects("Invalid choice. Please select 1 or 2.", (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)

        pg.display.flip()
        clock.tick(60)
# user goes in the room after the first right hallway can go back if they want
def user_right_door():
    input_box.text = ''  # Clear input box
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            input_box.handle_event(event)

        screen.fill(BLACK)
        text_objects("You have chosen to go slow and safe", (360, 50), True)
        text_objects("You have entered a corner with a door with a hallway on your left", (360, 100), True)
        text_objects("You have two options", (360, 150), True)
        text_objects("1. Find a way to open the door", (360, 200), True)
        text_objects("2. Go to the hallway on your right", (360, 250), True)
        input_box.update()
        input_box.draw(screen)

        user_input = input_box.is_enter_pressed()  # Get the user input
        if user_input:  # Check if Enter was pressed
            user_input = user_input.strip()  # Strip whitespace
            screen.fill(BLACK)
            if user_input == '1':
                text_objects("You have chosen to open the door", (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)
                done = True
                return "You have chosen to open the door"
            elif user_input == '2':
                text_objects("You have chosen to go to the hallway on your right", (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)
                done = True
                return "You have chosen to go to the hallway on your right"
            else:
                text_objects("Invalid choice. Please select 1 or 2.", (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)

        pg.display.flip()
        clock.tick(60)
# the user took the right path at the start and how he is going to skip the door on the first hallway on the right and finds a zombie and can run off or fight the zombie
def left_halway():
    input_box.text = ''  # Clear input box
    # user finds a zombie and fights or dies
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            input_box.handle_event(event)

        screen.fill(BLACK)
        text_objects("You have chosen to go to the hallway on your left", (360, 50), True)
        text_objects("You have entered a hallway with a zombie", (360, 100), True)
        text_objects("You have two options", (360, 150), True)
        text_objects("1. Fight the zombie", (360, 200), True)
        text_objects("2. Run from the zombie", (360, 250), True)
        # input box
        input_box.update()
        input_box.draw(screen)
        # check if enter is pressed
        user_input = input_box.is_enter_pressed()  # Get the user input
        if user_input:  # Check if Enter was pressed
            user_input = user_input.strip()  # Strip whitespace
            screen.fill(BLACK)
            if user_input == '1':
                choice_text = "You have chosen to fight the zombie"
                text_objects(choice_text, (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)
                done = True
                return choice_text
            elif user_input == '2':
                choice_text = "You have chosen to run from the zombie"
                text_objects(choice_text, (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)
                done = True
                return choice_text
            else:
                choice_text = "Invalid choice. Please select 1 or 2."
                text_objects(choice_text, (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)

        pg.display.flip()
        clock.tick(60)
# User could die # also been updated to use clcck tick to pervent crashing also updated the fight loop to end when it should so it dont crash
def fight_with_zombie():
    input_box.text = ''  # Clear input box
    global death_text
    # recution for the health of the zombie and the user
    done = False
    zombie_health = 100
    user_health = 100
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            input_box.handle_event(event)

        screen.fill(BLACK)
        text_objects("You have chosen to fight the zombie", (360, 50), True)
        text_objects("You have entered a fight with the zombie", (360, 100), True)
        # user has chosen to fight the zombie
        # loop for the fight
        while zombie_health > 0 and user_health > 0:
            for event in pg.event.get():  # Process events during the fight
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

            # user attack
            zombie_health = max(0, zombie_health - random.randint(1, 10))  # Clamp to non-negative
            # zombie attack
            user_health = max(0, user_health - random.randint(1, 10))  # Clamp to non-negative
            
            # Clear the screen before updating health
            screen.fill(BLACK)
            text_objects("You have chosen to fight the zombie", (360, 50), True)
            text_objects("You have entered a fight with the zombie", (360, 100), True)
            
            # Display updated health
            text_objects(f"Zombie health: {zombie_health}", (360, 150), True)
            text_objects(f"User health: {user_health}", (360, 200), True)
            
            pg.display.flip()
            clock.tick(2)  # Limit the loop to 2 frames per second
            
            # Break the loop if either health reaches 0
            if zombie_health <= 0 or user_health <= 0:
                break
            
        # if user dies or kills the zombie
        if user_health <= 0:
            death_text = "You were killed by the zombie"
            text_objects(death_text, (360, 250), True)
            pg.display.flip()
            clock.tick(1)  # Allow the screen to update before exiting
            done = True
            return  # Ensure function exits after setting death_text
        elif zombie_health <= 0:
            text_objects("You have killed the zombie", (360, 250), True)
            pg.display.flip()
            clock.tick(1)  # Allow the screen to update before exiting
            done = True
            return "zombie_killed"  # Return a state indicating the zombie was killed
    
        pg.display.flip()
        clock.tick(60)
# user won the fight with the zombie has choose to go in the room or go back to the old door that user has walked passed
def user_won_fight():
    input_box.text = ''  # Clear input box
    done = False
    # user has won the fight with the zombie and there is a door behind the dead zombie
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            input_box.handle_event(event)

        screen.fill(BLACK)
        text_objects("You have killed the zombie", (360, 50), True)
        text_objects("You have found a door behind the dead zombie", (360, 100), True)
        text_objects("You have two options", (360, 150), True)
        text_objects("1. Open the door", (360, 200), True)
        text_objects("2. Go back to the hallway and open the door there", (360, 250), True)
        input_box.update()
        input_box.draw(screen)
        # check if enter is pressed
        user_input = input_box.is_enter_pressed()  # Get the user input
        if user_input:  # Check if Enter was pressed
            user_input = user_input.strip()  # Strip whitespace
            screen.fill(BLACK)
            if user_input == '1':
                text_objects("You have chosen to open the door", (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)
                return "door_behind_zombie"  # Transition to door_behind_zombie state
            elif user_input == '2':
                text_objects("You have chosen to go back to the hallway and open the door there", (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)
                return "hallway_door"  # Transition to hallway_door state
            else:
                text_objects("Invalid choice. Please select 1 or 2.", (360, 300), True)
                pg.display.flip()
                pg.time.wait(2000)
        pg.display.flip()
        clock.tick(60)
# user dies after going though this door
def door_behind_zombie():
    input_box.text = ''  # Clear input box
    global death_text  # Ensure death_text is updated globally
    # user has to open the door and there is a hallway behind the door
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            input_box.handle_event(event)

        screen.fill(BLACK)
        # user goes into the room behind the zombie and the room kills him
        text_objects("You have chosen to open the door", (360, 50), True)
        text_objects("You have entered a room with a chest", (360, 100), True)
        text_objects("You open the chest and the door behind you closes", (360, 150), True)
        # death text for this death
        death_text = "The chest was a trap and you died"
        text_objects(death_text, (360, 200), True)
        text_objects("You have died", (360, 250), True)
        pg.display.flip()
        pg.time.wait(20000)
        done = True
        return "death"  # Return a state to trigger the death screen
# user finds inside the room alter and can leave and go back or inspect the alter
def hallway_door():
    input_box.text = ''  # Clear input box
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            input_box.handle_event(event)

        screen.fill(BLACK)  
        text_objects("You have chosen to enter this room", (360, 50), True)
        text_objects("You have found writings on the walls and a blood altar", (360, 100), True)
        text_objects("You have two options", (360, 150), True)
        text_objects("1. Inspect the altar", (360, 200), True)
        text_objects("2. Leave the room and go back", (360, 250), True)
        input_box.update()
        input_box.draw(screen)

        user_input = input_box.is_enter_pressed()  # Get the user input
        if user_input:  # Check if Enter was pressed
            user_input = user_input.strip()  # Strip whitespace
            screen.fill(BLACK)
            if user_input == '1':
                text_objects("You have chosen to inspect the altar", (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)
                done = True
                return "inspect_altar"
            elif user_input == '2':
                text_objects("You have chosen to leave the room and go back", (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)
                done = True
                return "leave_room"
            else:
                text_objects("Invalid choice. Please select 1 or 2.", (360, 300), True)
                pg.display.flip()
                pg.time.wait(2000)

        pg.display.flip()
        clock.tick(60)
# user inspects blood altar and this is an end game where user takes what user has learned and brings what user learned is brought to employer 
def inspect_blood_alter(user_name):
    input_box.text = ''  # Clear input box
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            input_box.handle_event(event)
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                done = True  # Exit the loop when Enter is pressed
                return "User completed the game"
            
        try:
            background_image = pg.image.load("Blood_Altar_inside.png")
            background_image = pg.transform.scale(background_image, size)  # Scale the image to match the screen size
            screen.blit(background_image, (0, 0))  # Display the image at the top-left corner
        except FileNotFoundError:
            print("Error: 'Blood_Altar_inside.png' not found. Ensure the file is in the correct directory.")
            screen.fill(BLACK)  # Fill the screen only if the image fails to load
        else:
            screen.blit(background_image, (0, 0))  # Display the image at the top-left corner
        text_objects("You have chosen to inspect the altar", (360, 50), True)
        text_objects("You find ancient writings and symbols", (360, 100), True)
        text_objects("You take notes and decide to leave the temple", (360, 150), True)
        text_objects("You bring your findings to your employer", (360, 200), True)
        text_objects(f"{user_name} has completed the game!", (360, 250), True)
        text_objects("Press Enter to exit.", (360, 300), True)
        
        

            

        pg.display.flip()
        clock.tick(60)
# user goes to the left on left_or_right() and finds stairs can go down or go around the stairs
def user_left_1():
    input_box.text = ''  # Clear input box
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            input_box.handle_event(event)

        screen.fill(BLACK)  # Clear the screen before rendering text
        text_objects("You have chosen to go left", (size[0] // 2, 50), True, font_size=28)
        text_objects("User has entered a room with a staircase", (size[0] // 2, 100), True, font_size=24)
        text_objects("You have two options:", (size[0] // 2, 150), True, font_size=24)
        text_objects("1. Go down the stairs", (size[0] // 2, 200), True, font_size=24)
        text_objects("2. Go past the stairs", (size[0] // 2, 250), True, font_size=24)
        input_box.update()
        input_box.draw(screen)

        user_input = input_box.is_enter_pressed()  # Get the user input
        if user_input:  # Check if Enter was pressed
            user_input = user_input.strip()  # Strip whitespace
            screen.fill(BLACK)
            if user_input == '1':
                text_objects("You have chosen to go down the stairs", (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)
                done = True
                return "You have chosen to go down the stairs"
            elif user_input == '2':
                text_objects("You have chosen to go past the stairs", (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)
                done = True
                return "You have chosen to go past the stairs"
            else:
                text_objects("Invalid choice. Please select 1 or 2.", (360, 300), True)
                pg.display.flip()
                pg.time.wait(2000)

        pg.display.flip()
        clock.tick(60)
# user avoids the stairs
def user_walks_pass_stairs():
    input_box.text = ''  # Clear input box
    global death_text
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            input_box.handle_event(event)

        screen.fill(BLACK)
        text_objects("You have chosen to go past the stairs", (360, 50), True)
        text_objects("You have found a door at the end of the hallway", (360, 100), True)
        text_objects("You open the door and enter the room", (360, 150), True)
        text_objects("The door closes behind you and the room fills with gas", (360, 200), True)
        text_objects("You have died", (360, 250), True)
        death_text = "You were killed by poisonous gas"
        pg.display.flip()
        pg.time.wait(3000)
        done = True
        return  # for death_text
# user goes down stairs and is able to open a chest or leave it and if user chooses a chest then user goes finds key
def user_stairs():
    input_box.text = ''  # Clear input box
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            input_box.handle_event(event)

        screen.fill(BLACK)
        text_objects("You have chosen to go down the stairs", (360, 50), True)
        text_objects("You have entered a room with a chest", (360, 100), True)
        text_objects("You have two options", (360, 150), True)
        text_objects("1. Open the chest", (360, 200), True)
        text_objects("2. Leave the chest", (360, 250), True)
        input_box.update()
        input_box.draw(screen)

        user_input = input_box.is_enter_pressed()  # Get the user input
        if user_input:  # Check if Enter was pressed
            user_input = user_input.strip()  # Strip whitespace
            screen.fill(BLACK)
            if user_input == '1':
                return "open the chest"  # for recutusion fuction
            elif user_input == '2':
                return "leave the chest"  # for recutusion fuction
            else:
                text_objects("Invalid choice. Please select 1 or 2.", (360, 300), True)
                pg.display.flip()
                pg.time.wait(2000)

        pg.display.flip()
        clock.tick(60)
# user picked the chest and can find a key
def user_chest():
    input_box.text = ''  # Clear input box
    global key_taken  # Use the global variable
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            input_box.handle_event(event)

        screen.fill(BLACK)
        text_objects("You have chosen to open the chest", (360, 50), True)
        text_objects("You have found a key", (360, 100), True)
        text_objects("You have two options", (360, 150), True)
        text_objects("1. Take the key", (360, 200), True)
        text_objects("2. Leave the key", (360, 250), True)
        input_box.update()
        input_box.draw(screen)

        user_input = input_box.is_enter_pressed()  # Get the user input
        if user_input:  # Check if Enter was pressed
            user_input = user_input.strip()  # Strip whitespace
            screen.fill(BLACK)
            if user_input == '1':
                key_taken = True  # Log that the key is taken globally
                # recursive_game_state("user_took_key")  # Transition to user_took_key this
                choice_text = "You have chosen to take the key"
                text_objects(choice_text, (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)
                done = True
                return True  # Return True when the key is taken
            elif user_input == '2':
                key_taken = False  # Log that the key is not taken globally
                choice_text = 'You have chosen to leave the key'
                text_objects(choice_text, (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)
                done = True
                return key_taken
            else:
                text_objects("Invalid choice. Please select 1 or 2.", (360, 300), True)
                pg.display.flip()
                pg.time.wait(2000)
        pg.display.flip()
        clock.tick(60)
# user looks for key and takes it
def user_took_key():
    input_box.text = ''  # Clear input box
    input_box.set_position(size[0] // 2 - 100, 350)
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            input_box.handle_event(event)

        screen.fill(BLACK)
        text_objects("You have chosen to take the key", (size[0] // 2, 50), True, font_size=28)
        text_objects("You open the chest with the key", (size[0] // 2, 100), True, font_size=28)
        text_objects("There is rare gold and treasure in the chest", (size[0] // 2, 150), True, font_size=28)
        text_objects("You have two options:", (size[0] // 2, 200), True, font_size=28)
        text_objects("1. Leave everything and tell your employer", (size[0] // 2, 250), True, font_size=24)
        text_objects("2. Take everything and run", (size[0] // 2, 300), True, font_size=24)
        input_box.update()
        input_box.draw(screen)

        user_input = input_box.is_enter_pressed()  # Get the user input
        if user_input:  # Check if Enter was pressed
            user_input = user_input.strip()  # Strip whitespace
            screen.fill(BLACK)
            if user_input == '1':
                text_objects("You have chosen to leave everything and tell your employer", (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)
                done = True
                return "leave_employer"
            elif user_input == '2':
                text_objects("You have chosen to take everything and run", (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)
                done = True
                return "take_treasure"
            else:
                text_objects("Invalid choice. Please select 1 or 2.", (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)

        pg.display.flip()
        clock.tick(60)
# user tells enployer about treasure
def Leave_everything_and_tell_your_employer(user_name):
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                done = True  # Exit the loop when Enter is pressed

        screen.fill(BLACK)
        text_objects("You have chosen to leave everything and tell your employer", (360, 50), True)
        text_objects("You return to your employer with the findings", (360, 100), True)
        text_objects("Your employer is pleased with your honesty", (360, 150), True)
        text_objects(f"{user_name} has successfully completed the game!", (360, 200), True)
        text_objects("Press Enter to exit.", (360, 250), True)

        pg.display.flip()
        clock.tick(60)
        

    return "User completed the game"  # Indicate successful completion
# bad man
def user_took_treasure(user_name):
    input_box.text = ''  # Clear input box
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            input_box.handle_event(event)

        screen.fill(BLACK)
        text_objects("You have chosen to take everything and run", (360, 50), True)
        text_objects("You have taken the treasure and ran", (360, 100), True)
        # user has an ending screen
        text_objects(f"{user_name} has won the game but now {user_name} on the run from there employer", (360, 150), True)
        text_objects("Press enter to exit", (360, 200), True)
        input_box.update()
        input_box.draw(screen)
        user_input = input_box.is_enter_pressed()  # Get the user input
        if user_input:  # Check if Enter was pressed
            user_input = user_input.strip()  # Strip whitespace
            done = True
            return "User won" # if this shows up on the recution checks it will exit the game
        pg.display.flip()
        clock.tick(60)
# this is user leaving the keys for left stairs path also kind of useless but i made it while speeding though stuff but it is used
def user_leaved_key():
    input_box.text = ''  # Clear input box
    done = False
    while not done:
         for event in pg.event.get():
              if event.type == pg.QUIT:
                pg.quit()
                exit()
              input_box.handle_event(event)
    
         screen.fill(BLACK)
         text_objects("You have chosen to leave the key", (360, 50), True)
         text_objects("You have entered a room with a door", (360, 100), True)
         text_objects("You have two options", (360, 150), True)
         text_objects("1. Open the door", (360, 200), True)
         input_box.update()
         input_box.draw(screen)
         # check if enter is pressed
         user_input = input_box.is_enter_pressed()  # Get the user input
         if user_input:  # Check if Enter was pressed
            user_input = user_input.strip()  # Strip whitespace
            screen.fill(BLACK)
            if user_input == '1':
                choice_text = "You have chosen to open the door"
                text_objects(choice_text, (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)
                done = True
                return choice_text # this is used for recursion fuction so it can keep track of what user did
            else:
                choice_text = "Invalid choice. Please select 1 or 2."
                text_objects(choice_text, (size[0] // 2, 400), True, font_size=24)
                pg.display.flip()
                pg.time.wait(2000)
         pg.display.flip()
         clock.tick(60)
# user dies after passing the chest while entering the door after it this is left stair path
def user_opened_door():
    input_box.text = ''  # Clear input box
    global death_text
    # the door closes on the user and dies
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            input_box.handle_event(event)
           
        screen.fill(BLACK)
        text_objects("You have opened the door", (360, 50), True)
        text_objects("Walk in by pressing enter", (360, 100), True)
        pg.display.flip()
        user_input = input_box.is_enter_pressed()  # Get the user input
        if user_input:  # Check if Enter was pressed
            user_input = user_input.strip()  # Strip whitespace
            screen.fill(BLACK)
            death_text = "The door closes and the room fills with poisonous gas"
            text_objects(death_text, (360, 100), True)
            text_objects("You have died", (360, 150), True)
            pg.display.flip()
            pg.time.wait(4000)
            done = True  # Exit the loop when Enter is pressed
            return
# this is my recusion but yea elif was the best i could think of at the time 
def recursive_game_state(state, user_name=None):
    global death_text
    while True:  # Use a loop to manage state transitions
        if state == "main_menu":
            user_name = main_menu()
            if not user_name:
                return
            state = "start_game"

        elif state == "start_game":
            result = start_game(user_name)
            if result == "Game started":
                state = "left_or_right"

        elif state == "left_or_right":
            choice = left_or_right()
            if choice == '1':
                state = "user_left_1"
            elif choice == '2':
                state = "user_right_1"

        elif state == "user_left_1":
            left_choice = user_left_1()
            if left_choice == "You have chosen to go down the stairs":
                state = "user_stairs"
            elif left_choice == "You have chosen to go past the stairs":
                user_walks_pass_stairs()
                result = death_screan()
                if result == "replay":
                    state = "left_or_right"  # Ensure replay transitions to left_or_right
                return

        elif state == "user_stairs":
            chest_choice = user_stairs()
            if chest_choice == "open the chest":
                key_status = user_chest()
                if key_status:
                    state = "user_took_key"
                else:
                    state = "user_leaved_key"
            elif chest_choice == "leave the chest":
                state = "user_leaved_key"

        elif state == "user_took_key":
            treasure_choice = user_took_key()
            if treasure_choice == "take_treasure":
                user_took_treasure(user_name)
                return
            elif treasure_choice == "leave_employer":
                state = "leave_employer"

        elif state == "leave_employer":
            result = Leave_everything_and_tell_your_employer(user_name)
            if result == "User completed the game":
                return

        elif state == "user_leaved_key":
            door_choice = user_leaved_key()
            if door_choice == "You have chosen to open the door":
                user_opened_door()
                result = death_screan()
                if result == "replay":
                    state = "left_or_right"  # Ensure replay transitions to left_or_right
                return

        elif state == "user_right_1":
            right_choice = user_right_1()
            if right_choice == "You have chosen to go slow and safe":
                state = "user_right_door"
            elif right_choice == "You have chosen to run through the hallway":
                death_text = "You triggered a trap and died"
                result = death_screan()
                if result == "replay":
                    state = "left_or_right"  # Ensure replay transitions to left_or_right
                return

        elif state == "user_right_door":
            door_choice = user_right_door()
            if door_choice == "You have chosen to open the door":
                state = "hallway_door"
            elif door_choice == "You have chosen to go to the hallway on your right":
                state = "left_halway"

        elif state == "hallway_door":
            hallway_choice = hallway_door()
            if hallway_choice == "inspect_altar":
                inspect_blood_alter(user_name)
                return
            elif hallway_choice == "leave_room":
                return

        elif state == "left_halway":
            zombie_choice = left_halway()
            if zombie_choice == 'You have chosen to fight the zombie':
                result = fight_with_zombie()
                if result == "zombie_killed":
                    state = "user_won_fight"
                elif death_text:
                    result = death_screan()
                    if result == "replay":
                        state = "left_or_right"  # Ensure replay transitions to left_or_right
                    return
            elif zombie_choice == 'You have chosen to run from the zombie':
                death_text = "You were caught by the zombie while running"
                result = death_screan()
                if result == "replay":
                    state = "left_or_right"  # Ensure replay transitions to left_or_right
                return

        elif state == "user_won_fight":
            post_fight_choice = user_won_fight()
            if post_fight_choice == "door_behind_zombie":
                result = door_behind_zombie()
                if result == "death":
                    result = death_screan()
                    if result == "replay":
                        state = "left_or_right"  # Ensure replay transitions to left_or_right
                    return
            elif post_fight_choice == "hallway_door":
                state = "hallway_door"

"""
    Starts the game by calling the recursive game state function.
"""

def main():  # this calls recursive game state
    try:  # will try this and if it's broken it won't kill my pc
        while True:  # Add a loop to allow replaying
            result = recursive_game_state("main_menu")  # Start from main_menu initially
            if result == "replay":  # Restart the game if replay is selected
                recursive_game_state("left_or_right")  # Restart from left_or_right
            elif result == "exit":  # Exit the game if "exit" is returned
                break
    except Exception as e:
        print(f"An error occurred: {e}")  # found out you can use this for an error

    finally:
        pg.quit()

if __name__ == "__main__":
    main()

pg.quit()
