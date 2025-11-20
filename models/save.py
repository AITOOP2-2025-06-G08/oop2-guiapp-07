#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import audio2text
import os

def save_transcription_to_file(audio_file_path: str, output_filename: str, output_dir: str = "../outputs") -> None:
    """
    指定された音声ファイルを文字起こしした結果を指定されたフォルダ内のテキストファイルに保存する

    Parameters
    ----------
    audio_file_path : str
        文字起こしを行う音声ファイルのパス
    output_filename : str 
        文字起こし結果を保存するテキストファイル名（拡張子なしでも可）
    output_dir : str, optional
        保存先フォルダ（デフォルト: "outputs"）
    """
    # 音声ファイルの存在確認
    if not os.path.exists(audio_file_path):
        print(f"音声ファイルが見つかりません: {audio_file_path}")
        return

    # フォルダが存在しなければ作成
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir, output_dir)
    os.makedirs(folder_path, exist_ok=True)

    # 音声ファイルを文字起こし
    text = audio2text.audio_to_text(audio_file_path)

    # ファイル名を重複しない形で作成
    output_filename = get_unique_filename(folder_path, os.path.splitext(output_filename)[0], "txt")
    save_path = os.path.join(folder_path, output_filename)

    # ファイルに保存
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"文字起こし結果が保存されました: {save_path}")


def get_unique_filename(folder: str, basename: str = "result", ext: str = "txt") -> str:
    """
    指定フォルダ内で既存ファイルと重複しない新しいファイル名を生成する

    Parameters
    ----------
    folder : str
        ファイルを保存するフォルダ
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
        if i == 0:
            filename = f"{basename}.{ext}"
        else:
            filename = f"{basename}({i}).{ext}"
        if not os.path.exists(os.path.join(folder, filename)):
            return filename
        i += 1
