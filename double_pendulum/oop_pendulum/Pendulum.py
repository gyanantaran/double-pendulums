"""
Author: Vishal Paudel
"""

import pygame
from math import pi, sin, cos

from Constants import PIXELS_PER_METER, PIXELS_PER_KG, SMOOTH_RED, WHITE, ROD_WIDTH, WINDOW_SIZE, GRAVITY, RESOLUTION_DURATION

class Pendulum( object ):
    def __init__( self, theta: float, theta_dash: float, theta_doubleDash: float, pivot: tuple[int], LENGTH: float, MASS: float ):
        # The pivot, relative to the Pendulum surface (see below)
        self._pivot = pivot

        # length in meters
        self._LENGTH = LENGTH

        # The physics parameters, rad is the angle related unit
        self._theta = theta
        self._theta_dash = theta_dash
        self._theta_doubleDash = theta_doubleDash

        self._MASS = MASS  # in kg

        self._surface = pygame.Surface( WINDOW_SIZE ).convert_alpha()  # HARCODE ALERT

        # Colors
        self._BOB_COLOR = SMOOTH_RED
        self._ROD_COLOR = WHITE

    def update( self, deltaT ):
        detail_count = int( deltaT / RESOLUTION_DURATION )
        if( detail_count == 0 ):
            print( 'The number of intermediate detail fills was 0! reduce RESOLUTION_DURATION!' )
        else:
            for t in range( detail_count ):
                self._update_theta_doubleDash()
                self._update_theta_dash()
                self._update_theta()

    def render( self, screen ):
        self._surface.fill( ( 0, 0, 0, 0 ) )
        self._draw_pendulum()

        screen.blit( self._surface, ( 0, 0 ) )

    def update_pivot( self, x, y ):
        self._pivot = ( x, y )

    def _update_theta( self ):
        self._theta += self._theta_dash * RESOLUTION_DURATION

    def _update_theta_dash( self ):
        self._theta_dash += self._theta_doubleDash * RESOLUTION_DURATION

    def _update_theta_doubleDash( self ):
        self._theta_doubleDash = -1 * ( GRAVITY / self._LENGTH ) * sin( self._theta )

    def _draw_pendulum( self ):
        pos = self._get_pos()
        pygame.draw.line( self._surface, self._ROD_COLOR, self._pivot, pos, width=ROD_WIDTH )
        pygame.draw.circle( self._surface, self._BOB_COLOR, pos, self._MASS * PIXELS_PER_KG )

    def _get_pos( self ):
        x = self._pivot[ 0 ] + self._LENGTH * sin( self._theta ) * PIXELS_PER_METER
        y = self._pivot[ 1 ] + self._LENGTH * cos( self._theta ) * PIXELS_PER_METER
        return x, y
