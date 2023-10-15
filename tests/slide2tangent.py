from manim import *


class TangentLineProblem(Scene):
    def construct(self):
        # Create a coordinate system
        axes = Axes(
            x_range=[-1, 3],
            y_range=[-1, 5],
            axis_config={"color": BLUE},
        )

        # Create a curve (e.g., y = x^2)
        curve = axes.plot(lambda x: x ** 2, color=WHITE)

        # Calculate the equation of the tangent line (y = 4x - 4)
        x_value = 2
        tangent_slope = 4  # Derivative of y = x^2 at x = 2
        tangent_intercept = -4  # Calculate the intercept based on the point (2, 4)
        tangent_line = axes.plot(lambda x: tangent_slope * x + tangent_intercept, color=RED)

        # Add labels
        curve_label = axes.get_graph_label(curve, label="y = x^2", x_val=x_value, direction=DL)
        point_label = MathTex(f"P({x_value}, {x_value ** 2})", color=YELLOW).next_to(
            axes.coords_to_point(x_value, x_value ** 2), RIGHT)

        # Show everything
        self.play(Create(axes), Create(curve), Create(tangent_line), Write(curve_label), Write(point_label))
        self.wait(2)
