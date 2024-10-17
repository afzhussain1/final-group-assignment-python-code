import tkinter as tk
from tkinter import ttk
from youtube_app import CustomYouTubeApp

if __name__ == "__main__":
    root = tk.Tk()

    # apply styles with color
    style = ttk.Style(root)
    style.configure("Custom.TFrame", background="#FF0000")  # YouTube red
    style.configure("Custom.TLabel", background="#FF0000", foreground="#FFFFFF", font=("Arial", 12))  # White text
    style.configure("Video.TLabel", background="#FF0000", foreground="#FFFFFF", font=("Arial", 10))  # White text

    app = CustomYouTubeApp(root)  # Polymorphism
    root.mainloop()