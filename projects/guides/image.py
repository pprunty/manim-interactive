from manimlib import *


class FadeInImage(Scene):
    def construct(self):
        # Load an image (use your `raster_images` directory)
        image_path = "media/images/example.jpg"
        image_mobject = ImageMobject(image_path)

        # Add the image to the scene
        self.play(FadeIn(image_mobject.scale(0.33)))
        self.wait(1)


class MoveImage(Scene):
    def construct(self):
        # Load an image (use your `raster_images` directory)
        image_path = "media/images/example.jpg"
        image_mobject = ImageMobject(image_path)

        # Add the image to the scene
        self.play(FadeIn(image_mobject.scale(0.33)))

        # Scale and move the first image to the top-left corner
        self.play(image_mobject.animate.scale(0.6))
        self.play(image_mobject.animate.to_corner(UL, buff=0))
        self.wait(1)


class ImageWithBorder(Scene):
    def construct(self):
        # Load an image
        image = ImageMobject("media/images/example.jpg").scale(0.5)

        # Create a border using a rectangle
        border = Rectangle(
            width=image.get_width(),
            height=image.get_height()
        )
        border.set_stroke(WHITE, width=8)  # White border with thickness 4
        border.move_to(image.get_center())  # Align the border with the image

        # Add the image and border to the scene (separately)
        self.add(border, image)

        # Animate scaling the image and border together
        self.play(
            border.animate.scale(1.6),
            image.animate.scale(1.6)
        )
        self.wait(2)


class ScaleAndMoveImage(Scene):
    def construct(self):
        # Load an image (use your `raster_images` directory)
        image_path = "media/images/example.jpg"
        image_mobject = ImageMobject(image_path)

        # Add the image to the scene
        self.play(FadeIn(image_mobject.scale(0.5)))

        # Scale and move the first image to the top-left corner
        self.play(image_mobject.animate.scale(0.5).to_corner(UL, buff=0))
        self.wait(1)


class MoveImage(Scene):
    def construct(self):
        # Load the image
        image_path = "media/images/earth.png"
        image = ImageMobject(image_path).scale(0.8)  # Initial scale

        # Add the image to the scene at the center
        self.play(FadeIn(image))
        self.wait(1)

        # Move the image to the left
        self.play(image.animate.shift(LEFT * 3))
        self.wait(0.5)

        # Move the image back to the middle
        self.play(image.animate.shift(RIGHT * 3))
        self.wait(0.5)

        # Move the image to the right
        self.play(image.animate.shift(RIGHT * 3))
        self.wait(0.5)

        # Move the image back to the middle
        self.play(image.animate.shift(LEFT * 3))
        self.wait(0.5)

        # Move the image up
        self.play(image.animate.shift(UP * 2))
        self.wait(0.5)

        # Move the image down
        self.play(image.animate.shift(DOWN * 2))
        self.wait(1)

        # Move the image down
        self.play(image.animate.shift(DOWN * 2))
        self.wait(1)

        # End the scene
        self.play(FadeOut(image))


class ScaleImage(Scene):
    def construct(self):
        # Load the image
        image_path = "media/images/example.jpg"
        image = ImageMobject(image_path).scale(0.5)  # Initial scale of 0.5

        # Add the image to the scene
        self.play(FadeIn(image))
        self.wait(1)

        # Scale the image to twice its size
        self.play(image.animate.scale(2))
        self.wait(1)

        # Scale the image back to its original size
        self.play(image.animate.scale(0.5))
        self.wait(1)


class ShakeImage(Scene):
    def construct(self):
        # Load an image (use your `raster_images` directory)
        image_path = "media/images/example.jpg"
        image_mobject = ImageMobject(image_path)

        # Add the image to the scene
        self.play(FadeIn(image_mobject.scale(0.5)))

        # Define the shake animation
        shake_animation = [
            image_mobject.animate.shift(LEFT * 0.4),
            image_mobject.animate.shift(RIGHT * 0.4),
            image_mobject.animate.shift(LEFT * 0.4),
            image_mobject.animate.shift(RIGHT * 0.4),
        ]

        # Play the shake animation in sequence
        self.play(*shake_animation, run_time=0.3)  # Adjust `run_time` for speed

        # Keep the scene displayed
        self.wait(2)


class MoveTwoImages(Scene):
    def construct(self):
        image_path = "example.jpg"
        image_mobject_1 = ImageMobject(image_path)

        self.play(FadeIn(image_mobject_1.scale(0.5)))

        self.play(image_mobject_1.animate.scale(0.5).to_corner(UL, buff=0))
        self.wait(1)

        image_path = "example2.png"
        image_mobject_2 = ImageMobject(image_path)
        image_mobject_2.scale(0.5) 

        self.play(FadeIn(image_mobject_2))
        self.play(
            image_mobject_2.animate.scale(0.5).next_to(image_mobject_1, DOWN, buff=0)
        )
        self.wait(1)

class MorphSVGToSphere(Scene):
    def construct(self):
        svg_path = "410.svg"
        svg_image = SVGMobject(svg_path).scale(0.5)
        svg_image.set_fill(color=BLUE, opacity=0.8)
        svg_image.set_stroke(color=WHITE, width=1)

        sphere = Circle(radius=2)
        sphere.set_fill(color=BLUE, opacity=0.8)
        sphere.set_stroke(color=WHITE, width=1)

        self.play(FadeIn(svg_image))
        self.play(Transform(svg_image, sphere))
        self.play(Rotate(sphere, angle=PI))
        self.play(FadeOut(sphere))