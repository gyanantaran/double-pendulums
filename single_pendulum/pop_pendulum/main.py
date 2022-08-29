
import pygame                   # will use pygame as the graphics API
from math import pi, sin, cos   # using trigonometric constructs


# initialising
pygame.init()


# Game const
clock = pygame.time.Clock() # clocks the time between frame
fps = 40                    # number of frames per second
dt = 0.000001               # delta t for calculating the next postions
m_scale = 150               # one meter is hundred pixels
kg_scale = 10               # one kilo bob, is 10 pixel radius

# screen things
SIZE = width, height = (620, 480)               # dimensions of the game screen
pivot = x0, y0 = (width / 2, height / 2)        # pivot location
screen_surface = pygame.display.set_mode( SIZE )# screen object
TITLE = "Single Pendulum | Uniform Gravity"     # title of the game window
pygame.display.set_caption(TITLE)               # setting the title of the game
rod_width = 2                                   # width of rod

# colors
white = (250, 250, 250)     # white color
background = (23, 38, 38)   # background color
bob_color = (250, 0, 120)   # color or the bob

# constants
gravity = 9.8   # gravitational acceleration in m/s^2
m = 1           # mass of the bob
length = 1      # length of the rod

# state variables
theta = pi - 0.1   # angle of the rod from vertical, counter-clockwise
theta_dash = 0          # angular velocity
theta_double_dash = 0   # angular acceleration


# formulaes
def get_theta_double_dash(g: float = 10, l:float = 1, t: float = pi/4):
    """
    :param: g : (float) Gravity in meters per second squared
    :param: l : Length of rod in meters
    :param: t : theta at the moment in radians
    """
    return -1 * (g / l) * sin( theta )  # uniform gravity without damping


# game loop
running = True
while running:
    # adds elapsed seconds to the last clock mark, pauses if below 1/fps sec
    clock.tick( fps )

    # filling the surface
    screen_surface.fill( background )


    # on_event loop further to check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # quits game loop in the end of this cycle


    # on_loop calculations
    time = 1 / fps  # seconds available
    for _ in range( 0, int( time / dt ) ):
        # in this clock cycle updates the position, int( time / dt ) times
        theta_double_dash = get_theta_double_dash( gravity, length, theta )
        theta_dash += theta_double_dash * dt
        theta += theta_dash * dt


    # drawing
    pygame.draw.line( surface=screen_surface, color=white, start_pos=pivot, \
                    end_pos=(x0 + m_scale * length * sin( theta ), \
                    y0 + m_scale * length * cos( theta )), width=rod_width )

    pygame.draw.circle( surface=screen_surface, color=bob_color, \
                        center=(x0 + m_scale * length * sin( theta ), \
                        y0 + m_scale * length * cos( theta )), \
                        radius=kg_scale * m )

    pygame.display.update()

pygame.quit()
