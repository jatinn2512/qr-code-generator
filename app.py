import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    text = entry_text.get().strip()
    if text == "":
        messagebox.showwarning("Warning", "⚠️ Please enter some text or URL!")
        return

    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    
    filename = "qrcode.png" # Always save as qrcode.png
    img.save(filename)

    img_display = Image.open(filename)
    img_display = img_display.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img_display)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

    messagebox.showinfo("Success", f"✅ QR Code saved as {filename}")

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("450x500")
root.configure(bg="#f4f4f9")

title = tk.Label(root, text="🔗 QR Code Generator", font=("Arial", 18, "bold"), bg="#f4f4f9", fg="#333")
title.pack(pady=20)

tk.Label(root, text="Enter Text or URL:", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)
entry_text = tk.Entry(root, width=40, font=("Arial", 12), bd=2, relief="groove")
entry_text.pack(pady=10, ipady=5)

generate_btn = tk.Button(
    root,
    text="Generate QR Code",
    command=generate_qr,
    bg="#0078D7",
    fg="white",
    font=("Arial", 12, "bold"),
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2"
)
generate_btn.pack(pady=15)

qr_label = tk.Label(root, bg="#f4f4f9")
qr_label.pack(pady=20)


footer = tk.Label(root, text="Made with ❤️", font=("Arial", 10), bg="#f4f4f9", fg="#777")
footer.pack(side="bottom", pady=10)

root.mainloop()
