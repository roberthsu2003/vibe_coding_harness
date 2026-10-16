# Supervisor 與 SubAgent 終端協同工作流

在複雜的軟體開發中，讓單一 AI Agent 包辦「架構設計、代碼編寫、測試執行、代碼審查」往往會導致 Context 爆滿、注意力分散與自圓其說的錯誤。

透過 **Herdr**，你可以將終端機化身為多 Agent 協同的調度匯流排（Terminal-as-a-Bus），建立一個 **Supervisor（主代理 / 架構主管）** 負責拆解任務與把關，並在獨立窗格中生成多個 **SubAgent（子代理 / 執行者）** 分工協作。

---

## 導覽目錄

1. [概念比喻：虛擬敏捷開發小組（一般人一看就懂）](#1-概念比喻虛擬敏捷開發小組一般人一看就懂)
2. [底層核心原理：為什麼能跨 Agent 協同？](#2-底層核心原理為什麼能跨-agent-協同)
3. [深度科普：PTY（虛擬終端）到底是什麼？](#3-深度科普pty虛擬終端到底是什麼)
4. [技術架構數據流向圖](#4-技術架構數據流向圖)
5. [實戰演練：Supervisor 調度 SubAgent 完整範例](#5-實戰演練supervisor-調度-subagent-完整範例)
6. [Supervisor 角色提示詞 (Prompt Template)](#6-supervisor-角色提示詞-prompt-template)
7. [多 Agent 協同的最佳實踐](#7-多-agent-協同的最佳實踐)

---

## 1. 概念比喻：虛擬敏捷開發小組（一般人一看就懂）

如果把整個開發流程比喻為一家軟體公司，Herdr 的多 Agent 協同就像一個現代化的小型敏捷團隊：

![Herdr 團隊協同概念](assets/supervisor-subagent-concept.svg)

### 📖 白話文看懂這張圖：為什麼我們需要「團隊分工」？

如果你曾經直接叫一個 AI Agent（例如叫它「幫我寫一個完整的電商網站」），你一定遇過這種慘況：
> ❌ **單一 Agent 的慘痛經歷**：  
> 一開始講得頭頭是道，改了 20 個檔案後開始語無倫次；修好前台購物車卻把後台結帳改壞；甚至寫出有 Bug 的程式碼還自信滿滿地告訴你「全部測試通過」。最後因為對話紀錄太長（Context 爆滿），整個人變遲鈍。

**這就是為什麼我們需要 Herdr 把終端機變成一個「敏捷開發小組」：**

#### 💡 一個真實的生活比喻：蓋房子
- **主管（Supervisor）就像「建築設計師 / 監工」**：  
  他手上有整棟房子的藍圖與規格。但他**絕不會親自挽起袖子去拌水泥或砌磚塊**。他的工作只有三件事：
  1. 看藍圖，把大工程切成具體小工單（「今天只砌這面牆」）。
  2. 派工給泥作師傅，交待「砌好通知我」。
  3. 師傅回報做好了，監工拿水平尺去驗收；發現砌歪了，要求師傅敲掉重做。
- **子代理 A（Coder）就像「泥作師傅」**：  
  他不需要去背整棟大樓的力學結構算式，他只要專心把眼前這面牆砌得平整漂亮。因為任務明確單純，所以失誤率極低。
- **子代理 B（QA Tester）就像「品質驗收員」**：  
  他拿著儀器專挑毛病。他跟泥作師傅是平級的獨立角色，因此不會互相袒護，有問題就老實跟監工回報。
- **Herdr 就像「現代化工地管理系統」**：  
  給每個人一個獨立施工區（窗格），互不干擾；門口掛著「施工中 / 待檢驗 / 已完工」的指示牌；還有無線對講機讓監工隨時隨地派工。

#### 🌰 實戰情境小範例：開發「使用者登入系統」
當你對主管下指令：「請幫我完成登入驗證功能」，這個小組是這樣分工的：
1. **主管動腦**：主管思考後，把任務拆成兩張工單：
   - 工單 1：「在 `src/auth.py` 寫密碼雜湊與驗證邏輯」。
   - 工單 2：「在 `tests/test_auth.py` 寫自動化測試」。
2. **主管派工**：主管用 Herdr 指令把「工單 1」丟給窗格內的子代理 A。
3. **子代理 A 施工**：子代理 A 在自己的獨立目錄快速寫完程式碼，回到待命狀態。
4. **主管找測試員驗證**：主管叫子代理 B 跑測試。測試員回報：「空密碼會直接當機！」
5. **主管命令修正**：主管再次命令子代理 A：「修正空密碼的錯誤處理」。
6. **驗收通過**：全體測試通過，主管審查代碼無誤，將成果合併回主專案。全程人類只需要在旁邊泡咖啡監督！

| 角色 | 現實中的對應 | 在終端機中的具體職責 |
| :--- | :--- | :--- |
| **👑 主代理 (Supervisor)** | **技術主管 / 架構師 (Tech Lead)** | 負責全域架構思考與任務拆解。不親自修改大量代碼，保持腦袋（Context Window）乾淨，專注驗收與代碼審查（Code Review）。 |
| **🛠️ 子代理 A (SubAgent)** | **核心工程師 (Coder)** | 坐在獨立的工位（`.worktrees/auth` 分支目錄），只接收具體的單一任務指令（如「實作 JWT 驗證」），專心寫代碼。 |
| **🧪 子代理 B (SubAgent)** | **品保測試員 (QA Tester)** | 坐在獨立窗格中，客觀執行 `uv run pytest` 與 Linter，專挑毛病並將失敗日誌反饋給主管。 |
| **🏢 Herdr 終端多工台** | **現代化辦公室與對講機系統** | 為每位工程師分配獨立互不干擾的窗格（工位），門口設有狀態燈（工作中/等待確認/完成），並提供對講機讓主管一鍵派工。 |


---

## 2. 底層核心原理：為什麼能跨 Agent 協同？

為什麼 Herdr 能夠在**不需要修改任何 AI 模型的內部代碼**的情況下，讓彼此陌生的 Agent 互相對話與派發任務？其底層依賴三大技術基石：

```text
+-----------------------------------------------------------------------+
|  Supervisor Pane (w1:p1)                                              |
|  發出指令: herdr agent prompt coder "請為 @auth.py 撰寫單元測試"      |
+-----------------------------------------------------------------------+
                                   │ (CLI / Unix Socket 通訊)
                                   ▼
+-----------------------------------------------------------------------+
|  Herdr Daemon (中央服務 / IPC 匯流排)                                 |
|  1. 解析目標：Agent 名稱 coder → 所在 Pane ID (w1:p2)                 |
|  2. 透過 PTY 驅動向終端注入文字與按鍵模擬                            |
|  3. 監控終端輸出緩衝區與進程狀態 (working / blocked / done)           |
+-----------------------------------------------------------------------+
                                   │ (PTY 虛擬終端寫入)
                                   ▼
+-----------------------------------------------------------------------+
|  SubAgent Pane (w1:p2，Agent 名稱：coder)                             |
|  OpenCode / Claude Code 收到輸入，開始執行任務...                     |
+-----------------------------------------------------------------------+
```

### 1. Unix Domain Socket 與常駐服務 (Daemon)
Herdr 在背景執行一個輕量服務進程，透過本機 Unix Domain Socket 監聽指令。不管是由人類工程師下指令，還是由某個窗格內的 Supervisor Agent 下指令，都能透過標準的 CLI（`herdr pane ...`、`herdr agent ...`）向伺服器發送控制訊息。

### 2. 非侵入式跨進程控制（模型完全解耦）
Supervisor 不需要知道 SubAgent 背後是哪一家模型或工具（可以是 Claude Code、Codex、OpenCode、Gemini CLI 等），甚至不需要 SubAgent 提供特定的 API 接口。Supervisor 只要像人類一樣向子窗格「鍵入文字」，SubAgent 就會開始工作。

### 3. 狀態感知探針 (State Awareness)
Herdr 內建智慧探針，能主動回報子窗格內的狀態標籤：
- `idle`：子 Agent 待命中，可以接收新輸入（且已在畫面上被看過）。
- `working`：子 Agent 正在思考或執行。
- `blocked`：子 Agent 跳出批准或提問畫面，卡住等待回應。
- `done`：子 Agent 在背景完成了這輪任務、回到待命，但**還沒有人切過去看**（切到該分頁後會變回 `idle`）。
- `unknown`：窗格內有 Agent，但 Herdr 無法有把握地判斷狀態（**不代表已完成**）。

Supervisor 只要透過 `herdr agent get <名稱>` 查詢狀態，或用 `herdr agent wait <名稱>` 直接等到 Agent 停下來，就能得知子代理是否完成，不用自己寫正則表達式解析終端文字。

---

## 3. 深度科普：PTY（虛擬終端）到底是什麼？

在理解 Herdr 的運作時，經常會看到 **PTY（Pseudo-Terminal）** 這個詞。為什麼它這麼重要？

### 什麼是 PTY？
* **歷史由來**：在 Unix 早期，電腦使用者是透過實體的**硬體電傳打字機（Teletypewriter，簡稱 TTY）** 連接到大型主機。
* **現代演進**：現代電腦已經沒有實體打字機，但作業系統仍然保留了這套終端通訊介面。透過軟體模擬出來的「假終端 / 虛擬終端」，就叫做 **PTY（Pseudo-Terminal）**。

### PTY 的雙向結構：Master 與 Slave
每個 PTY 都是成對出現的通道：
1. **Master 端（掌控者）**：由 **Herdr Daemon** 持有。負責攔截輸出、讀寫資料與注入模擬鍵盤按鍵。
2. **Slave 端（被控者）**：提供標準終端設備給 **Shell 或 Agent**（例如 OpenCode、Claude Code、Python）。

```text
[ Herdr Daemon ] <---> (Master 端) === [ PTY 通道 ] === (Slave 端) <---> [ Agent 應用程式 ]
```

### 為什麼普通管線 (Pipe) 不夠？為什麼 AI Agent 非要 PTY 不可？

很多人會問：「為什麼不能直接用 `echo "指令" | opencode` 這種普通的管道（Pipe）？」

1. **支援互動式 TUI 與 ANSI 顏色**：
   現代 AI Coding Agent（如 OpenCode 的 TUI 介面、豐富色彩、游標跳轉）在啟動時會檢查底層是否為「真實終端（TTY）」。如果只是普通 Pipe，程式會退化成純文字甚至直接崩潰報錯 `stdout is not a tty`。
2. **單鍵即時響應（Raw 模式）**：
   一般管道必須按 Enter 才能把整行送出；但 PTY 支援 Raw 模式，能夠即時傳遞 `Ctrl+C`、`Ctrl+X`、`Esc` 等單鍵訊號。
3. **讓 Agent「以為眼前坐著真人」**：
   PTY 創造了一個完美的擬真環境，讓所有命令列工具與 Agent 都以為自己正在直接與人類鍵盤螢幕互動。Herdr 藉由掌控 PTY Master 端，就能神不知鬼不覺地代表 Supervisor 注入提示詞並讀取終端畫面。

---

## 4. 技術架構數據流向圖

以下是 Supervisor、Herdr IPC 匯流排與各 SubAgent 的底層數據流架構：

![Herdr Supervisor 與 SubAgent 技術架構](assets/supervisor-subagent-arch.svg)

### 📖 專有名詞白話翻譯機：這張圖到底在講什麼？

技術架構圖看起來很硬核，但其實它的運作邏輯非常親民，以下用最白話的方式拆解各個核心名詞：

| 專有名詞 | 白話翻譯 | 它在圖中負責做什麼？ |
| :--- | :--- | :--- |
| **Pane（窗格）** | **終端機裡的獨立小房間** | 就像把螢幕切成左右兩半，左邊是主管的主控台，右邊是小弟們的工位，彼此視窗完全獨立。 |
| **Daemon（守護進程）** | **24 小時值班的隱形大管家** | 一個在背景默默執行的服務。主管想命令小弟，不是直接大吼，而是告訴管家，由管家代為傳達。 |
| **Unix Domain Socket** | **辦公室內部專線電話** | 主管發送指令給管家時走的高速專用通訊管道，安全又極速。 |
| **PTY（虛擬終端）** | **軟體打造的「虛擬替身」** | 讓 AI Agent 誤以為自己正坐在人類的螢幕鍵盤前面。管家透過 PTY 就能像真人一樣對 Agent「打字輸入」。 |
| **State（狀態探針）** | **工位門口的紅綠燈** | 顯示 `working`（工作中）、`blocked`（卡住等人救）、`done`（已做完等待驗收），主管看燈號就知道進度。 |
| **Git Worktree** | **專案的平行時空（影分身）** | 為子代理複製一個獨立的工作目錄，他在裡面亂搞刪檔案，都不會影響到主管或你正在寫的程式。 |

#### 🔍 圖中的 4 條箭頭路線是怎麼跑的？
1. **路線 ①「交辦任務」**：主管在主控台執行 `herdr agent prompt coder "任務需求"`，指令透過專線電話（Socket）送給管家。
2. **路線 ②「注入 Prompt」**：管家透過 PTY 虛擬鍵盤，自動把這段提示詞「一字不漏打進」子代理 A 的視窗中並按下 Enter。
3. **路線 ③「Done / 狀態回傳」**：子代理 A 寫完程式，門口的指示燈自動從 `working` 變成 `done`。管家回報主管：「小弟 A 做完了！」
4. **路線 ④「測試與日誌反饋」**：主管叫子代理 B 跑測試，子代理 B 把紅字錯誤日誌回傳給主管，主管據此指示子代理 A 繼續修改。


---

## 5. 實戰演練：Supervisor 調度 SubAgent 完整範例

本例示範：**Supervisor 代理**（位於自己的窗格，例如 `w1:p1`）如何透過 Herdr 指令，在右側開一個工作於獨立 worktree 的 **SubAgent 代理**（命名為 `coder`），交辦編寫單元測試的任務，並確認完成。

> [!NOTE]
> 以下指令以 herdr 0.9.3 為準。指令語法請以本機 `herdr pane`、`herdr agent` 印出的說明為準；Pane ID 一律從指令回傳的 JSON 讀取，**不要自己猜**（格式像 `w1:p2`）。

### 步驟 1：建立獨立的 Git Worktree

為了避免子代理與主專案衝突，先讓子代理在獨立分支上作業：

```bash
git worktree add .worktrees/feature-auth -b feature-auth
```

> 💡 Herdr 也內建 `herdr worktree create` 指令，可執行 `herdr worktree` 查看參數。

### 步驟 2：Supervisor 建立子窗格並取得 Pane ID

Supervisor 決定將工作交辦出去時，在自己的終端執行：

```bash
# 從「自己這個窗格」向右分割，新窗格直接進入 worktree 目錄，且不搶走使用者的焦點
SPLIT_JSON=$(herdr pane split --current --direction right \
  --cwd "$PWD/.worktrees/feature-auth" --no-focus)
SUB_PANE_ID=$(echo "$SPLIT_JSON" | jq -r '.result.pane.pane_id')

echo "已建立子代理窗格: $SUB_PANE_ID"
```

- `--current`：以呼叫者自己的窗格為基準分割，避免誤切到別人正在看的窗格。
- `--no-focus`：背景作業時不切換使用者的畫面焦點。
- 窗格較窄或較高時，可把 `right` 改成 `down`。

### 步驟 3：在子窗格啟動 SubAgent

用 `herdr agent start` 啟動 Agent 並取一個好記的名字（之後都用名字指揮它）：

```bash
herdr agent start coder --kind opencode --pane "$SUB_PANE_ID"
```

- 這個指令會等到 Herdr 偵測到 Agent 已就緒、可以接收輸入才返回（預設最多等 30 秒），不必自己猜「啟動好了沒」。
- `--kind` 可換成 `claude`、`codex`、`gemini` 等，完整清單請執行 `herdr agent`。
- 子窗格必須停在 shell 提示字元、沒有其他程式在前景執行。

### 步驟 4：Supervisor 交辦任務並等待完成

```bash
TASK_PROMPT="請閱讀 @src/auth.py，為密碼雜湊與 JWT 驗證撰寫單元測試放在 tests/test_auth.py。完成後請執行 uv run pytest 確認通過。"

# 送出任務（自動附帶 Enter），並等到 Agent 停下來（idle / done / blocked）
herdr agent prompt coder "$TASK_PROMPT" --wait --timeout 600000
```

`--wait` 取代了自己寫 `while` 迴圈輪詢：它會一直等到子代理做完或卡住才返回，`--timeout` 單位是毫秒（範例為 10 分鐘）。

返回後確認狀態並讀取子代理的輸出：

```bash
herdr agent get coder                                        # 查看目前狀態
herdr agent read coder --source recent-unwrapped --lines 120 # 讀取最近的終端輸出
```

- 若狀態是 `blocked`：代表子代理跳出批准或提問畫面，先用 `agent read` 看它在問什麼，再決定回覆內容（例如 `herdr agent send-keys coder enter`，或交給人類處理）。
- 若想專門等到「卡住要人批准」的時刻，可用 `herdr agent wait coder --until blocked --timeout 120000`。

### 步驟 5：Supervisor 評審成果（Code Review & 對話）

SubAgent 完成後，Supervisor 在自己的主控台中審查改動：

```bash
# Supervisor 檢查子代理在 worktree 中產生的 Git 差異
git -C .worktrees/feature-auth diff
```

- **若成果滿意**：Supervisor 將該 worktree 的分支 merge 回 main，並執行 `herdr pane close "$SUB_PANE_ID"` 關閉子窗格。
- **若需要補充修改（雙向對話）**：Supervisor 再次交辦反饋：
  ```bash
  herdr agent prompt coder "測試覆蓋率未達 80%，請補充邊界條件測試（例如空密碼與過期 Token）。" --wait --timeout 600000
  ```

### 補充：讓測試窗格跑一般指令（不是 Agent）

子代理 B（QA）若只是要跑測試指令，不需要啟動 Agent，用 pane 指令即可：

```bash
TEST_PANE_ID=$(herdr pane split --current --direction down \
  --cwd "$PWD/.worktrees/feature-auth" --no-focus | jq -r '.result.pane.pane_id')

herdr pane run "$TEST_PANE_ID" "uv run pytest"                           # 送出指令並按 Enter
herdr pane wait-output "$TEST_PANE_ID" --regex "passed|failed|error" --timeout 120000
herdr pane read "$TEST_PANE_ID" --source recent-unwrapped --lines 120     # 讀取測試結果
```

> [!TIP]
> **口訣**：控制「Agent」用 `herdr agent ...`（start / prompt / wait / get / read）；控制「一般終端指令」用 `herdr pane ...`（split / run / wait-output / read）。

---

## 6. Supervisor 角色提示詞 (Prompt Template)

當你在啟動主 Agent（Supervisor）時，可以把以下指示加入 Prompt 或專案的 `AGENTS.md`，賦予它調度子代理的能力：

```text
你現在是本專案的「主管架構師 (Supervisor Agent)」。
你負責總體任務規劃、架構決策與品質審查，嚴禁直接在大專案中進行大量代碼塗改。

【協同工具與職責】
1. 本環境運行於 Herdr 終端多工台（環境變數 HERDR_ENV=1），你具備執行 herdr CLI 的權限。
   指令語法以 `herdr pane`、`herdr agent` 印出的說明為準。
2. 當任務規模較大時，你必須：
   - 透過 git worktree 在 .worktrees/ 下建立獨立任務目錄。
   - 執行 `herdr pane split --current --direction right --cwd <worktree 路徑> --no-focus` 開啟 SubAgent 窗格，
     並從回傳 JSON 的 .result.pane.pane_id 取得 Pane ID。
   - 執行 `herdr agent start <名稱> --kind <agent 種類> --pane <pane_id>` 啟動 SubAgent。
   - 使用 `herdr agent prompt <名稱> "指令" --wait` 派發明確任務並等待完成。
3. 派發原則：明確給予「目標、範圍、驗收標準」。
4. 當 SubAgent 停下時，先用 `herdr agent get` 確認狀態；若為 blocked，用 `herdr agent read` 查看原因再處理。
5. 完成後使用 `git diff` 進行嚴格審查；驗收合格方可 merge。
6. 不得關閉不是你建立的窗格、分頁或工作區。
```

---

## 7. 多 Agent 協同的最佳實踐

1. **一任務一 Worktree**：
   強烈建議每個 SubAgent 都在獨立的 `git worktree` 目錄下工作，這樣多個子代理可以同時修改代碼，完全不會發生檔案寫入衝突。
2. **小步派發，避免模糊長任務**：
   Supervisor 派發給 SubAgent 的任務粒度越小（例如「專門補測試」、「專門重構單一函式」），成功率越高。
3. **Supervisor 專注驗收與驗證**：
   Supervisor 最大的價值在於「不帶偏見的第三方審查」。子 Agent 寫完代碼後，由 Supervisor 檢查 diff 並由測試窗格確認通過，杜絕 AI 幻覺與自誇。
4. **善用 Herdr 視覺化佈局**：
   人類開發者隨時可按 `prefix+w` 或使用滑鼠點擊各個窗格，隨時接管任何一個 SubAgent 的操作，人機協同最為順暢。

---

## 動手練習

看懂原理後，跟著由淺至深的 6 關小範例實際操作一次：👉 **[Herdr 多 Agent 協同練習](practice/README.md)**
