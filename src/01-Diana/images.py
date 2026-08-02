from manim import *
from PIL import Image

BACKGROUND_IMG = ImageMobject("src/assets/sfondoSpazio.jpg")
BACKGROUND_IMG.set_resampling_algorithm(Image.Resampling.BICUBIC)
BACKGROUND_IMG.scale_to_fit_width(config.frame_width)
BACKGROUND_IMG.set_opacity(.4)

class DianaGuercino(Scene):
    def construct(self):
        diana_guercino = ImageMobject("src/assets/Diana-Cacciatrice-del-Guercino-1658.jpg")
        
        self.add(BACKGROUND_IMG)
        didascalia = VGroup(
            Tex("Diana Cacciatrice", color=YELLOW, font_size=80),
            Tex("Guercino, 1658", font_size=70),
        ).arrange_in_grid(rows=2, cell_alignment=LEFT)
        self.play(FadeIn(diana_guercino))
        self.play(diana_guercino.animate.shift(LEFT * 3.5))
        didascalia.next_to(diana_guercino, RIGHT, MED_LARGE_BUFF)
        self.play(Write(didascalia))
        self.wait(2)

class DianaCaserta(Scene):
    def construct(self):
        diana_caserta = ImageMobject("src/assets/Reggia-di-Caserta-Diana.jpg")
        diana_caserta.scale_to_fit_height(config.frame_height - 1)

        frase = [
            r'"rarissimi [ai quali]',
            r'sia dato dal destino',
            r'di posser contemplar',
            r'la Diana ignuda"'
        ]

        didascalia = VGroup(
            [ Tex(pezzo, color=YELLOW, font_size=70) for pezzo in frase ]
        )
        didascalia.arrange_in_grid(rows=len(frase), cell_alignment=LEFT)
        
        self.add(BACKGROUND_IMG)
                                          
        self.play(FadeIn(diana_caserta))
        self.play(diana_caserta.animate.shift(LEFT * 3.5))
        didascalia.next_to(diana_caserta, RIGHT, MED_LARGE_BUFF)
        self.play(Write(didascalia))
        self.wait(2)

class AtteoneCani(Scene):
    def construct(self):
        atteone_cani = ImageMobject("src/assets/Atteone-Cani.jpg")                          
        atteone_cani.scale(0.45)
        
        self.add(BACKGROUND_IMG)
        
        self.play(FadeIn(atteone_cani))
        self.wait(2)