from manimlib import *


class TextScene(Scene):
    def construct(self):
        text = Text("Hello, Manim!")
        self.play(Write(text))
        self.wait(2)


class SlowText(Scene):
    def construct(self):
        text = Text("Hello, Manim!")
        self.play(Write(text), run_time=3)
        self.wait(2)


class FastText(Scene):
    def construct(self):
        text = Text("Hello, Manim!")
        self.play(Write(text), run_time=0.5)
        self.wait(2)


class FadeOutText(Scene):
    def construct(self):
        # Create a text object
        text = Text("Hello, Manim!")

        self.add(text)
        self.wait(1) 
        self.play(FadeOut(text, run_time=2))
        self.wait(1)


class TransformText(Scene):
    def construct(self):
        text1 = Text("Hello, Manim!")
        text2 = Text("Transforming Text")
        self.play(Write(text1))
        self.wait(1)
        self.play(Transform(text1, text2), run_time=0.5)
        self.wait(2)


class AlternativeFontText(Scene):
    def construct(self):
        text = Text("Here is text in Arial Font", font="Arial", font_size=90)
        self.play(Write(text))
        self.wait(1)


class SlideInText(Scene):
    def construct(self):
        text = Text(
            """
            Here is text that animates into view
            """
        )
        self.play(FadeIn(text, UP))
        self.wait(1)
        self.play(FadeOut(text, run_time=1))
        self.wait(1)
        self.play(FadeIn(text, DOWN))


class ScaleText(Scene):
    def construct(self):
        text = Text("Scaling Text")
        self.play(Write(text))
        self.wait(1)
        self.play(text.animate.scale(2), run_time=2)
        self.wait(2)


class RotateText(Scene):
    def construct(self):
        text = Text("Rotating Text")
        self.play(Write(text))
        self.wait(1)
        self.play(Rotate(text, angle=PI))  # Rotate 180 degrees
        self.wait(2)
        self.play(Rotate(text, angle=PI), run_time=0.5)  # Rotate 180 degrees


class MoveText(Scene):
    def construct(self):
        text = Text("Moving Text")
        self.play(Write(text))
        self.wait(1)

        self.play(text.animate.to_corner(UL))
        self.wait(1)

        self.play(text.animate.to_corner(ORIGIN))
        self.wait(1)
        self.play(text.animate.scale(0.5).to_corner(DR))
        self.wait(1)


class ColorChangeText(Scene):
    def construct(self):
        text = Text("Changing Color")
        self.play(Write(text))
        self.wait(1)
        self.play(text.set_color, RED)  # Change text color to red
        self.wait(2)


class CombinedAnimation(Scene):
    def construct(self):
        text = Text("Combining Effects")
        self.play(Write(text))
        self.wait(1)
        self.play(text.set_color, BLUE, text.scale, 1.5, Rotate(text, angle=PI / 4))  # Combine effects
        self.wait(2)
