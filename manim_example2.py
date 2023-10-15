from manim import *

class IntroductionSlide(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Calculus Problems", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Create a coordinate plane
        axes = Axes(
            x_range=[-4, 4],
            y_range=[-2, 2],
            axis_config={"color": BLUE},
        )
        self.play(Create(axes))

        # Tangent Line Problem Graph
        tangent_graph = axes.plot(
            lambda x: x**2,
            color=GREEN,
        )

        # Area Problem Graph
        area_graph = axes.plot(
            lambda x: np.sin(x),
            color=YELLOW,
        )

        # Labels
        tangent_label = Text("Tangent Line Problem", color=GREEN).next_to(axes, DOWN)
        area_label = Text("Area Problem", color=YELLOW).next_to(axes, DOWN)

        # Animation
        self.play(
            Create(tangent_graph),
            Create(area_graph),
        )
        self.play(Write(tangent_label), Write(area_label))
        self.wait(3)


# only non GPT addition - added by rohan to execute the script after GPT defined the Scene
IntroductionSlide().render()
