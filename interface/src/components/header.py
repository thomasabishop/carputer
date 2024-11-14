import tkinter as tk
from datetime import datetime


class Header(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        content = tk.Frame(self)
        content.pack(fill=tk.X, padx=1)

        tk.Label(content, text="CARPUTER").pack(side=tk.LEFT)

        right_frame = tk.Frame(content)
        right_frame.pack(side=tk.RIGHT)

        tk.Label(right_frame, text="NET: Connected").pack(side=tk.LEFT, padx=5)
        tk.Label(right_frame, text="40.446° N 79.982° W").pack(side=tk.LEFT, padx=5)
        tk.Label(right_frame, text="Littlehampton, UK").pack(side=tk.LEFT, padx=5)

        self.time_label = tk.Label(right_frame)
        self.time_label.pack(side=tk.LEFT, padx=5)
        self.update_time()

    def update_time(self):
        self.time_label.config(text=datetime.now().strftime("%a %d %B %Y    %H:%M"))
        self.after(1000, self.update_time)
