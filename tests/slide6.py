from manim import *


class SummationNotation(Scene):
    def construct(self):
        # Create summation notation
        summation = MathTex(r"\sum_{i=1}^{n} i^2 = 1^2 + 2^2 + \ldots + n^2", color=WHITE, font_size=48)

        # Center the notation on the screen
        summation.move_to(ORIGIN)

        # Display the notation
        self.play(Write(summation))
        self.wait(2)
