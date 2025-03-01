import tkinter as tk
from tkinter import messagebox

def verificar_resposta(resposta):
    if resposta == "pet":
        messagebox.showinfo("Aviso", "Acho que você não entendeu direito, vou repetir!")
    repetir_pergunta()

def repetir_pergunta():
    global contador
    contador += 1
    label_pergunta.config(text=f"Existe duas unidades de cachorro: o Pet e o Repete. O Pet morreu. Quem ficou? ({contador})")

def on_enter(e):
    e.widget.config(bg='lightgray')

def on_leave(e):
    e.widget.config(bg='SystemButtonFace')

def main():
    global label_pergunta, contador
    contador = 1
    
    root = tk.Tk()
    root.title("Pet e Repete")
    root.geometry("400x200")
    
    label_pergunta = tk.Label(root, text=f"Existe duas unidades de cachorro: o Pet e o Repete. O Pet morreu. Quem ficou? ({contador})", wraplength=350)
    label_pergunta.pack(pady=20)
    
    frame_botoes = tk.Frame(root)
    frame_botoes.pack()
    
    botao_pet = tk.Button(frame_botoes, text="Pet", command=lambda: verificar_resposta("pet"))
    botao_pet.grid(row=0, column=0, padx=10)
    botao_pet.bind("<Enter>", on_enter)
    botao_pet.bind("<Leave>", on_leave)
    
    botao_repete = tk.Button(frame_botoes, text="Repete", command=repetir_pergunta)
    botao_repete.grid(row=0, column=1, padx=10)
    botao_repete.bind("<Enter>", on_enter)
    botao_repete.bind("<Leave>", on_leave)
    
    root.mainloop()

if __name__ == "__main__":
    main()
