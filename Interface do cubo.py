from ursina import *

# Inicializar a aplicação Ursina
app = Ursina()

# Adicionar uma câmera que permite controle com o mouse
editor_camera = EditorCamera(rotation_speed=200, panning_speed=20)
distância=1.07

# Função para criar um cubo colorido
def create_colored_cube(x, y, z):
    cube = Entity(scale=(1, 1, 1), position=(x, y, z))

    # Criar faces do cubo
    if y==1*distância:
        # Face de cima - amarelo
        top_face = Entity(parent=cube, model='quad', color=color.yellow, position=(0, 0.5, 0), rotation_x=-90, scale=(1, 1), double_sided=True)
    else:
        top_face = Entity(parent=cube, model='quad', color=color.black, position=(0, 0.5, 0), rotation_x=-90, scale=(1, 1), double_sided=True)
    
    if y==-1*distância:
        # Face de baixo - branco
        bottom_face = Entity(parent=cube, model='quad', color=color.white, position=(0, -0.5, 0), rotation_x=90, scale=(1, 1), double_sided=True)
    else:
        top_face = Entity(parent=cube, model='quad', color=color.black, position=(0,-0.5, 0), rotation_x=90, scale=(1, 1), double_sided=True)
        

    if z==-1*distância:
        # Face da frente - laranja
        front_face = Entity(parent=cube, model='quad', color=color.orange, position=(0, 0, -0.5), rotation_y=180, scale=(1, 1), double_sided=True)
    else:
        top_face = Entity(parent=cube, model='quad', color=color.black, position=(0, 0, -0.5), rotation_y=180, scale=(1, 1), double_sided=True)
        

    if z==1*distância:
        # Face de trás - vermelho
        back_face = Entity(parent=cube, model='quad', color=color.red, position=(0, 0, 0.5), scale=(1, 1), double_sided=True)
    else:
        top_face = Entity(parent=cube, model='quad', color=color.black, position=(0, 0, 0.5), scale=(1, 1), double_sided=True)
        

    if x==1*distância:
        #Face da direita - azul
        right_face = Entity(parent=cube, model='quad', color=color.blue, position=(0.5, 0, 0), rotation_y=-90, scale=(1, 1), double_sided=True)
    else:
        top_face = Entity(parent=cube, model='quad', color=color.black, position=(0.5, 0, 0), rotation_y=-90, scale=(1, 1), double_sided=True)


    if x==-1*distância:
        left_face = Entity(parent=cube, model='quad', color=color.green, position=(-0.5, 0, 0), rotation_y=90, scale=(1, 1), double_sided=True)
        # Face da esquerda - verde
    else:
        top_face = Entity(parent=cube, model='quad', color=color.black, position=(-0.5, 0, 0), rotation_y=90, scale=(1, 1), double_sided=True)


# Criar os cubos em uma grade 3x3x3
for x in range(-1, 2):  # x=-1, 0, 1
    for y in range(-1, 2):  # y=-1, 0, 1
        for z in range(-1, 2):  # z=-1, 0, 1
            create_colored_cube(x * distância, y * distância, z * distância)  # Multiplicando por 2 para espaçar os cubos

# Executar a aplicação
app.run()
