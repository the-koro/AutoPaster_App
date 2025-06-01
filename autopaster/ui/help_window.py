import tkinter as tk
from tkinter import ttk

def show_help_window(root):
        help_window = tk.Toplevel(root)
        help_window.title("Help")
        help_window.geometry("480x400")
        help_window.resizable(False, False)

        # Canvas for scroll (we won't add scrollbar)
        canvas = tk.Canvas(help_window, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        # Frame inserted into canvas
        frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        # Make frame auto-resize with the window
        def on_resize(event):
            canvas.itemconfig("frame", width=event.width)
            canvas.configure(scrollregion=canvas.bbox("all"))

        canvas.bind("<Configure>", on_resize)

        # Use tag to later modify the window size
        canvas.create_window((0, 0), window=frame, anchor="nw", tags="frame")

        # Add text
        ttk.Label(frame, text="AutoPaster by Theko", font=("Segoe UI", 15, "bold")).pack(anchor="w", padx=10, pady=(15, 0))
        ttk.Label(frame, text="📌 Usage Instructions:", font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=10, pady=(10, 0))
        ttk.Label(frame, text="1. Enter the paste interval in seconds.", wraplength=460).pack(anchor="w", padx=10, pady=2)
        ttk.Label(frame, text="2. Select the text you want to paste.", wraplength=460).pack(anchor="w", padx=10, pady=2)
        ttk.Label(frame, text="3. Copy the text to clipboard.", wraplength=460).pack(anchor="w", padx=10, pady=2)
        ttk.Label(frame, text="4. Click 'Start' and the text will be automatically pasted into the selected input field.", wraplength=460).pack(anchor="w", padx=10, pady=2)
        ttk.Label(frame, text="- Hotkeys: 'F8' to start/stop.", wraplength=460).pack(anchor="w", padx=10, pady=2)

        ttk.Label(frame, text="📌 Important:", font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=10, pady=(10, 0))
        ttk.Label(frame, text="- If interval is less than 0.2 s, you may experience:", wraplength=460).pack(anchor="w", padx=10, pady=2)
        ttk.Label(frame, text="- Lag in the target application.", wraplength=460).pack(anchor="w", padx=10, pady=0)
        ttk.Label(frame, text="- Ban or mute in chats.", wraplength=460).pack(anchor="w", padx=10, pady=0)
        ttk.Label(frame, text="- System overload or freezing.", wraplength=460).pack(anchor="w", padx=10, pady=0)
        ttk.Label(frame, text="Use with caution!", wraplength=460).pack(anchor="w", padx=10, pady=0)

        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))