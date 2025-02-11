from manimlib import *

class HelloWorld(Scene):
    def construct(self):
        code = """
print("Hello, World!")
"""
        
        rendered_code = Code(
            code=code,
            language="python",
            alignment="LEFT",
            font="monospace"
        )
        self.play(Write(rendered_code))
        self.wait(2)


class CodeTransform(Scene):
    def construct(self):
        # Define Python code
        python_code = Code(
            code="""
print("Hello, World!")
""",
            language="python",
            font="monospace",
            alignment="LEFT"
        ).scale(0.6)
        
        # Define C++ code
        cpp_code = Code(
            code="""
#include <iostream>
using namespace std;

int main() {
\tcout << "Hello, World!" << endl;
\treturn 0;
}
""",
            language="cpp",
            font="monospace",
            alignment="LEFT"
        ).scale(0.6)
        
        # Show Python code
        self.play(Write(python_code))
        self.wait(2)
        
        # Transform to C++ code
        self.play(Transform(python_code, cpp_code))
        self.wait(2)



class TypewriterHelloWorld(Scene):
    def construct(self):
        # The text we'll be typing
        text_str = "Hello, World!"

        # 1) Create the final text (used only for measuring width/height).
        #    We'll type onto a separate (empty) Text mobject.
        final_text = Text(text_str, font="Monospace").scale(1.2)

        # 2) Create a rectangle sized to fit the final text with a small margin.
        paper_rect = Rectangle(
            width=final_text.width + 0.5,   # add some horizontal margin
            height=final_text.height + 0.5, # add some vertical margin
            fill_color=WHITE,
            fill_opacity=1,
            stroke_color=BLACK,
            stroke_width=2
        )
        # Move the rectangle to the center of the scene
        paper_rect.move_to(ORIGIN)

        # 3) Create our initially empty Text mobject and place it over the rectangle center
        text_mobj = Text("", font="Monospace").scale(1.2)
        text_mobj.move_to(paper_rect.get_center())

        # 4) Create a simple cursor line and place it to the right of our empty text
        cursor = Line(ORIGIN, UP * 0.4, stroke_width=5)
        cursor.next_to(text_mobj, RIGHT, buff=0.1)

        # 5) Add the paper (behind), then text, then cursor
        #    (Order matters: objects added earlier render behind those added later.)
        self.add(paper_rect, text_mobj, cursor)

        # 6) Typewriter effect: build the string one character at a time
        for i in range(len(text_str) + 1):
            # Generate the next partial text
            partial_text = Text(text_str[:i], font="Monospace").scale(1.2)
            partial_text.move_to(paper_rect.get_center())

            # Animate text change + move the cursor
            self.play(
                Transform(text_mobj, partial_text),
                cursor.animate.next_to(text_mobj, RIGHT, buff=0.1),
                run_time=0.1
            )

        # 7) (Optional) remove the cursor after typing
        self.remove(cursor)
        self.wait(2)
