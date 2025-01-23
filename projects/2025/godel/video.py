from manimlib import *

class GodelIncompleteness(Scene):
    def construct(self):
        # Create text, scale it, and center it
        text = Text("This statement is false").scale(0.7)
        text.move_to(ORIGIN)  # Ensure the text is centered on the screen
        
        self.play(Write(text), run_time=1.2)
        self.wait(1)

        # Define the image path and image object
        image_path = "godel.png"
        image_mobject = ImageMobject(image_path)

        # Create the name text and position it below the image
        name_text = Text("Kurt Gödel (1906–1978)", font_size=26).scale(0.4)
        name_text.set_color("#A9A9A9")  # Set the text color to light gray
        name_text.next_to(image_mobject, DOWN, buff=-0.1)

        # Create animations to run simultaneously
        self.play(
            AnimationGroup(
                text.animate.scale(0.8).to_edge(UP, buff=1),  # Move text upward with a buffer
                FadeIn(image_mobject.scale(0.8), run_time=1.5),  # Fade in the image
                FadeIn(name_text, run_time=1.5),  # Fade in the name and years
                lag_ratio=0  # Synchronize animations
            )
        )
        self.wait(1)
