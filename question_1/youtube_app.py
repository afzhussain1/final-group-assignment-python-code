import tkinter as tk
import re
from tkinter import ttk, messagebox
from transformers import MarianMTModel, MarianTokenizer
from user_interface import UserInterFace
from styling import Styling


# Logging method with the Decorator
def logMethodCall(func):
    def wrapper(*args, **kwargs):
        print(f"Method is calling on the run time: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
class YouTubeApp(UserInterFace, Styling):
    def __init__(a, root):
        super().__init__(root)
        a._title = "YouTube Like Interface"  # Encapsulation
        a.users = {}  # empty object to store user credentials
        a.setupUi()  # Encapsulation

    @property
    def title(a):  # Encapsulation with getter
        return a._title

    @title.setter
    def title(a, value):  # Encapsulation with setter
        a._title = value

    @logMethodCall  # logging
    def setupUi(a):
        a.root.title(a._title)
        a.LoginSignup()

    @logMethodCall
    def LoginSignup(a):
        loginFrame = ttk.Frame(a.root)
        loginFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        ttk.Label(loginFrame, text="Username (Email):").grid(row=0, column=0, padx=5, pady=5)
        a.userInput = ttk.Entry(loginFrame)
        a.userInput.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(loginFrame, text="Password:").grid(row=1, column=0, padx=5, pady=5)
        a.passwordInput = ttk.Entry(loginFrame, show="*")
        a.passwordInput.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(loginFrame, text="Login", command=a.login).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(loginFrame, text="Signup", command=a.signup).grid(row=2, column=1, padx=5, pady=5)

    @logMethodCall  # calling logging
    def login(a):
        username = a.userInput.get()
        password = a.passwordInput.get()
        # apply logic to check the authentication
        if username in a.users and a.users[username] == password:
            messagebox.showinfo("Login Success", "Welcome!")
            a.Authenticated()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    @logMethodCall  # again calling the login method
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
        headerFrame = ttk.Frame(a.root)
        headerFrame.pack(side=tk.TOP, fill=tk.X)
        a.applyStyle(headerFrame, "Header.TFrame")
        titleLabel = ttk.Label(headerFrame, text=a._title, style="Header.TLabel")
        titleLabel.pack(padx=10, pady=10)

    @logMethodCall
    def videoList(a):
        videoFrame = ttk.Frame(a.root)
        videoFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        videos = ["Video 1", "Video 2", "Video 3", "Video 4"]
        for video in videos:
            a.videoItem(videoFrame, video)

    @logMethodCall
    def videoItem(a, parent, videoName):
        video_label = ttk.Label(parent, text=videoName, style="Video.TLabel")
        video_label.pack(padx=10, pady=5, anchor="w")

    @logMethodCall
    def translationB(a):
        buttonFrame = ttk.Frame(a.root)
        buttonFrame.pack(side=tk.TOP, fill=tk.X)
        tButton = ttk.Button(buttonFrame, text="Translated Text", command=a.showTranslation)
        tButton.pack(padx=10, pady=10)

    @logMethodCall
    def showTranslation(a):
        translationWindow = tk.Toplevel(a.root)
        translationWindow.title("Translate Text")

        ttk.Label(translationWindow, text="Enter text to translate:").grid(row=0, column=0, padx=10, pady=10)
        textEntry = ttk.Entry(translationWindow, width=50)
        textEntry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(translationWindow, text="Select target language:").grid(row=1, column=0, padx=10, pady=10)
        langCbox = ttk.Combobox(translationWindow, values=["fr", "de", "es"])  # Example languages
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
        tokenizer = MarianTokenizer.from_pretrained(modelName)
        model = MarianMTModel.from_pretrained(modelName)

        translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
        translatedT = tokenizer.decode(translated[0], skip_special_tokens=True)
        return translatedT

# Defining the custom class
class CustomYouTubeApp(YouTubeApp):
    @logMethodCall
    def header(a):
        super().header()
        headerFrame = ttk.Frame(a.root)
        headerFrame.pack(side=tk.TOP, fill=tk.X)
        a.applyStyle(headerFrame, "CustomHeader.TFrame")
        subtitleLabel = ttk.Label(headerFrame, text="Welcome to the Custom YouTube App!", style="CustomHeader.TLabel")
        subtitleLabel.pack(padx=10, pady=5)