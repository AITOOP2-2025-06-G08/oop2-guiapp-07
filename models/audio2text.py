#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mlx_whisper
import os

# 音声ファイルを指定して文字起こし
def audio_to_text(audio_file_path: str) -> str:
    print(f"文字起こしを開始: {audio_file_path}")
    # 音声ファイルが存在しない場合は空文字を返す
    if not os.path.exists(audio_file_path):
        print(f"音声ファイルが見つかりません: {audio_file_path}")
        return ""
    result = mlx_whisper.transcribe(
      audio_file_path, path_or_hf_repo="whisper-base-mlx"
    )
    print(f"文字起こしが完了:\n{result["text"]}。")
    return result["text"]

if __name__ == "__main__":
    audio_file = "record_audio_output.wav"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    audio_file = os.path.join(script_dir, audio_file)
    text = audio_to_text(audio_file_path=audio_file)
    print(text)