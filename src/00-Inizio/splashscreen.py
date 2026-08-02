from random import choice, randint, random

from manim import *


class Splashscreen(Scene):
    def construct(self):
        
        max_width = config.frame_width
        max_height = config.frame_height
        stars_colors = [ YELLOW, YELLOW_A, YELLOW_B, YELLOW_C, YELLOW_D ]
        comets = VGroup()
        comets_target = VGroup()

        for _ in range(15):
            random_x = randint(-int(max_width/2)*2, -int(max_width/2))
            random_y = randint(int(max_height), int(max_height) * 2)
            random_length = randint(1, 6)

            comet = Line(
                start=(random_x, random_y, 0),
                end=(random_x + random_length, random_y - random_length, 0))
            comet.set_opacity(.5)

            comet_target = Line(
                start=(random_x, random_y, 0),
                end=(random_x + (random_length*100), random_y - (random_length*100), 0))
            comet_target.set_opacity(0)

            comets.add(comet)
            comets_target.add(comet_target)

        stars = VGroup()
        for _ in range(80):
            random_x = (random() * max_width) - (max_width * .5)
            random_y = (random() * max_height) - (max_height * .5)

            SCALE_FACTOR = .3
            star = Star(
                inner_radius=(random() * DEFAULT_DOT_RADIUS) * SCALE_FACTOR,
                outer_radius=(random() * DEFAULT_DOT_RADIUS) * SCALE_FACTOR
            )
            star.move_to((random_x, random_y, 0))
            star.set_color(choice(stars_colors))
            star.set_opacity(randint(20, 50) * .01)
            stars.add(star)

        for star in stars:
            self.play(FadeIn(star))

        # TEXT AND IMAGE HERE
        with register_font("src/assets/ablation/Ablation_PersonalUse.otf"):
            title = Text("CASSINI\nASTRONOMO\nINNAMORATO", font="Ablation").set_z_index(3)
            subtitle = Text("SPETTACOLO\nSCIENTIFICO\nPOETICO\nMUSICALE", font="Ablation").scale(.7).set_z_index(3)

            VGroup(title, subtitle)\
                .arrange_in_grid(rows=2, buff=LARGE_BUFF, cell_alignment=LEFT)\
                .to_edge(LEFT, buff=LARGE_BUFF)\
                
            self.play(Write(title))
            self.wait()
            self.play(Write(subtitle))

        cassini = ImageMobject("src/assets/cassini-cartoon-removebg.png")\
            .scale(2)\
            .to_corner(DR, buff=-.5)\
            .set_z_index(3)
        self.play(FadeIn(cassini), run_time=5)
        
        idx = 0
        for comet in comets:
            self.play(FadeIn(comet))
            self.play(MoveAlongPath(comet, comets_target[idx]), run_time=2)
            self.play(FadeOut(comet))

            idx += 1

        self.wait(2)
        self.play(FadeOut(*self.mobjects))
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
        
