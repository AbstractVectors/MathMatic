from manim import *


class ExampleCalculation(Scene):
    def construct(self):
        # Create example summation and calculations
        example = MathTex(r"\sum_{i=1}^{5} i^2 =", "1^2 + 2^2 + 3^2 + 4^2 + 5^2", "=", "55", color=WHITE, font_size=48)
        example.arrange(DOWN, buff=0.5)

        # Center the equations on the screen
        example.move_to(ORIGIN)

        # Display the equations
        self.play(Write(example))
        self.wait(2)
