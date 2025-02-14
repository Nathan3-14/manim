from manim import Scene, Axes, Write, BLUE, FadeOut, ReplacementTransform, Tex, UP

class AxesTest(Scene):
    def construct(self) -> None:
        axes = Axes(x_range=(-10, 10), y_range=(-5, 5), tips=False)
        axes.add_coordinates()
        graph_1 = axes.plot(lambda x: (2 * x) - 2, color=BLUE)
        graph_1_label = axes.get_graph_label(graph_1, label="y=2x-2", x_val=2)
        graph_2 = axes.plot(lambda x: (2 * x) + 2, color=BLUE)
        graph_2_label = axes.get_graph_label(graph_2, label="y=2x+3", x_val=2)
        graph_3 = axes.plot(lambda x: (0.5 * x) + 2, color=BLUE)
        graph_3_label = axes.get_graph_label(graph_3, label=r"y=\frac{1}{2}x+2", x_val=2)
        graph_4 = axes.plot(lambda x: (4 * x) - 4, color=BLUE)
        graph_4_label = axes.get_graph_label(graph_4, label="y=4x-4", x_val=2)
        
        
        self.play(Write(axes))
        self.play(Write(graph_1), Write(graph_1_label))
        self.wait(0.5)
        self.play(ReplacementTransform(graph_1, graph_2), ReplacementTransform(graph_1_label, graph_2_label))
        self.wait(0.5)
        self.play(ReplacementTransform(graph_2, graph_3), ReplacementTransform(graph_2_label, graph_3_label))
        self.wait(0.5)
        self.play(ReplacementTransform(graph_3, graph_4), ReplacementTransform(graph_3_label, graph_4_label))
        self.wait(0.5)
        self.play(FadeOut(graph_4), FadeOut(graph_4_label))
        
        
