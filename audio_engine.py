# audio_engine.py

import numpy as np
from scipy.io.wavfile import write


class AudioEngine:

    def __init__(
        self,
        sample_rate=44100,
        duration=180
    ):
        self.sample_rate = sample_rate
        self.duration = duration

    def _time_array(self):

        return np.linspace(
            0,
            self.duration,
            int(self.sample_rate * self.duration),
            endpoint=False
        )

    def _sine_wave(
        self,
        frequency,
        amplitude=1.0
    ):

        t = self._time_array()

        return (
            amplitude *
            np.sin(
                2 * np.pi *
                frequency *
                t
            )
        )

    def _cosmic_ambient(self):

        t = self._time_array()

        noise = np.random.normal(
            0,
            1,
            len(t)
        )

        kernel_size = 2500

        kernel = np.ones(
            kernel_size
        ) / kernel_size

        smooth = np.convolve(
            noise,
            kernel,
            mode="same"
        )

        smooth *= 0.15

        return smooth

    def _fade_in_out(
        self,
        wave
    ):

        fade_seconds = 5

        fade_samples = (
            self.sample_rate *
            fade_seconds
        )

        fade_in = np.linspace(
            0,
            1,
            fade_samples
        )

        fade_out = np.linspace(
            1,
            0,
            fade_samples
        )

        wave[:fade_samples] *= fade_in

        wave[-fade_samples:] *= fade_out

        return wave

    def generate(
        self,
        personal_frequency,
        output_file="manifestation_audio.wav"
    ):

        print()
        print("Generating Audio Ritual...")

        base = self._sine_wave(
            personal_frequency,
            0.55
        )

        harmonic_1 = self._sine_wave(
            personal_frequency * 1.5,
            0.20
        )

        harmonic_2 = self._sine_wave(
            personal_frequency * 2.0,
            0.15
        )

        harmonic_3 = self._sine_wave(
            personal_frequency * 3.0,
            0.08
        )

        cosmic_bed = self._sine_wave(
            432,
            0.10
        )

        ambient = self._cosmic_ambient()

        wave = (
            base +
            harmonic_1 +
            harmonic_2 +
            harmonic_3 +
            cosmic_bed +
            ambient
        )

        wave = self._fade_in_out(
            wave
        )

        wave /= np.max(
            np.abs(wave)
        )

        audio = np.int16(
            wave * 32767
        )

        write(
            output_file,
            self.sample_rate,
            audio
        )

        print(
            f"Audio Saved: {output_file}"
        )

        return output_file


if __name__ == "__main__":

    engine = AudioEngine()

    engine.generate(
        personal_frequency=528,
        output_file="ritual.wav"
    )