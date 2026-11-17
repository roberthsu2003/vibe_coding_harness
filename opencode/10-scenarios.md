# 10　實戰情境

> ★★ 實戰　｜　[← 09 指令模式與 Herdr](09-cli-run.md)　｜　[章節首頁](README.md)　｜　📚 [維護指令與疑難排解](reference.md)

**這一站你會學到**：AI 做到一半想補充、改錯了想復原、對話太長變遲鈍時怎麼辦，以及怎麼把需求說清楚。

---

## 開始前：建立本節練習資料夾

先完成[課堂練習準備](../practice/README.md)的工具確認與教材下載，再在**一般終端機**逐行執行：

```bash
python3 ~/terminal-ai-course/practice/prepare.py ~/terminal-ai-labs/opencode/10
cd ~/terminal-ai-labs/opencode/10
opencode
```

看到目的資料夾已存在時，直接 `cd` 進去接續；要重做則把路徑最後一段改成 `10-retry`。本節的程式、筆記與初始 Git commit 都已準備好。

---

## 本章素材與操作順序

練習資料夾已附 `todo.md`、`travel.md`、`notes.md`、`reading-notes.md`、`calc.py` 與 `tests/`，因此可以直接做每個情境。各題可獨立練：要避免上一題影響下一題，就用新的 `10-b`、`10-c` 等路徑重新建立素材。

**每題都要實際觸發情境**：例如復原題先要求修改，再執行復原；不是只看操作說明或等待 AI 自己出錯。下方補齊各情境的實作與驗收。

## 情境 A：AI 正在做，才發現漏交代了需求

**小範例**：假設你剛送出 `請幫我建立 python_notes.md，介紹 Python 字典的常用方法`，AI 正在寫的時候：

- **想立刻補充條件**：直接打字並按 **`Enter`**，訊息會馬上影響它正在做的事：
  ```text
  每個方法都要加上執行結果註解，最後再附 2 題小練習。
  ```
- **想等它做完這一輪再處理下一件事**：打好訊息後按 **`Ctrl+X` → `Enter`**，訊息會排隊等候。
- **它已經走錯方向（例如用英文寫）**：先按 **`Esc`** 讓它停下來，再告訴它怎麼改：
  ```text
  請全部改用繁體中文撰寫說明文字。
  ```

## 情境 B：AI 越改越糟

**小範例**：假設你請 AI「幫我簡化 `todo.md`」，結果它把重要備註都刪光了。

1. 按 **`Esc`** 中斷目前動作。
2. 輸入 **`/undo`**，復原上一則訊息和它對 `todo.md` 做的修改（可以連續輸入好幾次；剛才那句話會自動回到輸入框，按 `/redo` 可恢復）。
3. 輸入 **`/diff`** 或 `!git status`，確認 `todo.md` 已經恢復原本的內容。
4. 把輸入框的指令改得更明確再送出：
   ```text
   請幫我美化 todo.md 的 Markdown 排版，但完整保留每一條原本的備註文字。
   ```

## 情境 C：對話太長，AI 開始忘東忘西

當右側欄的 `Context` 顯示空間快滿了，依情況這樣做：

| 情況 | 做法 | 小範例 |
| :--- | :--- | :--- |
| **還在做同一件事** | `/compact`：把前面的對話整理成摘要 | `/compact 保留目前決定的章節架構與命名規則` |
| **要開始新任務** | `/new`：開新對話（舊的用 `/sessions` 找回） | 寫完 `study-guide.md` 要改寫 `README.md` 前，輸入 `/new` |
| **只是想問個小問題** | `/btw`：回答不會加進對話，不佔空間 | `/btw Markdown 的收合區塊（details）怎麼寫？` |

> 右側欄的 `Context` 會顯示目前用了多少空間。OpenCode 也會在快滿時自動壓縮。

## 情境 D：想先看計畫，再讓 AI 動手

**小範例**：想拆分檔案又怕改亂，按 `Shift+Tab` 切到 **Plan** 模式，然後輸入：

```text
我想把目前的 notes.md 拆成 intro.md 與 faq.md，並在 README.md 建立目錄連結，請先列出修改計畫。
```

看完計畫覺得可以，再按 `Shift+Tab` 切回 **Build** 模式，輸入：`就照這個計畫執行。`

## 情境 E：想試另一種做法，又怕弄亂

**小範例**：你剛和 AI 討論完 `travel.md` 的「開車自駕版」，想試試「搭火車版」：

1. 輸入 **`/fork`** 複製一段新對話。
2. 在新對話裡輸入：
   ```text
   如果全程不開車、改搭火車與公車，請另存 travel-transit.md，保留 travel.md 原文。
   ```
3. 試完如果不滿意，輸入 **`/sessions`** 就能選回原本「開車自駕版」的對話。

## 情境 F：AI 改完了，想確認有沒有問題

**小範例**：AI 剛幫你改完 `calc.py` 和 `test_calc.py`：

1. 輸入 **`/diff`**，自己看一遍綠色新增與紅色刪除的程式碼。
2. 輸入 **`/review`**（也可以直接指定重點），請 AI 用審查者的角度再檢查一次：
   ```text
   /review 幫我檢查 calc.py 有沒有漏掉除以零的錯誤處理
   ```

## 情境 G：剛 commit 完才發現漏了東西

**小範例**：剛執行完 `git commit -m "docs: 新增旅遊筆記"`，才發現 `travel.md` 忘了加進去，直接請 AI：

```text
剛才的 commit 漏掉了 travel.md，請把它加進去並合併進前一個 commit（保留原本的 commit 訊息）。
```

> ⚠️ 這個做法（`git commit --amend`）只適合**還沒 push** 的 commit。

---

## 各情境的完整操作與驗收

| 情境 | 準備與實際操作 | 驗收 |
| :--- | :--- | :--- |
| A 補需求 | 先送出建立 python_notes 的原提示詞，再送出補充條件；來不及在工作中送出時，直接當下一輪要求追加。中斷題可先請它寫 20 個方法、工作中按 Esc 再改格式 | 檔案有中文說明、執行結果註解與 2 題練習 |
| B 復原 | 先記下 `todo.md` 的兩條備註，再送出 `請刪掉 todo.md 的所有備註，只留下項目。`，確定內容已刪才 `/undo` | `cat todo.md` 重新看到「帶耳機」「截圖交作業」；`/redo` 可再次刪掉，再 `/undo` 還原 |
| C 壓縮 | 先送出 `接下來的筆記都用三點摘要、小寫檔名，請記住。`，再 `/compact`，請它重述兩項格式；接著 `/new` 並用 `/sessions` 找回 | 能重述約定；新對話與舊對話可切換，短對話用量不一定減少 |
| D 計畫 | 使用現成 notes.md，Plan 階段先用一般終端機 `git diff -- notes.md README.md` 檢查，切 Build 才同意修改 | 核准前無改動；核准後 intro.md、faq.md 存在且 README 連結正確 |
| E 分岔 | 先 `/rename 自駕版`，再 `/fork`；在新對話要求另存 `travel-transit.md`，不要覆蓋 travel.md | 兩份檔案都存在，原檔仍是自駕；`/sessions` 切回原對話後檔案不會自動復原 |
| F 審查 | 先送出 `請為 calc.py 的 divide 加一句中文用途註解，不改邏輯。`，製造差異後才 `/diff`、`/review` | 審查應指出零除數沒有友善處理；不要只有「沒有改動可審查」 |
| G 補 commit | 使用下方獨立 Git 練習，不在自己的正式專案測試 | `git show --stat HEAD` 同時列出 README 與新建的行程檔 |

### G 的完整 Git 練習

本章初始素材已有 travel.md；為了重現「忘了加進 commit」，改用新檔 `travel-extra.md`。在一般終端機執行：

```bash
printf '\n## 課堂進度\n完成 Git 補檔練習。\n' >> README.md
printf '# 加碼行程\n\n下午到公園散步。\n' > travel-extra.md
git add README.md
git -c user.name=Classroom -c user.email=classroom@example.invalid -c commit.gpgsign=false commit -m "docs: 新增旅遊筆記"
git status --short
```

**修改前**：`travel-extra.md` 應為尚未追蹤。回 OpenCode 送出：

```text
剛才尚未 push 的 commit 漏了 travel-extra.md。請只加入這個檔案，以 git -c user.name=Classroom -c user.email=classroom@example.invalid -c commit.gpgsign=false commit --amend --no-edit 合併到前一個 commit，不加入其他檔案，保留原訊息。
```

**驗收（一般終端機）**：`git show --stat HEAD` 同時包含 README.md 與 travel-extra.md，`git log -1 --format=%s` 仍是「docs: 新增旅遊筆記」，沒有 push 任何東西。

### 目標、範圍、驗收的實作題

```text
請新增使用者登入的測試：只修改 tests/test_auth.py，不改 src/；新增空帳號與空密碼兩個案例，都應回傳 False。執行 python3 -m unittest discover -s tests -v，全部通過後回報測試數。
```

**驗收**：至少 6 個測試全部通過，`git diff -- src/` 無輸出。若想讓 AI 先問需求，可先送出 `我想加登入測試，你還需要知道什麼？`，回答「只測空帳號、空密碼，不改程式」，再請它實作與驗收。

## 把需求說清楚：目標、範圍、驗收

不用寫得很長，想到這三件事就好：

| 要素 | 問自己 | 範例 |
| :--- | :--- | :--- |
| **目標** | 要做什麼？ | 新增使用者登入的測試 |
| **範圍** | 什麼不能動？ | 不要改程式本身，只加測試 |
| **驗收** | 怎樣算完成？ | 測試全部通過 |

合起來就是一句話：

```text
請新增使用者登入的測試，不要改程式本身，完成後確認測試全部通過。
```

> [!TIP]
> 想不出來也沒關係，可以直接問 AI：「我想做 X，你還需要知道什麼？」

---

## ✅ 自我檢查

- [ ] 知道 `Esc`、`/undo`、`/compact`、`/new`、`/btw` 各在什麼時候用
- [ ] 用 Plan 看過 AI 的計畫，再切回 Build 執行
- [ ] 能用「目標、範圍、驗收」說出一個需求

> 🎉 完成 OpenCode 章節！遇到問題時查閱 [維護指令與疑難排解](reference.md)。
