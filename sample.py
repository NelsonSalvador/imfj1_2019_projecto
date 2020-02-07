# Import pygame into our program
import pygame
import pygame.freetype
import time

from scene import *
from object3d import *
from mesh import *
from material import *
from color import *

# Define a main function, just to keep things nice and tidy
def main():
    # Initialize pygame, with the default parameters
    pygame.init()

    #Incialização de variaveis 
    kup = False
    kdown = False
    kright = False
    kleft = False
    kpgup = False
    kpgdown = False
    ks = False
    ka = False
    kd = False
    kw = False
    kq = False
    ke = False
    

    # Define the size/resolution of our window
    res_x = 640
    res_y = 480

    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    # Create a scene
    scene = Scene("TestScene")
    scene.camera = Camera(False, res_x, res_y)

    # Moves the camera back 2 units
    scene.camera.position -= vector3(0,0,2)

    # Create a cube and place it in a scene, at position (0,0,0)
    # This cube has 1 unit of side, and is red
    

    obj3 = Object3d("TestObject1")
    obj3.position = vector3(2, 0, 2)
    obj3.mesh = Mesh.create_cube((1.5, 1, 1.5))
    obj3.material = Material(color(1,0,0,1), "TestMaterial3")

    obj4 = Object3d("TestObject2")
    obj4.position = vector3(0, 0, 3)
    obj4.mesh = Mesh.create_cube((1.5, 1.5, 1))
    obj4.material = Material(color(1,0,0,1), "TestMaterial4")

    obj5 = Object3d("TestObject3")
    obj5.position = vector3(3, 0, 0)
    obj5.mesh = Mesh.create_cube((0.25, 0.25, 0.25))
    obj5.material = Material(color(1,0,0,1), "TestMaterial4")

    # Create a second object, and add it as a child of the first object
    # When the first object rotates, this one will also mimic the transform
    obj2 = Object3d("ChildObject")
    obj2.position += vector3(0, 0.75, 0)
    obj2.mesh = Mesh.create_cube((0.5, 0.5, 0.5))
    obj2.material = Material(color(0,1,0,1), "TestMaterial2")

    obj1 = Object3d("TestObject")
    obj1.scale = vector3(1, 1, 1)
    obj1.position = vector3(0, -1, 0)
    obj1.mesh = Mesh.create_cube((1, 1, 1))
    obj1.material = Material(color(1,0,0,1), "TestMaterial1")

    scene.add_object(obj1)
    obj1.add_child(obj2)
    obj1.add_child(obj3)
    obj1.add_child(obj4)
    obj1.add_child(obj5)
    
    

    # Specify the rotation of the object. It will rotate 15 degrees around the axis given, 
    # every second
    angle = 0
    axis = vector3(1,0.7,0.2)
    axis.normalize()


    # Timer
    delta_time = 0
    prev_time = time.time()

    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)


    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            scene.add_object(obj1)
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    return
                if (event.key == pygame.K_UP):
                    kup = True
                if (event.key == pygame.K_DOWN):
                    kdown = True
                if (event.key == pygame.K_RIGHT):
                    kright = True
                if (event.key == pygame.K_LEFT):
                    kleft = True
                if (event.key == pygame.K_PAGEDOWN):
                    kpgdown = True
                if (event.key == pygame.K_PAGEUP):
                    kpgup = True
                if (event.key == pygame.K_w):
                    kw = True
                if (event.key == pygame.K_a):
                    ka = True
                if (event.key == pygame.K_s):
                    ks = True
                if (event.key == pygame.K_d):
                    kd = True
                if (event.key == pygame.K_q):
                    kq = True
                if (event.key == pygame.K_e):
                    ke = True
            elif (event.type == pygame.KEYUP):
                if (event.key == pygame.K_UP):
                    kup = False
                if (event.key == pygame.K_DOWN):
                    kdown = False
                if (event.key == pygame.K_RIGHT):
                    kright = False
                if (event.key == pygame.K_LEFT):
                    kleft = False
                if (event.key == pygame.K_PAGEUP):
                    kpgup = False
                if (event.key == pygame.K_PAGEDOWN):
                    kpgdown = False
                if (event.key == pygame.K_w):
                    kw = False
                if (event.key == pygame.K_a):
                    ka = False
                if (event.key == pygame.K_s):
                    ks = False
                if (event.key == pygame.K_d):
                    kd = False
                if (event.key == pygame.K_q):
                    kq = False
                if (event.key == pygame.K_e):
                    ke = False
                  
        if kup:
            axis = vector3(-1, 0, 0)
            angle = 50
            q = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation
        if kdown:
            axis = vector3(1,0,0)
            angle = 50
            q = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation
        if kright:
            axis = vector3(0,1,0)
            angle = 50
            q = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation
        if kleft:
            axis = vector3(0,-1,0)
            angle = 50
            q = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation
        if kpgup:
            axis = vector3(0,0,1)
            angle = 50
            q = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation
        if kpgdown:
            axis = vector3(0,0,-1)
            angle = 50
            q = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation
        if kq:
            scene.camera.position -= vector3(0,0,0.1)
        if ke:
            scene.camera.position += vector3(0,0,0.1)
        if ka:
            scene.camera.position += vector3(0.1,0,0)
        if kd:
            scene.camera.position -= vector3(0.1,0,0)
        if kw:
            scene.camera.position -= vector3(0,0.1,0)
        if ks:
            scene.camera.position += vector3(0,0.1,0)
        
        #Back Face culling
        #for i in obj1.mesh.polygons:
         #   n = cross_product(i[1], i[2])
          #  v =  scene.camera.position
           # if dot_product(v, n) < 0:
            #    obj1.mesh.polygons.append(i)
           # else:
            #    obj1.mesh.polygons.remove(i)
        #Mesh.render(screen, obj1.mesh.polygons, Material(color(1,0,0,1)))


        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,20))

        scene.render(screen)
        

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()


# Run the main function
main()
