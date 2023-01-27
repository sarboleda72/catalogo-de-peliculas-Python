import tkinter as tk
from client.gui_app import Frame, barra_menu

def main():
    root=tk.Tk()
    root.title('Catalogo de Peliculas')
    #root.iconbitmap('img/icono.ico')
    root.resizable(0,0)
    barra_menu(root) 
    #root.config(bg='green',width=800,height=800)

    app=Frame(root)  
    

    app.mainloop()

if __name__=='__main__':
    main()