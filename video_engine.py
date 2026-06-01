# video_engine.py

import math
import tempfile
import numpy as np

from PIL import (
    Image,
    ImageDraw,
    ImageFont
)

from moviepy.editor import (
    ImageClip,
    CompositeVideoClip,
    AudioFileClip,
    VideoClip
)


class VideoEngine:

    def __init__(
        self,
        # width=1280,
        # height=720,
        # duration=180, 
        # fps=24        
        width=1280,
        height=720,
        duration=30, 
        fps=24
    ):

        self.width = width
        self.height = height
        self.duration = duration
        self.fps = fps

        self.cx = width // 2
        self.cy = height // 2

    # ==========================================
    # TEXT OVERLAY
    # ==========================================

    def _create_text_image(
        self,
        text,
        fontsize=70
    ):

        image = Image.new(
            "RGBA",
            (self.width, self.height),
            (0, 0, 0, 0)
        )

        draw = ImageDraw.Draw(image)

        try:
            font = ImageFont.truetype(
                "/System/Library/Fonts/Supplemental/Arial.ttf",
                fontsize
            )
        except:
            font = ImageFont.load_default()

        bbox = draw.multiline_textbbox(
            (0, 0),
            text,
            font=font,
            align="center"
        )

        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = (self.width - text_width) // 2
        y = (self.height - text_height) // 2

        draw.multiline_text(
            (x, y),
            text,
            font=font,
            fill=(255, 255, 255, 255),
            align="center"
        )

        filename = (
            tempfile.mktemp(
                suffix=".png"
            )
        )

        image.save(filename)

        return filename

    # ==========================================
    # PARTICLES
    # ==========================================

    def _particle_frame(self, t):

        frame = np.zeros(
            (
                self.height,
                self.width,
                3
            ),
            dtype=np.uint8
        )

        particle_count = 200

        for i in range(particle_count):

            angle = (
                i * 0.618 +
                t * 0.4
            )

            radius = (
                (i * 5)
                % 350
            )

            x = int(
                self.cx +
                math.cos(angle) * radius
            )

            y = int(
                self.cy +
                math.sin(angle) * radius
            )

            if (
                0 <= x < self.width and
                0 <= y < self.height
            ):

                frame[
                    max(0, y-2):min(self.height, y+2),
                    max(0, x-2):min(self.width, x+2)
                ] = (
                    255,
                    255,
                    255
                )

        return frame

    # ==========================================
    # BACKGROUND
    # ==========================================

    def _build_cosmic_background(self):

        return VideoClip(
            self._particle_frame,
            duration=self.duration
        )

    # ==========================================
    # MANDALA
    # ==========================================

    def _build_mandala(
        self,
        mandala_file
    ):

        return (
            ImageClip(mandala_file)
            .set_duration(
                self.duration
            )
            .resize(height=500)
            .set_position("center")
        )

    # ==========================================
    # TITLE
    # ==========================================

    def _build_title(self):

        png = self._create_text_image(
            "PORTAL MANIFESTASI\nSEMESTA DIGITAL",
            fontsize=70
        )

        return (
            ImageClip(png)
            .set_start(0)
            .set_end(20)
        )

    # ==========================================
    # SEAL
    # ==========================================

    def _build_seal(
        self,
        manifestation_id,
        seal
    ):

        png = self._create_text_image(
            f"{manifestation_id}\n\n{seal}",
            fontsize=60
        )

        return (
            ImageClip(png)
            .set_start(120)
            .set_end(170)
        )

    # ==========================================
    # CLOSING
    # ==========================================

    def _build_closing(self):

        png = self._create_text_image(
            "PORTAL CLOSED\n\nREQUEST ACCEPTED",
            fontsize=70
        )

        return (
            ImageClip(png)
            .set_start(170)
            .set_end(180)
        )

    # ==========================================
    # RENDER
    # ==========================================

    def render(
        self,
        mandala_file,
        audio_file,
        manifestation_id,
        seal,
        output_file="ritual.mp4"
    ):

        print()
        print(
            "Rendering Ritual Video..."
        )

        background = (
            self._build_cosmic_background()
        )

        mandala = (
            self._build_mandala(
                mandala_file
            )
        )

        title = (
            self._build_title()
        )

        seal_clip = (
            self._build_seal(
                manifestation_id,
                seal
            )
        )

        closing = (
            self._build_closing()
        )

        final = CompositeVideoClip(
            [
                background,
                mandala,
                title,
                seal_clip,
                closing
            ],
            size=(
                self.width,
                self.height
            )
        )

        audio = AudioFileClip(
            audio_file
        )

        final = (
            final
            .set_audio(audio)
            .set_duration(
                self.duration
            )
        )

        final.write_videofile(
            output_file,
            fps=self.fps,
            codec="libx264",
            audio_codec="aac",
            preset="medium",
            bitrate="2500k"
        )

        return output_file