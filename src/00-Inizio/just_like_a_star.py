from manim.animation.creation import Write
from manim.animation.fading import FadeIn
from manim.constants import DOWN, UP
from manim.mobject.text.tex_mobject import Tex
from manim.scene.scene import Scene
from manim.utils.color.manim_colors import RED, YELLOW

class JustLikeAStar(Scene):
    def construct(self) -> None:
        frase = Tex("Just like a star across my sky", font_size=90, color=YELLOW)\
            .to_edge(UP, buff=2)
        frase_ita = Tex(r"Proprio come una stella\\attraverso il mio cielo", font_size=70)\
            .to_edge(DOWN, buff=2)

        self.play(Write(frase))
        self.play(FadeIn(frase_ita))


        self.wait(2)