import json
import os
from typing import Any, Dict


class DataModel:
    """
    アプリ全体で使用する設定データを管理するモデルクラス。

    Notes
    -----
    - 設定ファイル（settings.json）の読み取り・書き込みを担当する。
    - GUI や Controller から直接ファイルを扱わないようにするため、
      設定関連の処理は必ずこのクラスを経由する。
    """

    def __init__(self, settings_path: str = "settings.json") -> None:
        """
        Parameters
        ----------
        settings_path : str
            設定ファイル（JSON）のパス
        """

        # settings.json のパスを保持する
        self.settings_path = settings_path

        # 設定内容を保持する辞書
        self.settings: Dict[str, Any] = {}

        # アプリ起動時に設定ファイルを読み込む
        self.load_settings()

    # ---------------------------------------------------------
    # 設定ファイルの読み込み
    # ---------------------------------------------------------
    def load_settings(self) -> None:
        """
        JSON の設定ファイルを読み込み、`self.settings` に展開する。

        Notes
        -----
        - ファイルがない場合はデフォルト設定を生成する。
        """

        if not os.path.exists(self.settings_path):
            # ファイルがない場合 → デフォルト設定で新規作成
            self.settings = self._default_settings()
            self.save_settings()
            return

        try:
            with open(self.settings_path, "r", encoding="utf-8") as f:
                self.settings = json.load(f)
        except json.JSONDecodeError:
            # JSON が壊れている場合 → デフォルト設定で再生成
            self.settings = self._default_settings()
            self.save_settings()

    # ---------------------------------------------------------
    # 設定ファイルの保存
    # ---------------------------------------------------------
    def save_settings(self) -> None:
        """
        現在の設定 (`self.settings`) を JSON ファイルに保存する。
        """
        with open(self.settings_path, "w", encoding="utf-8") as f:
            json.dump(self.settings, f, indent=4, ensure_ascii=False)

    # ---------------------------------------------------------
    # デフォルト設定（最初に自動生成される設定）
    # ---------------------------------------------------------
    def _default_settings(self) -> Dict[str, Any]:
        """
        デフォルトの設定内容を返す。

        Returns
        -------
        Dict[str, Any]
            デフォルト設定の辞書
        """

        return {
            "window_width": 800,        # ウィンドウの横幅
            "window_height": 600,       # ウィンドウの高さ
            "theme": "light",           # アプリのテーマ
            "last_open_dir": "",        # 前回ファイルを開いたディレクトリ
        }

    # ---------------------------------------------------------
    # 設定値を取得する（GUI/Controller 側で使う）
    # ---------------------------------------------------------
    def get(self, key: str, default: Any = None) -> Any:
        """
        設定値を取得する。

        Parameters
        ----------
        key : str
            取得したい設定項目名
        default : Any
            該当キーが存在しない場合に返す値

        Returns
        -------
        Any
            設定値
        """

        return self.settings.get(key, default)

    # ---------------------------------------------------------
    # 設定値を変更する（変更したら save_settings を呼ぶ）
    # ---------------------------------------------------------
    def set(self, key: str, value: Any) -> None:
        """
        設定値を更新する。

        Parameters
        ----------
        key : str
            更新したい項目名
        value : Any
            新しい値
        """

        self.settings[key] = value
        self.save_settings()
