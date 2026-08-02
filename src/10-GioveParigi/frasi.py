from manim import *
from PIL import Image

class Sire(Scene):
    def construct(self):
        fraseFrancese = Tex("\"Sire, ce baragouineur \\\ là ne scait se qu’il dit\"\\\\",
                    color=YELLOW).scale_to_fit_width(config.frame_width - 3)
        fraseItaliano = Tex(r"Sire, questo fanfarone \\\ non sa quello che dice", 
            color=WHITE).scale_to_fit_width(config.frame_width - 5)
        VGroup(
            fraseFrancese,
            fraseItaliano
        ).arrange_in_grid(rows=2, buff=LARGE_BUFF)

        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.set_opacity(.4)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
        
        self.play(Write(fraseFrancese), Write(fraseItaliano))