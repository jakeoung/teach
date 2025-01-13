from manim import *

class MultiplicativeInverse(Scene):
    def construct(self):
        # Title
        title = Text("Multiplicative inverse of e modulo n", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Main content
        content = VGroup()

        # Problem statement
        problem = MathTex(r"\text{When }\gcd(e, n)=1,\text{ find }d\text{ such that }ed \equiv 1 \pmod{n}")
        content.add(problem)

        # Solution header
        solution_header = Text("Solution.", font_size=36, slant=ITALIC)
        content.add(solution_header)

        # Solution steps
        steps = VGroup(
            MathTex(r"\text{Since }\operatorname{gcd}(e, n)=1,\text{ we can apply Extended-Euclid.}"),
            Text("Then:", font_size=32),
            MathTex(r"ex + ny = 1\text{ for some integers }x\text{ and }y"),
            MathTex(r"ex - 1 = ny\text{ for some integer }y"),
            MathTex(r"n \mid ex-1"),
            MathTex(r"ex \equiv 1 \pmod{n}")
        )
        content.add(*steps)

        # Conclusion
        conclusion = Text("Hence, x is the multiplicative inverse of e modulo n", font_size=36)
        content.add(conclusion)

        # Arrange content
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        content.next_to(title, DOWN, buff=0.5)

        # Animate each element
        for item in content:
            self.play(FadeIn(item))
            self.wait(1.5)  # Increased wait time for better readability

        self.wait(2)

        # Fade out content and provide several examples
        self.play(FadeOut(content))
        self.wait(1)

        # Examples
        examples = VGroup()
        for e, n in [(3, 7), (5, 11), (7, 13)]:
            example = VGroup(
                MathTex(r"\text{Example: } e = " + str(e) + r", n = " + str(n)),
                MathTex(r"\gcd(" + str(e) + r", " + str(n) + r") = 1")
            )
            examples.add(example)

        # Arrange examples
        examples.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        examples.next_to(title, DOWN, buff=0.5)

        # Animate each example
        for example in examples:
            self.play(FadeIn(example))
            self.wait(1.5)
        
        self.wait(2)
        self.play(FadeOut(examples))
        self.wait(1)

        # Final remarks
        final_remarks = Text("The multiplicative inverse of e modulo n is unique.", font_size=36)
        self.play(Write(final_remarks))
        self.wait(2)
        self.play(FadeOut(final_remarks))
        self.wait(1)

        # End
        end = Text("End of presentation", font_size=40)
        self.play(Write(end))
        self.wait(2)

        # Fade out end
        

