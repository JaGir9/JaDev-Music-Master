from __future__ import annotations

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from .core.project import AudioProject


class SidebarButton(QPushButton):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        self.setCheckable(True)
        self.setMinimumHeight(42)


class DashboardPage(QWidget):
    def __init__(self, project: AudioProject) -> None:
        super().__init__()
        self.project = project

        root = QVBoxLayout(self)
        root.setSpacing(14)

        title = QLabel("JaDev Music Master")
        title.setObjectName("PageTitle")
        subtitle = QLabel("Adaptive Audio Production & Mastering Workstation")
        subtitle.setObjectName("PageSubtitle")

        hero = QFrame()
        hero.setObjectName("HeroCard")
        hero_layout = QVBoxLayout(hero)
        hero_layout.setContentsMargins(26, 24, 26, 24)

        hero_title = QLabel("FULL AUTO")
        hero_title.setObjectName("HeroTitle")
        hero_text = QLabel(
            "Drop music, analyze each track independently, apply conservative adaptive "
            "processing, run quality control, and export a lossless master."
        )
        hero_text.setWordWrap(True)

        add_btn = QPushButton("Add Audio Files")
        add_btn.setObjectName("PrimaryButton")
        add_btn.clicked.connect(self.add_files)

        self.queue = QListWidget()
        self.queue.setObjectName("Queue")
        self.queue.setMinimumHeight(220)

        process_btn = QPushButton("Analyze / Process Queue")
        process_btn.setObjectName("PrimaryButton")
        process_btn.clicked.connect(self.process_queue)

        hero_layout.addWidget(hero_title)
        hero_layout.addWidget(hero_text)
        hero_layout.addSpacing(8)
        hero_layout.addWidget(add_btn, 0, Qt.AlignmentFlag.AlignLeft)

        root.addWidget(title)
        root.addWidget(subtitle)
        root.addWidget(hero)
        root.addWidget(QLabel("Processing Queue"))
        root.addWidget(self.queue)
        root.addWidget(process_btn, 0, Qt.AlignmentFlag.AlignRight)

    def add_files(self) -> None:
        paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Add audio",
            "",
            "Audio (*.wav *.flac *.mp3 *.m4a *.aac *.ogg *.opus *.aiff *.aif *.alac);;All files (*.*)",
        )
        for path in paths:
            self.project.add(path)
            self.queue.addItem(path)

    def process_queue(self) -> None:
        if not self.project.tracks:
            QMessageBox.information(self, "JaDev Music Master", "Add at least one audio file first.")
            return
        QMessageBox.information(
            self,
            "Production scaffold",
            "The professional UI shell and project queue are active. "
            "Audio processing engines are scaffolded next under src/jadev_music_master/core.",
        )


class PlaceholderPage(QWidget):
    def __init__(self, title: str, description: str) -> None:
        super().__init__()
        layout = QVBoxLayout(self)
        heading = QLabel(title)
        heading.setObjectName("PageTitle")
        body = QLabel(description)
        body.setObjectName("PageSubtitle")
        body.setWordWrap(True)
        layout.addWidget(heading)
        layout.addWidget(body)
        layout.addStretch(1)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("JaDev Music Master")
        self.resize(1280, 800)

        self.project = AudioProject()
        host = QWidget()
        self.setCentralWidget(host)
        layout = QHBoxLayout(host)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        sidebar = QFrame()
        sidebar.setObjectName("Sidebar")
        sidebar.setFixedWidth(230)
        side = QVBoxLayout(sidebar)
        side.setContentsMargins(18, 22, 18, 22)
        side.setSpacing(8)

        brand = QLabel("JaDev\nMusic Master")
        brand.setObjectName("Brand")
        side.addWidget(brand)
        side.addSpacing(18)

        self.stack = QStackedWidget()
        pages = [
            ("Dashboard", DashboardPage(self.project)),
            ("Humanize & Master", PlaceholderPage("Humanize & Master", "Adaptive tonal, dynamic, transient, harmonic and stereo processing with safety constraints.")),
            ("Converter", PlaceholderPage("Smart Converter", "Format conversion with source-quality protection and no unnecessary resampling.")),
            ("Merge / Mix", PlaceholderPage("Merge / Mix", "Gapless join, crossfade, loudness matching and future BPM/key-aware transitions.")),
            ("Batch", PlaceholderPage("Batch Processor", "Independent analysis and processing for large audio queues.")),
            ("Quality Control", PlaceholderPage("Quality Control", "Loudness, true-peak, clipping, phase, source-quality and export verification.")),
            ("Settings", PlaceholderPage("Settings", "Output, processing strength, themes, paths, codecs and advanced options.")),
        ]

        self.buttons: list[SidebarButton] = []
        for index, (name, page) in enumerate(pages):
            self.stack.addWidget(page)
            button = SidebarButton(name)
            button.clicked.connect(lambda _checked=False, i=index: self.set_page(i))
            side.addWidget(button)
            self.buttons.append(button)

        side.addStretch(1)
        footer = QLabel("Offline-first • No API key required")
        footer.setObjectName("SidebarFooter")
        footer.setWordWrap(True)
        side.addWidget(footer)

        layout.addWidget(sidebar)
        layout.addWidget(self.stack, 1)

        self.set_page(0)

    def set_page(self, index: int) -> None:
        self.stack.setCurrentIndex(index)
        for i, button in enumerate(self.buttons):
            button.setChecked(i == index)


def _stylesheet() -> str:
    return """
    QWidget {
        background: #0c1017;
        color: #eaf0f7;
        font-family: "Segoe UI";
        font-size: 14px;
    }
    #Sidebar {
        background: #080b10;
        border-right: 1px solid #1b2431;
    }
    #Brand {
        font-size: 24px;
        font-weight: 700;
        color: #ffffff;
    }
    #SidebarFooter {
        color: #778397;
        font-size: 12px;
    }
    QPushButton {
        background: transparent;
        border: 1px solid transparent;
        border-radius: 9px;
        padding: 10px 14px;
        text-align: left;
        color: #aeb9c9;
    }
    QPushButton:hover {
        background: #121a25;
        color: #ffffff;
    }
    QPushButton:checked {
        background: #172334;
        border-color: #263a56;
        color: #ffffff;
    }
    #PrimaryButton {
        background: #2f6df6;
        border: 0;
        color: white;
        font-weight: 600;
        text-align: center;
        padding: 11px 18px;
    }
    #PrimaryButton:hover {
        background: #3c78ff;
    }
    #PageTitle {
        font-size: 30px;
        font-weight: 700;
    }
    #PageSubtitle {
        color: #8d9aae;
        font-size: 14px;
    }
    #HeroCard {
        background: #111823;
        border: 1px solid #202b3b;
        border-radius: 14px;
    }
    #HeroTitle {
        font-size: 18px;
        font-weight: 700;
    }
    #Queue {
        background: #0f151e;
        border: 1px solid #202b3b;
        border-radius: 10px;
        padding: 8px;
    }
    """


def run() -> None:
    app = QApplication(sys.argv)
    app.setApplicationName("JaDev Music Master")
    app.setStyleSheet(_stylesheet())
    window = MainWindow()
    window.show()
    raise SystemExit(app.exec())
