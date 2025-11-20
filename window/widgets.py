import os
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLineEdit, QLabel, 
    QTextEdit, QSpinBox, QGroupBox
)
from PySide6.QtCore import Signal, Qt

# --- カスタムウィジェット ---

class RecordingSettingsWidget(QGroupBox):
    """
    録音時間の設定と、録音開始ボタンを含むウィジェット。
    """
    # 録音開始をリクエストするシグナル (引数: 録音時間[秒])
    recording_start_requested = Signal(int)

    def __init__(self, parent=None):
        super().__init__("録音設定と操作", parent)
        self.layout = QVBoxLayout(self)
        
        # 1. 録音時間設定 (QSpinBoxを使用し、数値入力に限定)
        time_layout = QHBoxLayout()
        time_layout.addWidget(QLabel("録音時間 (秒):"))
        
        self.time_label = QLabel("10") 
        time_layout.addWidget(self.time_label)
        
        time_layout.addStretch(1)
        self.layout.addLayout(time_layout)
        
        # 2. 録音開始ボタン
        self.record_button = QPushButton("🔴 録音開始")
        self.record_button.clicked.connect(self._on_record_clicked)
        self.layout.addWidget(self.record_button)

    def _on_record_clicked(self):
        """
        録音ボタンがクリックされたときにシグナルを発火させる。
        """
        record_seconds = 10 
        self.recording_start_requested.emit(record_seconds)
        
    def set_recording_active(self, active: bool):
        """録音中のUI状態を切り替える (リーダーが使用)"""
        self.record_button.setEnabled(not active)
        self.time_input.setEnabled(not active)
        if active:
            self.record_button.setText("録音中...")
        else:
            self.record_button.setText("🔴 録音開始")


class ProcessAndSaveWidget(QGroupBox):
    """
    文字起こし実行ボタンと結果保存ボタンを含むウィジェット。
    """
    # 文字起こし開始をリクエストするシグナル
    transcribe_requested = Signal()
    # 結果保存をリクエストするシグナル
    save_requested = Signal()

    def __init__(self, parent=None):
        super().__init__("文字起こしと保存", parent)
        self.layout = QVBoxLayout(self)
        
        # 1. 文字起こし実行ボタン
        self.transcribe_button = QPushButton("🔊 文字起こし実行")
        self.transcribe_button.clicked.connect(self.transcribe_requested.emit)
        self.layout.addWidget(self.transcribe_button)
        
        # 2. 結果保存ボタン
        self.save_button = QPushButton("💾 結果をファイルに保存")
        self.save_button.clicked.connect(self.save_requested.emit)
        self.layout.addWidget(self.save_button)
        
        # 初期状態では無効にしておく (録音完了後に有効化される想定)
        self.set_processing_enabled(False)

    def set_processing_enabled(self, enabled: bool):
        """ボタンの有効/無効を切り替える (リーダーが使用)"""
        self.transcribe_button.setEnabled(enabled)
        self.save_button.setEnabled(enabled)


class StatusAndResultWidget(QWidget):
    """
    現在のステータス表示と文字起こし結果を表示するエリア。
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # 1. ステータス表示
        self.status_label = QLabel("待機中...")
        self.status_label.setStyleSheet("font-weight: bold; padding: 5px;")
        self.layout.addWidget(self.status_label)
        
        # 2. 結果表示エリア
        self.result_text = QTextEdit()
        self.result_text.setPlaceholderText("文字起こし結果がここに表示されます...")
        self.layout.addWidget(self.result_text)

    def set_status(self, message: str, is_error: bool = False):
        """ステータスメッセージを設定する (リーダーが使用)"""
        if is_error:
            self.status_label.setStyleSheet("font-weight: bold; color: red; padding: 5px;")
        else:
            self.status_label.setStyleSheet("font-weight: bold; color: black; padding: 5px;")
        self.status_label.setText(message)

    def set_result_text(self, text: str):
        """結果テキストを設定する (リーダーが使用)"""
        self.result_text.setText(text)
        self.result_text.repaint()
        
    def get_result_text(self) -> str:
        """現在の結果テキストを取得する (リーダー/保存担当が使用)"""
        return self.result_text.toPlainText()