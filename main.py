import sys
from PySide6.QtWidgets import QApplication

# 各モジュールのインポート
from window.gui_main import MainWindow
from controller import AudioController

# ※ 注意: 実行するには record.py, audio2text.py, save.py が存在する必要があります。
# テスト用にダミーが必要な場合は、空のファイルを作成してください。

def main():
    # 1. アプリケーションの作成
    app = QApplication(sys.argv)
    
    # 2. メインウィンドウの作成 (View)
    window = MainWindow()
    
    # 3. コントローラーの作成 (Controller)
    # ウィンドウ(View)をコントローラーに渡し、コントローラーがUIを操作できるようにする
    controller = AudioController(ui=window)
    
    # ==========================================
    # 🔗 シグナルとスロットの接続 (Binding)
    # ==========================================
    
    # --- A. 録音ボタンが押されたとき ---
    # Widgetのシグナル(seconds) -> Controllerの録音処理へ
    # ※ controller.handle_record_audioは引数を取らない仕様になっているため、lambdaで調整するか、
    # controller側を修正する必要があります。ここでは一旦lambdaで呼び出します。
    window.recording_settings.recording_start_requested.connect(
        lambda seconds: controller.handle_record_audio()
    )
    
    # --- B. 文字起こしボタンが押されたとき ---
    window.process_save.transcribe_requested.connect(
        controller.handle_transcribe_audio
    )
    
    # --- C. 保存ボタンが押されたとき ---
    window.process_save.save_requested.connect(
        controller.handle_save_transcription
    )

    # 4. アプリケーションの開始
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()