from manim import *


class LeftRiemannSumExample(Scene):
    def construct(self):
        # Create a coordinate system
        axes = Axes(
            x_range=[-1, 4],
            y_range=[-1, 5],
            axis_config={"color": BLUE},
        )

        # Create a curve (e.g., y = sin(x))
        curve = axes.plot(lambda x: np.sin(x), color=WHITE)

        # Divide the area under the curve into smaller rectangles (Left Riemann Sum)
        rectangles = axes.get_riemann_rectangles(curve, x_range=[0, PI], dx=0.5, color=GREEN, input_sample_type="left")

        # Add labels
        curve_label = axes.get_graph_label(curve, label="y = sin(x)", x_val=PI / 2, direction=DL)

        # Show everything
        self.play(Create(axes), Create(curve), Create(rectangles), Write(curve_label))
        self.wait(2)
