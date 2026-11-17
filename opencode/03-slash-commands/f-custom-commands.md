# 03-F　F 區：做一個自己的斜線指令

> ★ 入門　｜　[← E 區：查狀態與設定](e-status-settings.md)　｜　[回到 03 斜線指令總覽](../03-slash-commands.md)　｜　下一站：[04 環境配置 →](../04-config.md)

**這一區解決的問題**：「同一段提示詞老是要重打？怎麼用一個簡單的 Markdown（`.md`）檔案，做出專屬於自己的 `/指令`？」

在 OpenCode 裡，**做一個自訂斜線指令完全不用寫程式**——只要放一個 `.md` 檔案，檔名就會直接變成你的斜線指令！

---

## 開始前：建立本節練習資料夾

先完成[課堂練習準備](../../practice/README.md)的工具確認與教材下載，再在**一般終端機**逐行執行：

```bash
python3 ~/terminal-ai-course/practice/prepare.py ~/terminal-ai-labs/opencode/03-f
cd ~/terminal-ai-labs/opencode/03-f
opencode
```

看到目的資料夾已存在時，直接 `cd` 進去接續；要重做則把路徑最後一段改成 `03-f-retry`。本節的程式、筆記與初始 Git commit 都已準備好。

---

## 本節的素材與存檔位置

已附 reading-notes.md，第一個 `/summary` 範例可以直接用。手動存檔前，在一般終端機執行 `mkdir -p .opencode/commands`；用編輯器新增指定檔名，貼入完整 Markdown 內容並儲存。回 OpenCode 輸入 `/reload` 後，一個指令一次送出。

## 1. 方法一：一句話請 AI 幫你建立（最推薦！）

你連自己開檔案都不用，直接在對話框告訴 AI：

```text
請幫我建立一個 OpenCode 自訂斜線指令 /summary，放在 .opencode/commands/，功能是把我指定的文章或筆記整理成「三個重點＋一句行動建議」的繁體中文摘要。
```

AI 會自動建立 `.opencode/commands/summary.md`。之後你只要輸入：

```text
/summary @reading-notes.md
```

AI 就會立刻照你定義的格式整理出摘要！

---

## 2. 方法二：自己建立 `.md` 檔案

每個 `.md` 檔就是一個斜線指令，**檔名就是指令名稱**：

| 適用範圍 | 存放資料夾位置 |
| :--- | :--- |
| **只有這個資料夾能用** | `.opencode/commands/` |
| **電腦上所有專案都能用** | `~/.config/opencode/commands/` |

### 範例：做一個 `/hello` 打招呼指令（`.opencode/commands/hello.md`）

```markdown
---
description: 用一句充滿活力的話跟某人打招呼
---
請用一句充滿活力的繁體中文跟 $ARGUMENTS 打招呼，並祝他今天學習順利。
```

存檔後（若沒出現可輸入 `/reload`），在輸入框打 `/hello 小明`，AI 實際收到的就是：

```text
請用一句充滿活力的繁體中文跟 小明 打招呼，並祝他今天學習順利。
```

---

## 3. 指令 `.md` 檔裡可以使用的特殊語法

| 寫法 | 意思 | 範例 |
| :--- | :--- | :--- |
| `$ARGUMENTS` | 你在 `/指令` 後面輸入的全部文字 | `/hello 小明` → `$ARGUMENTS` 會變成 `小明` |
| `$1`、`$2` | 第 1 段、第 2 段文字（以空白分隔，最後一個會拿走剩下的全部） | `/card 小明 生日快樂` → `$1` 是 `小明`，`$2` 是 `生日快樂` |
| `` !`終端機指令` `` | 先執行終端機指令，把輸出結果放進提示詞裡 | `` !`date` ``（把今天的日期放進去） |

> [!TIP]
> 如果你的 `.md` 內容裡沒有寫 `$ARGUMENTS`，你在指令後面多打的文字也會自動接在整段提示詞的最後面。

### 範例：自動加上今天日期的日記模板（`.opencode/commands/diary.md`）

```markdown
---
description: 把我說的話整理成一篇有今天日期的 Markdown 日記，存進 diary.md
---
今天的系統時間是：
!`date "+%Y-%m-%d"`

請把以下我今天發生的事情，用溫暖流暢的繁體中文整理成一篇短日記（包含「今日亮點」與「明日期待」），並附加寫入 diary.md 檔案中：

$ARGUMENTS
```

> [!WARNING]
> `` !`指令` `` 會**直接執行，不會先問你**。請只寫你自己看得懂的安全指令（如 `date`、`git status`），不要把來路不明的指令貼進去。

---

### 實際驗收 `/summary`、`/hello` 與 `/diary`

1. `/summary @reading-notes.md`：在 `@` 選單選檔案，回覆應有三個重點、一句行動建議；來源檔不變。
2. `/hello 小明`：回覆應包含小明與一句鼓勵。改輸入 `/hello 小華` 再做一次，確認名字跟著變，而非固定寫死。
3. 完整儲存上面的 `diary.md` 後 `/reload`，送出 `/diary 今天學會用終端機與 AI 一起整理筆記`。
4. 在一般終端機執行 `date "+%Y-%m-%d"` 與 `cat diary.md`。**驗收**：日記日期與系統日期一致，包含今日亮點與明日期待；再送出一次 `/diary 晚上複習了自訂指令`，應附加第二筆而保留第一筆。

### `$1`、`$2` 也有完整範例

新增 `.opencode/commands/card.md`，貼上：

```markdown
---
description: 用姓名與祝福內容產生一張文字卡片
---
請用繁體中文輸出三行：
第一行：收件人：$1
第二行：祝福：$2
第三行：祝你今天學習順利！
不要修改檔案。
```

`/reload` 後送出 `/card 小明 生日快樂 天天開心`。**驗收**：第一行收件人為小明，第二行包含完整「生日快樂 天天開心」，不是只取兩個字。

**停用與移除**：將 `.opencode/commands/card.md` 改名為 `card.md.bak` 後重載，確認 `/card` 消失；改回、重載應恢復。練完移除本次建立的 summary、hello、diary、card 四份指令檔，再重載確認不再出現；成果 diary.md 可保留交作業。

**全域選做**：把 hello.md 複製到 `~/.config/opencode/commands/hello-lab.md`（先確認沒有同名檔案），在另一個空資料夾啟動 OpenCode 並 `/reload`。`/hello-lab 小明` 應能使用；練完只移除這份新建的 hello-lab.md，再重載確認消失。

## 4. 開頭 `---` 的選填設定欄位

開頭兩條 `---` 中間的欄位都可以依需求選填：

| 欄位 | 用途 | 範例 |
| :--- | :--- | :--- |
| `description` | 顯示在 `/` 選單右邊的一句話說明 | `description: 整理成今日日記` |
| `agent` | 指定由哪個代理執行（例如只規劃不改檔） | `agent: plan` |
| `model` | 指定這個指令專用的模型 | `model: opencode/nemotron-3.5-lightning-free` |
| `subagent` | 設為 `true` 時交給子代理在背景做，不佔用主對話 | `subagent: true` |

> [!NOTE]
> - 指令檔裡寫 `@檔名` **不會**自動展開；要附檔案時，請在打指令時從輸入框用 `@` 選取（例如 `/summary @notes.md`）。
> - 如果自訂指令和內建指令同名，會覆蓋掉內建指令。

---

## ✅ 動手練習：親手做出你的第一個 `/hello` 與 `/diary` 指令！

這個練習**只建立 Markdown 檔案、完全不寫程式**，卻能讓你擁有自己的專屬指令：

| 步驟 | 在對話框輸入 | 觀察重點 |
| :---: | :--- | :--- |
| **1** | `請幫我建立一個 OpenCode 自訂斜線指令 .opencode/commands/hello.md，description 寫「熱情打招呼」，內容是：請用一句繁體中文跟 $ARGUMENTS 打招呼，並送他一句鼓勵的話` | 讓 AI 幫你把 `.opencode/commands/hello.md` 建好 |
| **2** | `/reload` | 重新載入設定，讓新指令生效 |
| **3** | `/hello 小明` | 輸入 `/he` 時看看選單有沒有出現你的「熱情打招呼」？送出後看 AI 的回覆！ |
| **4** | `請幫我建立自訂斜線指令 .opencode/commands/diary.md，功能是把 $ARGUMENTS 整理成包含「今日收穫」與「明日目標」的短篇筆記，存成 my-diary.md` | 再做一個能自動幫你產生 Markdown 筆記檔的專屬指令 |
| **5** | `/reload` → 接著輸入 `/diary 今天學會了 OpenCode 的所有斜線指令，還做出了自己的指令！` | 體驗用一個斜線指令，瞬間讓 AI 產出排版漂亮的 `my-diary.md`！ |

---

[← E 區：查狀態與設定](e-status-settings.md)　｜　[回到 03 斜線指令總覽](../03-slash-commands.md)　｜　下一站：[04 環境配置 →](../04-config.md)
