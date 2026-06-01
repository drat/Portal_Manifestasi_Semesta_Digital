# mandala_generator.py

import math
import random
import hashlib

from PIL import (
    Image,
    ImageDraw
)


class MandalaGenerator:

    def __init__(
        self,
        width=1080,
        height=1080
    ):

        self.width = width
        self.height = height

        self.cx = width // 2
        self.cy = height // 2

    def _seed_from_signature(
        self,
        signature
    ):

        seed = int(
            hashlib.sha256(
                signature.encode()
            ).hexdigest(),
            16
        )

        random.seed(seed)

    def _draw_background(
        self,
        draw
    ):

        for r in range(
            max(self.width, self.height),
            0,
            -4
        ):

            color = (
                int(10 + r * 0.03),
                int(5 + r * 0.02),
                int(25 + r * 0.05)
            )

            draw.ellipse(
                (
                    self.cx - r,
                    self.cy - r,
                    self.cx + r,
                    self.cy + r
                ),
                outline=color
            )

    def _draw_resonance_rings(
        self,
        draw,
        count
    ):

        for i in range(count):

            radius = 80 + i * 40

            alpha = max(
                20,
                255 - i * 15
            )

            color = (
                180,
                120,
                255,
                alpha
            )

            draw.ellipse(
                (
                    self.cx - radius,
                    self.cy - radius,
                    self.cx + radius,
                    self.cy + radius
                ),
                outline=color,
                width=2
            )

    def _draw_flower_of_life(
        self,
        draw,
        layers
    ):

        radius = 70

        for layer in range(1, layers + 1):

            count = layer * 6

            distance = radius * layer

            for i in range(count):

                angle = (
                    2 *
                    math.pi *
                    i /
                    count
                )

                x = (
                    self.cx +
                    math.cos(angle)
                    * distance
                )

                y = (
                    self.cy +
                    math.sin(angle)
                    * distance
                )

                draw.ellipse(
                    (
                        x - radius,
                        y - radius,
                        x + radius,
                        y + radius
                    ),
                    outline=(
                        255,
                        220,
                        120
                    ),
                    width=2
                )

    def _draw_constellation(
        self,
        draw,
        count
    ):

        points = []

        for _ in range(count):

            x = random.randint(
                50,
                self.width - 50
            )

            y = random.randint(
                50,
                self.height - 50
            )

            points.append(
                (x, y)
            )

            draw.ellipse(
                (
                    x - 3,
                    y - 3,
                    x + 3,
                    y + 3
                ),
                fill=(
                    255,
                    255,
                    255
                )
            )

        for _ in range(
            count * 2
        ):

            p1 = random.choice(points)
            p2 = random.choice(points)

            draw.line(
                (
                    p1[0],
                    p1[1],
                    p2[0],
                    p2[1]
                ),
                fill=(
                    80,
                    150,
                    255
                ),
                width=1
            )

    def _draw_core(
        self,
        draw
    ):

        for r in range(
            120,
            0,
            -2
        ):

            draw.ellipse(
                (
                    self.cx - r,
                    self.cy - r,
                    self.cx + r,
                    self.cy + r
                ),
                outline=(
                    255,
                    255,
                    255
                )
            )

    def generate(
        self,
        signature,
        output_file="mandala.png"
    ):

        self._seed_from_signature(
            signature
        )

        image = Image.new(
            "RGB",
            (
                self.width,
                self.height
            ),
            (
                5,
                5,
                15
            )
        )

        draw = ImageDraw.Draw(
            image
        )

        self._draw_background(
            draw
        )

        self._draw_constellation(
            draw,
            random.randint(
                50,
                100
            )
        )

        self._draw_resonance_rings(
            draw,
            random.randint(
                10,
                20
            )
        )

        self._draw_flower_of_life(
            draw,
            random.randint(
                4,
                8
            )
        )

        self._draw_core(
            draw
        )

        image.save(
            output_file
        )

        print(
            f"Mandala Saved: {output_file}"
        )

        return output_file


if __name__ == "__main__":

    signature = """
    5bafeea21932d89f
    a88221dcff9283ab
    99f77e44d1238aa1
    """

    generator = (
        MandalaGenerator()
    )

    generator.generate(
        signature,
        "mandala.png"
    )