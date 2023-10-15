from manim import *


class AreaApproximation(Scene):
    def construct(self):
        # Function and interval
        def func(x):
            return x**2

        a = 0
        b = 4
        num_rectangles = 4
        dx = (b - a) / num_rectangles

        # Create axes
        axes = Axes(
            x_range=[0, 4],
            y_range=[0, 16],
            axis_config={"color": BLUE},
        )
        self.play(Create(axes))

        # Draw the curve
        graph = axes.plot(lambda x: func(x), color=GREEN)
        self.play(Create(graph))

        # Initialize rectangles
        rectangles = VGroup()

        for i in range(num_rectangles):
            x_left = a + i * dx
            x_right = x_left + dx
            height = func(x_left)
            rect = Rectangle(
                width=dx,
                height=height,
                stroke_width=1,
                stroke_color=WHITE,
                fill_opacity=0.5,
                fill_color=YELLOW,
            )
            rect.move_to(axes.c2p((x_left + x_right) / 2, height / 2))
            rectangles.add(rect)

        self.play(Create(rectangles))
        self.wait(1)

        # Animate the approximation
        for i in range(num_rectangles):
            self.play(
                rectangles[i].animate.shift(UP * func(a + (i + 0.5) * dx) * dx),
                run_time=1,
            )
            self.wait(0.5)

        self.wait(2)
