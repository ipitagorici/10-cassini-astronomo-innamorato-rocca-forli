from manim import *
from PIL import Image

BACKGROUND_IMG = ImageMobject("src/assets/sfondoSpazio.jpg")
BACKGROUND_IMG\
    .set_resampling_algorithm(Image.Resampling.BICUBIC)\
    .scale_to_fit_width(config.frame_width)\
    .set_opacity(.4)

class StellaRossa(Scene):
    def construct(self):
        TEXT_FSIZE = 60
        frase = VGroup()
        frase.add(Tex("Come la stella rossa", font_size=TEXT_FSIZE, color=YELLOW))\
            .add(Tex("che dalla sua chioma fiammeggiante", font_size=TEXT_FSIZE, color=YELLOW))\
            .add(Tex("fa calare malattie, pestilenza e guerra", font_size=TEXT_FSIZE, color=YELLOW))
        frase.arrange_in_grid(rows=3, cell_alignment=RIGHT, buff=MED_SMALL_BUFF)\
            .to_corner(UR)\
            .shift(DOWN * .25 + LEFT * .3)
        autore = Tex(r"(Omero)", font_size=TEXT_FSIZE, color=YELLOW).next_to(frase, DR).align_to(frase, RIGHT)
        
        elmo = ImageMobject("src/assets/elmoPiumaRossa.png")\
            .scale(1.8).to_corner(DL, buff=MED_SMALL_BUFF).shift(RIGHT * .15)
        
        self.add(BACKGROUND_IMG)
        
        self.play(
            FadeIn(elmo),
            Write(frase), 
        )
        self.play(Write(autore))

class Shakespeare(Scene):
    def construct(self):
        fraseEnglish = Tex("When beggars die, there are no comets seen;\\\\the heavens themselves blaze forth the death of princes",
                    color=YELLOW).scale_to_fit_width(config.frame_width - 1)
        fraseItalian = Tex("Quando muoiono i pezzenti, non si vedono comete;\\\\i cieli stessi fiammeggiano annunziando la morte dei principi",
                    color=WHITE).scale_to_fit_width(config.frame_width - 2)
        author = Tex("(W. Shakespeare, Giulio Cesare)", color=YELLOW)
        
        VGroup(fraseEnglish, fraseItalian, author)\
            .arrange_in_grid(rows=3, buff=LARGE_BUFF)\
            .center()
        author.align_to(fraseItalian, RIGHT)

        self.add(BACKGROUND_IMG)
        
        self.play(Write(fraseEnglish), Write(fraseItalian))
        self.play(Write(author))
        
class Vendetta(Scene):
    def construct(self):
        frase = Tex("Dal movimento de l’humor collerico\\\\gli animi de gli huomini sono incitati alla vendetta",
                    color=YELLOW).scale_to_fit_width(config.frame_width - 1.5)
        
        autore = Tex('(Tomaso Tomai - "Historia di Ravenna", 1580)', font_size=45, color=YELLOW)
        VGroup(frase, autore).arrange_in_grid(rows=2, buff=MED_LARGE_BUFF).center()
        autore.align_to(frase, RIGHT)
        self.add(BACKGROUND_IMG)
        
        self.play(Write(frase), Write(autore))
        
class Rammarichi(Scene):
    def construct(self):
        frase = Tex("Gli huomini fuggivano per i boschi,\\\\lasciando le case loro,\\\\" +
                    "sì come usciti fuori di senno,\\\\non si trovava chi avesse cura de gli animali,\\\\" +
                    "né chi lavorasse le terre, solo morti si vedevano,\\\\" +
                    "solo ramarichi, stridi e pianti s’udivano",
                    font_size=60,
                    color=YELLOW)
        autore = Tex('(Tomaso Tomai - "Historia di Ravenna", 1580)', font_size=45, color=YELLOW)
        VGroup(frase, autore).arrange_in_grid(rows=2, buff=MED_LARGE_BUFF).center()
        autore.align_to(frase, RIGHT)
        self.add(BACKGROUND_IMG)
        
        self.play(Write(frase), Write(autore))
        
class Paternoster(Scene):
    def construct(self):
        frase = Tex("Venne un certo liquore nell’aere come fuoco,\\\\" +
                    "e parea che la terra ardesse,\\\\e stette così per lo spazio del dire di due Paternoster;\\\\" +
                    "dietro a questo venne un tempo\\\\molto scuro e tenebroso con un tuono grandissimo,\\\\" +
                    "il quale durò fermamente\\\\per il dire di tre Paternoster",
                    color=YELLOW).scale_to_fit_width(config.frame_width - 1)
        autore = Tex('(Frate Benedetto Della Pugliola)', font_size=45, color=YELLOW)
        VGroup(frase, autore).arrange_in_grid(rows=2, buff=MED_LARGE_BUFF).center()
        autore.align_to(frase, RIGHT)
        self.add(BACKGROUND_IMG)
        
        self.play(Write(frase), Write(autore))
        
class StragiAllaCristianita(Scene):
    def construct(self):
        frase = Tex("Gran stragi alla Cristianità,\\\\onde Papa Callisto III ordinò,\\\\"+
                    "ch’in tutte le città nel mezzo giorni\\\\si suonassero le campane,\\\\"+
                    "acciò in quel tempo i fedeli\\\\facessero orazioni per placare l’ira del cielo",
                    font_size=65,
                    color=YELLOW)

        self.add(BACKGROUND_IMG)

        self.play(Write(frase))
