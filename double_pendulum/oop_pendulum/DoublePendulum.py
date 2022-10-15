"""
Author: Vishal Paudel

note: Can we you use this file structure with another Pendulum object to create 3-pendulums??
Equations??
"""

import pygame

from Constants import WINDOW_SIZE
from Pendulum import Pendulum

class DoublePendulum( object, Pendulum ):
    """
    Should pass two Pendulum objects?, this will modify their physics accordingly??

    Currently creates two pendulums on same surface
    """
    def __init__( self, pendulum0: Pendulum, pendulum1: Pendulum ):
        self.pendulum0 = pendulum0
        self.pendulum1 = pendulum1

        self.pendulum0._update_theta_doubleDash = self.update

        # HARDCODE ALERT
        self._surface = pygame.Surface( WINDOW_SIZE )

    def update( self, deltaT ):

        pos0 = self.pendulum0._get_pos()
        self._pendulum1.update_pivot( pos0[ 0 ], pos[ 1 ] )

    def render( self, screen ):

        self._suface.fill(  )
        pygame.draw.line
