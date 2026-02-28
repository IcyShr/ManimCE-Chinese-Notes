from manim import *
import numpy as np
"manim -pql 生成图示的代码.py "


class GIF_1_1(Scene):
    def construct(self):
        circle = Circle(radius=1)
        text = Text("Hello world.你好世界。")

        self.play(Create(circle))
        self.play(Write(text))
        self.wait(1)


"图2.1来源于https://docs.manim.community/en/v0.20.1/reference/manim.mobject.geometry.tips.ArrowTip.html"


class PNG_2_2(Scene):
    def construct(self):
        rect = Rectangle(width=2.0, height=2.0, grid_xstep=1.0, grid_ystep=1.0)
        rect.grid_lines.set_stroke(width=1)
        self.add(rect)


class PNG_2_3(Scene):
    def construct(self):
        vg = VGroup()
        for i in range(8):
            vg.add(RegularPolygram(7, density=i))
        self.add(vg.arrange_in_grid(2, 4, buff=1))


"图2.4的代码来源于示例图库"


class PNG_3_1(Scene):
    def construct(self):
        CONFIG = {
            "stroke_width": 5,
            "stroke_color": WHITE,
            "stroke_opacity": 1,
            "fill_opacity": 1,
            "fill_color": color_gradient([PURE_RED, YELLOW], 2),
        }

        rec = Rectangle(**CONFIG)
        cir = Circle(1, **CONFIG)
        tri = Triangle(**CONFIG)
        squ = Square(**CONFIG)

        self.add(Group(rec, cir, tri, squ).arrange())


class PNG_3_2(Scene):
    def construct(self):
        vg = VGroup()
        arr = Arrow(DOWN, UP).scale(2, scale_tips=True)

        vg.add(arr.copy())
        vg.add(arr.copy().set_stroke(color=BLUE))
        vg.add(arr.copy().set_stroke(color=BLUE, width=20))
        vg.add(arr.copy().set_stroke(color=BLUE, width=20, opacity=0.5))
        vg.add(arr.copy().set_stroke(color=BLUE, width=20, opacity=0.5, background=True))
        vg.add(arr.copy().set_stroke(color=BLUE, width=20, opacity=0.5, background=True, family=False))

        self.add(vg.arrange(buff=1.5))


class PNG_3_3(Scene):
    def construct(self):
        tri = Triangle(color=YELLOW)
        cir = Circle(1).set_color('#00ff00')
        squ = Square().set_color([RED, BLUE])

        self.add(VGroup(tri, cir, squ).arrange())


class PNG_3_4(Scene):
    def construct(self):
        squ = Square().set_fill(opacity=1).set_color(BLUE)
        squ1 = squ.copy().set_sheen(0.8, DR)
        squ2 = squ1.copy().set_sheen_direction(RIGHT)
        squ3 = squ2.copy().set_color([RED, YELLOW])

        self.add(VGroup(squ1, squ2, squ3).arrange(buff=1.5))


class PNG_3_5(Scene):
    def construct(self):
        vg = VGroup()
        for i in range(36):
            vg.add(Square(0.5).set_color(BLUE).set_fill(opacity=1))
        vg.arrange_in_grid(rows=6, cols=6, buff=0.3)
        
        vg.set_color_by_gradient(GREEN, RED, BLUE)
        vg1 = vg.copy().set_colors_by_radial_gradient(radius=3)

        self.add(VGroup(vg, vg1).arrange(buff=1))


class PNG_3_6(Scene):
    def construct(self):
        arc = Arc(radius=2, angle=PI/2).set_color(GREEN).set_stroke(width=20)

        arc_1 = arc.copy().set_cap_style(CapStyleType.AUTO)
        arc_2 = arc.copy().set_cap_style(CapStyleType.ROUND)
        arc_3 = arc.copy().set_cap_style(CapStyleType.BUTT)
        arc_4 = arc.copy().set_cap_style(CapStyleType.SQUARE)

        self.add(VGroup(arc_1, arc_2, arc_3, arc_4).arrange(buff=1))


class PNG_3_7(Scene):
    def construct(self):
        tri = Triangle().set_stroke(width=10).scale(1.5, scale_stroke=True)
        
        tri_1 = tri.copy().set_joint_type(LineJointType.AUTO)
        tri_2 = tri.copy().set_joint_type(LineJointType.ROUND)
        tri_3 = tri.copy().set_joint_type(LineJointType.BEVEL)
        tri_4 = tri.copy().set_joint_type(LineJointType.MITER)
        
        self.add(VGroup(tri_1, tri_2, tri_3, tri_4).arrange(buff=1))


class PNG_4_1(Scene):
    def construct(self):
        self.add(NumberPlane().add_coordinates())


"图4.2来源于互联网"


class PNG_4_3(Scene):
    def construct(self):
        A = VGroup(
            *[MathTex(r"A_"+str(i)).set_stroke(width=1) for i in range(5)]
        ).arrange(buff=0.5)
        B = VGroup(
            *[MathTex(r"B_"+str(i)).set_stroke(width=1) for i in range(3)]
        ).arrange(buff=0.5)

        B.next_to(A, DOWN, aligned_edge=LEFT, 
                  submobject_to_align=B[1], 
                  index_of_submobject_to_align=2)

        self.add(A, B)


class PNG_4_4(Scene):
    def construct(self):
        boxes = VGroup(*[Square(2-0.2*s) for s in range(0,6)])
        boxes.arrange_in_grid(rows=2, buff=0.3)
        self.add(boxes)


class PNG_4_5(Scene):
    def construct(self):
        boxes=VGroup(*[Square(2-0.2*s) for s in range(0,6)])
        boxes.arrange_in_grid(
            rows=2,
            buff=0.3,
            cell_alignment=UL,
        )
        self.add(boxes)


class PNG_4_6(Scene):
    def construct(self):
        boxes=VGroup(*[Square(2-0.2*s) for s in range(0,6)])
        boxes.arrange_in_grid(
            rows=2,
            buff=(0.3, 1),
            cell_alignment=UL,
            flow_order="lu",
        )
        self.add(boxes)