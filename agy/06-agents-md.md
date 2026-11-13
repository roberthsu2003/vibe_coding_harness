# 06　專案規範與規則

> ★★ 進階　｜　[← 05 Skill 配置](05-skills.md)　｜　[章節首頁](README.md)　｜　下一站：[07 Subagent 子代理 →](07-subagents.md)

**這一站你會學到**：用 `AGENTS.md` 與專案規則（Rules）告訴 AI 這個專案的規矩，讓它照你的方式工作。

---

## 1. 為什麼需要 `AGENTS.md`？

`agy` 進入一個專案時，會自動讀取根目錄的 `AGENTS.md`，把它當成這個專案的規矩。如果沒有這份檔案，AI 常會：

1. 用 `pip install` 把套件裝到系統的 Python，弄亂電腦環境，而不是用專案指定的 `uv`。
2. 不知道專案用什麼指令跑測試，或改完程式忘記跑測試驗證。
3. 寫出和團隊風格不一樣的程式，或忽略 Git commit 格式。

把規矩寫進 `AGENTS.md` 並 commit 進 Git，全班或團隊的 AI 就會遵守同一套標準。

---

## 2. 方法一：一句話請 AI 自動產生（推薦）

不用自己從頭寫，啟動 `agy` 後直接用中文請它掃描專案並建立：

```text
請讀一下這個專案的結構與設定檔，幫我在根目錄建立一份繁體中文的 AGENTS.md，寫清楚套件管理、執行程式與跑測試的方式。
```

產生後**自己打開讀一遍**，不對或漏掉的地方直接用中文請 AI 修改，確認沒問題再 commit 進 Git。

---

## 3. 方法二：直接套用範本

Python 專案可以直接參考這份範本，貼到專案根目錄的 `AGENTS.md`：

```markdown
# 專案協作規範

## 1. 溝通原則
- 一律使用繁體中文（Traditional Chinese）回覆。
- 修改檔案前，先說明預計修改哪些檔案與原因。
- 修改完成後，主動執行測試並檢查 git diff。

## 2. Python 環境與套件（uv）
- 本專案使用 uv 管理虛擬環境與套件，禁止直接使用 pip install。
- 新增套件：`uv add <套件名稱>`
- 新增開發用套件：`uv add --dev <套件名稱>`
- 執行程式：`uv run python main.py`
- 執行測試：`uv run pytest`

## 3. 程式碼品質與測試
- 新增功能時，請在 `tests/` 補上對應的單元測試。
- 修改既有程式不能弄壞原本的測試。
- 送出前請先執行：`uv run ruff check .`

## 4. Git 版本控制
- 不要把還沒通過測試的程式直接 commit 到 main 分支。
- 開發新功能或修 bug 時，請開獨立的 Git 分支或使用 Git worktree。
```

---

## 4. 規則可以放在哪裡？

| 範圍 | 位置 | 適合放什麼 |
| :--- | :--- | :--- |
| **所有專案（全域）** | `~/.gemini/config/AGENTS.md` | 個人習慣，例如「一律用繁體中文回覆」 |
| **這個專案** | 專案根目錄的 `AGENTS.md`（或 `GEMINI.md`） | 全專案共同的規矩，每次對話都會載入（建議 commit 進 Git） |
| **某個子資料夾** | 該資料夾裡的 `AGENTS.md` | 只適用那個資料夾（例如 `frontend/AGENTS.md`），AI 處理那裡的檔案時才載入 |
| **拆成多個規則檔** | `.agents/rules/*.md`（專案）或 `~/.gemini/config/rules/*.md`（全域） | 規則太多時，可依主題拆開（例如測試規範、API 規範） |

> [!TIP]
> 大多數專案**只要根目錄一份 `AGENTS.md` 就夠了**，不需要一開始就拆成多個檔案。

### 進階：拆成多個檔案時，怎麼指定載入時機？

放在 `rules/` 資料夾裡的 `.md` 檔，可以在最開頭加上 `trigger` 設定何時載入：

```markdown
---
trigger: always_on
---

- 一律使用繁體中文撰寫程式註解。
```

| `trigger` 的值 | 何時載入 | 範例用途 |
| :--- | :--- | :--- |
| `always_on` | 每一輪對話都載入 | 全專案通用的基本要求 |
| `model_decision` | AI 判斷跟任務有關時才讀（需加寫 `description`） | 只有改資料庫時才需要的規範 |
| `glob` | 碰到符合條件的檔案時才讀（需加寫 `globs`，如 `globs: ["tests/**/*.py"]`） | 只針對測試檔或前端檔的規則 |

**小範例**（`.agents/rules/testing.md`，只在處理 `tests/` 裡的 Python 檔時載入）：

```markdown
---
trigger: glob
globs: ["tests/**/*.py"]
---

- 測試函式名稱一律使用 `test_<功能>_<預期結果>`。
- 不要在測試中連線到真實外部 API，請使用 mock。
```

---

## 5. 進階：用 Hook 強制執行自動化腳本（`hooks.json`）

`AGENTS.md` 和 `rules/*.md` 是寫給 AI 看的「文字規範」，AI 偶爾還是可能忘記；如果你想確保**某些動作在特定時機點一定會自動執行**，就要用 **Hook（事件掛鉤）**。

| 機制 | 本質 | 誰來執行 | 適合做什麼 |
| :--- | :--- | :--- | :--- |
| **Rules（`AGENTS.md` / `rules/*.md`）** | 文字規範 | AI 閱讀後遵守 | 溝通語言、開發習慣、架構原則 |
| **Hook（`hooks.json`）** | 自動化腳本 | `agy` 系統在固定時機點自動觸發 | 改完檔自動排版、執行指令前先做安全檢查 |

### 放在哪裡？

- **這個專案**：專案根目錄的 `.agents/hooks.json`
- **所有專案（全域）**：`~/.gemini/config/hooks.json`

### 常見觸發時機

| 事件名稱 | 觸發時機 |
| :--- | :--- |
| `SessionStart` | 新對話開始時執行一次 |
| `PreToolUse` | AI **執行工具前**觸發（可搭配 `matcher` 指定工具，如 `run_command`） |
| `PostToolUse` | AI **執行工具後**觸發（適合自動跑檢查或格式化） |
| `Stop` | 這一輪執行結束時觸發 |

### 小範例：新增、停用與刪除 Hook

1. **新增 Hook**：在 `.agents/hooks.json` 加入規則（例如每次 AI 執行完 `run_command` 後，自動跑 `./scripts/lint.sh` 檢查）：

```json
{
  "my-linter-hook": {
    "PostToolUse": [
      {
        "matcher": "run_command",
        "hooks": [
          {
            "type": "command",
            "command": "./scripts/lint.sh",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

2. **停用 Hook**：不想刪除設定、只想暫時關閉時，加上 `"enabled": false`（改回 `true` 或刪掉這行即可重新啟用）：

```json
{
  "my-linter-hook": {
    "enabled": false,
    "PostToolUse": [ ... ]
  }
}
```

3. **刪除 Hook**：從 `.agents/hooks.json` 移除 `"my-linter-hook"` 這個區塊；如果只有這一個 Hook，也可以直接刪除 `.agents/hooks.json` 檔案。

> [!TIP]
> 在 `agy` 對話框輸入 **`/hooks`**，可以查看目前環境中所有已載入與啟用的 Hook。

---

## 6. 確認 AI 有讀到規則

建立好 `AGENTS.md` 後，在對話框問一句話就能確認：

```text
請說明這個專案的套件安裝方式與測試指令是什麼。先不要修改任何檔案。
```

AI 回答「使用 `uv add` 安裝、用 `uv run pytest` 跑測試」，就代表規則已經生效了！

---

## ✅ 自我檢查

- [ ] 在練習專案建立 `AGENTS.md`，並自己讀過一遍
- [ ] AI 能正確說出你在 `AGENTS.md` 裡寫的測試或套件安裝指令
- [ ] 說得出 `AGENTS.md`（每次都載入的規矩）和 [Skill](05-skills.md)（用到才翻開的工作手冊）的差別

---

[← 05 Skill 配置](05-skills.md)　｜　[章節首頁](README.md)　｜　下一站：[07 Subagent 子代理 →](07-subagents.md)
