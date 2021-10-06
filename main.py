import glhandler as gh
import objects as objs
import transform as trans

import numpy as np
import glfw
from OpenGL.GL import *

# Sets the window
window = gh.setWindow(600, 600, "Triangle")

# Configure shaders and construct variables
program = gh.setGPU()


ship = objs.Ship()
world = objs.World()

total_len = len(ship) + len(world)
vertices = np.zeros(total_len, [("position", np.float32, 2)])
# preenchendo as coordenadas de cada vértice
# vertices['position'] = [
#                         ( 0.0, 0.0), # vertice 0
#                         (+0.5,+0.5), # vertice 1
#                         (+0.5, 0.0), # vertice 2
#                         (-1.0,-1.0), # vertice 3
#                         (-0.5, 0.0), # vertice 4
#                         (+1.0,-1.0)  # vertice 5
#                     ]
vertices['position'][:len(ship)] = ship
vertices['position'][len(ship):len(vertices)] = world

# Sets the GPU Buffer
gh.setGPUBuffer( program, vertices )

loc_color = glGetUniformLocation(program, "color")

R = 1
G = 0
B = 0

glfw.show_window(window)

while not glfw.window_should_close(window):

    glfw.poll_events() 
    
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1.0,1.0,1.0,1.0)

    # loc = glGetUniformLocation(program, "mat_transformation")
    
    glUniform4f(loc_color, R, G, B, 1.0)
    glDrawArrays(GL_TRIANGLES, 0, len(ship)-4)
    glUniform4f(loc_color, R, G, B, 1.0)
    glDrawArrays(GL_TRIANGLES, 1, len(ship)-3)
    glUniform4f(loc_color, 0, 0, 0, 1.0)
    glDrawArrays(GL_TRIANGLES, 4, len(ship))
    glUniform4f(loc_color, R, G, B, 1.0)

    glUniform4f(loc_color, R, G, B, 1.0)
    glDrawArrays(GL_TRIANGLE_STRIP, len(ship), len(world))


    glfw.swap_buffers(window)

glfw.terminate()

