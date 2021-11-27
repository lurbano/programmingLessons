from vpython import *
import numpy as np

scene.range = 10

ball = sphere(radius=0.5)
floor = curve(pos=[vec(-10,0,0), vec(10,0,0)])

v_i = vector(2, 10, 0)
ball.v = v_i * 1.0  # m/s
ball.mass = 1.0    # kg

g = vec(0,9.8,0)     # m/s^2

windSpeed = vec(-5, 0, 0)   # m/s

l_vxyArrows = False

ball.arrow = arrow(pos = ball.pos, axis = ball.v, shaftwidth=0.2)

if l_vxyArrows:
    ball.vx_arrow = arrow(pos = ball.pos,
                          axis = vec(ball.v.x, 0, 0),
                          color=color.red,
                          shaftwidth=0.2)
    ball.vy_arrow = arrow(pos = ball.pos + ball.vx_arrow.axis,
                          axis = vec(0, ball.v.y, 0),
                          color=color.yellow,
                          shaftwidth=0.2)

dt = 0.05

while True:
    sleep(dt)

    # determine acceleration based on forces
    # 1. Gravitational Force
    Fg = ball.mass * g
    # 2. Wind Force
    fc = 0.1
    Fw = vec(fc*windSpeed.x**2, fc*windSpeed.y**2, 0)
    # 3. Net force
    F = Fg + Fw

    # calculate acceleration
    a = F / ball.mass
    print(a, ball.v)

    # update velocity based on acceleration
    ball.v = ball.v - a * dt

    # update ball position based on velocity vector
    ball.pos.x = ball.pos.x + ball.v.x * dt
    ball.pos.y = ball.pos.y + ball.v.y * dt

    #update positions of the arrow
    ball.arrow.pos = ball.pos

    # update directions of arrow
    ball.arrow.axis = ball.v

    if l_vxyArrows:
        ball.vx_arrow.pos = ball.pos
        ball.vy_arrow.pos = ball.pos + ball.vx_arrow.axis
        ball.vx_arrow.axis = vec(ball.v.x, 0, 0)
        ball.vy_arrow.axis = vec(0, ball.v.y, 0)

    # bounce (conserve momentum)
    if ball.pos.y <= 0:
        ball.pos.y = 0
        ball.v.y = v_i.y
