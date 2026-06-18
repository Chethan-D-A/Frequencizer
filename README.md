# Frequencizer

An offline frequency generator built with Python and PySide6.

Frequencizer allows users to generate pure tones, experiment with binaural beats, export WAV files, and explore audio frequencies through a modern desktop interface.

---

## Features

* Sine Wave Generation
* Square Wave Generation
* Triangle Wave Generation
* Sawtooth Wave Generation
* Infinite Playback
* Timed Playback
* Live Volume Control
* Live Frequency Updates
* Binaural Beats Support
* Stereo WAV Export
* Built-in Guide Window
* Fully Offline Operation
* Cross-Platform Python Code

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Chethan-D-A/Frequencizer.git
cd Frequencizer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

## Requirements

* Python 3.10+
* NumPy
* SciPy
* SoundDevice
* PySide6

---

## Project Structure

```text
Frequencizer/
├── main.py
├── gui.py
├── audio_engine.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Binaural Beats

Binaural beats require:

* Stereo headphones
* Different frequencies in each ear

Example:

```text
Left Ear  = 440 Hz
Right Ear = 444 Hz
Difference = 4 Hz
```

The perceived binaural beat is the frequency difference between the two channels.

---

## Scientific Disclaimer

Frequencizer is a signal generation tool intended for:

* Education
* Audio Testing
* Experimentation
* Personal Exploration

Research on binaural beats remains mixed. Some studies report effects on relaxation, mood, attention, or sleep, while others find weak or inconsistent results.

Frequencizer does not provide:

* Medical treatment
* Mental health treatment
* Cognitive enhancement guarantees
* Healing guarantees

Claims regarding frequency healing, DNA repair, intelligence enhancement, or similar effects should be evaluated critically.

---

## Platform Support

Tested on:
- Windows

Expected to work on:
- Linux
- macOS

---

## License

Released under the MIT License.
