#!/usr/bin/env python
# -*- coding: utf-8 -*-

import audio2text
import os

def save_transcription_to_file(audio_file_path: str, output_filename: str) -> None:
    """
    指定された音声ファイルを文字起こしした結果を指定されたテキストファイルに保存する

    Parameters
    ----------
        audio_file_path : str
            文字起こしを行う音声ファイルのパス
        output_filename : str 
            文字起こし結果を保存するテキストファイルのパス
    """
    # 音声ファイルの存在確認
    if not os.path.exists(audio_file_path):
        print(f"音声ファイルが見つかりません: {audio_file_path}")
        return
    # 音声ファイルを文字起こし
    text = audio2text.audio_to_text(audio_file_path)
    # 文字起こし結果をファイルに保存
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_filename = get_filename(os.path.splitext(output_filename)[0], "txt")
    save_path = os.path.join(script_dir, output_filename)
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"文字起こし結果が保存されました: {save_path}")
        

def get_filename(basename = "result", ext = "txt") -> str:
    """
    既存ファイルと重複しない新しいファイル名を生成する。

    Parameters
    ----------
    basename : str, optional
        ファイル名のベース（デフォルト: "result"）
    ext : str, optional
        拡張子（デフォルト: "txt"）

    Returns
    -------
    str
        重複しない新しいファイル名
    """
    i = 0
    while True:
        # 最初のファイル名が存在しない場合はそれを返す
        if os.path.exists(f"{basename}.{ext}") is False and i == 0:
            return f"{basename}.{ext}"
        # 2つ目以降のファイル名をチェック
        filename = f"{basename}({i+1}).{ext}"
        if not os.path.exists(filename):
            # 存在しない場合はそのファイル名を返す
            return filename
        i += 1
