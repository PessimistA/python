import tkinter as tk
from tkinter import messagebox
import sqlite3

# Veritabanı bağlantısı ve tablo oluşturma
conn = sqlite3.connect('sozluk.db')
cursor = conn.cursor()

# Tabloyu oluştur (eğer yoksa)
cursor.execute('''
CREATE TABLE IF NOT EXISTS kelimeler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kelime TEXT NOT NULL,
    anlam TEXT NOT NULL
)
''')

conn.commit()

# Tkinter pencere oluşturma
root = tk.Tk()
root.title("Python Sözlük Uygulaması")


# Kelime ve anlam ekleme kısmı
kelime_label = tk.Label(root, text="Kelime:",fg="blue",bg="pink")
kelime_label.grid(row=0, column=0)

kelime_entry = tk.Entry(root,fg="blue",bg="pink")
kelime_entry.grid(row=0, column=1)

anlam_label = tk.Label(root, text="Anlam:",fg="blue",bg="pink")
anlam_label.grid(row=1, column=0)

anlam_entry = tk.Entry(root,fg="blue",bg="pink")
anlam_entry.grid(row=1, column=1)

# Kelime ekleme fonksiyonu
def kelime_ekle():
    kelime = kelime_entry.get()
    anlam = anlam_entry.get()

    if kelime and anlam:
        cursor.execute('INSERT INTO kelimeler (kelime, anlam) VALUES (?, ?)', (kelime, anlam))
        conn.commit()
        messagebox.showinfo("Başarılı", "Kelime başarıyla eklendi!")
    else:
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurun!")

# Kelime arama fonksiyonu
def kelime_ara():
    kelime = kelime_entry.get()
    cursor.execute('SELECT anlam FROM kelimeler WHERE kelime=?', (kelime,))
    sonuc = cursor.fetchone()
    
    if sonuc:
        anlam_entry.delete(0, tk.END)
        anlam_entry.insert(0, sonuc[0])
    else:
        messagebox.showerror("Hata", "Kelime bulunamadı!")

# Kelime ekle butonu
ekle_button = tk.Button(root, text="Kelime Ekle", command=kelime_ekle, fg="blue",bg="pink")
ekle_button.grid(row=2, column=0, columnspan=2)

# Kelime ara butonu
ara_button = tk.Button(root, text="Kelime Ara", command=kelime_ara, fg="white",bg="blue")
ara_button.grid(row=3, column=0, columnspan=2)

# Tkinter ana döngü
root.mainloop()

# Veritabanı bağlantısını kapatma
conn.close()