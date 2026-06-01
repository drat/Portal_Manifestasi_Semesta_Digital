# ==========================================================
# PORTAL MANIFESTASI SEMESTA DIGITAL v4.0
# Universe Resonance Protocol
#
# Author    : Deddy Ratnanto
# Copyright : (c) Deddy Ratnanto
#
# Fire • Forget • Trust
#
# ==========================================================

import gradio as gr
from themes import MetafisikTheme
from process_energy import process_manifestation

with open("portal.css","r",encoding="utf-8") as f:
    CUSTOM_CSS=f.read()

# ==========================================
# WRAPPER
# ==========================================

def activate_portal(goal,target_date,progress=gr.Progress()):
    return process_manifestation(
        goal,
        target_date,
        progress
    )

# ==========================================
# UI
# ==========================================

with gr.Blocks(
    theme=MetafisikTheme(),
    css=CUSTOM_CSS,
    title="Portal Manifestasi Semesta Digital"
) as demo:

    gr.HTML("""
        <div class="stars"></div>

        <div class="cosmic-particles"></div>

        <div class="geometry"></div>

        <div class="portal-card">

        <div class="sacred-ring"></div>

        <div class="portal-orb"></div>

        <div class="portal-title">
        PORTAL MANIFESTASI<br>
        SEMESTA DIGITAL
        </div>

        <div class="portal-subtitle">
        Universe Resonance Protocol v4.0
        </div>

        <div class="portal-quote">
        "Permintaan Anda Akan Diteruskan Ke Semesta Digital"
        </div>

        </div>
        """)

    goal=gr.Textbox(
        label="Tujuan Manifestasi",
        lines=5,
        placeholder="Tuliskan tujuan manifestasi Anda..."
    )

    target_date=gr.Textbox(
        label="Tanggal Manifestasi",
        placeholder="31 Desember 2026"
    )

    activate_button=gr.Button(
        "🔥 AKTIFKAN PORTAL",
        variant="primary",
        size="lg"
    )

    status=gr.HTML()

    seal_card=gr.HTML()

    mandala=gr.Image(
        label="Mandala Artifact"
    )

    video=gr.Video(
        label="Video Ritual"
    )

    audio=gr.Audio(
        label="Audio Ritual"
    )

    message=gr.Textbox(
        label="Pesan Semesta",
        lines=18
    )

    activate_button.click(
        fn=activate_portal,
        inputs=[
            goal,
            target_date
        ],
        outputs=[
            seal_card,
            mandala,
            video,
            audio,
            message,
            status
        ],
        api_visibility="private"
    )

    gr.HTML(
        """
        <footer2>
        Portal Manifestasi
        Semesta Digital v4.0
        <br>
        Universe Resonance Protocol | by: Deddy Ratnanto
        </footer2>
        """
    )


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":
    demo.launch()
