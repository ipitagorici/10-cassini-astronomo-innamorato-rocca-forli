from manim import RIGHT, Tex, Write
from manim.animation.fading import FadeOut
from manim.constants import DOWN, LEFT, UP
from manim.mobject.types.vectorized_mobject import VGroup
from manim.scene.scene import Scene
from manim.utils.color.manim_colors import RED


class FeelingGood(Scene):
    def construct(self) -> None:
        FONT_BIG = 75
        FONT_SMALL = 60
        
        phrases = VGroup(
            VGroup(
                Tex("Stars when you shine, you know how I feel", font_size=FONT_BIG-5, color=RED).to_edge(UP, buff=2),
                Tex("Stelle quando brilli, sai come mi sento", font_size=FONT_SMALL).to_edge(DOWN, buff=2)
            ),
            VGroup(
                Tex("And this new world, is a new world", font_size=FONT_BIG, color=RED).to_edge(UP, buff=2),
                Tex("E questo vecchio mondo, è un nuovo mondo", font_size=FONT_SMALL).to_edge(DOWN, buff=2)
            ),
            VGroup(
                Tex(r"Oh, freedom is mine.\\And I know how I feel", font_size=FONT_BIG, color=RED).to_edge(UP, buff=2),
                Tex(r"La libertà è mia.\\E sai come mi sento", font_size=FONT_SMALL).to_edge(DOWN, buff=2)
            ),
            VGroup(
                Tex(r"It's a new Dawn\\It's a new Day\\It's a new Life", font_size=FONT_BIG, color=RED).to_edge(LEFT),
                Tex(r"E' una nuova Alba\\E' un nuovo Giorno\\E' una nuova Vita", font_size=FONT_SMALL).to_edge(RIGHT)
            ),
            VGroup(
                Tex(r"And I'm feeling...\\good", font_size=FONT_BIG, color=RED).to_edge(UP, buff=2),
                Tex(r"E mi sento...\\bene", font_size=FONT_SMALL).to_edge(DOWN, buff=2)
            ),
        )

        for (i, p) in enumerate(phrases):
            if i != 0:
                self.play(FadeOut(phrases[i-1]))
            
            self.next_section(f"verso {i}")
            self.play(Write(p))


        self.wait(2)