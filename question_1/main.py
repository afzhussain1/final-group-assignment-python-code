import tkinter as tk
from youtube_app import CustomYouTubeApp

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomYouTubeApp(root)  # Polymorphism - Child class used in place of parent class
    root.mainloop()