from manim import *

class Anagram(Scene):
    def construct(self):
        OFFSET = 3

        partenza = Tex(r"\textsc{Lothario Sarsi Sigensano}")
        destinazione = Tex(r"\textsc{Horatio Grassi Salonensi}")

        partenza.scale_to_fit_width(config.frame_width - OFFSET)
        destinazione.scale_to_fit_width(config.frame_width - OFFSET)

        self.play(Write(partenza))
        self.wait(1)

        self.play(
            TransformMatchingShapes(
                partenza,
                destinazione,
                path_arc=PI/2
            ),
            run_time=3
        )
