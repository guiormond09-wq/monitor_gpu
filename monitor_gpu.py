import psutil
import tkinter as tk
from tkinter import ttk

def atualizar():
    # Uso da CPU
    uso_cpu = psutil.cpu_percent()
    lbl_cpu.config(text=f"Uso da CPU: {uso_cpu:.1f}%")
    barra_cpu["value"] = uso_cpu

    # RAM usada
    ram = psutil.virtual_memory()
    ram_usada = ram.used / (1024 ** 3)
    ram_total = ram.total / (1024 ** 3)
    lbl_ram.config(
        text=f"RAM usada: {ram_usada:.2f} GB / {ram_total:.2f} GB ({ram.percent}%)"
    )
    barra_ram["value"] = ram.percent

    # Disco usado
    disco = psutil.disk_usage("/")
    disco_usado = disco.used / (1024 ** 3)
    disco_total = disco.total / (1024 ** 3)
    lbl_disco.config(
        text=f"Armazenamento usado: {disco_usado:.2f} GB / {disco_total:.2f} GB ({disco.percent}%)"
    )
    barra_disco["value"] = disco.percent

    root.after(1000, atualizar)

# ======================
# INTERFACE
# ======================

root = tk.Tk()
root.title("Monitor do Sistema")
root.geometry("450x350")
root.configure(bg="#202020")

titulo = tk.Label(
    root, text="Monitor do Sistema",
    font=("Segoe UI", 20, "bold"),
    fg="white", bg="#202020"
)
titulo.pack(pady=10)

# CPU
lbl_cpu = tk.Label(root, text="Uso da CPU: --%", font=("Segoe UI", 14, "bold"),
                   fg="#00ffaa", bg="#202020")
lbl_cpu.pack()
barra_cpu = ttk.Progressbar(root, length=300, maximum=100)
barra_cpu.pack(pady=5)

# RAM
lbl_ram = tk.Label(root, text="RAM usada: --", font=("Segoe UI", 14, "bold"),
                   fg="#ffaa00", bg="#202020")
lbl_ram.pack()
barra_ram = ttk.Progressbar(root, length=300, maximum=100)
barra_ram.pack(pady=5)

# DISCO
lbl_disco = tk.Label(root, text="Armazenamento usado: --", font=("Segoe UI", 14, "bold"),
                     fg="#ff4444", bg="#202020")
lbl_disco.pack()
barra_disco = ttk.Progressbar(root, length=300, maximum=100)
barra_disco.pack(pady=5)

lbl_status = tk.Label(root, text="Atualizando em tempo real",
                      font=("Segoe UI", 11), fg="gray", bg="#202020")
lbl_status.pack(pady=10)

atualizar()
root.mainloop()
