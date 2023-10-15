from manim import *


class SubIntervals(Scene):
    def construct(self):
        # Define the axes
        axes = Axes(
            x_range=[0, 5],
            y_range=[0, 1],
            axis_config={"color": BLUE},
        )

        # Create the x-axis
        x_axis = axes.get_x_axis()

        # Create vertical lines to represent sub-intervals
        num_intervals = 5
        sub_intervals = VGroup(*[
            Line(
                axes.c2p(i / num_intervals, 0),
                axes.c2p(i / num_intervals, -0.2),
                stroke_color=RED,
            )
            for i in range(num_intervals + 1)
        ])

        # Add text labels for a, b, and Delta x
        label_a = axes.get_x_axis_label("a")
        label_b = axes.get_x_axis_label("b", edge=DL)
        delta_x_label = MathTex("\\Delta x").next_to(sub_intervals[1], DOWN)

        # Show everything
        self.play(Create(axes), Create(x_axis), Write(label_a), Write(label_b))

        # Animate the partitioning into sub-intervals
        self.play(Create(sub_intervals))
        self.play(Write(delta_x_label))

        self.wait(1)
