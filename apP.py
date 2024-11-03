import tkinter as tk
from tkinter import font

def show_fonts(index=0):
    # Nếu đã hiển thị hết các font, dừng chương trình
    if index >= len(available_fonts):
        print("Đã hiển thị tất cả các font có sẵn.")
        return

    font_name = available_fonts[index]
    new_window = tk.Toplevel(root)
    new_window.title(f"Font: {font_name}")

    label = tk.Label(new_window, text=f"Đây là font {font_name}", font=(font_name, 22))
    label.pack(padx=20, pady=20)

    new_window.protocol("WM_DELETE_WINDOW", lambda: (new_window.destroy(), show_fonts(index + 1)))

root = tk.Tk()
root.title("Ứng Dụng Tiếng Việt")

available_fonts = font.families()
print("Các font có sẵn:", available_fonts)

show_fonts()

root.mainloop()
