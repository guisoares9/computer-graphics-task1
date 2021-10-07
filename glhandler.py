import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

t_x = 0
t_y = 0

theta = 0

# Capturando eventos de teclado e mouse
def key_event(window,key,scancode,action,mods):
    
    global t_x, t_y, theta

    if (key == 265) | (key == 87):
        t_y += 0.02
    if (key == 264) | (key == 83):
        t_y -= 0.02
    if (key == 263) | (key == 65):
        t_x -= 0.02
    if (key == 262) | (key == 68):
        t_x += 0.02
    if (key == 81):
        theta += 0.1
    if (key == 69):
        theta -= 0.1


    print('[key event] key=',key)
    print('[key event] scancode=',scancode)
    print('[key event] action=',action)
    print('[key event] mods=',mods)
    print('-------')

def mouse_event(window,button,action,mods):
    print('[mouse event] button=',button)
    print('[mouse event] action=',action)
    print('[mouse event] mods=',mods)
    print('-------')

def setWindow(width, height, name):
    # Inicializando janela
    glfw.init()
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE);
    window = glfw.create_window(width, height, name, None, None)
    glfw.make_context_current(window)
        
    glfw.set_key_callback(window,key_event)

    glfw.set_mouse_button_callback(window,mouse_event)

    return window

def setGPU():
    # GLSL para Vertex Shader
    vertex_code = """
        attribute vec2 position;
        uniform mat4 mat_transformation;
        void main(){
            gl_Position = mat_transformation * vec4(position,0.0,1.0);
        }
        """

    # GLSL para Fragment Shader
    fragment_code = """
        uniform vec4 color;
        void main(){
            gl_FragColor = color;
        }
        """
        
    # Request a program and shader slots from GPU
    program  = glCreateProgram()
    vertex   = glCreateShader(GL_VERTEX_SHADER)
    fragment = glCreateShader(GL_FRAGMENT_SHADER)

    # Set shaders source
    glShaderSource(vertex, vertex_code)
    glShaderSource(fragment, fragment_code)

    # Compile shaders
    glCompileShader(vertex)
    if not glGetShaderiv(vertex, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(vertex).decode()
        print(error)
        raise RuntimeError("Erro de compilacao do Vertex Shader")

    # Compilando o Fragment Shader
    glCompileShader(fragment)
    if not glGetShaderiv(fragment, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(fragment).decode()
        print(error)
        raise RuntimeError("Erro de compilacao do Fragment Shader")

    # Attach shader objects to the program
    glAttachShader(program, vertex)
    glAttachShader(program, fragment)

    # Build program
    glLinkProgram(program)
    if not glGetProgramiv(program, GL_LINK_STATUS):
        print(glGetProgramInfoLog(program))
        raise RuntimeError('Linking error')
        
    # Make program the default program
    glUseProgram(program)

    return program

def setGPUBuffer(program, vertices ):
    # Request a buffer slot from GPU
    buffer = glGenBuffers(1)
    # Make this buffer the default one
    glBindBuffer(GL_ARRAY_BUFFER, buffer)

    # Upload data1
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)

    # Bind the position attribute
    # --------------------------------------
    stride = vertices.strides[0]
    offset = ctypes.c_void_p(0)

    loc = glGetAttribLocation(program, "position")
    glEnableVertexAttribArray(loc)

    glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, offset)

if __name__ == '__main__':


    # Sets the window
    window = setWindow(600, 600, "Triangle")

    # Configure shaders and construct variables
    program = setGPU()

    vertices = np.zeros(6, [("position", np.float32, 2)])
    # preenchendo as coordenadas de cada vértice
    vertices['position'] = [
                            ( 0.0, 0.0), # vertice 0
                            (+0.5,+0.5), # vertice 1
                            (+0.5, 0.0), # vertice 2
                            (-1.0,-1.0), # vertice 3
                            (-0.5, 0.0), # vertice 4
                            (+1.0,-1.0)  # vertice 5
                        ]

    # Sets the GPU Buffer
    setGPUBuffer( program, vertices )


    loc_color = glGetUniformLocation(program, "color")

    glfw.show_window(window)

    while not glfw.window_should_close(window):

        glfw.poll_events() 
        
        glClear(GL_COLOR_BUFFER_BIT)
    
        glClearColor(1.0, 1.0, 1.0, 1.0)

        glUniform4f(loc_color, 0.0, 1.0, 1.0, 1.0) 
        
        glDrawArrays(GL_TRIANGLES, 0, len(vertices)) 

        glfw.swap_buffers(window)

    glfw.terminate()
