import tkinter as tk
from tkinter import ttk

# Login method and with decorators
def logMethodCall(func):
    def wrapper(*args, **kwargs):
        print(f"Calling method: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# method overriding  and mainclass
class CustomYouTubeAppClass():
    @logMethodCall  # Decorator for logging
    def createHeader(self):
        super().createHeader()  # Calling the parent class method (Method Overriding)
        headerFrame = ttk.Frame(self.root)
        headerFrame.pack(side=tk.TOP, fill=tk.X)
        self.applyStyle(headerFrame, "CustomHeader.TFrame")  # Using method from multiple inheritance
        subtitleLabel = ttk.Label(headerFrame, text="Welcome to the Custom YouTube App!")
        subtitleLabel.pack(padx=10, pady=5)

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = CustomYouTubeAppClass(root)  # Polymorphism with main call
    root.mainloop()


















