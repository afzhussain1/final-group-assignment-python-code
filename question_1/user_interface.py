import tkinter as tk
from tkinter import ttk

# Base class for user interface class
class UserInterFace:
    def __init__(a, root):
        a.root = root

    def setup(a):
        raise NotImplementedError("Subclass must implement abstract method")
