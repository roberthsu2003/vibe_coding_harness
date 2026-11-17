# 09　指令模式與 Herdr

> ★★★ 深入　｜　[← 08 權限設定與沙盒](08-permissions.md)　｜　[章節首頁](README.md)　｜　下一站：[10 實戰情境 →](10-scenarios.md)

**這一站你會學到**：不進入對話畫面，直接用一行指令叫 `agy` 做事（`agy -p`）；以及搭配 Herdr 同時跑好幾個工作。

---

## 開始前：建立本節練習資料夾

先完成[課堂練習準備](../practice/README.md)的工具確認與教材下載，再在**一般終端機**逐行執行：

```bash
python3 ~/terminal-ai-course/practice/prepare.py ~/terminal-ai-labs/agy/09
cd ~/terminal-ai-labs/agy/09
agy
```

看到目的資料夾已存在時，直接 `cd` 進去接續；要重做則把路徑最後一段改成 `09-retry`。本節的程式、筆記與初始 Git commit 都已準備好。

---

## 1. `agy -p`：一行指令完成一件事

有時候你只想快速問個問題、請 AI 檢查一個檔案，或是把 AI 的回答交給下一個終端機指令處理。這時可以用 **`-p`**（`--print`）非互動模式，跑完就會直接印出結果並回到終端機：

本節已附 `README.md`、`calc.py` 與 `tests/`。先在一般終端機確認登入與模型可用，再依序執行：

```bash
# 1. 唯讀提問，回答後回到終端機
agy -p "請用繁體中文說明 README.md 的用途、執行與測試方式，不要修改"

# 2. 同一題指定模型與思考強度（先用 agy models 確認帳號可用）
agy -p "檢查 calc.py 的除數為零時會發生什麼，只回報不要修改" --model gemini-4-argon-high --effort high

# 3. 緊接上一個對話，請它把審查結果保存
agy -p "請把剛才發現的問題與重現方法存成 review.md，不改 Python 檔案" -c

# 4. 輸出 JSON：只讀取現成資料
agy -p "只讀 src/auth.py，回報函式名稱與用途" --output-format json
```

**驗收**：第 1 步應提到兩個 Python 指令，第 2 步指出 `ZeroDivisionError`，第 3 步用 `cat review.md` 確認有相同問題，第 4 步輸出可解析的 JSON 且內容提到 `login`。模型不可用時換成 `agy models` 實際列出的模型；Orchestrator 不加 `--effort`。

### Orchestrator 完整修改題（帳號有此選項才做）

```bash
agy -p '請修改 calc.py 的 divide：b 為 0 時拋出 ValueError("除數不可為零")；在 tests/test_calc.py 補測試並執行 python3 -m unittest discover -s tests -v。' --model "Orchestrator (Argon)"
python3 -m unittest discover -s tests -v
git diff -- calc.py tests/test_calc.py
```

**驗收**：至少 5 題測試通過，差異包含錯誤處理與新測試。出現權限詢問時閱讀後只同意本題的修改與測試操作；若此模式無法互動授權，回互動式 `agy` 送出同一題並依畫面批准即可。

### 常用命令列參數

| 參數 | 縮寫 | 用途 |
| :--- | :--- | :--- |
| `--print` | `-p` | 一行指令模式，印出回答後直接結束（別名：`--prompt`） |
| `--prompt-interactive` | `-i` | 啟動時先跑這句指令，跑完**留在對話畫面**繼續聊 |
| `--continue` | `-c` | 接續最近一次的對話 |
| `--model` | | 指定這次要用的模型（如 `gemini-4-argon-high`） |
| `--effort` | | 指定思考強度（`low`、`medium`、`high`、`xhigh`、`max`，依模型而定；Orchestrator 不適用） |
| `--mode` | | 指定執行模式（`plan`、`accept-edits`、`auto`） |
| `--output-format` | | 輸出格式：`text`（預設）、`json` 或 `stream-json` |
| `--print-timeout` | | 設定最長等待時間（例如 `300s`） |

> 💡 **搭配 [Glow](../glow/README.md) 閱讀排版好的長回答**：
> ```bash
> agy -p "說明這個專案的架構" | glow -p
> ```

Orchestrator 的方案與模型分工見 [01 模型選擇教學](01-install.md#orchestrator自動搭配規劃與執行模型)；非互動模式的用法可對照 [官方 Headless mode 文件](https://antigravity.google/docs/cli/headless/#select-a-model-effort-or-agent)。

---

## 2. 搭配 Herdr 多工開發

AI 在改程式或跑測試時通常要花一點時間。搭配終端機多工工具 [Herdr](../herdr/README.md)，你可以把畫面切開，一邊讓 `agy` 工作，一邊看測試結果或瀏覽檔案：

1. 在 Herdr 的左側窗格執行 `agy` 寫程式。
2. 按 `prefix+v` 切出右邊的窗格，再按 `prefix+s` 上下切開：
   - **右上窗格**：跑 `python3 -m unittest discover -s tests -v` 或啟動本地伺服器，隨時看結果。
   - **右下窗格**：開 [Yazi](../yazi/README.md) 看 AI 改了哪些檔案，或跑 `git status`。
3. 看一眼 Herdr 的狀態燈號，就能知道 `agy` 是在工作（🟡）、等你同意權限（🔴），還是已經做完了（🟢）。

```text
+-----------------------+-----------------------+
|                       |  Python 測試          |
|                       |                       |
|  agy                  +-----------------------+
|                       |  yazi / git status    |
|                       |                       |
+-----------------------+-----------------------+
```

如果要同時做好幾個新功能，還可以搭配 [Git Worktree](../worktree/README.md)，在 Herdr 的不同分頁各開一個 `agy`，讓多個 AI 同時動工互不干擾！

> 詳細操作請見 [Herdr 教材](../herdr/README.md)。

---

## Herdr 版面也實際做一次

先依 [Herdr 安裝與啟動](../herdr/01-install.md)安裝並開啟 Herdr。在左窗格 `cd ~/terminal-ai-labs/agy/09` 後執行 `agy`，送出上面的除數為零修改題。右側窗格也 `cd` 到同一路徑，執行 `python3 -m unittest discover -s tests -v`；右下窗格執行 `git diff --stat`。

**驗收**：左側有 AI 回覆、右側顯示通過測試與兩份檔案的修改統計。測試沒有自動重跑時，AI 完成後手動再跑一次即可。未安裝 Yazi 或 uv 也能用這組 Python／Git 指令完成版面練習。

`--mode`：另啟 `agy --mode plan`，送出 `請規劃幫 README 加一節使用說明，先不要改檔案`，確認只產生計畫後離開。`--print-timeout`：執行 `agy -p "只回覆 OK" --print-timeout 300s`，應回覆或在時限後明確逾時，不能把逾時算成完成。Glow 選做題先確認 `glow --version`，再執行本章管線，應看到排版後的 README 摘要。

## ✅ 自我檢查

- [ ] 用 `agy -p "你好"` 在終端機直接拿到 AI 的回答
- [ ] 說得出 `agy -p`（印完就結束）和 `agy -i`（問完繼續留在對話框）的差別
- [ ] 試過把 `agy -p` 的輸出接給 `glow -p` 閱讀（如果有安裝 Glow）

---

[← 08 權限設定與沙盒](08-permissions.md)　｜　[章節首頁](README.md)　｜　下一站：[10 實戰情境 →](10-scenarios.md)
