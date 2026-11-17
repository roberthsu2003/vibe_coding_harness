# 07　Subagent 子代理與自訂代理

> ★★★ 深入　｜　[← 06 專案規範與規則](06-agents-md.md)　｜　[章節首頁](README.md)　｜　下一站：[08 權限設定與沙盒 →](08-permissions.md)

**這一站你會學到**：
1. **什麼是子代理（Subagent）**：主代理如何把任務派給內建子代理（`research`、`browser`、`self`）。
2. **如何建立「自訂代理（Custom Agent）」**：提供「區域（專案）」與「全域（個人）」兩個完整動手範例。
3. **如何監控、停止與徹底刪除代理**：包含停止背景執行中的子代理，以及刪除自訂代理檔案的完整步驟。
4. **多代理團隊協作（`/swarm`、`/boost`、`/teamwork`）**：如何讓多個 AI 代理在共享留言板上平行分工與交叉檢查。

---

## 開始前：建立本節練習資料夾

先完成[課堂練習準備](../practice/README.md)的工具確認與教材下載，再在**一般終端機**逐行執行：

```bash
python3 ~/terminal-ai-course/practice/prepare.py ~/terminal-ai-labs/agy/07
cd ~/terminal-ai-labs/agy/07
agy
```

看到目的資料夾已存在時，直接 `cd` 進去接續；要重做則把路徑最後一段改成 `07-retry`。本節的程式、筆記與初始 Git commit 都已準備好。

---

## 1. 什麼是 Subagent（子代理）？

在專案變大或任務變複雜時，如果讓同一個 AI（主代理）包辦所有事，對話視窗很快就會被大量的搜尋紀錄和檔案內容塞滿，讓 AI 開始忘東忘西、回應變慢。

**子代理（Subagent）** 就像主代理派出來的專門助手，在背景獨立工作：

| 比較項目 | 主代理（Main Agent） | 子代理（Subagent） | [Skill（工作手冊）](05-skills.md) |
| :--- | :--- | :--- | :--- |
| **本質** | 與你直接對話的 AI 窗口 | 主代理派出去在背景跑的分身助手 | 給 AI 翻閱的步驟說明書（同一個 AI 執行） |
| **對話記憶（Context）** | 保留你整場對話的歷史紀錄 | **完全獨立的乾淨空間**，做完只把結論回報給主代理 | 共用目前對話視窗的記憶 |
| **執行方式** | 一次做一件事 | 可同時派出多個子代理在背景**平行處理** | 依手冊步驟依序執行 |
| **工具與權限** | 擁有全部預設工具 | 可限制只給特定工具（例如只給「唯讀」權限，不怕改壞程式） | 不額外隔離權限 |

---

## 2. 內建子代理 vs 自訂代理

`agy` 裡的代理分成兩大類，**這也是新手最容易搞混的地方**：

1. **內建子代理（Built-in Subagents）**：系統自帶（如 `research`、`browser`、`self`），隨時待命讓主代理在背景呼叫，**不會**列在終端機 `agy agent` 的自訂清單裡。
2. **自訂代理（Custom Agents）與外掛代理**：由你自己建立（放在 `.agents/agents/` 或 `~/.gemini/config/agents/`）或由 Plugin 安裝，會顯示在 `agy agent` 與 `/agents` 的 `Available Agents` 清單中。

### 四個常見的內建子代理

| 內建子代理名稱 | 專門做什麼 | 權限與特色 | 怎麼呼叫？ |
| :--- | :--- | :--- | :--- |
| **`research`** | 查資料與探索專案。負責大範圍搜尋檔案、讀懂架構或整理文件 | **唯讀沙盒環境**（無網路、不能改檔案），只看不改最安全 | 主代理自動派，或用中文點名：「`請派 research 子代理...`」 |
| **`browser`** | 開啟並操作 Chrome 瀏覽器，測試網頁畫面、點擊按鈕、讀網頁內容 | 透過 Chrome DevTools 操作網頁，沒有終端機或改檔權限 | 輸入 **`/browser <任務>`**，或請主代理打開網頁檢查 |
| **`self`** | 分身助手。複製一個跟主代理一模一樣的分身，在背景處理獨立子任務 | 繼承主代理的全部工具、規則與模型 | 主代理需要平行修改或測試時自動派出，也可直接點名 |
| **`image-generator`** | 依照文字描述產生或編輯圖片素材 | 專門產出圖片並回傳檔案路徑 | 請 AI 幫你產生圖片或 Logo 時自動呼叫 |

### 動手體驗：呼叫內建 `research` 子代理並觀察背景運作

不需要任何設定，現在直接在 `agy` 對話框輸入：

```text
請派出 research 子代理，幫我掃描目前資料夾有哪些 Markdown 檔案，整理成一份簡單的表格清單給我。
```

**觀察重點**：
1. 畫面上會顯示主代理呼叫了 `invoke_subagent`（角色如 `Workspace Markdown Scanner`）。
2. 輸入 **`/agents`** 打開代理管理面板，在 **Subagents** 區塊可以看到這個子代理的執行狀態（`running` 執行中 → `done` 已完成）。
3. 在該子代理上按 **`Enter`**，可以點進去偷看它在背景讀了哪些檔案、怎麼思考；按 **`Esc`** 返回。

---

## 3. 自訂代理（Custom Agent）：區域 vs 全域

除了內建子代理，你也可以自己寫一個 Markdown 檔（`agent.md`），打造專屬角色的代理（例如「資安審查員」、「Python 測試專家」、「筆記校對員」）。

自訂代理既可以當成**背景子代理**（讓主代理派工作給它），也可以切換成**主代理**（直接跟它對話）！

| 類型 | 存放路徑 | 適用範圍 | 適合放什麼 |
| :--- | :--- | :--- | :--- |
| **區域（專案代理）** | `<專案根目錄>/.agents/agents/<名稱>/agent.md`<br>（或 `.agents/agents/<名稱>.md`） | **只有這個專案**<br>（可 commit 進 Git 分享給組員） | 專案專屬的程式碼審查員、資料庫規則專家 |
| **全域（個人代理）** | `~/.gemini/config/agents/<名稱>/agent.md`<br>（或 `~/.gemini/config/agents/<名稱>.md`） | **你電腦上的所有專案** | 個人常用的文章潤稿員、錯字檢查員、資安稽核員 |
| **外部外掛（Plugin）** | `~/.gemini/config/plugins/<外掛名稱>/agents/*.md` | **所有專案**（隨外掛啟用） | 官方外掛附帶的專家（如 Firebase 外掛的 `firestore-rules-author`） |

> [!NOTE]
> - 專案資料夾名稱是 **`.agents`**（有 **s**），裡面的子資料夾也是 **`agents`**（有 **s**）。
> - 如果區域（專案）設定了自訂代理，請確認該專案資料夾已在啟動 `agy` 時選擇信任（Trusted Workspace），系統才會自動載入專案內的代理。

---

## 4. 完整實作範例：從零建立、測試到驗證

以下提供兩個完整範例，不管你有沒有寫程式都能跟著做完！

### 範例 1（區域・專案代理）：打造「嚴格程式碼審查員 `code-reviewer`」

我們先建立一個故意寫得很隨便的小程式，再建立一位**唯讀、只挑毛病不改檔**的 `code-reviewer` 代理來審查它。

#### 步驟 1：建立測試用的小程式 `calc.py`

在 `agy` 對話框輸入（或自己建立檔案）：

```text
請幫我建立一個簡單的 calc.py，裡面寫一個 divide(a, b) 函式直接回傳 a / b，不要加任何錯誤處理或註解。
```

#### 步驟 2：建立區域自訂代理 `.agents/agents/code-reviewer/agent.md`

在終端機執行以下指令（或直接請 AI 幫你建立這個檔案）：

```bash
mkdir -p .agents/agents/code-reviewer
cat << 'EOF' > .agents/agents/code-reviewer/agent.md
---
name: code-reviewer
description: 嚴格的程式碼審查專家，專門找出潛在 Bug、邊界條件錯誤與安全漏洞。當使用者要求進行 Code Review 或檢查程式碼品質時使用。
tools:
  - view_file
  - grep_search
  - find_by_name
  - list_dir
subagent: true
mainAgent: true
---

# 角色設定
你是一位嚴格但講話清楚的資深程式碼審查員（Code Reviewer）。
你只有讀取檔案的權限，**絕對不要自己修改檔案**，只負責提出審查報告。

# 審查步驟與輸出格式
請閱讀指定的程式碼，並固定以下列繁體中文格式回報：
1. **🎯 總體評分**（1～5 顆星）
2. **🐛 發現的潛在問題**（例如除以零、未處理例外、型別問題）
3. **💡 具體修改建議**（附上建議修改後的程式碼片段）
EOF
```

#### 步驟 3：確認 `agy` 有抓到這個新代理

1. **在一般終端機檢查**：
   ```bash
   agy agent
   ```
   輸出會顯示：
   ```text
   Available agents:
   code-reviewer
   ```
2. **在 `agy` 對話框檢查**：
   輸入 **`/agents`**，在上方 **`Available Agents`** 清單中就會看到 `code-reviewer`！

#### 步驟 4：實際呼叫測試（兩種用法都試試看！）

- **用法 A：當成「子代理」派出去檢查（推薦）**
  在原本的 `agy` 對話框直接說：
  ```text
  請派 code-reviewer 子代理幫我檢查 calc.py 有沒有潛在問題。
  ```
  主代理就會在背景派出 `code-reviewer`，並把「🎯 總體評分、🐛 發現的潛在問題、💡 具體修改建議」完整帶回來給你！

- **用法 B：切換成「主代理」直接跟它對話**
  - 方法 1：輸入 **`/agents`**，用 `↑` / `↓` 選中 `code-reviewer` 按 `Enter`（綠燈 `●` 代表選中），再按 `Esc` 離開面板，就會切換為 `code-reviewer`（若原本在對話中，會自動分支出一段新對話）。
  - 方法 2：從終端機啟動時直接指定：
    ```bash
    agy --agent code-reviewer
    ```

---

### 範例 2（全域・個人代理）：完全不寫程式！打造「筆記潤稿與錯字校對員 `note-editor`」

如果你常寫報告或 Markdown 筆記，可以把這個代理放在**全域目錄（`~/.gemini/config/agents/`）**，以後電腦上任何資料夾都能呼叫它！

#### 步驟 1：在全域目錄建立 `~/.gemini/config/agents/note-editor/agent.md`

在終端機執行（或在 `agy` 對話框請 AI 幫你建）：

```bash
mkdir -p ~/.gemini/config/agents/note-editor
cat << 'EOF' > ~/.gemini/config/agents/note-editor/agent.md
---
name: note-editor
description: 繁體中文筆記潤稿與錯別字校對專家。當使用者需要檢查文章錯字、排版或潤飾 Markdown 筆記時委派給此代理。
tools:
  - view_file
  - grep_search
  - find_by_name
  - list_dir
subagent: true
mainAgent: true
---

# 角色設定
你是一位細心的繁體中文文字編輯與 Markdown 排版顧問。

# 工作原則
1. 找出檔案中的錯別字、不通順的語句、中英文夾雜未加空白或標點符號問題。
2. 固定輸出一個「**修改前後對照表**」（欄位：原句、建議修改、原因說明）。
3. 最後給出一份排版與閱讀體驗的小建議。
EOF
```

#### 步驟 2：建立一份有錯字的測試筆記並呼叫 `note-editor`

回到 `agy` 對話框，依序輸入：

```text
# 1. 先建立一份故意寫錯字的短筆記
請幫我建立 draft-note.md，寫入這段話：「今天我學了如何使用AI代理，它可以幫我查資料、寫成式，真得非常方變又省時間！」

# 2. 派 note-editor 子代理去校對
請派 note-editor 子代理幫我檢查 draft-note.md 的錯字與排版。
```

**結果**：`note-editor` 會在背景讀完 `draft-note.md`，並整理出「寫成式 → 寫程式」、「真得 → 真的」、「方變 → 方便」的對照表格回報給你！

---

### 兩個自訂代理的驗收與重載

- **code-reviewer**：用 `cat calc.py` 記下原內容，完成審查後再執行 `git diff -- calc.py`。**應看到**報告指出除以零風險、三個指定小節，且沒有修改差異。若回覆只說啟動成功，請再點名要求它完成檢查並回傳報告。
- **note-editor**：讀取 `draft-note.md`，報告應至少指出「成式／真得／方變」三處錯字。另建一個空資料夾、在其中啟動 agy，輸入 `/agents` 應仍找到 `note-editor`，但找不到專案限定的 `code-reviewer`，這才驗證了全域與區域的差別。
- **載入**：若建立後選單沒有更新，先離開並在本章資料夾重新啟動 agy，再輸入 `/agents`。全域練習前請確認同名檔案原本不存在，避免覆蓋自己的代理。

### 其餘內建子代理也實際試一次

| 角色 | 準備與輸入 | 驗收與收尾 |
| :--- | :--- | :--- |
| research | 本章已附 README 與 notes/；輸入 `請派 research 子代理列出 notes/ 的 Markdown 檔名、標題與行數，只讀不改。` | 清單至少含 ch1、ch2、ch3、faq；對照一般終端機 `wc -l notes/*.md` |
| self | 輸入 `請派 self 子代理建立 self-summary.md，讀取 README.md 後寫出三點摘要。` | `cat self-summary.md` 有三點摘要，且在 `/agents` 有對應紀錄 |
| browser | 先完成 [03-C 瀏覽器練習](03-slash-commands/c-tasks.md#browser讓-ai-操作瀏覽器查資料) | 看到瀏覽器工具紀錄與本機頁面結果，結束後停止伺服器 |
| image-generator | 輸入 `請使用 image-generator 產生一張沒有文字的藍色機器人插圖，存成 robot.png，最後回報實際路徑。` | 用檔案總管打開回報的圖片；需帳號支援圖片功能與額度。無權限時記錄限制，不能以文字描述當成圖片成果 |

### 停用、恢復與停止的實測

在一般終端機把 `.agents/agents/code-reviewer/agent.md` 改名成 `agent.md.bak`，重新啟動，確認 `code-reviewer` 不在清單；再改回並重啟，確認重新出現。

要觀察停止操作，送出 `請派 research 子代理逐一閱讀目前全部 Python 和 Markdown 檔，整理每個檔案的用途與行數。`，立刻進入 `/agents`。若仍為 `running`，選中後按 `K`，確認狀態變為已停止；若已做完，直接查看完成紀錄即可，不必為了練習強行重啟更多工作。最後依第 6 節只清除本次建立的代理；重啟後確認這兩個名稱消失，其他既有代理仍在。

## 5. 看懂 `agent.md` 設定欄位（YAML Frontmatter）

自訂代理檔案最上方兩條 `---` 之間的設定欄位如下：

| 欄位名稱 | 必填 | 預設值 | 說明與常用設定 |
| :--- | :---: | :---: | :--- |
| **`name`** | ✅ | — | 代理的唯一英文名稱（小寫英文＋連字號，如 `code-reviewer`），建議與資料夾名稱一致 |
| **`description`** | ✅ | — | **最關鍵的欄位**：寫清楚「這個代理擅長做什麼、何時該派它上場」，主代理會根據這段話決定要不要自動派工作給它 |
| **`subagent`** | | `true` | 設為 `true` 時，主代理可以在背景把它當成子代理呼叫（`invoke_subagent`） |
| **`mainAgent`** | | `true` | 設為 `true` 時，會出現在 `/agents` 選單與 `agy --agent <名稱>`，讓你直接拿它當主代理對話 |
| **`tools`** | | 唯讀基本工具 | 允許此代理使用的工具清單。常用工具名稱：<br>• 唯讀類：`view_file`、`grep_search`、`find_by_name`、`list_dir`<br>• 修改與執行類：`write_to_file`、`replace_file_content`、`run_command` |
| **`model`** | | `inherit` | 指定此代理使用的模型等級：`inherit`（跟隨主代理）、`flash`（速度快）、`pro`（深度推理） |
| **`commandExecutionPolicy`** | | `sandbox` | 終端機指令執行策略：`sandbox`（沙盒安全執行）、`auto`、`eager`、`off` |
| **`skills`** | | `[]` | 掛載給這個代理使用的 Skill 路徑清單（例如 `skills/security-checklist`） |

> [!WARNING]
> **注意 `tools` 名稱不要拼錯**：如果在 `tools` 填了不存在或拼錯的工具名稱，可能會導致子代理啟動時卡住（Hang）。若只需要唯讀檢查，照上面範例填 `view_file`、`grep_search`、`find_by_name`、`list_dir` 最安全；若不確定工具名稱，也可以先省略 `tools` 欄位。

---

## 6. 如何監控、停止與徹底刪除代理？（超重要！）

使用子代理與自訂代理時，「刪除／停止」分成兩種情況：
- **情況 A**：某個子代理正在背景跑（或卡住了），你想**強制停止（Kill）它**。
- **情況 B**：你練習完或不再需要某個自訂代理（如剛剛建的 `code-reviewer`、`note-editor`），想**把它從電腦或專案裡徹底刪掉**。

---

### 情況 A：監控與強制停止「正在背景執行的子代理」

當主代理派出子代理時，你可以隨時在 **`/agents`** 面板掌控它的一舉一動：

```text
/agents
```

#### `/agents` 面板操作與快捷鍵

| 按鍵 / 操作 | 功能說明 |
| :--- | :--- |
| **`↑` / `↓`** | 在 `Available Agents`（可用代理）與 `Subagents`（背景子代理）之間上下移動 |
| **`Enter`** | • 在群組標題按 `Enter`：展開或收合子代理清單<br>• 在某個子代理上按 `Enter`：進入全螢幕 **Detail View**，查看它的完整思考過程與指令輸出 |
| **`K`**（或 `k`） | **🔥 強制停止（Kill）正在執行（`running`）的子代理**（包含它底下的所有子執行緒與暫存工作區） |
| **`A` / `D`** | 當子代理請求權限（例如要改檔或跑指令）時，直接按 **`A` 同意（Approve）** 或 **`D` 拒絕（Deny）** |
| **`Esc`** | 離開 Detail View 或關閉 `/agents` 面板回到對話框 |

> [!TIP]
> **不進 `/agents` 面板也能快速操作**：
> - **直接用講的叫主代理停掉它**：在對話框輸入「`請停止目前正在執行的子代理`」。
> - **在對話框外快速審核權限**：按 **`Alt+J`** 跳到正在等你同意的子代理，或按 **`Ctrl+K`** 直接批准狀態列上的子代理請求。
> - **直接私訊某個子代理追加指示**：在對話框輸入 `@<子代理名稱> <你的指示>`（例如 `@research:Workspace-Scanner 順便幫我算一下總共有幾行`），如果該子代理已經完成進入待命（`Idle`），收到訊息會自動醒來繼續做！

---

### 情況 B：建立、停用與徹底刪除「自訂代理檔案」總整理

練習完第 4 節的 `code-reviewer` 與 `note-editor` 後，可以用下表的方法停用或徹底刪除：

| 操作項目 | 區域（專案代理） | 全域（個人代理） | 外部外掛代理（Plugin） |
| :--- | :--- | :--- | :--- |
| **檔案位置** | `.agents/agents/<名稱>/agent.md`<br>（或 `.agents/agents/<名稱>.md`） | `~/.gemini/config/agents/<名稱>/agent.md`<br>（或 `~/.gemini/config/agents/<名稱>.md`） | `~/.gemini/config/plugins/<外掛名>/agents/` |
| **查看目前已載入** | 終端機跑 `agy agent`<br>或對話框打 `/agents` | 終端機跑 `agy agent`<br>或對話框打 `/agents` | 終端機跑 `agy agent`<br>或對話框打 `/plugin` |
| **暫時停用（不刪除）** | 把 `agent.md` 改名為 `agent.md.bak` | 把 `agent.md` 改名為 `agent.md.bak` | `agy plugin disable <外掛名>` |
| **徹底刪除（終端機指令）** | `rm -rf .agents/agents/<名稱>` | `rm -rf ~/.gemini/config/agents/<名稱>` | `agy plugin uninstall <外掛名>` |
| **徹底刪除（免打指令・叫 AI 刪）** | 對 AI 說：<br>`請幫我刪除這個專案的 <名稱> 自訂代理` | 對 AI 說：<br>`請幫我刪除全域的 <名稱> 自訂代理` | 輸入 `/plugin` 從管理面板移除外掛 |

#### 動手清理：把剛剛練習建立的兩個自訂代理刪掉

你可以選擇**在終端機執行指令**，或**直接請 AI 幫你刪除**：

**方法一：在一般終端機執行刪除指令並驗證**

```bash
# 1. 刪除區域（專案）的 code-reviewer 代理與測試檔
rm -rf .agents/agents/code-reviewer calc.py

# 2. 刪除全域（個人）的 note-editor 代理與測試筆記
rm -rf ~/.gemini/config/agents/note-editor draft-note.md

# 3. 檢查是否已徹底清除（若無其他自訂代理，輸出應為空白）
agy agent
```

**方法二：直接在 `agy` 對話框用中文請 AI 刪除**

```text
請幫我刪除這個專案的 code-reviewer 自訂代理（.agents/agents/code-reviewer），以及全域的 note-editor 自訂代理（~/.gemini/config/agents/note-editor），並順便刪掉測試用的 calc.py 與 draft-note.md。
```

刪完後重新啟動，再輸入 **`/agents`**，確認本次建立的 `code-reviewer` 與 `note-editor` 已消失；原本安裝的其他代理應保留。

---

## 7. `/swarm`：平行代理協作團隊

一般子代理是「主代理派一個小助手去查資料，查完私下回報給主代理」；但當一個大任務可以拆成**好幾個不會互相衝突的檔案或模組**，而且你希望有專門的審查員（`@verifier`）幫大家檢查改動、跑測試時，就可以出動 **`/swarm`**（目前為 Preview，支援 Google AI Pro 與 Ultra 方案）。

### 怎麼運作？協調者、工作代理與共享留言板

當你輸入 `/swarm <任務>` 時，目前的對話會變成團隊的**協調者（Coordinator）**，自動幫你組隊：

1. **拆工作、一人負責一塊**：協調者把任務拆開，指派給具名的工作代理（例如 `@day1-writer`、`@day2-writer`）。如果多個代理需要同時改程式碼，協調者可以給每個代理獨立的工作區副本（Workspace `share` 或 `branch`），不會互相蓋掉檔案。
2. **公開任務簡報（Brief）**：協調者會在**共享留言板**貼出簡報，寫清楚每個人負責哪個檔案、哪裡不能動，以及怎樣算完成。
3. **專屬審查員（`@verifier`）**：通常每 2～4 位工作代理會配一位 `@verifier`。它不負責寫功能，專門看大家的修改差異、檢查品質或跑測試，發現問題就在留言板 `@` 負責的代理修好。
4. **共享留言板與休眠省額度**：所有進度、提問與檢查結果都貼在留言板上。還在等別人回覆的代理會進入休眠（`waiting`），**休眠時完全不消耗額度**，直到有人在留言板 `@` 它的名字才會醒來繼續做。

> [!CAUTION]
> **注意額度消耗**：Swarm 裡的每位成員都是獨立的 AI 代理，消耗模型額度（Quota）的速度會比單一對話快。如果某位成員額度用完了，它會先暫停並提示你；這時可以請協調者幫它切換成另一個模型繼續做。

---

### 完整範例：用 `/swarm` 讓多位代理平行寫檔案並交叉檢查

#### 1. 啟動 Swarm

在 `agy` 對話框輸入（完全不寫程式也能測試）：

```text
/swarm 規劃「台北出發兩天一夜台南美食之旅」，請派兩位代理分別建立 tainan-day1.md 與 tainan-day2.md（各自包含早中晚行程與預估花費），最後由 verifier 審查兩個檔案格式一致且兩天總預算不超過台幣 6,000 元
```

啟動後，對話框下方會出現 **Swarm 即時狀態列**，顯示目前的討論和誰正在工作。全部完成後，按 **`Alt+X`** 可以收起狀態列。

#### 2. 開啟全螢幕即時看板（Live Board）

輸入 **`/swarm board`** 或按快捷鍵 **`Alt+S`**（macOS 終端機需將 Option 設為 Meta/Alt 鍵），就能打開全螢幕看板，裡面有三個窗格：
- **Roster（成員名單）**：看誰在工作（`working`）、誰在待命（`waiting`）、誰已被終止（`killed`）、用哪個模型。
- **Posts（貼文動態）**：留言板上的所有對話紀錄。
- **Message（訊息內容）**：完整顯示目前選中的貼文。

**看板常用按鍵：**

| 按鍵 | 功能 |
| :--- | :--- |
| `j` / `k` 或 `↓` / `↑` | 上下移動選取貼文、成員，或捲動內容 |
| `g` / `G` | 跳到第一則或最後一則 |
| `Tab` / `Shift+Tab` | 在 Roster、Posts、Message 三個窗格之間切換 |
| `Enter` 或 `Space` | 展開或收合選中的貼文與成員細節 |
| `f` | 開關自動跟隨最新貼文（Follow mode） |
| `p` | 只看選中成員的發言；再按一次 `p` 或 `Esc` 顯示全部 |
| `z` | 把目前的窗格放大到全螢幕，或還原 |
| `o` | 直接打開該成員的獨立對話視窗 |
| `q` 或 `Esc` | 離開看板，回到對話框 |

#### 3. 中途調整方向、私訊成員或停止 Swarm 成員

- **改方向**：直接跟主對話的協調者說，它會在留言板上通知大家。
- **私訊某位成員**：在輸入框用 `@` 點名（只會送給那個代理，不會貼上公開留言板）：
  ```text
  @verifier 請順便確認兩天的行程有沒有排到週一公休的店家
  ```
- **停止／移除某位 Swarm 成員**：直接對主對話的協調者說「`請結束（kill）所有已完成的 swarm 成員`」或指定成員名稱，協調者就會終止該成員並自動清理它的暫存工作區（Worktree）。
- **清理練習產生的檔案**：測試完後，可請 AI 刪掉 `tainan-day1.md` 與 `tainan-day2.md`。

---

### 更多程式碼開發 `/swarm` 實用範例（都有現成素材）

以下每題請用新的練習資料夾（例如 `07-code1`、`07-code2`），依本章開頭的 `prepare.py` 指令建立後再啟動 agy。這樣不用先有 TypeScript 或 Go 專案，也能完整實作。

| 題目與準備 | 在輸入框送出 | 一般終端機驗收 |
| :--- | :--- | :--- |
| 多檔加測試：使用素材中的 calc 與 auth | `/swarm 請兩位 worker 分別在 tests/test_calc.py 加入負數除法邊界測試、在 tests/test_auth.py 加入空帳號與空密碼的測試，不修改程式，由 verifier 執行 python3 -m unittest discover -s tests -v。` | 測試數增加且全部 OK；`git diff` 只包含兩份測試檔 |
| 不同模型檢查：先用 /model 確認可用模型 | `/swarm 為 calc.py 的 divide 加上除數為零時拋出 ValueError("除數不可為零") 的行為，補測試；若帳號有另一可用模型，讓 verifier 用不同模型檢查並執行 python3 -m unittest discover -s tests -v，無其他模型則明確回報並沿用。` | 新增零除數測試且全部 OK；看板列出的模型與結果一致 |
| 平行調查：使用現有 src/ | `/swarm 請兩位唯讀 worker 分別調查 src/server.py 的呼叫流程、src/auth.py 的登入判斷，verifier 對照原始碼，最後主代理建立 call-report.md，不改任何 Python 檔案。` | 報告能連起 handle_request → welcome → login；Python 檔案無差異 |
| 修失敗測試：終端機先 cd broken，執行 python3 -m unittest -v，應 3 題中 2 題失敗 | `/swarm 只修正 broken/calc.py 的 add 實作，不修改測試；由 worker 分析與修復，verifier 在 broken/ 執行 python3 -m unittest -v，三個測試全部通過才完成。` | `(cd broken && python3 -m unittest -v)` 顯示 3 題 OK，`git diff -- broken/test_calc.py` 無輸出 |

每題完成後輸入 `/swarm board` 查看審查結果，按 `Esc` 返回；請協調者結束已完成成員，再按 `Alt+X` 收起狀態列。兩天旅遊範例也要實際開啟兩份檔案核對早中晚、花費與總預算；金額只作虛構練習估算。

### `/boost` 與 `/teamwork` 也有完整練習

- **Boost**：在本章素材送出 `/boost 請深入檢查 calc.py 的 divide 在整數、負數、除以零時的行為，只讀不改；建立 divide-review.md，包含三種輸入、實際結果、風險與建議。`。**驗收**：報告至少列出 `(12, 3)`、`(-6, 2)`、`(1, 0)`，最後一項指出目前會拋 `ZeroDivisionError`；`git diff -- calc.py` 無改動。
- **Teamwork（付費功能）**：先閱讀 [03-C 的完整訪談與分階段範例](03-slash-commands/c-tasks.md)，使用已附 `notes/` 作素材。**驗收**：依該節逐項核對章節、索引與審查結果，完成後停止團隊。


---

## 8. 怎麼選？Subagents、`/boost`、`/swarm` 與 `/teamwork`

**先決定模型如何搭配，再決定任務怎麼分工。** [Orchestrator](01-install.md#orchestrator自動搭配規劃與執行模型) 在 `/model` 裡選擇，讓規劃與執行模型在同一項任務中自動交接；下表則幫你選擇子代理與多代理團隊的工作方式。日常功能開發可先使用一般子代理或 Orchestrator；需要多位具名代理平行處理不同模組時，再考慮 `/swarm`。[官方 Subagents 說明](https://antigravity.google/docs/subagents)、[官方 `/agents` 指令說明](https://antigravity.google/docs/cli/commands/agents/)

| 比較項目 | Subagents（子代理／自訂代理） | `/boost` | `/swarm` | `/teamwork` |
| :--- | :--- | :--- | :--- | :--- |
| **什麼時候用** | 派一個專門助手查資料、審程式碼、校對文件或操作瀏覽器 | 很難的單一問題（如棘手 Bug、演算法、深度比較分析） | 可以拆成好幾個獨立檔案或模組同時平行處理 | 全專案大改版、跨階段的長期工程（如整個專案換框架） |
| **合作方式** | 子代理在背景獨立做完，直接把結論回報給主代理 | 多個代理從不同角度推理、挑戰盲點並交叉驗證 | 具名工作代理與審查員（`@verifier`）在共享留言板合作 | 先訪談定規格，再依里程碑與審核關卡推進 |
| **怎麼啟動** | 主代理自動派、用中文點名，或用 `/agents` 切換 | `/boost <問題>` | `/swarm <任務>` | `/teamwork <目標>` |
| **怎麼停止／刪除** | 在 `/agents` 按 **`K`** 停止背景子代理；刪掉 `.agents/agents/<名稱>` 移除自訂代理 | 按 `Ctrl+C` 中斷目前回合 | 請協調者 `kill` 成員；按 `Alt+X` 收起狀態列 | 按 `Ctrl+C` 中斷目前回合 |

---

## 9. 常見問題排解

| 遇到的狀況 | 原因與解決方法 |
| :--- | :--- |
| **在終端機跑 `agy agent` 卻什麼都沒顯示** | `agy agent` 只會列出**自訂代理**與**已啟用外掛附帶的代理**；內建子代理（`research`、`browser`、`self`）本來就不會顯示在裡面，主代理隨時都能直接呼叫它們。 |
| **建立了 `.agents/agents/<名稱>/agent.md`，但 `/agents` 裡沒看到** | 1. 確認資料夾名稱有加 **s**：`.agents/agents/<名稱>/agent.md`。<br>2. 確認 `agent.md` 最開頭有 `---` 包住的 `name` 與 `description`。<br>3. 確認該專案資料夾已被加入信任清單（Trusted Workspace）。 |
| **自訂子代理啟動後一直卡住沒回應** | 檢查 `agent.md` 的 `tools:` 清單是否有拼錯字（例如把 `view_file` 寫成 `read`）。在 `/agents` 面板選中它按 **`K`** 強制停止，修正 `agent.md` 後再試一次。 |
| **在 `/agents` 面板對某個子代理按 `K` 沒反應** | **`K`** 只能用來停止正在執行中（`running`）的子代理；如果狀態已經是 `done`、`error` 或 `killed`，它已經結束並釋放資源了（不消耗任何額度），按 `Enter` 可看歷史紀錄。 |

---

## ✅ 自我檢查

- [ ] 說得出**內建子代理**（`research`、`browser`、`self`）與**自訂代理**（`agent.md`）的差別
- [ ] 跟著第 4 節實際建立過一個自訂代理（如 `code-reviewer` 或 `note-editor`），並在 `/agents` 中看到它
- [ ] 知道怎麼在 `/agents` 按 **`K`** 停止正在背景跑的子代理，並練習完把剛剛建立的自訂代理徹底刪除
- [ ] 說得出一般子代理、`/boost`、`/swarm` 與 `/teamwork` 各自適合在什麼時候用

---

[← 06 專案規範與規則](06-agents-md.md)　｜　[章節首頁](README.md)　｜　下一站：[08 權限設定與沙盒 →](08-permissions.md)
