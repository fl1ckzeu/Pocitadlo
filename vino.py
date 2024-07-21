import tkinter as tk
from tkinter import messagebox
import os
import sys

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def calculate():
    try:
        red_wine = int(entry_red.get()) * 265
        white_wine = int(entry_white.get()) * 230
        rose_wine = int(entry_rose.get()) * 325

        total_price = red_wine + white_wine + rose_wine

        result_text = (f"Červené víno: {red_wine} $\n"
                       f"Bílé víno: {white_wine} $\n"
                       f"Růžové víno: {rose_wine} $\n"
                       f"---------------------------\n"
                       f"Celková cena: {total_price} $")
        messagebox.showinfo("Výsledek", result_text)
    except ValueError:
        messagebox.showerror("Chyba", "Prosím, zadejte platné číslo.")

# Hlavní okno
root = tk.Tk()
root.title("Výpočet vína")

# Nastavení ikony
icon_path = resource_path("logo.png")
if os.path.exists(icon_path):
    icon = tk.PhotoImage(file=icon_path)
    root.iconphoto(False, icon)
else:
    print(f"Ikona nebyla nalezena: {icon_path}")

# Vytvoření hlavního rámu
main_frame = tk.Frame(root)
main_frame.pack(pady=20)

# Červené víno
red_wine_image_path = resource_path("cervene-vino.png")
if os.path.exists(red_wine_image_path):
    img_red = tk.PhotoImage(file=red_wine_image_path)
    label_red = tk.Label(main_frame, image=img_red)
    label_red.grid(row=0, column=0, padx=10, pady=5)
else:
    print(f"Obrázek červeného vína nebyl nalezen: {red_wine_image_path}")
label_red_text = tk.Label(main_frame, text="Červené víno")
label_red_text.grid(row=0, column=1, padx=10, pady=5)
entry_red = tk.Entry(main_frame)
entry_red.grid(row=0, column=2, padx=10, pady=5)

# Bílé víno
white_wine_image_path = resource_path("bile-vino.png")
if os.path.exists(white_wine_image_path):
    img_white = tk.PhotoImage(file=white_wine_image_path)
    label_white = tk.Label(main_frame, image=img_white)
    label_white.grid(row=1, column=0, padx=10, pady=5)
else:
    print(f"Obrázek bílého vína nebyl nalezen: {white_wine_image_path}")
label_white_text = tk.Label(main_frame, text="Bílé víno")
label_white_text.grid(row=1, column=1, padx=10, pady=5)
entry_white = tk.Entry(main_frame)
entry_white.grid(row=1, column=2, padx=10, pady=5)

# Růžové víno
rose_wine_image_path = resource_path("ruzove-vino.png")
if os.path.exists(rose_wine_image_path):
    img_rose = tk.PhotoImage(file=rose_wine_image_path)
    label_rose = tk.Label(main_frame, image=img_rose)
    label_rose.grid(row=2, column=0, padx=10, pady=5)
else:
    print(f"Obrázek růžového vína nebyl nalezen: {rose_wine_image_path}")
label_rose_text = tk.Label(main_frame, text="Růžové víno")
label_rose_text.grid(row=2, column=1, padx=10, pady=5)
entry_rose = tk.Entry(main_frame)
entry_rose.grid(row=2, column=2, padx=10, pady=5)

# Tlačítko pro výpočet
button_calculate = tk.Button(root, text="Vypočítat", command=calculate)
button_calculate.pack(pady=20)

root.mainloop()
