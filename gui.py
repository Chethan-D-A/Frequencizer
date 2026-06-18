from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QComboBox,
    QSlider,
    QCheckBox,
    QStatusBar,
    QDialog,
    QTextEdit,
    QVBoxLayout
)

from audio_engine import (
    start_playback,
    stop_playback,
    update_volume,
    update_frequency,
    update_waveform,
    update_binaural,
    generate_waveform,
    generate_binaural_waveform,
    export_wav
)

from PySide6.QtWidgets import QFileDialog

from PySide6.QtCore import Qt

import sys


class FrequencizerWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Frequencizer v1.0"
        )

        self.resize(
            900,
            700
        )

        self.build_ui()

    def build_ui(self):

        main_layout = QVBoxLayout()

        title = QLabel(
            "Frequencizer v1.0"
        )

        title.setAlignment(
            Qt.AlignCenter
        )

        title.setStyleSheet(
            """
            font-size: 24px;
            font-weight: bold;
            """
        )

        main_layout.addWidget(
            title
        )

        # -------------------------
        # General Settings
        # -------------------------

        general_group = QGroupBox(
            "General Settings"
        )

        general_layout = QVBoxLayout()

        general_layout.addWidget(
            QLabel("Frequency (Hz)")
        )

        self.freq_input = QLineEdit()
        self.freq_input.setText(
            "440"
        )

        general_layout.addWidget(
            self.freq_input
        )

        general_layout.addWidget(
            QLabel("Duration (seconds)")
        )

        self.duration_input = QLineEdit()
        self.duration_input.setText(
            "3"
        )

        general_layout.addWidget(
            self.duration_input
        )

        general_layout.addWidget(
            QLabel("Waveform")
        )

        self.waveform_combo = QComboBox()

        self.waveform_combo.addItems([
            "Sine",
            "Square",
            "Triangle",
            "Sawtooth"
        ])

        general_layout.addWidget(
            self.waveform_combo
        )

        general_layout.addWidget(
            QLabel("Volume")
        )

        self.volume_slider = QSlider(
            Qt.Horizontal
        )

        self.volume_slider.setRange(
            0,
            100
        )

        self.volume_slider.setValue(
            50
        )

        general_layout.addWidget(
            self.volume_slider
        )

        general_group.setLayout(
            general_layout
        )

        main_layout.addWidget(
            general_group
        )

        # -------------------------
        # Binaural
        # -------------------------

        binaural_group = QGroupBox(
            "Binaural Beats"
        )

        binaural_layout = QVBoxLayout()

        self.enable_binaural = QCheckBox(
            "Enable Binaural"
        )

        binaural_layout.addWidget(
            self.enable_binaural
        )

        binaural_layout.addWidget(
            QLabel("Left Frequency")
        )

        self.left_input = QLineEdit()
        self.left_input.setText(
            "440"
        )

        binaural_layout.addWidget(
            self.left_input
        )

        binaural_layout.addWidget(
            QLabel("Right Frequency")
        )

        self.right_input = QLineEdit()
        self.right_input.setText(
            "444"
        )

        binaural_layout.addWidget(
            self.right_input
        )

        notice = QLabel(
            "Use headphones for binaural beats."
        )

        binaural_layout.addWidget(
            notice
        )

        binaural_group.setLayout(
            binaural_layout
        )

        main_layout.addWidget(
            binaural_group
        )

        # -------------------------
        # Playback
        # -------------------------

        playback_group = QGroupBox(
            "Playback Controls"
        )

        playback_layout = QVBoxLayout()

        self.timed_button = QPushButton(
            "Timed Play"
        )

        self.infinite_button = QPushButton(
            "Infinite Play"
        )

        self.stop_button = QPushButton(
            "Stop"
        )

        playback_layout.addWidget(
            self.timed_button
        )

        playback_layout.addWidget(
            self.infinite_button
        )

        playback_layout.addWidget(
            self.stop_button
        )

        playback_group.setLayout(
            playback_layout
        )

        main_layout.addWidget(
            playback_group
        )

        # -------------------------
        # Export
        # -------------------------

        export_group = QGroupBox(
            "Export"
        )

        export_layout = QVBoxLayout()

        self.export_button = QPushButton(
            "Export WAV"
        )

        export_layout.addWidget(
            self.export_button
        )

        export_group.setLayout(
            export_layout
        )

        main_layout.addWidget(
            export_group
        )

        # -------------------------
        # Status Bar
        # -------------------------

        self.status_bar = QStatusBar()

        self.status_bar.showMessage(
            "Ready"
        )

        main_layout.addWidget(
            self.status_bar
        )

        self.setLayout(
            main_layout
        )

        self.infinite_button.clicked.connect(
            self.play_infinite
        )

        self.timed_button.clicked.connect(
            self.play_timed
        )

        self.stop_button.clicked.connect(
            self.stop_audio
        )

        self.export_button.clicked.connect(
            self.export_audio
        )

        self.guide_button = QPushButton("Guide")

        export_layout.addWidget(
            self.guide_button
        )

        self.guide_button.clicked.connect(
            self.show_guide
        )

        self.volume_slider.valueChanged.connect(
            self.volume_changed
        )

        self.waveform_combo.currentTextChanged.connect(
            self.waveform_changed
        )

        self.freq_input.editingFinished.connect(
            self.frequency_changed
        )

    def show_guide(self):

        guide_text = """
    FREQUENCIZER v1.0 GUIDE

    ========================
    BASIC USAGE
    ========================

    Frequency:
    The frequency of the tone in Hertz (Hz).

    Examples:

    40 Hz   -> Deep bass testing
    100 Hz  -> Speaker testing
    440 Hz  -> Musical reference tone
    1000 Hz -> Hearing and calibration tests

    Waveforms:

    Sine
    - Pure tone
    - Most mathematically simple waveform

    Square
    - Rich in odd harmonics
    - Useful for experiments

    Triangle
    - Softer harmonic content

    Sawtooth
    - Rich harmonic spectrum

    ========================
    BINAURAL BEATS
    ========================

    Binaural beats require:

    ✓ Stereo headphones
    ✓ Different frequencies in each ear

    Example:

    Left Ear  = 440 Hz
    Right Ear = 444 Hz

    Difference = 4 Hz

    The brain perceives an internal 4 Hz beat.

    Without headphones the effect is greatly reduced.

    ========================
    COMMON BINAURAL RANGES
    ========================

    Delta
    0.5 - 4 Hz difference

    Often associated with:
    - Deep sleep
    - Rest

    Theta
    4 - 8 Hz difference

    Often associated with:
    - Meditation
    - Relaxation

    Alpha
    8 - 13 Hz difference

    Often associated with:
    - Calm focus
    - Relaxed alertness

    Beta
    13 - 30 Hz difference

    Often associated with:
    - Active thinking
    - Concentration

    Gamma
    30 - 100 Hz difference

    Often associated with:
    - Information processing
    - Complex cognition

    ========================
    POPULAR FREQUENCY CLAIMS
    ========================

    432 Hz

    Often claimed online to promote:
    - Relaxation
    - Calmness
    - Natural harmony

    Some studies suggest possible physiological differences compared to 440 Hz, but strong scientific conclusions are not established. :contentReference[oaicite:0]{index=0}

    528 Hz

    Often called:
    - Love Frequency
    - Miracle Tone

    Claims include:
    - Healing
    - Transformation
    - DNA repair

    These claims are not supported by robust scientific evidence.

    Solfeggio Frequencies

    174 Hz
    285 Hz
    396 Hz
    417 Hz
    528 Hz
    639 Hz
    741 Hz
    852 Hz
    963 Hz

    Many benefits are claimed online.

    Scientific evidence remains limited.

    ========================
    IMPORTANT DISCLAIMER
    ========================

    Frequencizer is a signal generation tool.

    It does NOT provide:

    - Medical treatment
    - Mental health treatment
    - Cognitive enhancement guarantees
    - Healing guarantees

    Research on binaural beats shows mixed results.
    Some studies report benefits while others show little effect or inconsistent outcomes. :contentReference[oaicite:1]{index=1}

    Use Frequencizer for:

    ✓ Education
    ✓ Audio testing
    ✓ Experimentation
    ✓ Exploration

    Evaluate extraordinary claims critically.
    """

        guide_dialog = QDialog(self)

        guide_dialog.setWindowTitle(
            "Frequencizer Guide"
        )

        guide_dialog.resize(
            800,
            600
        )

        layout = QVBoxLayout()

        text_box = QTextEdit()

        text_box.setReadOnly(True)

        text_box.setPlainText(
            guide_text
        )

        layout.addWidget(
            text_box
        )

        guide_dialog.setLayout(
            layout
        )

        guide_dialog.exec()

    def get_binaural_state(self):

        try:

            update_binaural(
                self.enable_binaural.isChecked(),
                float(self.left_input.text()),
                float(self.right_input.text())
            )

        except:
            pass

    def play_infinite(self):

        try:

            self.get_binaural_state()

            frequency = float(
                self.freq_input.text()
            )

            waveform = (
                self.waveform_combo.currentText()
            )

            volume = (
                    self.volume_slider.value() / 100
            )

            start_playback(
                frequency,
                waveform,
                volume
            )

            self.status_bar.showMessage(
                "Infinite Playback"
            )

        except Exception as e:

            self.status_bar.showMessage(
                str(e)
            )

    def play_timed(self):

        try:

            self.play_infinite()

            duration = float(
                self.duration_input.text()
            )

            from PySide6.QtCore import QTimer

            QTimer.singleShot(
                int(duration * 1000),
                self.stop_audio
            )

            self.status_bar.showMessage(
                f"Timed Playback ({duration}s)"
            )

        except Exception as e:

            self.status_bar.showMessage(
                str(e)
            )

    def stop_audio(self):

        stop_playback()

        self.status_bar.showMessage(
            "Stopped"
        )

    def volume_changed(self, value):

        update_volume(
            value / 100
        )

    def waveform_changed(self):

        update_waveform(
            self.waveform_combo.currentText()
        )

    def frequency_changed(self):

        try:

            update_frequency(
                float(
                    self.freq_input.text()
                )
            )

        except:
            pass

    def export_audio(self):

        try:

            duration = float(
                self.duration_input.text()
            )

            volume = (
                    self.volume_slider.value() / 100
            )

            waveform_type = (
                self.waveform_combo.currentText()
            )

            self.get_binaural_state()

            if self.enable_binaural.isChecked():

                waveform = (
                    generate_binaural_waveform(
                        waveform_type,
                        float(
                            self.left_input.text()
                        ),
                        float(
                            self.right_input.text()
                        ),
                        duration,
                        volume
                    )
                )

            else:

                waveform = (
                    generate_waveform(
                        waveform_type,
                        float(
                            self.freq_input.text()
                        ),
                        duration,
                        volume
                    )
                )

            filename, _ = (
                QFileDialog.getSaveFileName(
                    self,
                    "Export WAV",
                    "",
                    "WAV Files (*.wav)"
                )
            )

            if filename:
                export_wav(
                    filename,
                    waveform
                )

                self.status_bar.showMessage(
                    "WAV Export Successful"
                )

        except Exception as e:

            self.status_bar.showMessage(
                str(e)
            )

def start_app():

    app = QApplication(
        sys.argv
    )

    app.setStyleSheet(
        """
        QWidget {
            background-color: #202124;
            color: white;
            font-size: 13px;
        }

        QLineEdit,
        QComboBox {
            background-color: #2d2f31;
            border: 1px solid #555;
            padding: 5px;
        }

        QPushButton {
            background-color: #303134;
            border: 1px solid #666;
            padding: 8px;
        }

        QPushButton:hover {
            background-color: #3a3c3f;
        }

        QGroupBox {
            border: 1px solid #555;
            margin-top: 10px;
            padding-top: 10px;
            font-weight: bold;
        }

        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 5px;
        }
        """
    )

    window = FrequencizerWindow()

    window.show()

    sys.exit(
        app.exec()
    )

