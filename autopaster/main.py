import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from autopaster.app import AutoPaster
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoPaster(root)
    root.mainloop()