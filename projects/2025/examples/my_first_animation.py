from manimlib import *


class MyFirstAnimation(Scene):
    def construct(self):
        text1 = Text("Fast Animation")
        text2 = Text("Slow Animation")
        text3 = Text("Smooth Animation")

        # Fast animation
        self.play(Write(text1), run_time=0.5)
        self.wait(1)

        # Slow animation
        self.play(Transform(text1, text2), run_time=3)
        self.wait(1)

        # Smooth animation
        self.play(Transform(text1, text3), run_time=2, rate_func=smooth)
        self.wait(1)
