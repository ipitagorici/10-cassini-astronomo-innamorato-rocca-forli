from manim import LEFT, RIGHT, FadeIn, ImageMobject, Tex, Scene, Write, config
from manim.constants import MED_LARGE_BUFF
from manim.mobject.types.vectorized_mobject import VGroup
from manim.utils.color import WHITE, YELLOW


class KaoruIkeya(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_opacity(.4)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
        
        kaoru_img = ImageMobject("src/assets/Kaoru-Ikeya.jpg")
        name = Tex("Kaoru Ikeya", color=YELLOW).scale(2)
        date = Tex("(1943 - presente)", color=WHITE).scale(1.25)
        metadata = VGroup(name, date).arrange_in_grid(rows=2, cell_alignment=LEFT)

        self.play(FadeIn(kaoru_img))
        self.play(kaoru_img.animate.shift(LEFT * 3))
        metadata.next_to(kaoru_img, RIGHT, MED_LARGE_BUFF)
        self.play(Write(metadata))