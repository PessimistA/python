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
kelime_label = tk.Label(root, text="Türkçe Kelime:",fg="blue",bg="pink")
kelime_label.grid(row=0, column=0)

kelime_entry = tk.Entry(root,fg="blue",bg="pink")
kelime_entry.grid(row=0, column=1)

anlam_label = tk.Label(root, text="İngilizce Anlam:",fg="blue",bg="pink")
anlam_label.grid(row=1, column=0)

anlam_entry = tk.Entry(root,fg="blue",bg="pink")
anlam_entry.grid(row=1, column=1)

#arama yapmak için arayüzler
kelime_label2 = tk.Label(root, text="İngilizce Kelime:", fg="white",bg="blue")
kelime_label2.grid(row=0, column=4)

kelime_entry2 = tk.Entry(root, fg="white",bg="blue")
kelime_entry2.grid(row=0, column=5)

anlam_label2 = tk.Label(root, text="Türkçe Anlam:", fg="white",bg="blue")
anlam_label2.grid(row=1, column=4)

anlam_entry2 = tk.Entry(root, fg="white",bg="blue")
anlam_entry2.grid(row=1, column=5)

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
    anlam = kelime_entry2.get()
    cursor.execute('SELECT kelime FROM kelimeler WHERE anlam=?', (anlam,))#burası değiştirildi 1.ver den alınan değer anlam oldu
    sonuc = cursor.fetchone()#tuple olarak aldığından sonuç kısmında ilk dönen değer yani[0] kullanılır
    
    if sonuc:
        anlam_entry2.delete(0, tk.END)
        anlam_entry2.insert(0, sonuc[0])
    else:
        messagebox.showerror("Hata", "Anlam bulunamadı!")

# Kelime ekle butonu
ekle_button = tk.Button(root, text="Kelime Ekle", command=kelime_ekle, fg="blue",bg="pink")
ekle_button.grid(row=2, column=0, columnspan=2)

# Kelime ara butonu
ara_button = tk.Button(root, text="Kelime Ara", command=kelime_ara, fg="white",bg="blue")
ara_button.grid(row=2, column=4, columnspan=2)

# Tkinter ana döngü
root.mainloop()

# Veritabanı bağlantısını kapatma
conn.close()
