# 04　環境配置

> ★★ 進階　｜　[← 03 斜線指令](03-slash-commands.md)　｜　[章節首頁](README.md)　｜　下一站：[05 Skill 配置 →](05-skills.md)

**這一站你會學到**：agy 的設定檔放在哪裡、怎麼修改常用設定、怎麼設定個人規則與 MCP，以及如何檢查環境。

![agy 的設定檔位置](assets/config-map.svg)

---

## 開始前：建立本節練習資料夾

先完成[課堂練習準備](../practice/README.md)的工具確認與教材下載，再在**一般終端機**逐行執行：

```bash
python3 ~/terminal-ai-course/practice/prepare.py ~/terminal-ai-labs/agy/04
cd ~/terminal-ai-labs/agy/04
agy
```

看到目的資料夾已存在時，直接 `cd` 進去接續；要重做則把路徑最後一段改成 `04-retry`。本節的程式、筆記與初始 Git commit 都已準備好。

---

## 1. 先記住兩個層級

| 層級 | 生效範圍 | 適合放什麼 | 例子 |
| :--- | :--- | :--- | :--- |
| **全域** | 你電腦上的所有專案 | 個人偏好 | 一律用繁體中文回覆 |
| **專案** | 只有這個專案 | 團隊規範 | 這個專案一律用 `uv` |

> [!TIP]
> 判斷方法：**換一個專案還用得到嗎？** 用得到就放全域，只有這個專案需要就放專案。

---

## 2. 修改設定的三種方式

### 方式一：用 `/config` 選單（推薦）

```text
/config
```

用方向鍵選擇、按 `Enter` 修改，存檔由 agy 處理，不用擔心格式打錯。

### 方式二：請 AI 幫你改

直接用中文說：

```text
請幫我把 agy 設定成任務完成時要發出通知
```

### 方式三：直接編輯 `settings.json`（進階）

設定檔位置：

```text
~/.gemini/antigravity-cli/settings.json
```

可以用這個指令開啟：

```text
/open ~/.gemini/antigravity-cli/settings.json
```

範例：

```json
{
  "agentMode": "accept-edits",
  "notifications": true,
  "verbosity": "medium",
  "permissions": {
    "allow": ["command(git status)", "command(ls)"],
    "deny": ["command(sudo)"]
  }
}
```

> [!WARNING]
> JSON 格式很嚴格：不能寫註解，最後一項後面不能有逗號。改壞時，agy 會提示設定檔格式錯誤。

---

## 3. 常用設定項目

| 設定 | 用途 | 預設值 | 常見的值 |
| :--- | :--- | :---: | :--- |
| `agentMode` | 啟動時的執行模式 | 空白（預設模式） | `plan`、`accept-edits`、`auto` |
| `model` | 預設模型 | 空白 | 建議用 `/model` 選擇 |
| `colorScheme` | 配色 | `terminal` | 建議用 `/config` 預覽後選擇 |
| `editor` | 按 `Ctrl+G` 開啟的外部編輯器 | `"auto"`（讀 `$EDITOR`，否則 `vim`） | `"nano"`、`"vim"`、`"code --wait"` |
| `notifications` | 需要你處理時發出通知 | `false` | `true` |
| `verbosity` | 畫面顯示的詳細程度 | `medium` | 建議用 `/config` 選擇 |
| `showTips` | 顯示使用小提示 | `true` | `false` |
| `queuedMessages` | AI 工作中收到新訊息的處理方式 | `queue` | `send-immediately` |
| `toolPermission` | 工具的整體授權方式 | `request-review` | 詳見 [08](08-permissions.md) |
| `enableTerminalSandbox` | 在沙盒裡執行終端指令 | `false` | `true` |
| `permissions` | 允許、詢問、禁止的規則 | 無 | 詳見 [08](08-permissions.md) |

完整清單請見[官方 CLI Reference](https://antigravity.google/docs/cli/reference/)。

### 只想這次生效？

啟動時加上參數，不會改到存好的設定：

```bash
# 這次用規劃模式
agy --mode plan

# 這次用指定的模型
agy --model gemini-3.8-flash-medium

# 這次套用指定的設定，不會存檔
agy --settings '{"notifications": true}'
```

---

## 4. 設定個人規則（全域）

想讓 AI 在**每個專案**都用繁體中文回覆？用一句話就能完成：

```text
請幫我在全域規則檔 ~/.gemini/config/AGENTS.md 加上：一律使用繁體中文回覆
```

檔案內容會像這樣：

```markdown
# 我的個人規則

- 一律使用繁體中文回覆。
- 修改檔案之前，先說明要改什麼、為什麼要改。
```

### 規則可以放在哪裡？

| 層級 | 位置 | 說明 |
| :--- | :--- | :--- |
| 全域 | `~/.gemini/config/AGENTS.md` | 永遠生效 |
| 全域 | `~/.gemini/config/rules/*.md` | 拆成多個檔案，需要設定 `trigger` |
| 專案 | `AGENTS.md`（專案根目錄或子資料夾） | 永遠生效，對該資料夾和子資料夾有效 |
| 專案 | `.agents/rules/*.md` | 拆成多個檔案，需要設定 `trigger` |

`GEMINI.md` 的作用和 `AGENTS.md` 相同。專案規則的寫法請看 [06 專案規範與規則](06-agents-md.md)。

---

## 5. 連接外部工具：MCP

MCP（Model Context Protocol）讓 AI 能使用外部工具，例如資料庫、GitHub、Figma。不需要的話可以先跳過。

設定檔位置：

```text
~/.gemini/config/mcp_config.json
```

完整小範例：連接本機檔案工具。先確認 `node --version` 與 `npx --version` 有輸出（需要 Node.js；首次下載套件需要網路）。

1. 在本章練習資料夾執行 `pwd`，複製完整路徑。
2. 建立 `.agents/`，用編輯器新增**專案設定** `.agents/mcp_config.json`，將下方最後一個參數換成剛才 `pwd` 的完整路徑。不要把 `~` 當完整路徑傳給 MCP 程式。

```json
{
  "mcpServers": {
    "lab-files": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/請換成本章練習專案的完整路徑"]
    }
  }
}
```

| 欄位 | 用在哪裡 | 說明 |
| :--- | :--- | :--- |
| `command`、`args`、`env` | 本機工具 | 要執行的程式、參數、環境變數 |
| `url` | 遠端服務 | 伺服器的網址 |

3. 重新啟動 `agy`，輸入 `/mcp`，確認 `lab-files` 已連線且有列出檔案工具。
4. 回到對話框送出：

```text
請使用 lab-files MCP 的工具讀取 README.md，回報其中的測試指令。請指出使用的 MCP 工具名稱，不要改用終端機或一般讀檔工具。
```

**驗收**：工具紀錄應顯示 `lab-files` 的讀檔呼叫，回答包含 `python3 -m unittest discover -s tests -v`。若只有普通讀檔紀錄，請要求它重做這一步。若 MCP 未連線，先檢查 Node、網路與完整路徑。

**收尾**：在 `/mcp` 停用 `lab-files`，確認工具不再可用；重新啟用並再讀一次。練完刪除本節新建的 `.agents/mcp_config.json` 中 `lab-files` 項目，重啟後 `/mcp` 不應再列出它。專案 MCP 路徑依 [官方設定說明](https://antigravity.google/docs/settings)；檔案工具見 [官方 Filesystem Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)。

也可練習全域 CLI 管理（與上面的專案範例**擇一**）：在本章資料夾執行 `pwd`，把完整路徑放進下方指令的最後一個參數。

```bash
# 新增：最後一個參數請貼上 pwd 顯示的完整路徑
agy mcp add lab-files npx -y @modelcontextprotocol/server-filesystem /請換成本章練習專案的完整路徑

# 查看：列出目前的伺服器與狀態
agy mcp list

# 停用 / 重新啟用：暫時關閉，保留設定
agy mcp disable lab-files
agy mcp enable lab-files

# 刪除：從設定中永久移除
agy mcp remove lab-files
```

> [!CAUTION]
> 請不要把 API 金鑰寫在要 commit 進 Git 的檔案裡。MCP 伺服器能代替 AI 操作外部服務，只安裝你信任的來源。

---

## 6. 登入與 API 金鑰

大多數同學用 Google 帳號登入就好，第一次執行 `agy` 時會引導你完成，請見 [01 安裝與登入](01-install.md)。

| 狀況 | 做法 |
| :--- | :--- |
| 想換帳號 | 輸入 `/logout`，再重新啟動 `agy` |
| 想用自己的 Gemini API 金鑰 | 設定環境變數 `GEMINI_API_KEY`，並把 `settings.json` 的 `modelProvider` 設為 `"gemini"` |
| 終端機找不到 `agy` | 確認 `~/.local/bin` 在 PATH 裡，或執行 `agy install` 並重開終端機 |

---

## 完整小練習：設定、重新啟動、驗證與還原

### A. 三種設定方式都實際試一次

1. 在 `/config` 記下 `Notifications` 原值，切換一次並關閉選單；重新開 `/config`，確認值保留，再改回原值。
2. 送出 `請只把 agy 的 notifications 設成 true，保留所有其他設定。`，允許寫入後，重新開 `/config` 確認已開啟。
3. 要試手動編輯，先離開 agy，在一般終端機備份（`-i` 遇到同名備份會先詢問）：

```bash
cp -i ~/.gemini/antigravity-cli/settings.json ~/.gemini/antigravity-cli/settings.json.class-backup
nano ~/.gemini/antigravity-cli/settings.json
```

只把既有 `notifications` 改成 `false`，不要覆蓋整份設定。nano 用 `Ctrl+O`、`Enter` 儲存，再 `Ctrl+X` 離開。執行：

```bash
python3 -m json.tool ~/.gemini/antigravity-cli/settings.json
agy
```

**驗收**：JSON 檢查沒有錯誤，`/config` 顯示通知關閉。練完用編輯器把本節變更的欄位改回備份值；其他設定保留。

### B. 只在這次啟動生效

離開後執行 `agy --mode plan`，送出 `請規劃為 README.md 新增一節操作說明，先不要實作。`。**驗收**：顯示 plan 模式，`git diff -- README.md` 無輸出。結束對話，再正常執行 `agy`，確認回到原本預設模式。要試 `--settings`，用上面的通知參數啟動，確認 `/config` 的有效值，結束後正常啟動應仍使用保存的值。

### C. 驗證全域規則

先備份既有 `~/.gemini/config/AGENTS.md`（若不存在就記下「原本沒有」），再使用第 4 節的提示詞**追加**繁體中文規則。離開後重新啟動，在對話框輸入：

```text
請閱讀 README.md，用三點說明專案用途。
```

**驗收**：回答使用繁體中文。另建一個空資料夾、在裡面啟動 agy，送出 `Explain what a coding agent is in one sentence.`，觀察是否仍用繁體中文。練完刪除本次追加的那一條規則（原檔若只因本次練習而建立，可移除該檔）。

### D. 選做：使用自己的 Gemini API 金鑰

先確認金鑰已有可用額度。離開 agy 後，在 Bash 終端機輸入（輸入內容不會顯示）：

```bash
read -s -p "Gemini API Key: " GEMINI_API_KEY
export GEMINI_API_KEY
```

備份 `settings.json`，只把 `modelProvider` 設成 `"gemini"`，再啟動 agy，選該供應商可用模型，送出 `請只回覆「連線成功」。`。**驗收**：無認證錯誤並收到回答。練完離開、還原 `modelProvider` 原值，再在終端機執行 `unset GEMINI_API_KEY`。macOS 預設 zsh 請先輸入 `bash` 再執行上述 `read`，完成後用 `exit` 回原 shell。

## 7. ✅ 自我檢查與環境健康檢查

設定完成後，進入 `agy` 逐項確認：

- [ ] 說得出「全域設定（`~/.gemini/`）」與「專案設定（專案資料夾）」的差別
- [ ] 用 `/config` 開啟過設定選單，知道怎麼調整通知或配色
- [ ] 在全域規則 `~/.gemini/config/AGENTS.md` 加上「一律使用繁體中文回覆」
- [ ] 依下表檢查環境狀態：

| 檢查項目 | 輸入 | 應該看到 |
| :--- | :--- | :--- |
| 版本 | 在終端機執行 `agy --version` | 顯示版本號 |
| 模型 | `/model` | 目前選擇的模型 |
| 設定 | `/config` | 你調整過的值 |
| 權限 | `/permissions` | 你設定的規則 |
| 額度 | `/usage` | 還有可用額度 |
| Skill | `/skills` | 你安裝的 Skill |
| MCP | `/mcp` | 伺服器的連線狀態 |
| 規則 | `請告訴我你現在遵守哪些規則？` | AI 能說出你寫的規則 |

---

[← 03 斜線指令](03-slash-commands.md)　｜　[章節首頁](README.md)　｜　下一站：[05 Skill 配置 →](05-skills.md)
