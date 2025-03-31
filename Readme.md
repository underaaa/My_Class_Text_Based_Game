# Text-Based Adventure Game

## Overview
This is a text-based adventure game built using Python and Pygame. The game takes you on a journey through a mysterious temple where you make choices that determine your fate. The game features multiple paths, challenges, and endings based on your decisions.

## Features
- **Interactive Gameplay**: Make choices using an input box to navigate through the game.
- **Multiple Endings**: Your decisions lead to different outcomes, including victory or death.
- **Dynamic Text Rendering**: Text is displayed with word wrapping and centering for better readability.
- **Replay Option**: Restart the game after completing or dying.
- **Zombie Fight**: Engage in a random chance-based fight with a zombie.
- **Exploration**: Navigate through hallways, rooms, and stairs with various challenges.

## How to Play
1. **Start the Game**: Run the Python script to begin.
2. **Enter Your Name**: Provide your name in the input box at the main menu.
3. **Make Choices**: Follow the on-screen instructions and type the number corresponding to your choice.
4. **Explore the Temple**: Navigate through the temple by making decisions at each step.
5. **Survive or Die**: Your choices will determine whether you survive, win, or meet an untimely death.
6. **Fight or Die**: You have a fight with a zombie and you have a change to live or Die
7. **Replay**: If you die, you can choose to replay the game.

## Controls
- **Mouse**: Click on the input box to activate it.
- **Keyboard**: 
  - Type your choices (e.g., `1` or `2`) and press `Enter`.
  - Press `R` to replay after dying.
  - Press `Enter` to proceed through screens.

## Requirements
- Python 3.x
- Pygame library (`pip install pygame`)

## File Descriptions
- **Text based gam.py**: The main game script containing all the logic and gameplay.
- **Blood_Altar_inside.png**: Background image for the altar scene.
- **Death.jpg**: Background image for the death screen.
- **_readme.txt**: This README file.

## Known Issues
- Replay state should be going to left or right but i cant find out why it wont change after chaning everything that sould change it
- Ensure the required image files (`Blood_Altar_inside.png` and `Death.jpg`) are in the same directory as the script.

## Future Improvements
- Improve the start menu to explain the game better.
- Optimize the recursive game state logic for better readability and maintainability.

## Credits
- Base code and logic: Jacob Smith
- Input box responsiveness and text rendering: AI-assisted with code 
- Pygame library: [https://www.pygame.org/](https://www.pygame.org/)

Enjoy the game and explore the mysteries of the temple!
