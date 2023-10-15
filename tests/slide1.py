from manim import *


class TitleSlide(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Calculus", font_size=72)
        subtitle = Text("Exploring the Tangent Line and Area Problems", font_size=36)

        # Positioning the title and subtitle
        title.move_to(2 * UP)
        subtitle.next_to(title, DOWN)

        # Adding elements to the scene
        self.play(Write(title))
        self.play(Write(subtitle))

        # Wait for a few seconds
        self.wait(2)

        # Fade out the title and subtitle
        self.play(FadeOut(title), FadeOut(subtitle))

