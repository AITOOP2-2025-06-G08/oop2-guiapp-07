# controller.py

from models import record
from models import audio2text
from models import save


class AudioController:
    """
    UIとモデルの橋渡し役（Controller）
    各ボタン（録音 / 文字起こし / 保存）の処理を分割して実行する。
    """

    def __init__(self, ui):
        self.ui = ui
        self.audio_filename = "record_audio_output.wav"      # 録音ファイルの固定名
        self.transcription_filename = "transcription_result.txt"  # 保存用テキスト名
        self.transcribed_text = ""  # 文字起こし結果を保持（UI表示用にも使える）

    # ==============================
    # 🎤 録音ボタン（録音だけ行う）
    # ==============================
    def handle_record_audio(self):
        try:
            self.ui.update_status("録音を開始します...")
            record.record_audio(self.audio_filename, record_seconds=10)
            self.ui.update_status(f"録音完了：{self.audio_filename} に保存しました。")
            self.ui.enable_transcription_ui()
        except Exception as e:
            self.ui.show_error(f"録音でエラーが発生しました: {str(e)}")

    # ==============================
    # ✍ 文字起こしボタン（文字起こしだけ行う）
    # ==============================
    def handle_transcribe_audio(self):
        try:
            self.ui.update_status("文字起こしを開始します...")
            self.transcribed_text = audio2text.audio_to_text(self.audio_filename)
            
            if not self.transcribed_text:
                self.ui.show_error("文字起こしに失敗しました（内容が空です）。")
                return

            # 成功時はUIに表示（表示機能がある前提）
            self.ui.display_transcription(self.transcribed_text)
            self.ui.update_status("文字起こしが完了しました。")
        except Exception as e:
            self.ui.show_error(f"文字起こしでエラーが発生しました: {str(e)}")

    # ==============================
    # 💾 保存ボタン（保存だけ行う）
    # ==============================
    def handle_save_transcription(self):
        try:
            self.ui.update_status("文字起こし結果を保存します...")
            save.save_transcription_to_file(self.audio_filename, self.transcription_filename)
            self.ui.update_status(f"保存完了：{self.transcription_filename}")
        except Exception as e:
            self.ui.show_error(f"保存でエラーが発生しました: {str(e)}")
