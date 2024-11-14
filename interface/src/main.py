import tkinter as tk

from components.header import Header
from containers.main_dashboard import MainDashboard


class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Carputer")
        self.root.geometry("800x480")

        # Configure root grid
        self.root.grid_rowconfigure(2, weight=1)  # Empty space at bottom
        self.root.grid_columnconfigure(0, weight=1)

        # Add header
        self.header = Header(self.root)
        self.header.grid(row=0, column=0, sticky="ew", padx=1, pady=1)

        # Add main dashboard immediately after header
        self.dashboard = MainDashboard(self.root)
        self.dashboard.grid(
            row=1, column=0, sticky="new", padx=1, pady=20
        )  # Note 'new' sticky


if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()
