import tkinter as tk
from tkinter import messagebox

sözlük ={}

# Tkinter pencere oluşturma
root = tk.Tk()
root.title("Python Sözlük Uygulaması")


# Kelime ve anlam ekleme kısmı
kelime_label = tk.Label(root, text="İngilizce Kelime:",fg="blue",bg="pink")
kelime_label.grid(row=0, column=0)

kelime_entry = tk.Entry(root,fg="blue",bg="pink")
kelime_entry.grid(row=0, column=1)

anlam_label = tk.Label(root, text="Türkçe Anlam:",fg="blue",bg="pink")
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
        sözlük[kelime] = anlam
        messagebox.showinfo("Başarılı", "Kelime başarıyla eklendi!")
        # Sözlüğü metin formatında dosyaya ekleme
        with open("dictionary.txt", "a") as file:
            file.write(f"{kelime}: {anlam}\n")
    else:
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurun!")
    
# Kelime arama fonksiyonu
def kelime_ara():
    kelime = kelime_entry2.get()
    with open("dictionary.txt", "r") as file:
        for line in file:
            k, a = line.strip().split(": ", 1)
            if k == kelime:
                anlam_entry2.delete(0, tk.END)
                anlam_entry2.insert(0, a)
                return
    messagebox.showerror("Hata", "Anlam bulunamadı!")



# Kelime ekle butonu
ekle_button = tk.Button(root, text="Kelime Ekle", command=kelime_ekle, fg="blue",bg="pink")
ekle_button.grid(row=2, column=0, columnspan=2)

# Kelime ara butonu
ara_button = tk.Button(root, text="Kelime Ara", command=kelime_ara, fg="white",bg="blue")
ara_button.grid(row=2, column=4, columnspan=2)

# Tkinter ana döngü
root.mainloop()

