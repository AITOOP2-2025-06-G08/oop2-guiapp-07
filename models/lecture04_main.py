#!/usr/bin/env python
# -*- coding: utf-8 -*-


from models import record
from models import save
import os

if __name__ == "__main__":
    # 音声ファイルのパスを設定
    audio_file = "record_audio_output.wav"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    audio_file = os.path.join(script_dir, audio_file)
    # 録音
    record.record_audio(audio_file, record_seconds = 10)
    # 文字起こし結果を保存
    save.save_transcription_to_file(audio_file, "transcription.txt")
