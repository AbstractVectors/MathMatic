from manim import *


class DerivativeFormula(Scene):
    def construct(self):
        # Create a mathematical formula
        formula = MathTex("f'(x) =", "2x", color=WHITE, font_size=60)

        # Center the formula on the screen
        formula.move_to(ORIGIN)

        # Display the formula
        self.play(Write(formula))
        self.wait(2)
