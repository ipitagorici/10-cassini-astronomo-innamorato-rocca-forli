from manim import *
import numpy as np

class Pitagorici(Scene):
    def construct(self):
        title_pitagorici = Title(r"\textsc{Un'iniziativa}")
        pitagorici_logo = ImageMobject("src/assets/pitagorici-aps-logo.png").scale(2)
        self.play(Write(title_pitagorici))
        self.play(FadeIn(pitagorici_logo))
        self.wait(5)
        self.play(FadeOut(pitagorici_logo), Unwrite(title_pitagorici))
        
        SPONSORS_IMGS_FOLDER = "src/assets/sponsors/"
        title_sponsor = Title(r"\textsc{Con il supporto di}")
        comitato_cassini = ImageMobject(SPONSORS_IMGS_FOLDER + "Logo_CN.png")\
            .scale(.3)
        comune_forli = Group(
            ImageMobject(SPONSORS_IMGS_FOLDER + "Logo-Forli.png"),
            ImageMobject(SPONSORS_IMGS_FOLDER + "Banda-Forli.png")
        ).arrange_in_grid(cols=2, buff=MED_LARGE_BUFF)\
            .scale(.17)
        incensi = Group(
            Tex(r"\textbf{\textsc{INCENSI}}"),
            Tex("strumenti musicali")
        )
        incensi[0].scale_to_fit_width(incensi[1].width)
        incensi.arrange_in_grid(rows=2, buff=SMALL_BUFF).scale(1.2)
        centro_usato = ImageMobject(SPONSORS_IMGS_FOLDER + "centro-usato.png").scale(.3)
        self.play(Write(title_sponsor)) 
        sponsor_logos = Group(comitato_cassini, comune_forli, centro_usato, incensi)
        for sponsor in sponsor_logos:
            sponsor.center()
            self.play(FadeIn(sponsor)); self.wait(2)
            self.play(FadeOut(sponsor)); self.wait()
        self.play(Unwrite(title_sponsor))
        self.wait()