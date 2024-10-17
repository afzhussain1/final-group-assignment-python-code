import tkinter as tk
import re
from tkinter import ttk, messagebox
from transformers import MarianMTModel, MarianTokenizer
from user_interface import UserInterFace
from styling import Styling
import cv2
import numpy as np
from PIL import Image, ImageTk

# Logging method with the Decorator
def logMethodCall(func):
    def wrapper(*args, **kwargs):
        print(f"Method is calling on the run time: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class YouTubeApp:
    def __init__(a, root):
        a.root = root
        a._title = "YouTube Like Interface"  
        a.users = {}  # Empty object to store user credentials
        a.setupUi()  

    @property
    def title(a):  
        return a._title

    @title.setter
    def title(a, value):  
        a._title = value

    @logMethodCall  # Logging
    def setupUi(a):
        a.root.title(a._title)
        a.root.configure(bg='#FF0000')  # Set the background color to YouTube red
        a.LoginSignup()

    @logMethodCall  # decorator
    def LoginSignup(a):
        loginFrame = ttk.Frame(a.root, style="Custom.TFrame")
        loginFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        ttk.Label(loginFrame, text="Username (Email):", style="Custom.TLabel").grid(row=0, column=0, padx=5, pady=5)
        a.userInput = ttk.Entry(loginFrame)
        a.userInput.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(loginFrame, text="Password:", style="Custom.TLabel").grid(row=1, column=0, padx=5, pady=5)
        a.passwordInput = ttk.Entry(loginFrame, show="*")
        a.passwordInput.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(loginFrame, text="Login", command=a.login).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(loginFrame, text="Signup", command=a.signup).grid(row=2, column=1, padx=5, pady=5)

    @logMethodCall
    def login(a):
        username = a.userInput.get()
        password = a.passwordInput.get()
        # Logic to check authentication
        if username in a.users and a.users[username] == password:
            messagebox.showinfo("Login Success", "Welcome!")
            a.Authenticated()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials") # calling the error function

    @logMethodCall
    def signup(a):
        username = a.userInput.get()
        password = a.passwordInput.get()

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", username):
            messagebox.showerror("Signup Failed", "Invalid email format!")
            return

        # Validate password requirements
        if len(password) < 5 or not any(char.isupper() for char in password):
            messagebox.showerror("Signup Failed", "Password must be at least 5 characters long and contain at least one uppercase letter!")
            return

        # User registration logic
        if username in a.users:
            messagebox.showerror("Signup Failed", "Username already exists!")
        elif not username or not password:
            messagebox.showerror("Signup Failed", "Username and password cannot be empty!")
        else:
            a.users[username] = password
            messagebox.showinfo("Signup Success", f"User {username} registered successfully!")

    @logMethodCall 
    def Authenticated(a):
        for widget in a.root.winfo_children():
            widget.destroy()
        a.root.title(a._title)
        a.header()
        a.videoList()
        a.translationB()

    @logMethodCall
    def header(a):
        headerFrame = ttk.Frame(a.root, style="Custom.TFrame")
        headerFrame.pack(side=tk.TOP, fill=tk.X)
        titleLabel = ttk.Label(headerFrame, text=a._title, style="Custom.TLabel")
        titleLabel.pack(padx=10, pady=10)

    @logMethodCall
    def videoList(a):
        videoFrame = ttk.Frame(a.root, style="Custom.TFrame")
        videoFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # objects to URLs
        videos = {
            "Video 1": "https://www.youtube.com/watch?v=L0EaiHdGs5k&list=RDL0EaiHdGs5k&start_radio=1",
            "Video 2": "https://www.youtube.com/watch?v=kqtD5dpn9C8",
            "Video 3": "https://www.youtube.com/watch?v=kqtD5dpn9C2",
            "Video 4": "https://www.youtube.com/watch?v=kqtD5dpn9C8"
        }
        print("videoList method called. Videos to display:", videos)  # Debug statement
        for videoName, videoURL in videos.items():
            a.videoItem(videoFrame, videoName, videoURL)

    @logMethodCall
    def videoItem(a, parent, videoName, videoURL):
        print("videoItem method called with video:", videoName)  
        video_label = ttk.Label(parent, text=videoName, style="Video.TLabel")
        video_label.pack(padx=10, pady=5, anchor="w")

        # button to open the 
        video_label.bind("<Button-1>", lambda e: a.playVideo(videoURL))

    @logMethodCall
    def playVideo(a, videoURL):
        vWindow = tk.Toplevel(a.root)
        vWindow.title(videoURL)

        # function to call the video
        cap = cv2.VideoCapture(videoURL)

        def updateFrame():
            ret, frame = cap.read()
            if ret:
                # Rgb color 
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)

                # lable images
                label.imgtk = imgtk
                label.configure(image=imgtk)

                label.after(10, update_frame)
            else:
                cap.release()
                vWindow.destroy()

        label = tk.Label(vWindow)
        label.pack()

        # call the th function
        updateFrame()

    @logMethodCall
    def translationB(a):
        buttonFrame = ttk.Frame(a.root, style="Custom.TFrame")
        buttonFrame.pack(side=tk.TOP, fill=tk.X)
        tButton = ttk.Button(buttonFrame, text="Translated Text", command=a.showTranslation)
        tButton.pack(padx=10, pady=10)

    @logMethodCall
    def showTranslation(a):
        translationWindow = tk.Toplevel(a.root)
        translationWindow.title("Translate Text")

        ttk.Label(translationWindow, text="Enter text to translate:", style="Custom.TLabel").grid(row=0, column=0, padx=10, pady=10)
        textEntry = ttk.Entry(translationWindow, width=50)
        textEntry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(translationWindow, text="Select target language:", style="Custom.TLabel").grid(row=1, column=0, padx=10, pady=10)
        languages = [
            "af", "sq", "am", "ar", "hy", "as", "az", "bn", "eu", "be", "bs", "bg", "ca", "ceb", "ny", "zh", "co", "hr", 
            "cs", "da", "nl", "en", "eo", "et", "tl", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", 
            "iw", "hi", "hmn", "hu", "is", "ig", "id", "ga", "it", "ja", "jw", "kn", "kk", "km", "rw", "ko", "ku", "ky", 
            "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "or", "ps", 
            "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", 
            "sw", "sv", "tg", "ta", "tt", "te", "th", "tr", "tk", "uk", "ur", "ug", "uz", "vi", "cy", "xh", "yi", "yo", 
            "zu"
        ]
        langCbox = ttk.Combobox(translationWindow, values=languages)
        langCbox.grid(row=1, column=1, padx=10, pady=10)
        langCbox.current(0)

        def translate():
            text = textEntry.get()
            targetLang = langCbox.get()
            if text:
                translatedT = a.translateText(text, targetLang)
                messagebox.showinfo("Translation Result", f"Translated text: {translatedT}")
            else:
                messagebox.showerror("Error", "Please enter some text to translate")

        tButton = ttk.Button(translationWindow, text="Translate", command=translate)
        tButton.grid(row=2, columnspan=2, pady=10)

    def translateText(a, text, targetLang):
        modelName = f'Helsinki-NLP/opus-mt-en-{targetLang}'
        tokenizer = MarianTokenizer.from_pretrained(modelName)  # method name to translate
        model = MarianMTModel.from_pretrained(modelName)  # translation call

        translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
        translatedT = tokenizer.decode(translated[0], skip_special_tokens=True)
        return translatedT

# Defining the custom class
class CustomYouTubeApp(YouTubeApp):
    @logMethodCall
    def header(a):
        super().header()
        headerFrame = ttk.Frame(a.root, style="Custom.TFrame")
        headerFrame.pack(side=tk.TOP, fill=tk.X)
        subtitleLabel = ttk.Label(headerFrame, text="Welcome to the Custom YouTube App!", style="Custom.TLabel")
        subtitleLabel.pack(padx=10, pady=5)
