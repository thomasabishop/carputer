import tkinter as tk


class MainDashboard(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Configure column weights
        for i in range(4):
            self.columnconfigure(i, weight=1)

        # Configure row weights - first rows for buttons, last row takes remaining space
        self.rowconfigure(2, weight=1)  # Last row expands

        buttons_top = ["DRIVE", "PARK", "NAVIGATE", "DASHCAMS"]
        for i, text in enumerate(buttons_top):
            self._create_button(text, 0, i)

        self._create_button("MUSIC", 1, 0)

    def _create_button(self, text, row, col, colspan=1):
        btn = tk.Button(self, text=text)
        btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=1, pady=1)
        return btn
