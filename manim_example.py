from manim import *

class koch_animation(Scene):
    def construct(self):
        def KochCurve(
            n, length=12, stroke_width=8, color=("#FF4500", "#FFA500", "#FED8B1")
        ):

            l = length / (3 ** n)

            LineGroup = Line().set_length(l)

            def next(LineGroup):
                return VGroup(
                    *[LineGroup.copy().rotate(i) for i in [0, PI / 3, -PI / 3, 0]]
                ).arrange(RIGHT, buff=0, aligned_edge=DOWN)

            for _ in range(n):
                LineGroup = next(LineGroup)

            curve = (
                VMobject(stroke_width=stroke_width)
                .set_points(LineGroup.get_all_points())
                .set_color(color)
            )
            return curve

        level = Variable(0, Tex("recursive depth"), var_type=Integer).set_color("#CC5500")
        txt = (
            VGroup(Tex("Koch Curve", font_size=60), level)
            .arrange(DOWN, aligned_edge=LEFT)
            .to_corner(UL)
        )
        koch = KochCurve(0, stroke_width=12).to_edge(DOWN, buff=2.5)

        self.add(txt, koch)
        self.wait()

        for i in range(1, 6):
            self.play(
                level.tracker.animate.set_value(i),
                koch.animate.become(
                    KochCurve(i, stroke_width=12 - (2 * i)).to_edge(DOWN, buff=2.5)
                ),
            )
            self.wait()

koch_animation().render()