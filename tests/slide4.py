from manim import *

class AreaProblem(Scene):
    def construct(self):
        # Create a coordinate system
        axes = Axes(
            x_range=[-1, 4],
            y_range=[-1, 5],
            axis_config={"color": BLUE},
        )

        # Create a curve (e.g., y = sin(x))
        curve = axes.plot(lambda x: np.sin(x), color=WHITE)

        # Shade the area under the curve
        area = axes.get_area(curve, x_range=[0, PI], color=YELLOW, opacity=0.5)

        # Add labels
        curve_label = axes.get_graph_label(curve, label="y = sin(x)", x_val=PI / 2, direction=DL)

        # Show everything
        self.play(Create(axes), Create(curve), Create(area), Write(curve_label))
        self.wait(2)
