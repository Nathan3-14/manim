from manim import (
    Scene, Axes, DashedLine, Circle,
    Write, ReplacementTransform, Create, FadeOut,
    BLUE, RIGHT, LEFT, DOWN, RED, GREEN, 
    Tex, MathTex
)

class Parabola(Scene):
    def question_1(self) -> None:
        given_parabola = self.axes.plot(lambda x: (x**2) - 2*(x) - 3, color=RED)
        # given_parabola_label = axes.get_graph_label(given_parabola, "y=x^2-x-3", x_val=2)
        solve_parabola = self.axes.plot(lambda x: (x**2) + (x) - 2, color=BLUE)
        solve_line = self.axes.plot(lambda x: (-3)*(x) - 1, color=GREEN)
        
        given_parabola_equation = MathTex(r"\ x^{2}-2x-3", color=RED)
        calculation = MathTex(
            r"x^{2}-2x-3 \\",
            r"-x^{2}+\ x-2",
            tex_to_color_map={
                r"x^{2}-2x-3": RED,
                r"x^{2}+\ x-2": BLUE
            }
        )
        answer = MathTex(
            r"-3x-1",
            color=GREEN
        )
        given_parabola_equation.next_to(self.axes, RIGHT)
        calculation.next_to(self.axes, RIGHT)
        answer.next_to(calculation, DOWN)

        solve_solution_a = DashedLine(self.axes.coords_to_point(-2, 5), self.axes.coords_to_point(-2, 0))
        solve_solution_b = DashedLine(self.axes.coords_to_point(1, -4), self.axes.coords_to_point(1, 0))
        solve_circle_a = Circle(0.25, color=GREEN)
        solve_circle_b = Circle(0.25, color=GREEN)
        solve_circle_a.move_to(self.axes.c2p(-2, 0))
        solve_circle_b.move_to(self.axes.c2p(1, 0))
        
        self.play(Write(self.axes))
        self.play(Write(given_parabola), Write(given_parabola_equation))
        self.wait(2)
        self.play(ReplacementTransform(given_parabola_equation, calculation))
        self.wait(2)
        self.play(Write(answer))
        self.wait(2)
        self.play(Write(solve_line))
        self.wait(1)
        self.play(Create(solve_solution_a), Create(solve_solution_b))
        self.wait(1)
        self.play(Create(solve_circle_a), Create(solve_circle_b), FadeOut(solve_solution_a), FadeOut(solve_solution_b))
        self.wait(2)
        self.play(FadeOut(given_parabola), FadeOut(solve_line))
        self.wait(1)
        self.play(Write(solve_parabola))
        
    def construct(self) -> None:
        self.axes = Axes(
            x_range=(-5, 5),
            y_range=(-5, 10),
            x_length=10,
            tips=False
        ).move_to(LEFT)
        self.axes.add_coordinates()
        
        self.question_1()
        self.wait(5)
