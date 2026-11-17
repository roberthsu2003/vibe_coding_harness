#!/usr/bin/env python3
"""Create an independent classroom repository. Refuse to overwrite existing work."""

import argparse
from pathlib import Path
import shutil
import subprocess
import textwrap


FILES = {
    "README.md": """
        # 課堂練習專案

        用途：學習 AI 代理讀檔、修改、測試與檢查差異。
        Python 3 即可執行，不需要外部套件。

        ## 執行
        `python3 main.py`

        ## 測試
        `python3 -m unittest discover -s tests -v`

        ## 素材
        - `src/auth.py`：課堂用登入判斷，並非正式驗證系統。
        - `calc.py`：除法小程式，尚未定義除以零的友善錯誤訊息。
        - `notes.md`：可拆成基礎、指令與問答的筆記。
    """,
    ".gitignore": "__pycache__/\n.venv/\n.pytest_cache/\n.ruff_cache/\n",
    "pyproject.toml": """
        [project]
        name = "terminal-ai-lab"
        version = "0.1.0"
        requires-python = ">=3.9"
        dependencies = []

        [dependency-groups]
        dev = ["pytest", "ruff"]
    """,
    "main.py": """
        from calc import divide

        # TODO: 為輸出加上中文說明
        if __name__ == "__main__":
            print(divide(12, 3))
    """,
    "calc.py": """
        def divide(a, b):
            return a / b
    """,
    "test_calc.py": """
        import unittest
        from calc import divide

        class DivideTests(unittest.TestCase):
            def test_divide(self):
                self.assertEqual(divide(12, 3), 4)

        if __name__ == "__main__":
            unittest.main()
    """,
    "src/__init__.py": "",
    "src/auth.py": """
        def login(username, password):
            # 僅供課堂辨識程式碼位置，不可用於正式系統。
            return username == "student" and password == "learn"
    """,
    "src/app.py": """
        from src.auth import login

        def welcome(username, password):
            return "登入成功" if login(username, password) else "登入失敗"
    """,
    "src/server.py": """
        from src.app import welcome

        def handle_request():
            return welcome("student", "learn")
    """,
    "tests/test_calc.py": """
        import unittest
        from calc import divide

        class DivideTests(unittest.TestCase):
            def test_positive(self):
                self.assertEqual(divide(12, 3), 4)

            def test_negative(self):
                self.assertEqual(divide(-6, 2), -3)
    """,
    "tests/test_auth.py": """
        import unittest
        from src.auth import login

        class LoginTests(unittest.TestCase):
            def test_valid(self):
                self.assertTrue(login("student", "learn"))

            def test_invalid(self):
                self.assertFalse(login("student", "wrong"))
    """,
    "broken/calc.py": "def add(a, b):\n    return a - b\n",
    "broken/test_calc.py": """
        import unittest
        from calc import add

        class AddTests(unittest.TestCase):
            def test_positive(self):
                self.assertEqual(add(2, 3), 5)

            def test_zero(self):
                self.assertEqual(add(7, 0), 7)

            def test_negative(self):
                self.assertEqual(add(-2, -3), -5)
    """,
    "todo.md": "# 今日待辦\n\n- [x] 安裝工具\n- [ ] 閱讀基本操作（備註：帶耳機）\n- [ ] 完成練習（備註：截圖交作業）\n",
    "travel.md": "# 台南自駕一日遊\n\n早上：開車到安平。\n中午：吃午餐，預算 200 元。\n下午：逛公園，返回台北。\n\n此為虛構練習，不代表實際交通或店家資訊。\n",
    "draft.md": "# 學習心得\n\n今天學會讓 AI 幫我整理筆記，我想繼續練習。\n",
    "reading-notes.md": "# 時間管理\n\n先列出三項重要任務。\n一次專心做一件事。\n睡前回顧完成進度。\n",
    "notes.md": "# 基礎\n\nAI 代理可以讀檔、修改與測試。\n\n# 指令\n\n使用 /diff 查看修改。\n使用 /btw 提問。\n\n# 常見問題\n\n找不到檔案時，先確認工作目錄。\n",
    "notes/ch1.md": "# 時間管理\n\n每天先選三件重要的事，完成後打勾。\n",
    "notes/ch2.md": "# 專注力\n\n關閉通知，每次專心二十五分鐘。\n",
    "notes/ch3.md": "# 睡眠品質\n\n維持固定作息，睡前減少使用手機。\n",
    "notes/faq.md": "# 常見問題\n\n如何查看改動？使用 /diff。\n",
    "study-guide.md": "# 複習指南\n\n先讀筆記，再動手操作，最後驗證結果。\n",
    "protected.txt": "這是權限練習用檔案，請保留。\n",
}


def prepare(destination):
    destination = destination.expanduser().resolve()
    if destination.exists():
        raise ValueError(f"資料夾已存在，未修改任何檔案：{destination}\n請換一個新名稱，例如加上 -retry。")
    if shutil.which("git") is None:
        raise ValueError("請先安裝 Git，再建立練習專案。")
    destination.mkdir(parents=True)
    for name, content in FILES.items():
        path = destination / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(content).lstrip("\n"), encoding="utf-8")
    for command in (
        ["git", "init", "-b", "main"],
        ["git", "add", "."],
        ["git", "-c", "user.name=Classroom", "-c", "user.email=classroom@example.invalid",
         "-c", "commit.gpgsign=false", "-c", "core.hooksPath=/dev/null",
         "commit", "-m", "chore: prepare classroom materials"],
    ):
        subprocess.run(command, cwd=destination, check=True, capture_output=True, text=True)
    print(f"已建立獨立練習專案：{destination}")
    print(f'cd "{destination}"')
    print("python3 -m unittest discover -s tests -v  # 預期 4 個測試通過")
    print("broken/ 是故意放入錯誤的修復題，其他章節不用執行它。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="尚未存在的練習資料夾")
    args = parser.parse_args()
    try:
        prepare(args.destination)
    except (ValueError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"建立失敗：{error}\n")
