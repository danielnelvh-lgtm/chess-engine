"""Pygame window that draws a Board. Run: python gui.py"""
import pygame

from board import Board

SQ = 80                      # square size in pixels
SIZE = SQ * 8
LIGHT = (240, 217, 181)
DARK = (181, 136, 99)

# Unicode chess glyphs: the filled set for both colours, tinted by colour
GLYPHS = {1: "♟", 2: "♞", 3: "♝", 4: "♜", 5: "♛", 6: "♚"}


def load_font():
    # Needs a font that has chess glyphs - DejaVu Sans does (pacman -S ttf-dejavu)
    path = pygame.font.match_font("dejavusans")
    return pygame.font.Font(path, int(SQ * 0.8))


def draw_board(screen):
    for r in range(8):
        for c in range(8):
            colour = LIGHT if (r + c) % 2 == 0 else DARK
            pygame.draw.rect(screen, colour, (c * SQ, r * SQ, SQ, SQ))


def draw_pieces(screen, board, font):
    for r in range(8):
        for c in range(8):
            p = board.piece_at(r, c)
            if p == 0:
                continue
            glyph = GLYPHS[abs(p)]
            fill = (255, 255, 255) if p > 0 else (20, 20, 20)
            centre = (c * SQ + SQ // 2, r * SQ + SQ // 2)
            # draw a dark outline first so white pieces show on light squares
            outline = font.render(glyph, True, (0, 0, 0))
            for dx, dy in ((-2, 0), (2, 0), (0, -2), (0, 2)):
                screen.blit(outline, outline.get_rect(center=(centre[0] + dx, centre[1] + dy)))
            text = font.render(glyph, True, fill)
            screen.blit(text, text.get_rect(center=centre))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SIZE, SIZE))
    pygame.display.set_caption("Chess")
    font = load_font()
    board = Board()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_board(screen)
        draw_pieces(screen, board, font)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()