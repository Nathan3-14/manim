from manim import (
    Scene, Axes, DashedLine, Circle,
    Write, ReplacementTransform, Create, FadeOut,
    BLUE, RIGHT, LEFT, DOWN, RED, GREEN, 
    Tex, MathTex,
    ManimColor, ParametricFunction
)
import re
from typing import List
from fractions import Fraction
from sys import argv

EQUATION_PATTERN = r"(?<!\n)(?=[+-])"

def check_equation_string(a: str) -> bool:
    a_split = re.split(r"(?<=[+-])|(?=[+-])", a)
    if len(a_split) != 5:
        return False
    for index, term in enumerate(a_split):
        match index:
            case 0:
                if "x^2" not in term:
                    return False
            case 2:
                if "x" not in term:
                    return False
            case 4:
                if "x" in term:
                    return False
    return True

    
class Equation:
    def __init__(self, equation_string: str) -> None:
        self.equation_string = equation_string
    
    def subtract_equation_strings(self, a: str, b: str) -> str:
        if not check_equation_string(a) or not check_equation_string(b):
            return a
        a_split = re.split(EQUATION_PATTERN, a)
        b_split = re.split(EQUATION_PATTERN, b)
        output: List[str] = []

        try:
            for i in range(3):
                value_a = a_split[i]
                value_b = b_split[i]
                variable = ""
                print(f"A: '{value_a}' B: '{value_b}'")
                match i:
                    case 0|1:
                        fraction_value_a = Fraction(value_a.split("x")[0])
                        fraction_value_b = Fraction(value_b.split("x")[0])
                        variable += "x"
                    case _:
                        fraction_value_a = Fraction(value_a)
                        fraction_value_b = Fraction(value_b)
                        
                result = str(fraction_value_a-fraction_value_b)
                output.append(("+" if result[0] != "-" and i != 0 else "") + result + variable + ("^2" if i == 0 else ""))
        except Exception as e:
            print(e)
        return "".join(output)

    def divide_equation_string(self, a: str, div: int|float|Fraction) -> str:
        if not check_equation_string(a):
            return a
        a_split = re.split(EQUATION_PATTERN, a)
        output: List[str] = []

        try:
            for i in range(3):
                value_a = a_split[i]
                variable = ""
                match i:
                    case 0|1:
                        fraction_value_a = Fraction(value_a.split("x")[0])
                        variable = "x"
                    case _:
                        fraction_value_a = Fraction(value_a)
                result = str(fraction_value_a/div)
                output.append(("+" if result[0] != "-" and i != 0 else "") + result + variable + ("^2" if i == 0 else ""))
        except Exception as e:
            print(e)
        return "".join(output)
    
    def substitute(self, x: float) -> float:
            if not check_equation_string(self.equation_string):
                return 80085
            equation_split = re.split(EQUATION_PATTERN, self.equation_string)
            answer = 0.0
            for part in equation_split:
                coeficient = part.split("x")[0]
                match len(part.split("x")):
                    case 1: #no xs present
                        answer += float(Fraction(coeficient))
                    case 2: #either x or x^2
                        if part.split("x")[1] == "":
                            answer += float(Fraction(coeficient)) * x
                        else:
                            answer += float(Fraction(coeficient)) * (x ** float(Fraction(part.split("x")[1][1:])))
            return answer
        
    def __sub__(self, object: "Equation") -> "Equation":
        return Equation(self.subtract_equation_strings(self.equation_string, object.equation_string))
    
    def __truediv__(self, number: int|float|Fraction) -> "Equation":
        if isinstance(number, float) or isinstance(number, Fraction) or isinstance(number, int):
            return Equation(self.divide_equation_string(self.equation_string, number))
        else:
            return self
    
    def __str__(self) -> str:
        output = ""
        for index, part in enumerate(re.split(r"(?=[+-])", self.equation_string)):
            part_split = part.split("x")
            coeficient = part_split[0]
            match len(part_split):
                case 1:
                    if coeficient == "0":
                        continue
                case _:
                    if coeficient.strip("+-") == "0":
                        continue
                    elif coeficient.strip("+-") == "1":
                        output += ("+" if part[0] != "-" and index != 0 else "-") + "x" + part_split[1]
                        continue
            output += part
        return output

    def latex(self) -> str:
        pattern = r"(\d+)/(\d+)" #? Captures any two numbers seperated by a /

        replacement = r"\\frac{\1}{\2}"

        result = re.sub(pattern, replacement, str(self))
        return result


    def __repr__(self) -> str:
        return str(self)
class Parabola(Scene):
    def parabola_question(self, given_equation: str, solvefor_equation: str) -> None:
        given_parabola = self.axes.plot(lambda x: (x**2) - 2*(x) - 3, color=RED)
        # given_parabola_label = axes.get_graph_label(given_parabola, "y=x^2-x-3", x_val=2)
        solve_parabola = self.axes.plot(lambda x: (x**2) + (x) - 2, color=BLUE)
        solve_line = self.axes.plot(lambda x: (-3)*(x) - 1, color=GREEN)
        
        given_parabola_equation = MathTex(r"\ x^{2}-2x-3", tex_to_color_map={}, color=RED)
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
            tex_to_color_map={},
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
        
        self.play(Write(given_parabola), Write(given_parabola_equation))
        self.wait(2)
        self.play(ReplacementTransform(given_parabola_equation, calculation))
        self.wait(2)
        self.play(Write(answer))
        self.wait(2)
        self.play(Write(solve_line))
        self.wait(1)
        self.play(Create(solve_solution_a), Create(solve_solution_b))
        self.play(Create(solve_circle_a), Create(solve_circle_b), FadeOut(solve_solution_a), FadeOut(solve_solution_b))
        self.wait(2)
        self.play(FadeOut(given_parabola), FadeOut(solve_line))
        self.wait(1)
        self.play(Write(solve_parabola))
        self.wait(3)
        self.play(FadeOut(solve_circle_a), FadeOut(solve_circle_b), FadeOut(solve_parabola), FadeOut(calculation), FadeOut(answer))
    
    def draw_equation(self, equation: Equation, color: ManimColor=RED) -> ParametricFunction:
        temp = self.axes.plot(equation.substitute, color=color)
        return temp
    
    def solve_sequence(self) -> None:
        # steps: List[Write] = []

        given_parabola = self.draw_equation(self.given_equation, color=BLUE) 
        print(f"---- {str(self.given_equation)}")
        solve_parabola = self.draw_equation(self.solve_equation, color=RED)
        divider = 2
        calculation_a = MathTex(
            self.given_equation.latex() + r" \\",
            r"-\ " + self.solve_equation.latex(),
            tex_to_color_map={
                self.given_equation.latex(): BLUE,
                self.solve_equation.latex(): RED
            }
        )
        self.solve_equation /= divider
        print(f"[][][][] {(self.solve_equation).latex()}")
        #TODO maybe rewrite a instead TODO#
        calculation_b = MathTex(
            self.given_equation.latex() + r" \\",
            r"-\ " + self.solve_equation.latex(),
            tex_to_color_map={
                self.given_equation.latex(): BLUE,
                self.solve_equation.latex(): RED
            }
        )
        calculation_a.next_to(self.axes, RIGHT)
        calculation_b.next_to(self.axes, RIGHT)
        result = MathTex(
            (self.given_equation-self.solve_equation).latex(),
            color=GREEN,
            tex_to_color_map={}
        )
        result.next_to(calculation_a, DOWN)
        action_remark = MathTex(
            rf"\div {divider}",
            tex_to_color_map={}
        )
        action_remark.next_to(calculation_a, DOWN)
        self.play(Write(given_parabola), Write(solve_parabola))
        self.play(Write(calculation_a))
        if divider != 1:
            self.play(Write(action_remark))
            self.play(ReplacementTransform(calculation_a, calculation_b), FadeOut(action_remark))
        self.play(Write(result))
        # divide_remark = MathTex(r"\div 2", tex_to_color_map={})
        # calculation_b = MathTex(
        #     r"x^{2}-2x-3 \\",
        #     r"-x^{2}+\frac{1}{2}x-1",
        #     tex_to_color_map={
        #         r"x^{2}-2x-3": RED,
        #         r"x^{2}+\frac{1}{2}x-1": BLUE
        #     }
        # )
    
    def construct(self) -> None:
        self.given_equation = Equation("1x^2-1x-2")
        self.solve_equation = Equation("1x^2+5x+6")
        
        self.axes = Axes(
            x_range=(-5, 5),
            y_range=(-5, 10),
            x_length=8,
            tips=False
        ).move_to(LEFT)
        self.axes.add_coordinates()
        self.play(Write(self.axes))
        
        self.solve_sequence()
        self.wait(2)

if __name__ == "__main__":
    tgiven_equation = Equation("1x^2+3x+3")
    tsolve_equation = Equation("1x^2+1/2x+2")
    print(tsolve_equation.latex())
    