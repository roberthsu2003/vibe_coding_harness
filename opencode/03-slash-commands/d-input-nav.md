# 03-D　D 區：輸入輔助與切換位置

> ★ 入門　｜　[← C 區：復原與對話管理](c-session.md)　｜　[回到 03 斜線指令總覽](../03-slash-commands.md)　｜　下一區：[E 區：查狀態與設定 →](e-status-settings.md)

**這一區解決的問題**：「聊到一半想隨口問個小問題？想用習慣的編輯器寫一段長提示？或是想切換到另一個筆記資料夾？」

---

## 開始前：建立本節練習資料夾

先完成[課堂練習準備](../../practice/README.md)的工具確認與教材下載，再在**一般終端機**逐行執行：

```bash
python3 ~/terminal-ai-course/practice/prepare.py ~/terminal-ai-labs/opencode/03-d
cd ~/terminal-ai-labs/opencode/03-d
opencode
```

看到目的資料夾已存在時，直接 `cd` 進去接續；要重做則把路徑最後一段改成 `03-d-retry`。本節的程式、筆記與初始 Git commit 都已準備好。

---

## 1. 輸入輔助指令

### `/btw`：問個題外話（不污染主對話）

當你正在請 AI 整理筆記，突然想問一個小問題，又不想打亂原本的話題：

```text
/btw Markdown 的可勾選核取方塊（Checkbox）語法怎麼寫？
```

- **結果**：AI 的回答會顯示在彈出視窗中，**不會加進目前的對話紀錄**，也不影響 AI 手上的工作。正適合隨口問問！

---

### `/editor`：用文字編輯器寫長訊息

當你要交代一整頁大綱或很長的需求，在小小一行輸入框不好打字時：

```text
/editor
```

- **結果**：開啟你設定的文字編輯器（如 VS Code 或 Vim）。寫完存檔並關閉後，內容會自動帶回 OpenCode 輸入框，再按 `Enter` 送出。
- **事前準備**：需要先設定好 `EDITOR` 環境變數，詳見 [04 環境配置](../04-config.md#4-環境變數)。快捷鍵：`Ctrl+X` → `E`。

---

### `/terminal`：在畫面裡開一個終端機

```text
/terminal
```

- **結果**：在 OpenCode 畫面內直接開啟一個終端機窗格，不用離開 OpenCode 就能查看檔案清單（例如輸入 `ls`）。

> [!NOTE]
> 開啟後，鍵盤輸入會送進終端機窗格。如果你打斜線指令卻出現 `no such file or directory`，代表你的游標還停在終端機窗格裡，記得先切回對話輸入框。

---

## 2. 切換位置與連線指令

### `/cd`：切換工作資料夾

想讓 AI 改去讀寫子資料夾裡的 Markdown 筆記：

```text
/cd notes
```

- **結果**：邊打字會邊列出符合的資料夾名稱，選好後直接切換過去。

---

### `/open`：切換到別的專案或最近對話

```text
/open
```

- **結果**：列出最近開啟過的專案資料夾與對話，選一個就切換過去。別名：`/project`、`/projects`。

---

### `/worktrees`：管理 Git Worktree（進階）

```text
/worktrees
```

- **結果**：列出這個專案的 Git Worktree（按 `Ctrl+A` 新增、`Ctrl+D` 刪除）。Worktree 的概念與用法請見 [Branch 與 Worktree](../../worktree/README.md)。

---

### `/pair`：用手機或瀏覽器連線（進階）

```text
/pair
```

- **結果**：顯示連線網址與 QR Code，讓你的手機或瀏覽器連上這個 OpenCode 畫面。別名：`/web`。

> [!WARNING]
> 這個連結等於進入你電腦的通行證，**千萬不要分享給別人，也不要截圖貼到群組**！

---

## 完整小範例：輸入、切目錄、Worktree 與連線

### A. 用編輯器寫一則需求

離開 OpenCode，先在一般終端機確認 `nano --version`，再執行：

```bash
EDITOR=nano opencode --standalone
```

送出「你好」後輸入 `/editor`，在 nano 輸入 `請在 notes/faq.md 追加一題「如何查看改動？」，答案是使用 /diff。`，按 `Ctrl+O`、`Enter` 儲存，`Ctrl+X` 關閉。回到輸入框後再按 `Enter`。

**驗收**：`cat notes/faq.md` 可見新增問答；編輯器返回文字與 AI 修改流程都有實際發生。

### B. 內建終端機與切換工作目錄

1. 對話開始後輸入 `/terminal`，在終端機窗格執行 `pwd`、`ls notes`，應看到本節路徑與 ch1、ch2、ch3、faq。
2. 在該 shell 輸入 `exit` 結束，將焦點切回 OpenCode 對話輸入框，再輸入 `/cd notes`。
3. 送出 `請讀 faq.md，回報第一個標題，不修改`，應找到「常見問題」；再 `/cd ..` 回原目錄。
4. 離開本節，在一般終端機 `mkdir -p ~/terminal-ai-labs/second-project`，執行 `opencode ~/terminal-ai-labs/second-project`，送出「這是第二專案」後離開，再回本節啟動。
5. 輸入 `/open`，選剛才的 second-project，確認路徑改變；再 `/open` 選回本節。

**驗收**：兩個資料夾都在最近專案清單中，切換後路徑與讀取結果一致；不用只看 AI 是否聲稱切換成功。

### C. Worktree 從建立到移除

本節素材已是 Git 專案。先在一般終端機從本節根目錄執行：

```bash
git worktree add -b notes-practice ../03-d-worktree
git worktree list
```

回 OpenCode 輸入 `/worktrees`，應能看到新工作區。切到該工作區，在 Build 送出 `請建立 worktree-note.md，寫「此檔只屬於新工作區」。`。

**驗收**：一般終端機 `cat ../03-d-worktree/worktree-note.md` 能讀到內容，原工作區沒有該檔。看完從 OpenCode 切回原工作區，在一般終端機執行 `mv ../03-d-worktree/worktree-note.md ./worktree-note-result.md` 保存成果，再執行 `git worktree remove ../03-d-worktree`；不要用 force 刪掉尚未保存的檔案。`git worktree list` 應只剩原工作區。要使用面板的新增／刪除按鈕，可再做一次，名稱改為 notes-panel，結果也要用 git worktree list 驗證。

### D. 用自己的瀏覽器配對

輸入 `/pair`，只在自己的手機或瀏覽器開啟畫面提供的網址／QR Code，依提示驗證；送出 `請只回覆「配對成功」`，觀察終端機也出現同一段對話。**驗收**：兩邊內容同步。結束後關閉瀏覽器連線，依配對介面的停止／撤銷選項結束連線，再確認原連線不再可操作；若版本未提供單獨撤銷，就結束本次 OpenCode 服務後確認連線失效。

## ✅ 動手練習：用 `/btw` 查語法並建立子資料夾筆記

這個練習**完全不寫程式**，帶你體驗「隨口查語法 → 建立子資料夾 `.md` 筆記 → 切換目錄」：

| 步驟 | 在對話框輸入 | 觀察重點 |
| :---: | :--- | :--- |
| **1** | `/btw Markdown 怎麼寫出折疊收合區塊（details / summary）？` | 觀察彈出視窗的回答，看完關閉後確認沒有混進主對話紀錄 |
| **2** | `請幫我建立一個 notes 資料夾，並在裡面新增 faq.md，用折疊語法寫 3 個常見問答` | 讓 AI 把剛才學到的折疊語法實際寫成 `notes/faq.md` |
| **3** | `/cd notes` | 體驗把目前的工作目錄切換進剛才建立的 `notes` 資料夾 |
| **4** | `/cd ..` | 再切換回原本的上一層資料夾 |

---

[← C 區：復原與對話管理](c-session.md)　｜　[回到 03 斜線指令總覽](../03-slash-commands.md)　｜　下一區：[E 區：查狀態與設定 →](e-status-settings.md)
