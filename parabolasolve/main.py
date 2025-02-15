from manim import (
    Scene, Axes,
    Write,
    BLUE, RIGHT, LEFT, DOWN, RED, GREEN, 
    Tex, MathTex
)

class Parabola(Scene):
    def construct(self) -> None:
        axes = Axes(
            x_range=(-5, 5),
            y_range=(-5, 10),
            x_length=10,
            tips=False
        ).move_to(LEFT)
        axes.add_coordinates()
        
        given_parabola = axes.plot(lambda x: (x**2) - 2*(x) + 1, color=RED)
        # given_parabola_label = axes.get_graph_label(given_parabola, "y=x^2-x-3", x_val=2)
        solve_parabola = axes.plot(lambda x: (x**2) + 4*(x) + 3, color=BLUE)
        # solve_parabola_label = axes.get_graph_label(solve_parabola, "y=x^2+x-1", x_val=2)
        
        given_parabola_equation = MathTex("x^{2}-2x+1", color=RED)
        solve_parabola_equation = MathTex("x^{2}+4x+3", color=BLUE)
        given_parabola_equation.next_to(axes, RIGHT)
        solve_parabola_equation.next_to(given_parabola_equation, DOWN)
        
        self.play(Write(axes))
        self.play(Write(given_parabola), Write(given_parabola_equation))
        self.wait(2)
        self.play(Write(solve_parabola), Write(solve_parabola_equation))
        self.wait(2)
