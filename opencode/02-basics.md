# 02　基本操作

> ★ 入門　｜　[← 01 安裝與連線](01-install.md)　｜　[章節首頁](README.md)　｜　下一站：[03 斜線指令 →](03-slash-commands.md)

**這一站你會學到**：和 AI 對話、讓它看指定的檔案、切換主代理，以及最常用的快捷鍵。

---

## 開始前：建立本節練習資料夾

先完成[課堂練習準備](../practice/README.md)的工具確認與教材下載，再在**一般終端機**逐行執行：

```bash
python3 ~/terminal-ai-course/practice/prepare.py ~/terminal-ai-labs/opencode/02
cd ~/terminal-ai-labs/opencode/02
opencode
```

看到目的資料夾已存在時，直接 `cd` 進去接續；要重做則把路徑最後一段改成 `02-retry`。本節的程式、筆記與初始 Git commit 都已準備好。

---

## 1. 啟動與離開

```bash
cd ~/terminal-ai-labs/opencode/02
opencode
```

也可以直接帶路徑：`opencode ~/terminal-ai-labs/opencode/02`。想接著上次的對話：`opencode -c`。

離開時輸入 `/exit`，或按 `Ctrl+C`。

## 2. 四種輸入方式

| 輸入 | 效果 | 範例 |
| :--- | :--- | :--- |
| 一般文字 | 交代 AI 做事 | `幫我在 README 加上安裝說明` |
| **`@名稱`** | 跳出選單，可以選檔案、Skill 或子代理 | `請看 @src/app.py，說明它在做什麼` |
| **`!指令`** | 在空白的輸入框打 `!`，進入 shell 模式執行指令，按 `Esc` 取消 | `!git status` |
| **`/指令`** | 斜線指令，操作 OpenCode 本身 | `/undo` |

> 想打多行再送出：按 `Ctrl+J`（或 `Shift+Enter`）換行，最後按 `Enter` 送出。

> [!TIP]
> `@` 選單右邊會標示種類：**skill**、**agent**，沒有標示的是檔案。只想看檔案的一部分時，可以加上行號，例如 `@src/app.py#20-45`。

## 3. 第一次對話

```text
請閱讀這個專案的目錄結構和 README，用三句話說明這個專案在做什麼。先不要修改任何檔案。
```

## 4. 兩個主代理：Build 和 Plan

按 **`Shift+Tab`** 切換，輸入框下方會顯示目前是哪一個：

| 主代理 | 做什麼 | 什麼時候用 |
| :--- | :--- | :--- |
| **Build**（預設） | 可以改檔案、執行指令 | 要它動手做的時候 |
| **Plan** | 只分析和規劃，不會修改專案檔案 | 想先看看它打算怎麼做的時候 |

> [!NOTE]
> 舊版是按 `Tab`，OpenCode 2 改成 `Shift+Tab`。畫面底部的 `shift+tab agents` 就是在提示這件事。

---

## 5. 快捷鍵

![OpenCode 常用指令速查卡](assets/opencode-shortcuts.svg)

很多功能有快捷鍵。OpenCode 的快捷鍵常以 **`Ctrl+X`** 開頭（稱為 Leader 鍵）：先按 `Ctrl+X`，放開，再按下一個鍵。

| 功能 | 快捷鍵 | 對應的斜線指令 |
| :--- | :--- | :--- |
| 中斷 AI | `Esc` | — |
| 切換主代理 | `Shift+Tab` | `/agents` |
| 切換思考強度 | `Ctrl+T` | `/variants` |
| 指令面板 | `Ctrl+P` | — |
| 切換模型 | `Ctrl+X` → `M` | `/models` |
| 開新對話 | `Ctrl+X` → `N` | `/new` |
| 切換舊對話 | `Ctrl+X` → `L` | `/sessions` |
| 復原上一步 | `Ctrl+X` → `U` | `/undo` |
| 重做 | `Ctrl+X` → `R` | `/redo` |
| 壓縮對話 | `Ctrl+X` → `C` | `/compact` |
| 用編輯器寫訊息 | `Ctrl+X` → `E` | `/editor` |
| 匯出對話 | `Ctrl+X` → `X` | `/export` |
| 顯示／隱藏側邊欄 | `Ctrl+X` → `B` | — |

> 所有斜線指令和小範例，下一站會一個一個介紹。

---

## 完整小範例：Build、Plan 與復原

素材已包含 `src/app.py`，請在輸入框一次送出一列：

| 步驟 | 操作 | 預期結果 |
| :--- | :--- | :--- |
| 1 | `請閱讀 README.md，用三點說明用途，不要修改。` | 能說出程式與測試指令 |
| 2 | `請說明 @src/app.py 的 welcome 如何判斷成功或失敗。`（從 `@` 選單選檔案） | 找到 `src/auth.py` 的登入判斷 |
| 3 | `!git status --short` | 尚未修改時沒有輸出；按 `Esc` 離開 shell 模式 |
| 4 | `Shift+Tab` 切到 Plan，送出 `請規劃把 main.py 的輸出改為「計算結果：4.0」。` | 提出計畫，檔案尚未修改 |
| 5 | 切回 Build，送出 `請照剛才的計畫執行。` | `main.py` 被修改 |
| 6 | `/diff` | 看見輸出文字的改動，按 `Esc` 返回 |
| 7 | `/undo` | 最新一輪修改被撤銷；不要送新訊息 |
| 8 | 清空回填的提示詞，再輸入 `/redo` | 修改恢復 |

**驗收（一般終端機）**：執行 `python3 main.py` 應印出 `計算結果：4.0`；執行 `python3 -m unittest discover -s tests -v` 應 4 個測試通過。輸入 `/exit` 後再於終端機執行 `opencode -c`，應接回這段對話。

快捷鍵實測：按 `Ctrl+P` 打開面板，再按 `Esc` 返回；按 `Ctrl+X` 後放開再按 `B`，側邊欄應切換顯示，再做一次還原。

## ✅ 動手練習

1. 啟動 OpenCode，問它專案在做什麼。
2. 用 `@` 引用一個檔案，請它解釋。
3. 輸入 `!ls` 看看結果。
4. 請它新增一個小檔案，再用 `/undo` 復原。
5. 按 `Shift+Tab` 切換到 Plan，觀察輸入框下方的變化，再切回 Build。

> 下一站：[03 斜線指令 →](03-slash-commands.md)
