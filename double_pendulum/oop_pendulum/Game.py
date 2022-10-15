
import pygame
from os import environ

from Constants import WINDOW_SIZE, WINDOW_TITLE, FPS, DULL_PINK
from Pendulum import Pendulum

class Game( object ):

    def __init__( self ):
        self._running = True  # game loop variable
        self._display_screen = None  # main display screen

        self._SIZE = self._WIDTH, self._HEIGHT = WINDOW_SIZE  # display screen dimensions
        self._TITLE = WINDOW_TITLE
        self._FPS = FPS

        self._clock = None
        self._deltaT = 0

        self.pendulum0 = None  # test pendulum
        self.pendulum1 = None  # test pendulum

    def _init( self ):
        """
        initialises and creates the pygame and other Game objects
        """
        success = True

        pygame.init()  # initialising the subsystems of pygame

        environ[ "SDL_VIDEO_CENTERED" ] = '1'  # centering the window?

        self._display_screen = pygame.display.set_mode( self._SIZE )  # creating the display screen
        if( self._display_screen == None ):
            success = False
            print( 'Pygame error: Failed to create display screen' )
        else:
            pygame.display.set_caption( self._TITLE )  # updating the title

            pendulum0 = Pendulum( 1, 0, 0, pivot=( self._WIDTH // 2, self._HEIGHT // 2 ), LENGTH=2, MASS=5 )
            pendulum1 = Pendulum( 2, 0, 0, pivot=( self._WIDTH // 2, self._HEIGHT // 2 ), LENGTH=2, MASS=5 )

            self._double = DoublePendulum( pendulum0, pendulum1 )

            self._clock = pygame.time.Clock()  # initialising the clock

        return success

    def _loadMedia( self, path ):
        success = True

        return success

    def _events( self ):
        # the event loop
        for event in pygame.event.get():

            match( event.type ):
                case( pygame.QUIT ):
                    self._running = False
                    break

    def _update( self ):
        self._double.update( self._deltaT )

    def _render( self ):
        self._display_screen.fill( DULL_PINK )
        self.double.render( self._display_screen )

        pygame.display.update()

    def _cleanup( self ):
        pygame.quit()

    def execute( self ):

        if( not( self._init() ) ):
            print( 'Failed to initialise inside execute.' )
        else:
            while( self._running ):
                self._deltaT = self._clock.tick( self._FPS ) / 1000

                self._events()
                self._update()
                self._render()

        self._cleanup()

        print( 'Exited a Game instance!' )

