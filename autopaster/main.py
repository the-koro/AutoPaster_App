# Add the parent directory to the Python path
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the AutoPaster class
from autopaster.app import AutoPaster
import tkinter as tk

# Run the AutoPaster class
if __name__ == "__main__":
    root = tk.Tk()
    app = AutoPaster(root)
    root.mainloop()
