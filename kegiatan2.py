# import modul tkinter untuk GUI
import tkinter as tk
# membuat window utama aplikasi
app = tk.Tk()
app.title("Kalkulator Sederhana")

# fungsi operasi
def tambah():
    hasil.set(float(e1.get()) + float(e2.get()))
def kurang():
    hasil.set(float(e1.get()) - float(e2.get()))
def kali():
    hasil.set(float(e1.get()) * float(e2.get()))
def bagi():
    hasil.set(float(e1.get()) / float(e2.get()))

# memberi ruang kosong kiri kanan agar tombol bisa di tengah
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(4, weight=1)
# label dan entry angka pertama dan angka kedua
tk.Label(app, text="Angka 1").grid(row=0, column=1, padx=10, pady=10)
e1 = tk.Entry(app)
e1.grid(row=0, column=2, padx=10, pady=10)
tk.Label(app, text="Angka 2").grid(row=1, column=1, padx=10, pady=10)
e2 = tk.Entry(app)
e2.grid(row=1, column=2, padx=10, pady=10)
# tombol operasi
tk.Button(app, text="+", width=6, command=tambah).grid(row=2, column=1, padx=2, pady=10)
tk.Button(app, text="-", width=6, command=kurang).grid(row=2, column=2, padx=2, pady=10)
tk.Button(app, text="x", width=6, command=kali).grid(row=2, column=3, padx=2, pady=10)
tk.Button(app, text=":", width=6, command=bagi).grid(row=2, column=4, padx=2, pady=10)
# hasil
hasil = tk.StringVar()
tk.Label(app, text="Hasil").grid(row=3, column=0, padx=10, pady=5)
tk.Label(app, textvariable=hasil).grid(row=3, column=1)

# jalankan aplikasi
app.mainloop()