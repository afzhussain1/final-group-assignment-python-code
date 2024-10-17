# YouTube Like Interface Application

This is a simple YouTube-like interface application built using Python and Tkinter. The application demonstrates various programming concepts such as encapsulation, polymorphism, multiple inheritance, and decorators. Additionally, it integrates with MarianMT for text translation and TensorFlow for image classification.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- User login and signup functionality
- Video list display
- Text translation using MarianMT
- Image classification using TensorFlow
- Customizable styles through multiple inheritance
- Logging of method calls using decorators

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/afzhussain1/final-group-assignment-python-code.git
    cd youtube-like-interface
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

    Ensure your `requirements.txt` includes:
    ```
    torch
    transformers
    tk
    pillow
    opencv-python
    tensorflow
    ```

## Usage

1. **Run the application**:
    ```bash
    python main.py
    ```

2. **Login or Signup**:
    - Enter a username and password to log in or sign up.

3. **View Videos**:
    - After logging in, you can view a list of sample videos.

4. **Translate Text**:
    - Click on the "Translate Text" button to open a new window where you can enter text and select a target language for translation.

5. **Classify Images**:
    - Click on the "Classify Image" button to open a file dialog and select an image for classification.

## Project Structure

### main.py
This is the main script where the application is initialized and run. It contains the primary class `YouTubeApp` and its methods.

### user_interface.py
This file contains the `UserInterFace` class, which manages the user interface components.

### styling.py
This file contains the `Styling` class, which is responsible for the application's visual styles and themes.

### requirements.txt
This file lists the dependencies required to run the application, such as `transformers`, `torch`, `tk`, `pillow`, `opencv-python`, and `tensorflow`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


# Side-Scrolling 2D Game

This is a simple side-scrolling 2D game built using Pygame. In the game, the player can move left and right, jump, and shoot projectiles to defeat enemies and collect collectibles. The game includes levels, score tracking, and lives management.

## Features

- Fullscreen game display
- Player movement (left, right, jump)
- Shooting projectiles
- Enemy and collectible spawning
- Collision detection
- Score, lives, and level tracking

## Requirements

- Python 3.x
- Pygame

## Installation

1. Install Python from [python.org](https://www.python.org/).
2. Install Pygame by running the following command:

   ```bash
   pip install pygame


   Running the Game
Save the game script as main.py.

Ensure that the images (player.png, enemy.png, miscellaneous-angle.png, sdd.png) are located in the directory specified in the script or adjust the file paths accordingly.

Run the game by executing the following command in the terminal:

bash
Copy code
python main.py
Controls
Left Arrow Key: Move left
Right Arrow Key: Move right
Spacebar: Jump
F Key: Shoot projectile
Game Logic
The player starts with 3 lives.
The player can move left and right and jump.
The player can shoot projectiles to defeat enemies.
Enemies move horizontally and bounce off the screen edges.
Collectibles appear randomly and can be collected to increase the score.
The game progresses through levels, with the number of enemies increasing in each level.
If the player collides with an enemy, they lose a life.
If the player collects a collectible, their score increases.
If the player loses all lives, the game ends.
