from manimlib import *

CONFIG = {
    "camera_class": ThreeDCamera,
}

class Pyramid3D(Scene):
    def construct(self):
        # Set up the 3D camera orientation using Euler angles
        self.camera.frame.set_euler_angles(
            phi=75 * DEGREES,  # Tilt the camera from the z-axis
            theta=30 * DEGREES  # Rotate around the vertical axis
        )

        # Define the vertices of the pyramid
        base_length = 2
        height = 2
        vertices = [
            [-base_length / 2, -base_length / 2, 0],  # Bottom-left corner
            [base_length / 2, -base_length / 2, 0],   # Bottom-right corner
            [base_length / 2, base_length / 2, 0],    # Top-right corner
            [-base_length / 2, base_length / 2, 0],   # Top-left corner
            [0, 0, height],                           # Apex
        ]

        # Define the faces of the pyramid
        faces = [
            [0, 1, 4],  # Front face
            [1, 2, 4],  # Right face
            [2, 3, 4],  # Back face
            [3, 0, 4],  # Left face
            [0, 1, 2, 3],  # Base (square)
        ]

        # Create a Polyhedron
        pyramid = Polyhedron(
            vertices=vertices,
            faces=faces,
            face_config={"fill_opacity": 0.7, "fill_color": BLUE},
            edge_config={"stroke_color": WHITE},
        )

        # Add the pyramid to the scene
        self.add(pyramid)

        # Rotate the camera for better visualization
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)

from manimlib import *

from manimlib import *

class Basic3DScene(ThreeDScene):
    def construct(self):
        # Set up 3D camera orientation
        self.camera.frame.set_euler_angles(
            phi=60 * DEGREES,  # Angle from the z-axis
            theta=45 * DEGREES  # Angle around the xy-plane
        )

        # Add 3D axes
        # axes = ThreeDAxes()

        # Create a cube
        cube = Cube()

        # Set cube colors
        for face in cube:
            face.set_color(BLUE)  # Set each face to blue
            face.set_opacity(0.7)  # Set the opacity of each face

        # Scale the cube
        cube.scale(2)

        # Add objects to the scene
        # self.add(axes, cube)

        # Rotate the cube over time
        self.play(Rotate(cube, angle=PI, axis=UP), run_time=3)  # Rotate around the y-axis
        self.play(Rotate(cube, angle=PI / 2, axis=RIGHT), run_time=2)  # Rotate around the x-axis

        # Hold the scene for a moment
        self.wait(2)


from manimlib import *

class PrismDemo(ThreeDScene):
    def construct(self):
        # Set up 3D camera orientation
        self.camera.frame.set_euler_angles(
            phi=60 * DEGREES,  # Tilt from z-axis
            theta=45 * DEGREES  # Rotate around the xy-plane
        )

        # Create a Prism
        prism = Prism(width=3.0, height=2.0, depth=1.5, color=BLUE, opacity=0.7)

        # Position and scale the Prism (if needed)
        prism.move_to(ORIGIN)  # Center the prism in the scene

        # Add the prism to the scene
        self.add(prism)

        # Rotate the prism for visualization
        self.play(
            Rotate(prism, angle=PI, axis=UP), run_time=3
        )
        self.play(
            Rotate(prism, angle=PI / 2, axis=RIGHT), run_time=2
        )

        # Hold the final view
        self.wait(2)


import random

class RandomMeshAnimation(ThreeDScene):
    def construct(self):
        # Set up the 3D camera orientation
        self.camera.frame.set_euler_angles(
            phi=60 * DEGREES,
            theta=45 * DEGREES
        )

        # Create a sphere as the base surface
        sphere = Sphere(radius=2.0, resolution=(20, 20), color=BLUE_E)
        self.add(sphere)  # Add the base sphere for context

        # Create a mesh on the sphere
        mesh = SurfaceMesh(
            uv_surface=sphere,
            resolution=(10, 10),
            stroke_width=1.5,
            stroke_color=WHITE
        )
        self.add(mesh)

        # Define an animation function for randomizing mesh vertices
        def randomize_mesh(mobject: SurfaceMesh):
            nudged_points = mobject.uv_surface.get_points().copy()
            for i, point in enumerate(nudged_points):
                # Randomly perturb each vertex within a small range
                nudged_points[i] += np.array([
                    random.uniform(-0.1, 0.1),  # Random x-offset
                    random.uniform(-0.1, 0.1),  # Random y-offset
                    random.uniform(-0.1, 0.1),  # Random z-offset
                ])
            mobject.uv_surface.set_points(nudged_points)

        # Animate the mesh with a random motion
        self.play(
            UpdateFromFunc(mesh, randomize_mesh),
            run_time=5,
            rate_func=there_and_back
        )

        # Hold the final frame
        self.wait(2)


class Prismify(VGroup3D):
    def __init__(self, vmobject, depth=1.0, direction=IN, **kwargs):
        # At the moment, this assume stright edges
        vect = depth * direction
        pieces = [vmobject.copy()]
        points = vmobject.get_anchors()
        for p1, p2 in adjacent_pairs(points):
            wall = VMobject()
            wall.match_style(vmobject)
            wall.set_points_as_corners([p1, p2, p2 + vect, p1 + vect])
            pieces.append(wall)
        top = vmobject.copy()
        top.shift(vect)
        top.reverse_points()
        pieces.append(top)
        super().__init__(*pieces, **kwargs)

from manimlib import *
import random
import numpy as np

class SmoothedBlobScene(ThreeDScene):
    def construct(self):
        # Set up the 3D camera orientation
        self.camera.frame.set_euler_angles(
            phi=60 * DEGREES,
            theta=45 * DEGREES
        )

        # Create a high-resolution sphere
        sphere = Sphere(radius=2.0, resolution=(50, 50), color=BLUE_E)

        # Perturb the vertices to create a blob effect
        points = sphere.get_points()
        for i, point in enumerate(points):
            points[i] += np.array([
                random.uniform(-0.2, 0.2),  # Random x-offset
                random.uniform(-0.2, 0.2),  # Random y-offset
                random.uniform(-0.2, 0.2)   # Random z-offset
            ])
        sphere.set_points(points)

        # Apply a gradient color (manually)
        colors = [RED, ORANGE, YELLOW]
        sphere.set_color_by_gradient(*colors)

        # Add the blob to the scene
        self.add(sphere)

        # Hold the scene to display the smoothed blob
        self.wait(5)


