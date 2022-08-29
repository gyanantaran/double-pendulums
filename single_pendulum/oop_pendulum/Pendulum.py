
import pygame
from math import pi, sin, cos


class Pendulum( object ):

    def __init__( self, mass: float = 1, length: float = 1, theta: float = pi - 0.1, theta_dash: float = 0, theta_double_dash: float = 0, bob_color: tuple = (250, 0, 120), pivot: tuple = (0, 0) ):
        #state variables
        self._mass = mass                           # mass of bob
        self._length = length                       # length of the rod
        self._theta = theta                         # angular acceleration
        self._theta_dash = theta_dash               # angular velocity
        self._theta_double_dash = theta_double_dash # angular acceleration
        self._meter_scale = 100                     # one meter equals these many pixels
        self._mass_scale = 10                       # one kg bob has this pixel radius

        # colors
        self._bob_color = bob_color
        self._rod_color = (250, 250, 250)

        # others
        self._pivot = pivot
        self._last_ten_lst = []
        self._last_x = 20
        self._dt = 0.000001
        self._gradient = 250 / self._last_x
        self._rod_width = 2

    def get_location( self ):
        x = self._pivot[0] + self._meter_scale * self._length * sin( self._theta )
        y = self._pivot[1] + self._meter_scale * self._length * cos( self._theta )

        return (x, y)

    def update_state( self, gravity, fps ):
        # on loop calculations
        time = 1 / fps
        for _ in range( 0, int( time / self._dt ) ):
            # in this clock cycle updates the position, int( time / dt ) times
            self._theta_double_dash = self.get_theta_double_dash( gravity )
            self._theta_dash += self._theta_double_dash * self._dt
            self._theta += self._theta_dash * self._dt

            if len( self._last_ten_lst ) > self._last_x - 1:
                self._last_ten_lst = self._last_ten_lst[1:]

        self._last_ten_lst.append( self.get_location() )

    def render( self, screen ):
        # last ten locations
        for i in range( 0, len( self._last_ten_lst ) - 1 ):
            pygame.draw.line( screen, (250 - self._gradient * i, 250 - self._gradient * i, 250 - self._gradient * i, 0.5 + (1 / (self._gradient * i + 1))), self._last_ten_lst[i], self._last_ten_lst[i + 1], width=1 )
            # pygame.draw.circle( screen, self._rod_color, self._last_ten_lst[i], 1 )

        # the rod
        pygame.draw.line( screen, self._rod_color, self._pivot, self.get_location(), self._rod_width )

        # the bob
        pygame.draw.circle( screen, self._bob_color, self.get_location(), self._mass_scale * self._mass )

    def get_theta_double_dash( self, gravity ):
        return -1 * (gravity / self._length) * sin( self._theta )  # uniform gravity without damping

if __name__ == "__main__":
    pendulum = Pendulum()

