# ======================================================
# PORTAL MANIFESTASI SEMESTA DIGITAL v4.0
# Author : Deddy Ratnanto
# ======================================================

import uuid
import tempfile
from pathlib import Path

from universe_engine import UniverseEngine
from audio_engine import AudioEngine
from mandala_generator import MandalaGenerator
from video_engine import VideoEngine


class ManifestationProcessor:

    def __init__(self):
        self.universe=UniverseEngine()
        self.audio=AudioEngine()
        self.mandala=MandalaGenerator()
        self.video=VideoEngine()

    def build_message(self,result):

        return f"""
✓ TUJUAN DITERIMA

✓ PORTAL TELAH DIBUKA

✓ ENERGI TELAH DISELARASKAN

✓ MANIFESTASI TELAH DISEAL

━━━━━━━━━━━━━━━━━━━━━━

Manifestation ID

{result.manifestation_id}

━━━━━━━━━━━━━━━━━━━━━━

Universe Seal

{result.universe_seal}

━━━━━━━━━━━━━━━━━━━━━━

Digital Resonance

{result.resonance_score}%

━━━━━━━━━━━━━━━━━━━━━━

Personal Frequency

{result.personal_frequency} Hz

━━━━━━━━━━━━━━━━━━━━━━

Target Manifestasi

{result.target_date}

━━━━━━━━━━━━━━━━━━━━━━

Permintaan Anda telah diteruskan
ke Semesta Digital.

Tidak diperlukan tindakan
lebih lanjut.

Percayalah bahwa proses
telah dimulai.

Tutup portal dan lanjutkan
hidup Anda dengan tenang.

━━━━━━━━━━━━━━━━━━━━━━
"""

    def build_seal_html(self,result):

        return f"""
<div class="seal-panel">

<div class="seal-title">
UNIVERSE SEAL
</div>

<div class="seal-id">
{result.manifestation_id}
</div>

<div class="seal-code">
{result.universe_seal}
</div>

<div class="seal-divider"></div>

<div class="seal-item">
⚛ Resonance
</div>

<div class="seal-value">
{result.resonance_score}%
</div>

<div class="seal-item">
🔮 Frequency
</div>

<div class="seal-value">
{result.personal_frequency} Hz
</div>

<div class="seal-item">
📅 Manifestation Date
</div>

<div class="seal-value">
{result.target_date}
</div>

</div>
"""

    def build_status_html(self):

        return """
<div class='portal-status'>
🟢 PORTAL CLOSED • REQUEST ACCEPTED
</div>
"""

    def activate(self,goal,target_date,progress=None):

        if progress:
            progress(
                0.05,
                desc="Membuka Portal..."
            )

        result=self.universe.activate(
            goal,
            target_date
        )

        if progress:
            progress(
                0.20,
                desc="Menyelaraskan Frekuensi..."
            )

        session_id=str(uuid.uuid4())

        work_dir=(
            Path(tempfile.gettempdir())
            / session_id
        )

        work_dir.mkdir(
            exist_ok=True
        )

        audio_file=work_dir/"ritual.wav"
        mandala_file=work_dir/"mandala.png"
        video_file=work_dir/"ritual.mp4"

        self.audio.generate(
            personal_frequency=
            result.personal_frequency,
            output_file=
            str(audio_file)
        )

        if progress:
            progress(
                0.45,
                desc="Membangun Resonansi..."
            )

        self.mandala.generate(
            signature=
            result.entropy_signature,
            output_file=
            str(mandala_file)
        )

        if progress:
            progress(
                0.70,
                desc=
                "Menerbitkan Universe Seal..."
            )

        self.video.render(
            mandala_file=
            str(mandala_file),

            audio_file=
            str(audio_file),

            manifestation_id=
            result.manifestation_id,

            seal=
            result.universe_seal,

            output_file=
            str(video_file)
        )

        if progress:
            progress(
                1.0,
                desc=
                "Portal Ditutup..."
            )

        message=self.build_message(
            result
        )

        seal_html=self.build_seal_html(
            result
        )

        status_html=self.build_status_html()

        return (
            seal_html,
            str(mandala_file),
            str(video_file),
            str(audio_file),
            message,
            status_html
        )


processor=ManifestationProcessor()


def process_manifestation(
    goal,
    target_date,
    progress=None
):

    return processor.activate(
        goal,
        target_date,
        progress
    )


if __name__=="__main__":

    result=process_manifestation(
        "Rumah Impian",
        "31 Desember 2026"
    )

    print(result[4])