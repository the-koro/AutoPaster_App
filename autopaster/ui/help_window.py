import tkinter as tk
from tkinter import ttk

from autopaster.core.locale_load import load_text

class HelpWindow:
    def __init__(self, root):
        self.root = root
        self.help_window = None

        self.helpwindow_title = load_text("HelpTitle")
        self.howtouseapp_label = load_text("HowToUseAppLabel")
        self.howtouseuse_label = load_text("HowToUseUseLabel")
        self.howtouseuse_text = load_text("HowToUseUse")
        self.howtousehotkeys_label = load_text("HowToUseHotkeysLabel")
        self.howtousehotkeys_text = load_text("HowToUseHotkeys")
        self.howtouseimportant_label = load_text("HowToUseImportantLabel")
        self.howtouseimportant_text = load_text("HowToUseImportant")


    def show(self):
        if self.help_window is not None and self.help_window.winfo_exists():
            # If the window already exists, just bring it to the front
            self.help_window.lift()
            return

        self.help_window = tk.Toplevel(self.root)
        self.help_window.title(self.helpwindow_title)
        self.help_window.resizable(False, False)

        # Create a canvas and a frame inside it, so we can dynamically resize the window
        canvas = tk.Canvas(self.help_window, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw", tags="frame")

        def on_resize(event):
            # On resize, adjust the size of the frame and the scrollregion
            canvas.itemconfig("frame", width=event.width)
            canvas.configure(scrollregion=canvas.bbox("all"))

        canvas.bind("<Configure>", on_resize)

        # Create the labels
        labels = [
            (self.howtouseapp_label, ("Segoe UI", 15, "bold")),
            (self.howtouseuse_label, ("Segoe UI", 12, "bold")),
            (self.howtouseuse_text, None),
            (self.howtousehotkeys_label, ("Segoe UI", 12, "bold")),
            (self.howtousehotkeys_text, None),
            (self.howtouseimportant_label, ("Segoe UI", 12, "bold")),
            (self.howtouseimportant_text, None),
        ]

        for text, font in labels:
            kwargs = {"text": text, "anchor": "w", "justify": "left"}
            if font:
                kwargs["font"] = font
            label = ttk.Label(frame, **kwargs)
            label.pack(anchor="w", padx=10, pady=5)

        # Update the window
        self.help_window.update_idletasks()
        frame.update_idletasks()

        # Automatically adjust the size
        max_width = max(label.winfo_reqwidth() for label in frame.winfo_children()) + 20
        total_height = canvas.bbox("all")[3]

        # Apply the new size
        self.help_window.geometry(f"{max_width}x{total_height}")
