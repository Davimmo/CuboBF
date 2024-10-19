from ursina import *


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

def criar_cubos():
    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                # make a model with a separate color on each face
                combine_parent = Entity(enabled=False)
                for i in range(3):
                    dir = Vec3(0,0,0)
                    dir[i] = 1

                    if x==1 and cube_colors[i*2]==color.blue:
                        e = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=cube_colors[i*2])
                        e.look_at(dir, 'up')
                    else:
                        e = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=color.black)
                        e.look_at(dir, 'up')                        

                    if x==-1 and cube_colors[(i*2)+1]==color.green:
                        e_flipped = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=cube_colors[(i*2)+1])
                        e_flipped.look_at(-dir, 'up')
                    else:
                        e = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=color.black)
                        e.look_at(dir, 'up')                     

                    
                    if y==1 and cube_colors[i*2]==color.yellow:
                        e = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=cube_colors[i*2])
                        e.look_at(dir, 'up')
                    else:
                        e = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=color.black)
                        e.look_at(dir, 'up')  

                    if y==-1 and cube_colors[(i*2)+1]==color.white:
                        e_flipped = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=cube_colors[(i*2)+1])
                        e_flipped.look_at(-dir, 'up')
                    else:
                        e = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=color.black)
                        e.look_at(dir, 'up')  

                    if z==1 and cube_colors[i*2]==color.red:
                        e = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=cube_colors[i*2])
                        e.look_at(dir, 'up')
                    else:
                        e = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=color.black)
                        e.look_at(dir, 'up')  
                        
                    if z==-1 and cube_colors[(i*2)+1]==color.orange:
                        e_flipped = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=cube_colors[(i*2)+1])
                        e_flipped.look_at(-dir, 'up')
                    else:
                        e = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube', color=color.black)
                        e.look_at(dir, 'up')                      


                    combine_parent.combine()

                    e = Entity(model=copy(combine_parent.model), position=Vec3(x,y,z), texture='white_cube')
                    cubes.append(e)

