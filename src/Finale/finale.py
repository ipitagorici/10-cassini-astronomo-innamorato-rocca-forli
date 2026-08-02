from manim import *
from PIL import Image

class Finale(Scene):
    def construct(self):
        fine = Tex(r"\textsc{fine}").scale_to_fit_width(config.frame_width - 4)
        self.play(Write(fine))
