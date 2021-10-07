import glhandler as gh
import objects as objs
import transform as trans
import time
import numpy as np
import glfw
from OpenGL.GL import *

# Sets the window
window = gh.setWindow(800, 800, "Move: WASD or ArrowKeys, Rotate: to left Q and to right E")

# Configure shaders and construct variables
program = gh.setGPU()

# Import objects (ship; planet; continent; sun; moon)
ship = objs.Ship()
planet, continent = objs.Planet(), objs.Continent()
sun, moon = objs.Sun(), objs.Moon()
stars = objs.Stars()

# Sets 'vertices' array size
total_len = len(ship) + len(planet) + len(continent) + len(sun) + len(moon) + len(stars)
vertices = np.zeros(total_len, [("position", np.float32, 2)])

# Fill 'vertices' with the objects points
aux0 = 0
aux1 = len(stars)
vertices['position'][aux0:aux1] = stars
aux0 = aux1
aux1 += len(planet)
vertices['position'][aux0:aux1] = planet
aux0 = aux1
aux1 += len(continent)
vertices['position'][aux0:aux1] = continent
aux0 = aux1
aux1 += len(sun)
vertices['position'][aux0:aux1] = sun
aux0 = aux1
aux1 += len(moon)
vertices['position'][aux0:aux1] = moon
aux0 = aux1
aux1 += len(ship)
vertices['position'][aux0:aux1] = ship

# Sets the GPU Buffer
gh.setGPUBuffer(program, vertices)

loc_color = glGetUniformLocation(program, "color")

R = 1
G = 0
B = 0

tx = 0
ty = 0
theta = 0
last_tx = 0
last_ty = 0
tx_planeta = 0
ty_planeta = 0
glfw.show_window(window)

t0 = time.time()

while not glfw.window_should_close(window):

    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.005, 0.01, 0.1, 1.0)

    loc = glGetUniformLocation(program, "mat_transformation")

    theta += gh.dtheta
    if 1 > abs(tx + gh.dt_x*np.cos(theta) - gh.dt_y*np.sin(theta)):
        tx = tx + gh.dt_x*np.cos(theta) - gh.dt_y*np.sin(theta)
    if 1 > abs(ty + gh.dt_x*np.sin(theta) + gh.dt_y*np.cos(theta)):
        ty = ty + gh.dt_x*np.sin(theta) + gh.dt_y*np.cos(theta)

    tx_planeta = -tx
    ty_planeta = -ty
    d_sun = np.sqrt((tx_planeta-0.7)**2+(ty_planeta+0.7)**2)
    d_planeta = np.sqrt((tx_planeta)**2+(ty_planeta)**2)
    last_tx = tx
    last_ty = ty

    gh.dt_x = 0
    gh.dt_y = 0
    gh.dtheta = 0

# Stars
    mat_transform = trans.createEyeMat()
    mat_transform = trans.scale(1, 1, mat_transform)
    mat_transform = trans.translate(0, 0, mat_transform)
    glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transform)


    R, G, B = 1, 1, 1
    glUniform4f(loc_color, R, G, B, 1.0)
    glDrawArrays(GL_POINTS, 0, len(stars))
# Sun
    mat_transform = trans.createEyeMat()
    mat_transform = trans.scale(0.3/(d_sun+.001), 0.3/(d_sun+.001), mat_transform)
    mat_transform = trans.translate(-0.7+tx_planeta/10, 0.7+ty_planeta/10, mat_transform)
    glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transform)
    R, G, B = 1, 0.7, 0
    glUniform4f(loc_color, R, G, B, 1.0)
    glDrawArrays(GL_TRIANGLE_FAN, len(stars) + len(planet) + len(continent), len(sun))

# Planet
    d = tx**2 + ty**2
    mat_transform = trans.createEyeMat()
    mat_transform = trans.scale(.5/(5*d_planeta**4+1), .5/(5*d_planeta**4+1), mat_transform)
    mat_transform = trans.translate(0+tx_planeta, -0.5+ty_planeta, mat_transform)
    glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transform)
    R, G, B = 0, 0, 1
    glUniform4f(loc_color, R, G, B, 1.0)
    glDrawArrays(GL_TRIANGLE_FAN, len(stars), len(planet))

# Continent
    mat_transform = trans.createEyeMat()
    mat_transform = trans.scale(0.48/(5*d_planeta**4+1), 0.48/(5*d_planeta**4+1), mat_transform)
    mat_transform = trans.translate(0+tx_planeta, -0.5+ty_planeta, mat_transform)
    glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transform)
    R, G, B = 0, 1, 0
    glUniform4f(loc_color, R, G, B, 1.0)
    glDrawArrays(GL_TRIANGLES, len(planet)+len(stars), len(continent))


# Moon
    t = time.time() - t0
    mat_transform = trans.createEyeMat()
    mat_transform = trans.scale(0.15, 0.15, mat_transform)
    mat_transform = trans.translate(0.9, 0, mat_transform)
    mat_transform = trans.rotateZ(t, mat_transform)
    mat_transform = trans.scale(1/(5*d_planeta**4+1), 1/(5*d_planeta**4+1), mat_transform)
    mat_transform = trans.translate(0.0+tx_planeta, -0.5+ty_planeta, mat_transform)
    glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transform)
    R, G, B = 0.3, 0.3, 0.3
    glUniform4f(loc_color, R, G, B, 1.0)
    glDrawArrays(GL_TRIANGLE_FAN, len(stars) + len(planet) + len(continent) + len(sun), len(moon))

# Ship
    mat_transform = trans.createEyeMat()
    mat_transform = trans.translate(-0.05, -0.05, mat_transform)
    mat_transform = trans.scale(2, 2, mat_transform)
    mat_transform = trans.rotateZ(theta, mat_transform)

    mat_transform = trans.translate(tx, ty, mat_transform)
    glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transform)
    R, G, B = 1, 0, 0
    glUniform4f(loc_color, R, G, B, 1.0)
    glDrawArrays(GL_TRIANGLES, len(stars) + len(planet) + len(continent) + len(sun) + len(moon), len(ship)-4)
    glUniform4f(loc_color, R, G, B, 1.0)
    glDrawArrays(GL_TRIANGLES, len(stars) + len(planet) + len(continent) + len(sun) + len(moon)+1, len(ship)-3)
    glUniform4f(loc_color, 0, 0, 0, 1.0)
    glDrawArrays(GL_TRIANGLES, len(stars) + len(planet) + len(continent) + len(sun) + len(moon)+4, 3)

    glfw.swap_buffers(window)

glfw.terminate()
