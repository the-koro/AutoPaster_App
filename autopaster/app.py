import time
import tkinter as tk
from tkinter import ttk, messagebox
import threading

from autopaster.core.hotkeys import register_hotkeys
from autopaster.core.locale_load import load_text
from autopaster.core.pasting import paste
from autopaster.ui.help_window import show_help_window

# Main class
class AutoPaster:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoPaster")
        self.root.geometry("280x320")
        self.root.resizable(False, False)
        self.running = False

        self.app_name = load_text("AppName")

        self.interval_text = load_text("Interval")
        self.random_offset_text = load_text("RandomOffset")
        self.max_paste_times_text = load_text("MaxPasteTimes")

        self.press_enter_text = load_text("PressEnter")
        self.accurate_enter_text = load_text("AccurateEnter")

        self.start_button_text = load_text("StartButton")
        self.stop_button_text = load_text("StopButton")
        self.help_button_text = load_text("HelpButton")

        self.stopped_text = load_text("Stopped")
        self.running_text = load_text("Running")
        self.invalid_interval_text = load_text("InvalidInterval")
        self.invalid_random_offset_text = load_text("InvalidRandomOffset")

        self.help_title_text = load_text("HelpTitle")
        self.warning_text = load_text("Warning")

        # Program label
        self.program_label = ttk.Label(root, text=self.app_name, font=("Segoe UI", 15, "bold"))
        self.program_label.pack(anchor="w", padx=10, pady=(5, 0))

        # Interval input field
        self.interval_label = ttk.Label(root, text=self.interval_text)
        self.interval_label.pack(padx=10, pady=5, anchor="w")

        self.interval_var = tk.DoubleVar(value="1.0")
        self.interval_entry = ttk.Entry(root, textvariable=self.interval_var)
        self.interval_entry.pack(padx=10, pady=0, anchor="w")

        # Random offset input field
        self.random_label = ttk.Label(root, text=self.random_offset_text)
        self.random_label.pack(padx=10, pady=5, anchor="w")

        self.random_var = tk.DoubleVar(value="0.1")
        self.random_entry = ttk.Entry(root, textvariable=self.random_var)
        self.random_entry.pack(padx=10, pady=0, anchor="w")

        # Maximum paste count
        self.max_paste_label = ttk.Label(root, text=self.max_paste_times_text)
        self.max_paste_label.pack(padx=10, pady=5, anchor="w")

        self.max_paste_var = tk.IntVar(value="-1")
        self.max_paste_entry = ttk.Entry(root, textvariable=self.max_paste_var)
        self.max_paste_entry.pack(padx=10, pady=0, anchor="w")

        # Press Enter checkbox
        self.press_enter = tk.BooleanVar(value=False)
        self.enter_checkbox = ttk.Checkbutton(root, text=self.press_enter_text, variable=self.press_enter)
        self.enter_checkbox.pack(padx=10, pady=5, anchor="w")

        # Accurate Enter checkbox
        self.accurate_enter = tk.BooleanVar(value=False)
        self.accurate_enter_checkbox = ttk.Checkbutton(root, text=self.accurate_enter_text, variable=self.accurate_enter)
        self.accurate_enter_checkbox.pack(padx=10, pady=0, anchor="w")

        # Buttons
        button_frame = ttk.Frame(root)
        button_frame.pack(padx=10, pady=2, anchor="w")

        self.toggle_button = ttk.Button(button_frame, text=self.start_button_text, command=self.toggle_start_stop)
        self.toggle_button.pack(side="left", padx=(0, 5))

        self.help_button = ttk.Button(button_frame, text=self.help_button_text, command=self.show_help)
        self.help_button.pack(side="left")

        # Status and counter
        self.pasted = 0

        status_frame = ttk.Frame(root)
        status_frame.pack(padx=10, pady=10, anchor="w")

        self.status_label = ttk.Label(status_frame, text=self.stopped_text, foreground="red")
        self.status_label.pack(side="left", padx=5, anchor="w")

        self.progress_label = ttk.Label(status_frame, text="N/A", foreground="black")
        self.progress_label.pack(side="left", padx=5, anchor="w")

        # Warning
        self.warning_shown = False

        # Hotkeys
        register_hotkeys(self)

    def show_help(self):
        show_help_window(self.root)

    def toggle_start_stop(self):
        self.progress_label.config(text="N/A")
        self.pasted = 0
        if self.running:
            self.reset()
        else:
            try:
                interval = float(self.interval_var.get())
                if interval < 0:
                    raise ValueError
            except ValueError:
                self.status_label.config(text=self.invalid_interval_text, foreground="orange")
                return
            try:
                random_offset = float(self.random_var.get())
                if random_offset < 0:
                    raise ValueError
            except ValueError:
                self.status_label.config(text=self.invalid_random_offset_text, foreground="orange")
                return

            if interval < 0.2:
                if self.warning_shown == False:
                    self.warning_shown = True
                    messagebox.showwarning("Warning",
                        "You have set the interval below 0.2 seconds.\n\n"
                        "⚠️ This may:\n"
                        "- cause lag in the target application,\n"
                        "- get you banned or muted in chat apps,\n"
                        "- overload your system and cause freezes.\n\n"
                        "Use with caution!")

            self.running = True
            self.toggle_button.config(text=self.stop_button_text)
            self.status_label.config(text=self.running_text, foreground="green")
            self.progress_label.config(text="N/A")
            threading.Thread(target=self.paste_loop, args=(), daemon=True).start()

    def paste_loop(self):
        while self.running:
            if self.root.focus_displayof() is not None:
                time.sleep(0.1)
                continue
            paste(interval=self.interval_var.get(),
                    random_offset=self.random_var.get(), 
                    max_paste_times=self.max_paste_var.get(),
                    press_enter=self.press_enter.get(),
                    accurate_enter=self.accurate_enter.get())
            self.increase_counter()
            if self.max_paste_var.get() > 0 and self.pasted >= self.max_paste_var.get():
                break

    def increase_counter(self):
        self.pasted += 1
        self.progress_label.config(text=f"Pasted {self.pasted} times")

    def reset(self, reset_counter=True):
        self.running = False
        self.toggle_button.config(text=self.start_button_text)
        self.status_label.config(text=self.stopped_text, foreground="red")
        if reset_counter:
            self.progress_label.config(text="N/A")
            self.pasted = 0