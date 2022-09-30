import sys
import pygame as pg
import pygame_gui as pg_gui
from pygame.locals import QUIT
from automata import Automata

WIDTH = 700
HEIGHT = 400
FPS = 60

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY1 = (68,68,68)
GRAY2 = (38,38,38)
LBLUE = (95,203,255)
RPINK = (254,44,84)
GREEN = (0,255,128)

class Game_Screen:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.manager = pg_gui.UIManager((WIDTH, HEIGHT), 'data/theme.json')
        pg.display.set_caption("Automata incendio forestal")

        self.automata = Automata()
        self.setup_gui()

        self.delay = 0
        self.is_running = False

    def run(self):
        clock = pg.time.Clock()
        run = True
        while run:
            self.screen.fill(GRAY1)
            time_delta = clock.tick(60)/1000.0
            for event in pg.event.get():
                if event.type == QUIT:
                    run = False

                if event.type == pg_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.play_button:
                        if self.is_running:
                            self.is_running = False 
                            self.play_button.set_text('Play')
                        else:
                            self.is_running = True
                            self.play_button.set_text('Stop')
                    if event.ui_element == self.clear_button: self.automata.clear_grid()
                    if event.ui_element == self.random_button: self.automata.noise_grid()
                    if event.ui_element == self.step_button: self.automata.update_generation()
                if event.type == pg_gui.UI_HORIZONTAL_SLIDER_MOVED:
                    if event.ui_element == self.delay_slider:  self.delay = int(event.value)
                if event.type == pg_gui.UI_DROP_DOWN_MENU_CHANGED:
                    if event.ui_element == self.size_dropdown: 
                        self.automata.setSize(self.size_dropdown.selected_option)
                
                self.manager.process_events(event)
            self.manager.update(time_delta)

            self.setup_interfaze()
            if self.is_running:
                self.automata.update_generation()

            self.manager.draw_ui(self.screen) # Dibuja elementos de la gui
            pg.display.flip()
            # clock.tick(FPS) # De moment
            pg.time.delay(self.delay)

        pg.quit()

    def setup_gui(self):
        #Botones
        self.play_button = pg_gui.elements.UIButton(
            relative_rect=pg.Rect((425, 350), (250, 35)),
            text='Play', manager=self.manager)
        self.random_button = pg_gui.elements.UIButton(
            relative_rect=pg.Rect((425, 315), (100, 35)),
            text='Randomise', manager=self.manager)
        self.step_button = pg_gui.elements.UIButton(
            relative_rect=pg.Rect((530, 315), (70, 35)),
            text='+Step', manager=self.manager)
        self.clear_button = pg_gui.elements.UIButton(
            relative_rect=pg.Rect((605, 315), (70, 35)),
            text='Clear', manager=self.manager)
        
        #Grid size drow menu
        self.size_dropdown = pg_gui.elements.UIDropDownMenu(
            self.automata.options_size, self.automata.options_size[1], 
            relative_rect=pg.Rect(515, 225, 160, 35),
            manager=self.manager, expansion_height_limit=100)

        # Speed scroll bar
        self.delay_slider = pg_gui.elements.UIHorizontalSlider(
            relative_rect=pg.Rect(515, 270, 160, 25), start_value=0.0, 
            value_range=(0.0, 85.0), manager=self.manager)

        self.manager.add_font_paths("Montserrat",
                            "data/fonts/Montserrat-Regular.ttf",
                            "data/fonts/Montserrat-Bold.ttf",
                            "data/fonts/Montserrat-Italic.ttf",
                            "data/fonts/Montserrat-BoldItalic.ttf")
        self.manager.preload_fonts([
                            {'name': 'Montserrat', 'html_size': 4.5, 'style': 'bold'},
                            {'name': 'Montserrat', 'html_size': 4.5, 'style': 'regular'},
                            {'name': 'Montserrat', 'html_size': 2, 'style': 'regular'},
                            {'name': 'Montserrat', 'html_size': 2, 'style': 'italic'},
                            {'name': 'Montserrat', 'html_size': 6, 'style': 'bold'},
                            {'name': 'Montserrat', 'html_size': 6, 'style': 'regular'},
                            {'name': 'Montserrat', 'html_size': 6, 'style': 'bold_italic'},
                            {'name': 'Montserrat', 'html_size': 4, 'style': 'bold'},
                            {'name': 'Montserrat', 'html_size': 4, 'style': 'regular'},
                            {'name': 'Montserrat', 'html_size': 4, 'style': 'italic'}
        ])
        self.hmtl_text_1 = pg_gui.elements.UITextBox(
            '<font face=Montserrat color=regular_text><font color=#E784A2 size=4.5>'
            '<br><b><u><effect id=spin_me>Rock Paper Scissors</effect></u><br><br>'
            '<font color=#FFFFFF size=4.5>'
            'Automata celular aplicado al juego de piedra papel o tijera<br><br>'
            'Este programa utiliza la </font>'
            '<font color=#236845 size=4.5>'
            '<b><a href="https://es.wikipedia.org/wiki/Vecindad_de_Moore">vecindad de moore</a></b>'
            '</font><font color=#FFFFFF size=4.5>'
            ', El color de cada píxel se calcula jugando una partida virtual de piedra, '
            'papel o tijera de 9 jugadores. La celda actual se enfrenta a sus 8 vecinos '
            'inmediatos. Si el recuento de vecinos rivales es mayoria en entonces la celda actual se '
            'convierte en la ganadora. Por ejemplo, si la celda '
            'actual es tijera, y el recuento de rocas es mayoria (3 o mas ya que son 8 rivales), y hay '
            '4 rocas que la rodean, entonces se '
            'convierte en una roca.'
            '<br><br></font></font>',
            pg.Rect(425, 20, 250, 180),
            manager=self.manager,
            object_id='#text_box_1')
        
        #Subtitulos
        font1 = pg.font.SysFont('data/fonts/Montserrat-Regular.ttf', 24)
        self.text2 = font1.render('Map size:', True, GRAY2)
        self.text2Rect = self.text2.get_rect()
        self.text2Rect.center = (465, 243)
        self.text3 = font1.render('Speed:', True, GRAY2)
        self.text3Rect = self.text2.get_rect()
        self.text3Rect.center = (465, 283)

    def setup_interfaze(self):
        self.draw_grid(self.automata.grid)
        pg.draw.rect(self.screen, GRAY2, (400, 0, 300, 400), 0, 0)
        pg.draw.rect(self.screen, WHITE, (410, 10, 280, 380), 0, 10)
        pg.draw.rect(self.screen, GRAY1, (425, 310, 250, 2), 0, 10) # separador
        pg.draw.rect(self.screen, GRAY1, (425, 210, 250, 2), 0, 10) # separador
        self.screen.blit(self.text2, self.text2Rect)
        self.screen.blit(self.text3, self.text3Rect)

    def draw_grid(self, grid):
        width, height = 400, 400
        ix, iy = 0, 0
        x, y = ix, iy
        sx = width / len(grid[0])
        sy = height / len(grid)
        for row in grid:
            for col in row:
                if col == 1: pg.draw.rect(self.screen, GREEN, (x, y, sx, sy), 0, 8)
                if col == 2: pg.draw.rect(self.screen, LBLUE, (x, y, sx, sy), 0, 8)
                if col == 3: pg.draw.rect(self.screen, RPINK, (x, y, sx, sy), 0, 8)
                x += sx
            x = ix
            y += sy 