from tkinter import *
import qrcode
from tkinter import messagebox

# Função que ira gera o QRcode


def gera_qr_code():
    url = url_entry.get()

    if len(url) == 0:
        messagebox.showinfo(
            title="Erro URL!",
            message="Favor insira uma URL válida!!"
        )
    else:
        opcao_escolhida = messagebox.askokcancel(
            title="CONFIRMA URL!",
            message=f"O endereço da URL é:'{url}'\n Pronto para Salvar?"
        )

    if opcao_escolhida:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save('qrExport.png')


# app
if __name__ == '__main__':
    app = Tk()

    app.title("Gerador de Código QR")
    app.config(padx=10, pady=100)

    # Labels
    url_label = Label(text="Insira a URL:")
    url_label.grid(row=2, column=0)

    # Entry
    url_entry = Entry(width=35)
    url_entry.grid(row=2, column=1,  columnspan=2)
    url_entry.focus()

    # Button
    url_button = Button(text="Gerar QR Code", width=36, command=gera_qr_code)
    url_button.grid(row=4, column=1, columnspan=2)

    app.mainloop()
