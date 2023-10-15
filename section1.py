from manim import *


class AreaProblem(Scene):
    def construct(self):
        # Define the axes
        axes = Axes(
            x_range=[0, 5],
            y_range=[0, 3],
            axis_config={"color": BLUE},
        )

        # Create the graph of the function f(x)
        graph = axes.plot(lambda x: 0.2*(x-1)*(x-4), color=GREEN, x_range=[1, 4])

        # Shade the area under the curve
        area = axes.get_area(graph, x_range=[1, 4], color=BLUE, opacity=0.3)

        # Label the axes and the curve
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("f(x)")
        curve_label = MathTex("f(x) = 0.2(x-1)(x-4)").to_edge(UR)

        # Show everything
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(graph), Write(curve_label))
        self.wait(1)
        self.play(FadeIn(area), run_time=2)
        self.wait(1)
