# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import ttkbootstrap as ttk
from window import WindowTk

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = ttk.Window(themename="superhero")
    root.geometry("440x350")
    app = WindowTk(root)
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
