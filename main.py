from tkinter import *
from tkinter import ttk
import tkinter as tk

#comandos para se usar quando pressionado os botoes de cores(mudar a cor atual)

cor_atual = "black"

def escolher_preto():
    global cor_atual
    cor_atual = "black"

def escolher_vermelho():
    global cor_atual
    cor_atual = "red"

def escolher_verde():
    global cor_atual
    cor_atual = "green"

def escolher_azul():
    global cor_atual
    cor_atual = "blue"


# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
    global cor_atual

    # AQUI é o momento certo de "fotografar" o estado da caixinha,
    # porque é aqui que a figura nasce
    preenchido_atual = preenchimento_Var.get()

    if tipo_figura_var.get() == 'Linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y), cor_atual, preenchido_atual)

    elif tipo_figura_var.get() == 'Circulo':
        figura_nova = ('circulo', (event.x, event.y, 0), cor_atual, preenchido_atual)
    
    elif tipo_figura_var.get() == 'Retangulo':
        figura_nova = ("retangulo", (event.x, event.y, event.x, event.y), cor_atual, preenchido_atual)

    elif tipo_figura_var.get() == 'Oval':
        figura_nova = ('oval', (event.x, event.y, 0, 0), cor_atual, preenchido_atual)

    else :
        figura_nova = ("rabisco", [(event.x, event.y)], cor_atual, preenchido_atual)

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    global cor_atual

    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))

    elif figura_nova[0] == "circulo":
        # Calcula o raio para o circulo
        raio = ( (figura_nova[1][0] - event.x)**2 + (figura_nova[1][1] - event.y)**2 ) ** 0.5
        # figura_nova[2] é a cor e figura_nova[3] é o preenchido que já estavam guardados - so repassamos eles
        figura_nova = ('circulo', (figura_nova[1][0], figura_nova[1][1], raio), figura_nova[2], figura_nova[3]) 

    elif figura_nova[0] == 'oval':
        # Calcula dois raios, horizontal e vertical
        raioX = abs(figura_nova[1][0] - event.x)
        raioY = abs(figura_nova[1][1] - event.y)
        figura_nova = ('oval', (figura_nova[1][0], figura_nova[1][1], raioX, raioY), figura_nova[2], figura_nova[3])

    elif figura_nova[0] == 'retangulo':
        #a mesma coisa de atualizar linha porque o create_rectangle so precisa de dois pontos, assim como o create_line
        figura_nova = ('retangulo', (figura_nova[1][0], figura_nova[1][1], event.x, event.y), figura_nova[2], figura_nova[3])

    else : # figura_nova[0] == "linha"
        figura_nova = ("linha", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), figura_nova[2], figura_nova[3])

    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figuras.append(figura_nova) # salva as figuras na tela
    desenhar_figuras()

# Cria a imagem na tela, sem deixar as versoes depois de soltar o mouse
def desenhar_figuras():
    canvas.delete("all")
    # agora cada figura traz seu proprio "preenchido" junto - nao usamos mais preenchimento_Var.get() aqui
    for fig, values, cor, preenchido in figuras:
        if fig == "linha":
            canvas.create_line(values[0], values[1], values[2], values[3], fill= cor)
        # recebe os pontos x e y do inicio e x e y do fim e cria o retangulo com base nesses pontos
        elif fig == "retangulo":
            if preenchido == True:
                canvas.create_rectangle(values[0], values[1], values[2], values[3], fill= cor)
            else: #se preenchido == False
                canvas.create_rectangle(values[0], values[1], values[2], values[3], outline= cor)

        # recebe os pontos centrais (cx, cy) e o raio e cria o circulo com base neles
        elif fig == 'circulo':
            cx, cy, raio = values
            if preenchido == True: #se esta marcado a caixinha de preenchimento (na hora que a figura foi criada)
                canvas.create_oval(cx-raio, cy-raio, cx+raio, cy+raio, fill= cor)
            else: #se nao estava marcado
                canvas.create_oval(cx-raio, cy-raio, cx+raio, cy+raio, outline= cor)

        # recebe os pontos centrais (cx, cy) e dois raios, para criar a oval
        elif fig == 'oval':
            cx, cy, raioX, raioY = values
            if preenchido == True:
                canvas.create_oval(cx-raioX, cy-raioY, cx+raioX, cy+raioY, fill= cor)    
            else:
                canvas.create_oval(cx-raioX, cy-raioY, cx+raioX, cy+raioY, outline= cor)  

        else : # fig == "rabisco"
            canvas.create_line(values, fill= cor)

# Cria a versao antes dela ser solta, com o efeito do dash
def desenhar_figura_nova(): 
    fig, values, cor, preenchido = figura_nova
    if fig == "linha":
        canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2))

    elif fig == 'retangulo':
        if preenchido == True:
            canvas.create_rectangle(values[0], values[1], values[2], values[3], fill= cor, dash=(4,2))
        else:
            canvas.create_rectangle(values[0], values[1], values[2], values[3], dash=(4,2))
    
    # Utiliza de um raio e dois pontos centrais para o circulo
    elif fig == 'circulo':
        cx, cy, raio = values
        if preenchido == True:
            canvas.create_oval(cx-raio, cy-raio, cx+raio, cy+raio, fill= cor, dash=(4, 2))
        else:
            canvas.create_oval(cx-raio, cy-raio, cx+raio, cy+raio, dash=(4, 2))

    # Utiliza de dois raios e dois pontos centrais para a criação da oval
    elif fig == 'oval':
        cx, cy, raioX, raioY = values
        if preenchido == True:
            canvas.create_oval(cx-raioX, cy-raioY, cx+raioX, cy+raioY, fill= cor, dash=(4,2))
        else:
            canvas.create_oval(cx-raioX, cy-raioY, cx+raioX, cy+raioY, dash=(4,2))

    else : # fig == "rabisco"
        canvas.create_line(values, dash=(4, 2))


def incompleta(figura):
    fig, values, cor, preenchido = figura
    if fig == "linha":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "retangulo":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == 'circulo':
        return values[2] == 0
    
    elif fig == 'oval':
        return values[2] == 0 or values[3] == 0
    
    else : # fig == "rabisco"
        return len(values) <= 1


#******* MAIN *******#

figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

raioX = 0
raioY = 0


root = Tk()
frame = Frame(root)

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 

# label
label = ttk.Label(frame,  text='Paint.v03')
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco', 'Circulo', 'Oval', 'Retangulo')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

#caixinha de preenchimento - direto no mesmo frame e na mesma linha (row=0), la no canto direito
frame_preench = Frame(frame)
frame_preench.grid(column=0, row=1, columnspan=3, sticky=E, **paddings)
preenchimento_Var = BooleanVar(root)
preench_menu = ttk.Checkbutton(frame_preench, variable= preenchimento_Var, text= "preenchido")
preench_menu.pack(side=RIGHT, padx=2)

#botoes de escolha de cores junto com a criaçao de outro frame para usar o pack, ja que o pack e o grid nao podem ser usados no mesmo frame
frame_cores = Frame(frame)
frame_cores.grid(column=0, row=1, columnspan=3, sticky=W, **paddings)

botao_vermelho = tk.Button(frame_cores, text="Vermelho", bg="red", command=escolher_vermelho)
botao_vermelho.pack(side=LEFT, padx=2)

botao_preto = tk.Button(frame_cores, text="preto", bg="gray", command=escolher_preto)
botao_preto.pack(side=LEFT, padx=2)

botao_verde = tk.Button(frame_cores, text="Verde", bg="green", command=escolher_verde)
botao_verde.pack(side=LEFT, padx=2)

botao_azul = tk.Button(frame_cores, text="Azul", bg="blue", command=escolher_azul)
botao_azul.pack(side=LEFT, padx=2)


# Área de desenho
canvas = Canvas(frame, bg='white', width=1500, height=800)
canvas.grid(column=0, row=2, columnspan=2, sticky=W, **paddings)

frame.pack()
# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()
