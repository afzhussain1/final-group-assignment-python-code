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
