# computer-graphics-task1
First group task for Computer Graphics subject using OpenGL tools.

## Install

The whole program was made in python3. Here is what you need to get to run our software:

```py
pip install numpy
pip install glfw
pip install OpenGL
```

And we execute by double clicking ``main.py`` or the terminal command ``python main.py`` 

## Execution

The program was a very interesting way to exercise OpenGL programming and to understand the way that everything is rendered in mostly computational screens.

First of all, this the screen that you should see when start the program:

![alt text](https://i.imgur.com/BE8mngl.png)

This is a "game" that you can control a red spaceship and fly away of the Earth. 
To control it you can use **WASD** or the **ArrowKeys** and to rotate it, use **Q** to rotate to the left and **E** to the right.

![alt text](https://i.imgur.com/8PdQ7vL.gif)

## How it works?

This project were divided in four files:

### ``transform.py``

Responsible to manage the transformation matrices, i.e, it generates the right matrices to do the fundamental transformations such as translation, scale and rotation.

### ``glhandler.py``

Holds all the specific OpenGL settings with the GPU buffer and the window. It also sets the key bindings to the game controls.

### ``objects.py``

It is made to return the arrays that contain the figure points to the drawn.

### ``main.py``

Finally, this is the main file to use all those functions to set up the game. The processes can be simplified to: Set the window; Load figures; Set the GPU; Transform and draw all the figures.