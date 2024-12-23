from ursina import *
import queue


app = Ursina()

cube_colors = [
    color.blue,  # right
    color.green,   # left
    color.yellow,    # top
    color.white,   # bottom
    color.red,    # back
    color.orange,    # front
]
cubes = []
animation_in_progress=False
fila_de_comandos=queue.Queue()

# Definir as cores
cube_colors = [
    color.blue,    # face direita
    color.green,   # face esquerda
    color.yellow,  # face superior
    color.white,   # face inferior
    color.red,     # face traseira
    color.orange   # face frontal
]

def criar_cubos():
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                # Criar um modelo com cores separadas para cada face
                combine_parent = Entity(enabled=False)

                for i in range(3):  # Iterar sobre os eixos X, Y e Z
                    dir = Vec3(0, 0, 0)
                    dir[i] = 1

                    # Face direita (x == 1) -> Azul
                    if x == 1 and i == 0:  # i == 0 se refere ao eixo X
                        e = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=cube_colors[0])
                        e.look_at(dir, 'up')
                    # Face esquerda (x == -1) -> Verde
                    elif x == -1 and i == 0:
                        e_flipped = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=cube_colors[1])
                        e_flipped.look_at(-dir, 'up')

                    # Face superior (y == 1) -> Amarelo
                    elif y == 1 and i == 1:  # i == 1 se refere ao eixo Y
                        e = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=cube_colors[2])
                        e.look_at(dir, 'up')
                    # Face inferior (y == -1) -> Branco
                    elif y == -1 and i == 1:
                        e_flipped = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=cube_colors[3])
                        e_flipped.look_at(-dir, 'up')

                    # Face traseira (z == 1) -> Vermelho
                    elif z == 1 and i == 2:  # i == 2 se refere ao eixo Z
                        e = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=cube_colors[4])
                        e.look_at(dir, 'up')
                    # Face frontal (z == -1) -> Laranja
                    elif z == -1 and i == 2:
                        e_flipped = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=cube_colors[5])
                        e_flipped.look_at(-dir, 'up')

                # Agora que todas as faces foram definidas, combinar o modelo
                combine_parent.combine()

                # Criar a entidade final do cubo e adicionar à lista de cubos
                e = Entity(model=copy(combine_parent.model), position=Vec3(x*1.1, y*1.1, z*1.1), texture='white_cube')
                cubes.append(e)

criar_cubos()



# rotate a side when we click on it
collider = Entity(model='cube', scale=3, collider='box', visible=False)

def collider_input(key):
    if mouse.hovered_entity == collider:
        if key == 'left mouse down':
            rotate_side(mouse.normal, 1)
        elif key == 'right mouse down':
            rotate_side(mouse.normal, -1)


def girar(key):
    if held_keys['alt'] and key == 'u':
        rotate_side('Rw',1)
    elif held_keys['alt'] and key == 'i':
        rotate_side('Lw',1)
    elif held_keys['alt'] and key == 'o':
        rotate_side('Uw',1)
    elif held_keys['alt'] and key == 'j':
        rotate_side('Dw',1)
    elif held_keys['alt'] and key == 'k':
        rotate_side('Bw',1)
    elif held_keys['alt'] and key == 'l':
        rotate_side('Fw',1)
    
    elif held_keys['alt'] and key == 'r':
        rotate_side('X',1)
    elif held_keys['alt'] and key == 't':
        rotate_side('Y',1)
    elif held_keys['alt'] and key == 'y':
        rotate_side('Z',1)
    elif held_keys['alt'] and key == 'f':
        rotate_side('X',-1)
    elif held_keys['alt'] and key == 'g':
        rotate_side('Y',-1)
    elif held_keys['alt'] and key == 'h':
        rotate_side('Z',-1)

    elif held_keys['alt'] and key == 'e':
        rotate_side('Rw',-1)
    elif held_keys['alt'] and key == 'w':
        rotate_side('Lw',-1)
    elif held_keys['alt'] and key == 'q':
        rotate_side('Uw',-1)
    elif held_keys['alt'] and key == 'd':
        rotate_side('Dw',-1)
    elif held_keys['alt'] and key == 's':
        rotate_side('Bw',-1)
    elif held_keys['alt'] and key == 'a':
        rotate_side('Fw',-1)    

    elif key == 'u':
        rotate_side(Vec3(1,0,0),1)
    elif key == 'i':
        rotate_side(Vec3(-1,0,0),1)
    elif key == 'o':
        rotate_side(Vec3(0,1,0),1)
    elif key == 'j':
        rotate_side(Vec3(0,-1,0),1)
    elif key == 'k':
        rotate_side(Vec3(0,0,1),1)
    elif key == 'l':
        rotate_side(Vec3(0,0,-1),1)

    elif key == 'e':
        rotate_side(Vec3(1,0,0),-1)
    elif key == 'w':
        rotate_side(Vec3(-1,0,0),-1)
    elif key == 'q':
        rotate_side(Vec3(0,1,0),-1)
    elif key == 'd':
        rotate_side(Vec3(0,-1,0),-1)
    elif key == 's':
        rotate_side(Vec3(0,0,1),-1)
    elif key == 'a':
        rotate_side(Vec3(0,0,-1),-1)

    elif key == 'r':
        rotate_side('M',1)
    elif key == 't':
        rotate_side('S',1)
    elif key == 'y':
        rotate_side('E',1)

    elif key == 'f':
        rotate_side('M',-1)
    elif key == 'g':
        rotate_side('S',-1)
    elif key == 'h':
        rotate_side('E',-1)
 

def input(key):
    if animation_in_progress is not True:
        girar(key)



collider.input = collider_input


rotation_helper = Entity()


def rotate_side(normal, direction=1, speed=0.5):
    global animation_in_progress
    if normal == Vec3(1,0,0):
        [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.x > 0]
        rotation_helper.animate('rotation_x', 90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    elif normal == Vec3(-1,0,0):
        [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.x < 0]
        rotation_helper.animate('rotation_x', -90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    elif normal == Vec3(0,1,0):
        [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.y > 0]
        rotation_helper.animate('rotation_y', 90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    elif normal == Vec3(0,-1,0):
        [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.y < 0]
        rotation_helper.animate('rotation_y', -90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    elif normal == Vec3(0,0,1):
        [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.z > 0]
        rotation_helper.animate('rotation_z', -90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    elif normal == Vec3(0,0,-1):
        [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.z < 0]
        rotation_helper.animate('rotation_z', 90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    
    if normal == 'Rw':
        [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.x >= 0]
        rotation_helper.animate('rotation_x', 90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    elif normal == 'Lw':
        [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.x <= 0]
        rotation_helper.animate('rotation_x', -90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    elif normal == 'Uw':
        [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.y >= 0]
        rotation_helper.animate('rotation_y', 90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    elif normal == 'Dw':
        [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.y <= 0]
        rotation_helper.animate('rotation_y', -90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    elif normal == 'Bw':
        [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.z >= 0]
        rotation_helper.animate('rotation_z', -90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    elif normal == 'Fw':
        [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.z <= 0]
        rotation_helper.animate('rotation_z', 90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')


    elif normal == 'M':
        [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.x == 0]
        rotation_helper.animate('rotation_x', 90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    elif normal == 'S':
        [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.z == 0]
        rotation_helper.animate('rotation_z', 90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    elif normal == 'E':
        [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.y == 0]
        rotation_helper.animate('rotation_y', 90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    
    elif normal=='X':
        [setattr(e, 'world_parent', rotation_helper) for e in cubes]
        rotation_helper.animate('rotation_x', 90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')

    elif normal=='Y':
        [setattr(e, 'world_parent', rotation_helper) for e in cubes]
        rotation_helper.animate('rotation_y', 90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    
    elif normal=='Z':
        [setattr(e, 'world_parent', rotation_helper) for e in cubes]
        rotation_helper.animate('rotation_z', 90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')




    invoke(reset_rotation_helper, delay=.2*speed)

    if speed or animation_in_progress:
        collider.ignore_input = True
        animation_in_progress =True
        

        @after(.25*speed)
        def _():
            collider.ignore_input = False
            global animation_in_progress
            animation_in_progress=False
            check_for_win()




def reset_rotation_helper():
    [setattr(e, 'world_parent', scene) for e in cubes]
    rotation_helper.rotation = (0,0,0)


win_text_entity = Text(y=.35, text='', color=color.green, origin=(0,0), scale=3)

def check_for_win():
    if {e.world_rotation for e in cubes} == {Vec3(0,0,0)}:
        win_text_entity.text = 'SOLVED!'
        win_text_entity.appear()
    else:
        win_text_entity.text = ''


def randomize():
    faces = (Vec3(1,0,0), Vec3(0,1,0), Vec3(0,0,1), Vec3(-1,0,0), Vec3(0,-1,0), Vec3(0,0,-1))
    for i in range(20):
        rotate_side(normal=random.choice(faces), direction=random.choice((-1,1)), speed=0)

randomize_button = Button(text='randomize', color=color.azure, position=(.7,-.4), on_click=randomize)
randomize_button.fit_to_text()

window.color = color._16
def executar_comandos_interface(string_comando=None):
    global fila_de_comandos
    comandos_dict={
        "R":(Vec3(1,0,0),1),
        "R'":(Vec3(1,0,0),-1),
        "L":(Vec3(-1,0,0),1),
        "L'":(Vec3(-1,0,0),-1),
        "F":(Vec3(0,0,-1),1),
        "F'":(Vec3(0,0,-1),-1),
        "B":(Vec3(0,0,1),1),
        "B'":(Vec3(0,0,1),-1),
        "U":(Vec3(0,1,0),1),
        "U'":(Vec3(0,1,0),-1),
        "D":(Vec3(0,-1,0),1),
        "D'":(Vec3(0,-1,0),-1),

        "M":('M',1),
        "M'":('M',1),
        "S":('S',1),
        "S'":('S',-1),
        "E":('E',-1),
        "E'":('E',-1),

        "R2":(Vec3(1,0,0),1),
        "L2":(Vec3(-1,0,0),1),
        "U2":(Vec3(0,1,0),1),
        "D2":(Vec3(0,-1,0),1),
        "B2":(Vec3(0,0,1),1),
        "F2":(Vec3(0,0,-1),1),

        "M2":('M',1),
        "S2":('S',1),
        "E2":('S',1),

        "RW":('Rw',1),
        "RW'":('Rw',-1),
        "LW":('Lw',1),
        "LW'":('Lw',-1),
        "FW":('Fw',1),
        "FW'":('Fw',-1),
        "BW":('Bw',1),
        "BW'":('Bw',-1),
        "UW":('Uw',1),
        "UW'":('Uw',-1),
        "DW":('Dw',1),
        "DW'":('Dw',-1),

        "RW2":('Rw',1),
        "LW2":('Lw',1),
        "FW2":('Fw',1),
        "BW2":('Bw',1),
        "UW2":('Uw',1),
        "DW2":('Dw',1),

        "X":('X',1),
        "X'":('X',-1),
        "Y":('Y',1),
        "Y'":('Y',-1),
        "Z":('Z',1),
        "Z'":('Z',-1)
        
        }

    if string_comando is not None:
        string_comando=string_comando.upper()
        lista_comandos=string_comando.split()
        print(" ".join(lista_comandos))
        for comando in lista_comandos:
            if str(comando).__contains__('2'):
                fila_de_comandos.put([comandos_dict[comando][0],comandos_dict[comando][1]])
                fila_de_comandos.put([comandos_dict[comando][0],comandos_dict[comando][1]])
            else:
                fila_de_comandos.put([comandos_dict[comando][0],comandos_dict[comando][1]])

    else:
        string_comando=input("Digite os movimentos separados por espaços")
        string_comando=string_comando.upper()
        lista_comandos=string_comando.split()
        print(" ".join(lista_comandos))
        for comando in lista_comandos:
            if str(comando).__contains__('2'):
                fila_de_comandos.put([comandos_dict[comando][0],comandos_dict[comando][1]])
                fila_de_comandos.put([comandos_dict[comando][0],comandos_dict[comando][1]])
            else:
                fila_de_comandos.put([comandos_dict[comando][0],comandos_dict[comando][1]])

def update():
    global fila_de_comandos
    if (not animation_in_progress) and (not fila_de_comandos.empty()):
        comando=fila_de_comandos.get()
        rotate_side(comando[0],comando[1])
  
invoke(executar_comandos_interface,"R' F2 D R2 B D2 R' F2 D' L B2 U2 R F2 U2 R B' D' L F' D' L F2 D2 L".replace("’","'"),delay=3)
invoke(executar_comandos_interface,'''
R U R' U' R' F R2 U' R' U' R U R' F'
L' R U R' U' R' F R2 U' R' U' R U R' F' L
DW2 L' R U R' U' R' F R2 U' R' U' R U R' F' L DW2
D' LW D L2 R U R' U' R' F R2 U' R' U' R U R' F' L2 D' LW' D
DW L' R U R' U' R' F R2 U' R' U' R U R' F' L DW'
LW D' L2 R U R' U' R' F R2 U' R' U' R U R' F' L2 D LW'
DW' L' R U R' U' R' F R2 U' R' U' R U R' F' L DW
DW' L R U R' U' R' F R2 U' R' U' R U R' F' L' DW
D' L2 R U R' U' R' F R2 U' R' U' R U R' F' L2 D
L2 R U R' U' R' F R2 U' R' U' R U R' F' L2
LW2 D' L2 R U R' U' R' F R2 U' R' U' R U R' F' L2 D LW2
LW' D' L2 R U R' U' R' F R2 U' R' U' R U R' F' L2 D LW
D' L2 R U R' U' R' F R2 U' R' U' R U R' F' L2 D
'''.replace("’","'"),delay=20)

EditorCamera()

app.run()
