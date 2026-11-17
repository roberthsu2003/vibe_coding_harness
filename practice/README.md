# 課堂練習準備

agy 與 OpenCode 的小範例共用這份素材。每章使用獨立的 Git 專案，可以單獨選章練習；每個範例會寫出準備、輸入位置與驗收方式。

## 1. 先確認工具

在**一般終端機**逐行執行：

```bash
git --version
python3 --version
```

需要 Git 與 Python 3.9 以上。Windows 請用 WSL 的 Ubuntu 終端機執行本練習；下列 Bash 指令也適用 macOS 與 Linux。AI 工具的安裝與登入請看 [agy 第 01 站](../agy/01-install.md) 或 [OpenCode 第 01 站](../opencode/01-install.md)。

使用 `uv` 的進階範例，請先依 [uv 官方安裝教學](https://docs.astral.sh/uv/getting-started/installation/) 安裝，確認 `uv --version` 有版本號。在練習專案執行 `uv sync` 會安裝 pytest 與 Ruff（首次需要網路）；日常範例使用 Python 內建 unittest，不必先裝套件。

## 2. 下載教材（只需一次）

```bash
git clone https://github.com/roberthsu2003/vibe_coding_harness.git ~/terminal-ai-course
```

已經下載過這個路徑就沿用。若教材放在別處，將各章的 `~/terminal-ai-course` 改成自己的教材路徑。

## 3. 建立某一章的練習專案

以 agy 第 02 站為例：

```bash
python3 ~/terminal-ai-course/practice/prepare.py ~/terminal-ai-labs/agy/02
cd ~/terminal-ai-labs/agy/02
python3 main.py
python3 -m unittest discover -s tests -v
git status --short
```

**應該看到**：程式印出 `4.0`，4 個測試通過（`OK`），最後的 Git 狀態沒有任何輸出。腳本已建立一次初始 commit，無需設定個人的 Git 姓名、信箱。

OpenCode 各章使用 `~/terminal-ai-labs/opencode/02` 等獨立路徑。分區斜線指令以 `03-a`、`03-b` 命名。各章開頭都有可複製的建立與啟動指令。

## 4. 操作與驗收約定

- `bash` 區塊在一般終端機執行；`text` 區塊在 AI 工具輸入框送出。
- 連續的提示詞請**一次送出一則，完成後再送下一則**；斜線指令也各自送出。`# 步驟` 是說明文字，不要連同多條指令一次貼給 AI。
- JSON、Markdown 範本上方標示了檔名：用文字編輯器建立該檔案並儲存。範本內的外層程式碼圍欄不屬於檔案內容。隱藏資料夾可用 `mkdir -p` 建立。
- 修改既有設定時，**合併指定欄位**，保留原有內容；變更全域設定前先記下原值，練完改回。專案資料夾彼此隔離，全域設定仍然共用。
- AI 文字每次可能不同，依各節的「驗收」檢查檔案、測試或介面狀態。只看到 AI 說「完成」還不算驗收。
- 檢查檔案可以另開終端機，`cd` 到練習路徑後執行 `cat 檔名`、`git diff` 或測試指令。

## 5. 重做與收尾

`prepare.py` 遇到已存在的目的資料夾會直接停止，**不覆寫學生進度**。要重做第 02 站，改用新路徑：

```bash
python3 ~/terminal-ai-course/practice/prepare.py ~/terminal-ai-labs/agy/02-retry
cd ~/terminal-ai-labs/agy/02-retry
```

練完先停止背景服務、排程或代理，離開 AI 工具。作業可交「輸入內容、成果檔案、驗收畫面」；不要附帳號憑證。想刪掉練習成果時，在檔案總管移除對應的單一章節資料夾即可。

← [agy 教材](../agy/README.md)　｜　[OpenCode 教材](../opencode/README.md)
