from vpython import *

scene.range = 10

ball = sphere(radius=0.5)
floor = curve(pos=[vec(-10,0,0), vec(10,0,0)])

ball.v = vector(0, 10, 0)

ball.arrow = arrow(pos = ball.pos, axis = ball.v, shaftwidth=0.2)
ball.vx_arrow = arrow(pos = ball.pos,
                      axis = vec(ball.v.x, 0, 0),
                      color=color.red,
                      shaftwidth=0.2)
ball.vy_arrow = arrow(pos = ball.pos + ball.vx_arrow.axis,
                      axis = vec(0, ball.v.y, 0),
                      color=color.yellow,
                      shaftwidth=0.2)

print(ball.vx_arrow.axis, ball.v.x)

dt = 0.05

while True:
    sleep(dt)
    #sleep(1)

    # update velocity based on gravitational acceleration
    ball.v.y = ball.v.y - 9.8 * dt

    # update ball position based on velocity vector
    ball.pos.x = ball.pos.x + ball.v.x * dt
    ball.pos.y = ball.pos.y + ball.v.y * dt

    #update positions of the arrows
    ball.arrow.pos = ball.pos
    ball.vx_arrow.pos = ball.pos
    ball.vy_arrow.pos = ball.pos + ball.vx_arrow.axis
    # update directions of arrows
    ball.arrow.axis = ball.v
    ball.vx_arrow.axis = vec(ball.v.x, 0, 0)
    ball.vy_arrow.axis = vec(0, ball.v.y, 0)

    if ball.pos.y <= 0:
        ball.v.y = -ball.v.y
