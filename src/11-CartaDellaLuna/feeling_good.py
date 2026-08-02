from manim import Tex, Write
from manim.animation.fading import FadeOut
from manim.mobject.types.vectorized_mobject import VGroup
from manim.scene.scene import Scene
from manim.utils.color.manim_colors import WHITE, YELLOW


class FeelingGood(Scene):
    def construct(self) -> None:
        FONT_SIZE_ORIGINAL_TEXT = 85 
        FONT_SIZE_TRANSLATED_TEXT = 60

        ORIGINAL_TEXT_CLR = YELLOW 
        TRANSLATED_TEXT_CLR = WHITE
        
        ELEMENTS_DISTANCE = 1.5

        phrases = VGroup(
            VGroup(
                Tex("Stars when you shine,\\\ you know how I feel", font_size=FONT_SIZE_ORIGINAL_TEXT, color=ORIGINAL_TEXT_CLR),
                Tex("Stelle quando brillate,\\\ sapete come mi sento", font_size=FONT_SIZE_TRANSLATED_TEXT, color=TRANSLATED_TEXT_CLR)
            ).arrange_in_grid(rows=2, buff=ELEMENTS_DISTANCE),
            VGroup(
                Tex("And this old world,\\\ is a new world", font_size=FONT_SIZE_ORIGINAL_TEXT, color=ORIGINAL_TEXT_CLR),
                Tex("E questo vecchio mondo,\\\ è un nuovo mondo", font_size=FONT_SIZE_TRANSLATED_TEXT, color=TRANSLATED_TEXT_CLR)
            ).arrange_in_grid(rows=2, buff=ELEMENTS_DISTANCE),
            VGroup(
                Tex(r"Oh, freedom is mine.\\And I know how I feel", font_size=FONT_SIZE_ORIGINAL_TEXT, color=ORIGINAL_TEXT_CLR),
                Tex(r"La libertà è mia.\\E so come mi sento", font_size=FONT_SIZE_TRANSLATED_TEXT, color=TRANSLATED_TEXT_CLR)
            ).arrange_in_grid(rows=2, buff=ELEMENTS_DISTANCE),
            VGroup(
                Tex(r"It's a new \textbf{dawn}\\It's a new \textbf{day}\\It's a new \textbf{life}", font_size=FONT_SIZE_ORIGINAL_TEXT, color=ORIGINAL_TEXT_CLR),
                Tex(r"È una nuova alba\\È un nuovo giorno\\È una nuova vita", font_size=FONT_SIZE_TRANSLATED_TEXT, color=TRANSLATED_TEXT_CLR)
            ).arrange_in_grid(cols=2, buff=ELEMENTS_DISTANCE - .5),
            VGroup(
                Tex(r"And I'm feeling...\\\textbf{good}", font_size=FONT_SIZE_ORIGINAL_TEXT, color=ORIGINAL_TEXT_CLR),
                Tex(r"E mi sento...\\\textbf{bene}", font_size=FONT_SIZE_TRANSLATED_TEXT, color=TRANSLATED_TEXT_CLR)
            ).arrange_in_grid(rows=2, buff=ELEMENTS_DISTANCE),
        )

        for (i, p) in enumerate(phrases):
            if i != 0:
                self.play(FadeOut(phrases[i-1]))
            
            self.next_section(f"verso {i}")
            self.play(Write(p))


        self.wait(2)