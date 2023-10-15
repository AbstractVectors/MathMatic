from manim import *


class SpecialSums(Scene):
    def construct(self):
        # Create special sums equations
        sums = MathTex(r"\sum_{i=1}^{n} i = \frac{n(n+1)}{2}", r"\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}", r"\sum_{i=1}^{n} i^3 = \left(\frac{n(n+1)}{2}\right)^2", color=WHITE, font_size=36)
        sums.arrange(DOWN, buff=0.5)

        # Center the equations on the screen
        sums.move_to(ORIGIN)

        # Display the equations
        self.play(Write(sums))
        self.wait(2)
