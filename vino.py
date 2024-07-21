import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        red_wine = int(entry_red.get()) * 265
        white_wine = int(entry_white.get()) * 230
        rose_wine = int(entry_rose.get()) * 325

        total_price = red_wine + white_wine + rose_wine

        result_text = (f"Červené víno: {red_wine} $\n"
                       f"Bílé víno: {white_wine} $\n"
                       f"Růžové víno: {rose_wine} $\n"
                       f"Celková cena: {total_price} $")
        messagebox.showinfo("Výsledek", result_text)
    except ValueError:
        messagebox.showerror("Chyba", "Prosím, zadejte platné číslo.")

# Hlavní okno
root = tk.Tk()
root.title("Výpočet vína")

# Nastavení ikony
icon = tk.PhotoImage(file="logo.png")
root.iconphoto(False, icon)

# Vytvoření hlavního rámu
main_frame = tk.Frame(root)
main_frame.pack(pady=20)

# Červené víno
img_red = tk.PhotoImage(file="cervene-vino.png")  # Zde musí být obrázek ve formátu PNG
label_red = tk.Label(main_frame, image=img_red)
label_red.grid(row=0, column=0, padx=10, pady=5)
label_red_text = tk.Label(main_frame, text="Červené víno")
label_red_text.grid(row=0, column=1, padx=10, pady=5)
entry_red = tk.Entry(main_frame)
entry_red.grid(row=0, column=2, padx=10, pady=5)

# Bílé víno
img_white = tk.PhotoImage(file="bile-vino.png")  # Zde musí být obrázek ve formátu PNG
label_white = tk.Label(main_frame, image=img_white)
label_white.grid(row=1, column=0, padx=10, pady=5)
label_white_text = tk.Label(main_frame, text="Bílé víno")
label_white_text.grid(row=1, column=1, padx=10, pady=5)
entry_white = tk.Entry(main_frame)
entry_white.grid(row=1, column=2, padx=10, pady=5)

# Růžové víno
img_rose = tk.PhotoImage(file="ruzove-vino.png")  # Zde musí být obrázek ve formátu PNG
label_rose = tk.Label(main_frame, image=img_rose)
label_rose.grid(row=2, column=0, padx=10, pady=5)
label_rose_text = tk.Label(main_frame, text="Růžové víno")
label_rose_text.grid(row=2, column=1, padx=10, pady=5)
entry_rose = tk.Entry(main_frame)
entry_rose.grid(row=2, column=2, padx=10, pady=5)

# Tlačítko pro výpočet
button_calculate = tk.Button(root, text="Vypočítat", command=calculate)
button_calculate.pack(pady=20)

root.mainloop()
