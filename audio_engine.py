import numpy as np
from scipy import signal
from scipy.io.wavfile import write
import sounddevice as sd

SAMPLE_RATE = 44100

stream = None
phase = 0

current_frequency = 440.0
current_volume = 0.5
current_waveform = "Sine"

binaural_enabled = False
left_frequency = 440.0
right_frequency = 444.0


def generate_waveform(
    waveform_type,
    frequency,
    duration,
    amplitude
):
    t = np.linspace(
        0,
        duration,
        int(duration * SAMPLE_RATE),
        endpoint=False
    )

    if waveform_type == "Sine":
        wave = np.sin(
            2 * np.pi * frequency * t
        )

    elif waveform_type == "Square":
        wave = signal.square(
            2 * np.pi * frequency * t
        )

    elif waveform_type == "Triangle":
        wave = signal.sawtooth(
            2 * np.pi * frequency * t,
            width=0.5
        )

    else:
        wave = signal.sawtooth(
            2 * np.pi * frequency * t
        )

    return amplitude * wave


def generate_binaural_waveform(
    waveform_type,
    left_freq,
    right_freq,
    duration,
    amplitude
):
    left = generate_waveform(
        waveform_type,
        left_freq,
        duration,
        amplitude
    )

    right = generate_waveform(
        waveform_type,
        right_freq,
        duration,
        amplitude
    )

    return np.column_stack(
        (left, right)
    )


def export_wav(filename, waveform):
    audio_data = (
        waveform * 32767
    ).astype(np.int16)

    write(
        filename,
        SAMPLE_RATE,
        audio_data
    )


def audio_callback(
    outdata,
    frames,
    time_info,
    status
):
    global phase

    t = (
        np.arange(frames) + phase
    ) / SAMPLE_RATE

    def make_wave(freq):

        if current_waveform == "Sine":
            return np.sin(
                2 * np.pi * freq * t
            )

        elif current_waveform == "Square":
            return signal.square(
                2 * np.pi * freq * t
            )

        elif current_waveform == "Triangle":
            return signal.sawtooth(
                2 * np.pi * freq * t,
                width=0.5
            )

        else:
            return signal.sawtooth(
                2 * np.pi * freq * t
            )

    if binaural_enabled:

        left_wave = make_wave(
            left_frequency
        )

        right_wave = make_wave(
            right_frequency
        )

        stereo = np.column_stack(
            (
                left_wave * current_volume,
                right_wave * current_volume
            )
        )

        outdata[:] = stereo

    else:

        mono = (
            make_wave(
                current_frequency
            ) * current_volume
        )

        stereo = np.column_stack(
            (mono, mono)
        )

        outdata[:] = stereo

    phase += frames


def start_playback(
    frequency,
    waveform,
    volume
):
    global stream
    global current_frequency
    global current_waveform
    global current_volume
    global phase

    current_frequency = frequency
    current_waveform = waveform
    current_volume = volume

    if stream is None:

        phase = 0

        stream = sd.OutputStream(
            samplerate=SAMPLE_RATE,
            channels=2,
            callback=audio_callback
        )

        stream.start()


def update_volume(volume):
    global current_volume
    current_volume = volume


def update_frequency(frequency):
    global current_frequency
    current_frequency = frequency


def update_waveform(waveform):
    global current_waveform
    current_waveform = waveform


def update_binaural(
    enabled,
    left_freq,
    right_freq
):
    global binaural_enabled
    global left_frequency
    global right_frequency

    binaural_enabled = enabled
    left_frequency = left_freq
    right_frequency = right_freq


def stop_playback():
    global stream

    if stream is not None:

        stream.stop()
        stream.close()

        stream = None