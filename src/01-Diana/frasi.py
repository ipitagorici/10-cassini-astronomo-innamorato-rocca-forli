from manim import *
from PIL import Image

BACKGROUND_IMG = ImageMobject("src/assets/sfondoSpazio.jpg")
BACKGROUND_IMG.set_resampling_algorithm(Image.Resampling.BICUBIC)
BACKGROUND_IMG.scale_to_fit_width(config.frame_width)
BACKGROUND_IMG.set_opacity(.4)

RESCALING_OFFSET = 1.5

class Beltade(Scene):
    def construct(self):
        frase = Tex("che cercavano […] il bene, la sapienza,\\\\la beltade",
                    color=YELLOW).scale_to_fit_width(config.frame_width - RESCALING_OFFSET)
        
        self.add(BACKGROUND_IMG)
                                          
        self.play(Write(frase))
        
class Cicada(Scene):
    def construct(self):
        frase = Tex("CICADA:\\\\"+
                    "\"Onde procede, o Tansillo,\\\\"+
                    "che l'animo in tal progresso s'appaga del suo tormento?\\\\"+
                    "Onde procede quel sprone ch'il stimola sempre\\\\oltre quel che possiede?\"",
                    color=YELLOW).scale_to_fit_width(config.frame_width - RESCALING_OFFSET)
        
        self.add(BACKGROUND_IMG)
        
        self.play(Write(frase))
