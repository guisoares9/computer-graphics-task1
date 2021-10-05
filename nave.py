

import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import triangle


glfw.init()
glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
window = glfw.create_window(500, 500, "Cores", None, None)
glfw.make_context_current(window)


vertex_code = """
        attribute vec2 position;
        uniform mat4 mat_transformation;
        void main(){
            gl_Position = mat_transformation * vec4(position,0.0,1.0);
        }
        """


fragment_code = """
        uniform vec4 color;
        void main(){
            gl_FragColor = color;
        }
        """


program = glCreateProgram()
vertex = glCreateShader(GL_VERTEX_SHADER)
fragment = glCreateShader(GL_FRAGMENT_SHADER)


glShaderSource(vertex, vertex_code)
glShaderSource(fragment, fragment_code)


glCompileShader(vertex)
if not glGetShaderiv(vertex, GL_COMPILE_STATUS):
    error = glGetShaderInfoLog(vertex).decode()
    print(error)
    raise RuntimeError("Erro de compilacao do Vertex Shader")


glCompileShader(fragment)
if not glGetShaderiv(fragment, GL_COMPILE_STATUS):
    error = glGetShaderInfoLog(fragment).decode()
    print(error)
    raise RuntimeError("Erro de compilacao do Fragment Shader")


glAttachShader(program, vertex)
glAttachShader(program, fragment)


glLinkProgram(program)
if not glGetProgramiv(program, GL_LINK_STATUS):
    print(glGetProgramInfoLog(program))
    raise RuntimeError('Linking error')


glUseProgram(program)


vertices = np.zeros(7, [("position", np.float32, 2)])


vertices['position'] = [
    (0.0, +0),
    (+0.25, 0.5),
    (0.25, 0.15),
    (0.5, 0),
    (0.2, 0.3),
    (0.3, 0.3),
    (0.25, 0.35)
]


buffer = glGenBuffers(1)

glBindBuffer(GL_ARRAY_BUFFER, buffer)


glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_DYNAMIC_DRAW)
glBindBuffer(GL_ARRAY_BUFFER, buffer)


stride = vertices.strides[0]
offset = ctypes.c_void_p(0)


loc = glGetAttribLocation(program, "position")
glEnableVertexAttribArray(loc)


glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, offset)


loc_color = glGetUniformLocation(program, "color")
R = 1.0
G = 0.0
B = 0.0


t_x = 0
t_y = 0


def key_event(window, key, scancode, action, mods):
    global t_x, t_y

    if key == 265:
        t_y += 0.02
    if key == 264:
        t_y -= 0.02
    if key == 263:
        t_x -= 0.02
    if key == 262:
        t_x += 0.02


glfw.set_key_callback(window, key_event)


glfw.show_window(window)


while not glfw.window_should_close(window):

    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1.0, 1.0, 1.0, 1.0)

    mat_translation = np.array([1.0, 0.0, 0.0, t_x,
                                0.0, 1.0, 0.0, t_y,
                                0.0, 0.0, 1.0, 0.0,
                                0.0, 0.0, 0.0, 1.0], np.float32)

    s_x = t_x
    s_y = t_y
    mat_scale = np.array([np.cos(t_x), -np.sin(t_x), 0.0, 0.0,
                          np.sin(t_x), np.cos(t_x), 0.0, 0.0,
                          0.0, 0.0, 1.0, 0.0,
                          0.0, 0.0, 0.0, 1.0], np.float32)

    loc = glGetUniformLocation(program, "mat_transformation")
    glUniformMatrix4fv(loc, 1, GL_TRUE, mat_translation)

    glUniform4f(loc_color, R, G, B, 1.0)
    glDrawArrays(GL_TRIANGLES, 0, len(vertices)-4)
    glUniform4f(loc_color, R, G, B, 1.0)
    glDrawArrays(GL_TRIANGLES, 1, len(vertices)-3)
    glUniform4f(loc_color, 0, 0, 0, 1.0)
    glDrawArrays(GL_TRIANGLES, 4, len(vertices))
    glUniform4f(loc_color, 0, 0, 0, 1.0)

    glfw.swap_buffers(window)

glfw.terminate()