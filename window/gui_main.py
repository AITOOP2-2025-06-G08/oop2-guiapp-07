import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt

# 作成したコンポーネントをインポート
from widgets import RecordingSettingsWidget, ProcessAndSaveWidget, StatusAndResultWidget


class MainWindow(QMainWindow):
    """
    アプリケーションのメインウィンドウ。作成したウィジェットを配置する。
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎤 音声文字起こしアプリ (PySide6)")
        self.setGeometry(100, 100, 800, 600)  # 初期サイズ

        # 中央ウィジェットの設定
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # メインレイアウト (垂直方向)
        main_layout = QVBoxLayout(central_widget)
        
        # --- 1. 操作パネルエリア (水平方向) ---
        control_panel_layout = QHBoxLayout()
        
        # 録音設定ウィジェット 
        self.recording_settings = RecordingSettingsWidget()
        control_panel_layout.addWidget(self.recording_settings)
        
        # 処理/保存ウィジェット 
        self.process_save = ProcessAndSaveWidget()
        control_panel_layout.addWidget(self.process_save)
        
        control_panel_layout.addStretch(1) # 右側にスペースを空ける
        
        main_layout.addLayout(control_panel_layout)
        
        # --- 2. ステータスと結果表示エリア (垂直方向) ---
        self.status_result = StatusAndResultWidget()
        main_layout.addWidget(self.status_result)
        
        # --- リーダーの接続ポイント ---
        # リーダーはここに、ロジッククラス（浅山氏担当）との接続コードを追加します。
        # 例: self.recording_settings.recording_start_requested.connect(self.start_recording)
        # 例: self.process_save.transcribe_requested.connect(self.start_transcription)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())