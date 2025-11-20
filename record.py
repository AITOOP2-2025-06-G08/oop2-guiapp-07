#!/usr/bin/env python
# -*- coding: utf-8 -*-


import ffmpeg

def record_audio(output_filename: str, record_seconds: int = 10) -> None:
    """
    マイクから音声を録音して指定されたファイルに保存する関数

    Parameters
    ----------
        output_filename : str
            録音した音声を保存するファイル名
        record_seconds : int
            録音時間(単位:秒, デフォルト:10秒)
    """
    # 録音処理
    try:
        print(f"{record_seconds}秒間、マイクからの録音を開始します...")
        (
            ffmpeg
            .input(':0', format='avfoundation', t=record_seconds) # macOSの例
            .output(output_filename, acodec='pcm_s16le', ar='44100', ac=1)
            .run(overwrite_output=True)
        )
        print(f"録音が完了しました。{output_filename}に保存されました。")

    except ffmpeg.Error as e:
        print(f"エラーが発生しました: {e.stderr.decode()}")
    except Exception as e:
        print(f"予期せぬエラー: {e}")