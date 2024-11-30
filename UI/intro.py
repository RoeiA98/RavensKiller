import pygame  # type: ignore
from UI.GameScenes import GameScenes

def name_input_validate(name):
        if not name or len(name) > 10:
            return False
        return all(char.isalpha() or char.isdigit() for char in name)

class GameIntro(GameScenes):
    def __init__(self):
        super().__init__()
        self.invalid_name = False
        self.user_display_font = pygame.font.SysFont("Verdana", 25)
    
    def display_intro(self):
        pygame.display.set_caption("Welcome")
        pygame.display.update()
        
        welcome_text = self.game_font.render(
            "Welcome to RavensKiller",
            True,
            'Black').convert_alpha()
        welcome_text_rect = welcome_text.get_rect(center=(500, 100))

        instructions_text = self.game_font.render(
            "Use arrows to move around, SPACE to shoot and ESC to pause",
            True,
            'Black').convert_alpha()
        instructions_text_rect = instructions_text.get_rect(center=(500, 150))
        
        name_input_text = self.game_font.render(
            "Enter name: ____________",
            True,
            'Black').convert_alpha()
        name_input_rect = name_input_text.get_rect(center=(500, 225))
        input_surface = self.game_font.render(self.name_input, True, 'Black')
        
        invalid_name_text = self.game_font.render("invalid name", True, 'Red')

        start_game_text = self.game_font.render(
            "Start Game",
            True,
            'Black').convert_alpha()
        start_game_text_rect = start_game_text.get_rect(center=self.start_button_rect.center)

        quit_game_text = self.game_font.render(
            "Quit Game",
            True,
            'Black').convert_alpha()
        quit_game_text_rect = quit_game_text.get_rect(center=self.quit_button_rect.center)

        self.game_screen.blit(self.image, (0, 0))
        self.game_screen.blit(welcome_text, welcome_text_rect)
        self.game_screen.blit(instructions_text, instructions_text_rect)
        pygame.draw.rect(self.game_screen, 'Grey', self.start_button_rect)
        pygame.draw.rect(self.game_screen, 'Grey', self.quit_button_rect)
        self.game_screen.blit(start_game_text, start_game_text_rect)
        self.game_screen.blit(quit_game_text, quit_game_text_rect)
        self.game_screen.blit(name_input_text, name_input_rect)
        self.game_screen.blit(input_surface, (455, 195))
        
        if self.invalid_name:
            self.game_screen.blit(invalid_name_text, (715, 195))
            
    def display_user_name(self):
        name = self.user_display_font.render(f"Player: {self.name_input}", True, "White").convert_alpha()
        self.game_screen.blit(name, (20, 515))
    
    def handle_game_intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.name_input = self.name_input[:-1]
                elif len(self.name_input) < 10 and (event.unicode.isalpha() or event.unicode.isdigit()):
                    self.name_input += event.unicode
                    
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # mouse left click
                if self.start_button_rect.collidepoint(event.pos): # Start Game
                    if name_input_validate(self.name_input):
                        pygame.time.delay(100)
                        return True
                    else:
                        self.invalid_name = True
                if self.quit_button_rect.collidepoint(event.pos):  # Quit Game
                    pygame.quit()
                    exit()