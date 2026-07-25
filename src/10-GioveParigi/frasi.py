from manim import *
from PIL import Image

class Sire(Scene):
    def construct(self):
        fraseFrancese = Tex("\"Sire, ce baragouineur \\\ là ne scait se qu’il dit\"\\\\",
                    font_size=90,
                    color=YELLOW)
        fraseItaliano = Tex(r"\textit{Sire, questo fanfarone \\\ non sa quello che dice}",
                    font_size=65,
                    color=YELLOW)
        VGroup(
            fraseFrancese,
            fraseItaliano
        ).arrange_in_grid(rows=2, buff=1.5)

        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.set_opacity(.4)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
        
        self.play(Write(fraseFrancese), Write(fraseItaliano))