# 03　斜線指令

> ★ 入門　｜　[← 02 基本操作](02-basics.md)　｜　[章節首頁](README.md)　｜　下一站：[04 環境配置 →](04-config.md)

**這一站你會學到**：什麼是斜線指令、新手必學的 8 個指令，以及每個常用指令的小範例。

![斜線指令地圖](assets/slash-map.svg)

---

## 1. 怎麼使用斜線指令？

斜線指令（Slash Command）是 agy 對話框裡的快捷功能，以 `/` 開頭。

1. 在對話框輸入 `/`，會跳出指令選單。
2. 繼續打字可以篩選，例如輸入 `/co` 會看到 `/compact`、`/config`、`/context`。
3. 按 `Enter` 執行。

有些指令可以直接接上一句中文，agy 會把這句話當成任務：

```text
/plan 幫購物車加上折扣碼功能
```

> [!TIP]
> 不用背！本章的範例都能直接複製來試。真的忘記時，輸入 `/help` 就能看到完整清單。

---

## 2. 新手必學 8 個指令

| 指令 | 一句話說明 | 什麼時候用 |
| :--- | :--- | :--- |
| [`/help`](#help查看所有指令) | 查看所有指令 | 忘記指令時 |
| [`/plan`](#plan先規劃再動手) | 先規劃，再動手 | 要做比較大的修改時 |
| [`/diff`](#diff看-ai-改了什麼) | 看 AI 改了什麼 | AI 改完檔案後 |
| [`/compact`](#compact壓縮對話) | 壓縮對話 | 對話太長、回應變慢時 |
| [`/clear`](#clear開始新對話) | 開始新對話 | 換一個新任務時 |
| [`/rewind`](#rewind回到之前的對話) | 回到之前的對話 | AI 走錯方向時 |
| [`/model`](#model切換模型) | 切換模型 | 想換快一點或強一點的模型時 |
| [`/exit`](#exit離開-agy) | 離開 agy | 下課時 |

---

## 3. A 區：查狀態

### `/help`：查看所有指令

```text
/help
```

**結果**：列出所有斜線指令和快捷鍵。直接輸入 `?` 也可以。

### `/context`：看對話空間用了多少

```text
/context
```

**結果**：開啟用量面板。如果快滿了，就該用 `/compact` 壓縮。

### `/usage`：看模型額度

```text
/usage
```

**結果**：顯示目前的模型使用額度。看到 429 或額度不足的錯誤時，先來這裡確認。別名：`/quota`。

### `/credits`：看剩餘點數

```text
/credits
```

**結果**：顯示剩餘的 G1 點數和購買連結。

### `/changelog`：看這一版更新了什麼

```text
/changelog
```

**結果**：開啟版本更新說明。

---

## 4. B 區：管對話

### `/compact`：壓縮對話

```text
/compact
```

**結果**：把前面的對話整理成摘要，騰出空間，然後結束這一輪。

也可以壓縮完馬上接著問：

```text
/compact 接下來請繼續完成登入頁面的表單驗證
```

### `/clear`：開始新對話

```text
/clear
```

**結果**：清空畫面並重置對話內容，適合換任務時使用。別名：`/new`。

### `/resume`：回到以前的對話

```text
/resume
```

**結果**：開啟對話清單，選一個就能接著做。別名：`/switch`、`/conversation`。

### `/rewind`：回到之前的對話

```text
/rewind
```

**結果**：列出之前的訊息，選一則就能把對話退回那個時間點。別名：`/undo`。

> [!NOTE]
> 退回之後，請用 `/diff` 或 `git status` 確認檔案的狀態是否符合你的預期。

### `/fork`：複製一份對話來試別的做法

```text
/fork
```

**結果**：複製目前的對話到新的工作階段。試失敗了，用 `/resume` 就能回到原本的對話。別名：`/branch`。

> [!WARNING]
> `/fork` 只複製**對話**，不會複製你的檔案。要隔離檔案，請搭配 [Git 分支或 worktree](../worktree/README.md)。

### `/btw`：順便問個問題

AI 正在工作，你突然想問別的事，又不想打斷它：

```text
/btw pytest 的 -v 參數是什麼意思？
```

**結果**：回答你的問題，主要任務不受影響。

### `/rename`：幫對話取名字

```text
/rename 購物車折扣碼功能
```

**結果**：之後在 `/resume` 的清單裡更容易找到這個對話。

---

## 5. C 區：派任務

### `/plan`：先規劃，再動手

```text
/plan 幫購物車加上折扣碼功能
```

**結果**：AI 先讀程式碼，寫出計畫給你確認，你同意後才開始改檔案。

### `/grill-me`：讓 AI 先問清楚需求

只有模糊的想法時最好用：

```text
/grill-me 我想做一個記帳網站
```

**結果**：AI 一次問你一個問題，例如「要不要登入功能？」，全部釐清後才開始動手。

指令可以連著用，先問清楚、再寫計畫：

```text
/plan /grill-me 我想做一個記帳網站
```

### `/goal`：不做完不停

```text
/goal 修好 tests/ 裡所有失敗的測試，直到全部通過
```

**結果**：AI 自動重複「修改 → 測試 → 修正」，中途不會停下來問你，直到確認目標達成。

> [!CAUTION]
> `/goal` 會持續運作，也會持續消耗額度。請先 commit 程式碼，並把完成條件寫清楚。想停下來時，按 `Ctrl+C` 中斷。

### `/browser`：讓 AI 操作瀏覽器

```text
/browser 打開 http://localhost:3000，確認登入按鈕點了有沒有反應
```

**結果**：派一個瀏覽器子代理開啟 Chrome 操作並回報，適合檢查網頁畫面或查資料。

### `/schedule`：定時執行

```text
/schedule 10m 檢查測試是否全部通過，再告訴我結果
```

**結果**：10 分鐘後執行一次。也可以設定固定週期：

```text
/schedule 每 30 分鐘 檢查一次 git status，有未提交的變更就提醒我
```

> [!NOTE]
> 排程是在 agy 裡的背景工作，執行期間請讓 agy 保持開啟。用 `/tasks` 可以查看。

### `/boost`：多代理深度思考

```text
/boost 分析為什麼結帳頁面偶爾會算錯金額
```

**結果**：多個代理反覆推理，適合很難的問題。因為動用多個代理，簡單的任務不需要用它。

### `/learn`：把這次學到的存起來

AI 這次犯的錯，下次不想再糾正一遍：

```text
/learn 記住這個專案一律用 uv，不要用 pip
```

**結果**：AI 整理出規則或 Skill，經你確認後保存。下次對話會自動套用。

### `/swarm`：平行代理協作團隊

當任務可以拆分成互不衝突的多個檔案、模組或調查方向時，派出多位具名代理平行動工，並由專屬審查代理（Verifier）跑測試與把關：

```text
/swarm 為 src/utils/date.ts 與 src/utils/currency.ts 補上單元測試，並執行 npm test 驗證
```

**結果**：主對話轉為協調者（Coordinator），自動建立具名工作代理（如 `@date-tests`、`@currency-tests`）與審查代理（`@verifier`），透過共享留言板同步進度。

執行期間可隨時開啟全螢幕即時看板觀看團隊討論與狀態：

```text
/swarm board
```

> [!WARNING]
> `/swarm` 目前為 Preview 功能，支援 **Google AI Pro** 與 **Google AI Ultra** 方案。由於每個工作代理都是獨立的 AI 代理，額度消耗速度會比單一對話快上許多。完整操作與快捷鍵（`Alt+S`）請見 [07 Subagent 與 Swarm](07-subagents.md#5-swarm平行代理協作團隊)。

### `/teamwork`：組一個長期專案 AI 團隊

```text
/teamwork 把這個網站從 JavaScript 改寫成 TypeScript
```

**結果**：先與你訪談確認規格，再由多個代理依里程碑與審核關卡分工處理大型長期專案。**僅限付費方案**，與 `/swarm` 的差異請見 [07 多代理模式比較](07-subagents.md#7-怎麼選subagentsboostswarm-與-teamwork)。

---

## 6. D 區：看成果

### `/diff`：看 AI 改了什麼

```text
/diff
```

**結果**：開啟變更檢視器，可以依「全部變更」、「每一輪」或「commit」查看。在檔案裡按 `Esc` 返回。

> [!TIP]
> 養成習慣：**AI 改完先看 `/diff`，確認沒問題再 commit。**

### `/artifact`：看 AI 產出的計畫

```text
/artifact
```

**結果**：開啟產出物審查面板，查看計畫、任務清單等文件。快捷鍵：`Ctrl+R`。

### `/tasks`：看背景工作

```text
/tasks
```

**結果**：開啟工作管理員，查看背景指令的記錄與排程的狀態。

### `/codesearch`：搜尋程式碼

```text
/codesearch 計算折扣
```

**結果**：開啟程式碼搜尋面板。別名：`/cs`、`/search`。

### `/copy`：複製 AI 的回答

```text
/copy
```

**結果**：複製最後一則回答。`/copy 2` 複製倒數第二則，`/copy btw` 複製最新的 `/btw` 回答。

### `/open`：用編輯器開檔案

```text
/open src/app.py
```

**結果**：用系統預設的編輯器開啟檔案。

---

## 7. E 區：調環境

這一區的指令都和[環境配置](04-config.md)有關。

### `/model`：切換模型

```text
/model
```

**結果**：開啟模型選單，選擇之後的預設模型。

也可以只有這一句換模型：

```text
/model gemini-4-argon-high 幫我檢查這段程式有沒有資安問題
```

### `/effort`：調整思考強度

```text
/effort high
```

**結果**：讓模型想得更深，但會比較慢。等級由低到高為 `low`、`medium`、`high`、`xhigh`、`max`，實際可用的等級依模型而定。

### `/config`：開啟設定選單

```text
/config
```

**結果**：開啟設定選單，可以修改執行模式、配色、通知等。別名：`/settings`。

### `/permissions`：管理 AI 的權限

```text
/permissions
```

**結果**：開啟權限管理畫面，查看或修改哪些操作允許、詢問或禁止。詳見 [08 權限設定與沙盒](08-permissions.md)。

### `/add-dir`：把別的資料夾加進來

```text
/add-dir ~/projects/shared-library
```

**結果**：AI 也能讀寫這個資料夾。

### `/skills`：查看 Skill

```text
/skills
```

**結果**：瀏覽已載入的 Skill。剛新增 Skill 時，輸入 `/skills reload` 重新載入。詳見 [05 Skill 配置](05-skills.md)。

### `/agents`：管理代理

```text
/agents
```

**結果**：開啟代理管理畫面，查看自訂代理和背景子代理。

### `/mcp`：管理 MCP 伺服器

```text
/mcp
```

**結果**：開啟 MCP 伺服器管理畫面，查看連線狀態。

### `/plugin`：管理外掛

```text
/plugin list
```

**結果**：列出已安裝的外掛。只輸入 `/plugin` 會開啟管理畫面。別名：`/plugins`。

### `/exit`：離開 agy

```text
/exit
```

**結果**：結束這次工作階段，回到終端機。別名：`/quit`。

---

## 8. 其他指令速查

比較少用，知道有這些功能就好：

| 指令 | 用途 | 小範例 |
| :--- | :--- | :--- |
| `/feedback` | 開啟意見回饋面板 | `/feedback` |
| `/hooks` | 瀏覽目前啟用的 Hook | `/hooks` |
| `/keybindings` | 修改快捷鍵 | `/keybindings` |
| `/logout` | 登出並移除登入憑證 | `/logout` |
| `/remote-control` | 開關遠端控制 | `/remote-control on` |
| `/statusline` | 自訂底部狀態列 | `/statusline` |
| `/title` | 開關終端機標題更新 | `/title off` |
| `/voice` | 語音對話或語音輸入 | `/voice dictate` |

---

## 9. 動手練習

在任何一個練習專案裡，依序輸入：

| 步驟 | 輸入 | 觀察重點 |
| :---: | :--- | :--- |
| 1 | `/help` | 看看有哪些指令 |
| 2 | `/plan 幫我新增一個 hello.py，執行時印出今天的日期` | 計畫裡寫了什麼？同意後讓它執行 |
| 3 | `/diff` | AI 改了哪些檔案？ |
| 4 | `/btw Python 怎麼取得今天的日期？` | 主要對話有被影響嗎？ |
| 5 | `/context` | 用掉了多少對話空間？ |
| 6 | `/compact` | 再看一次 `/context`，有變少嗎？ |

---

[← 02 基本操作](02-basics.md)　｜　[章節首頁](README.md)　｜　下一站：[04 環境配置 →](04-config.md)
