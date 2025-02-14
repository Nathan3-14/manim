from manim import Scene, Square, RED, BLUE, Circle, Create, Rotate, FadeOut, FadeIn, PI, ReplacementTransform


class Test(Scene):
    def construct(self) -> None:
        box = Square(2)
        box.set_fill(RED, opacity=0.5)
        circle = Circle()
        circle.set_fill(BLUE, opacity=1)
        
        box.next_to(circle)
        
        self.play(Create(box), FadeIn(circle))
        self.play(
            Rotate(box, angle=PI/4),
            ReplacementTransform(circle, box)
        )
        self.play(FadeOut(box), FadeOut(circle))
