from ursina import *

# Inicializar a aplicação Ursina
app = Ursina()

# Adicionar uma câmera que permite controle com o mouse
editor_camera = EditorCamera(rotation_speed=200, panning_speed=20)

# Criar a entidade principal do cubo
cube = Entity(scale=(2, 2, 2))

# Criar entidades para cada face com posições ajustadas e culling desativado
top_face = Entity(parent=cube, model='quad', color=color.yellow, position=(0, 1, 0), rotation_x=-90, scale=(2, 2), double_sided=True)
bottom_face = Entity(parent=cube, model='quad', color=color.white, position=(0, -1, 0), rotation_x=90, scale=(2, 2), double_sided=True)
back_face = Entity(parent=cube, model='quad', color=color.red, position=(0, 0, 1), scale=(2, 2), double_sided=True)
front_face = Entity(parent=cube, model='quad', color=color.orange, position=(0, 0, -1), rotation_y=180, scale=(2, 2), double_sided=True)
right_face = Entity(parent=cube, model='quad', color=color.blue, position=(1, 0, 0), rotation_y=-90, scale=(2, 2), double_sided=True)
left_face = Entity(parent=cube, model='quad', color=color.green, position=(-1, 0, 0), rotation_y=90, scale=(2, 2), double_sided=True)

# Executar a aplicação
app.run()
