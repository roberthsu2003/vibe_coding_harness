# 06　專案規範與規則

> ★★ 進階　｜　[← 05 Skill 配置](05-skills.md)　｜　[章節首頁](README.md)　｜　下一站：[07 Subagent 子代理 →](07-subagents.md)

**這一站你會學到**：用 `AGENTS.md` 與專案規則（Rules）告訴 AI 這個專案的規矩，並透過實際小範例親眼驗證 AI 真的有照做。

---

## 1. 為什麼需要 `AGENTS.md`？

`agy` 進入一個專案時，會自動讀取根目錄的 `AGENTS.md`，把它當成這個專案的規矩。如果沒有這份檔案，AI 常會：

1. 用 `pip install` 把套件裝到系統的 Python，弄亂電腦環境，而不是用專案指定的 `uv`。
2. 不知道專案用什麼指令跑測試，或改完程式忘記跑測試驗證。
3. 寫出和團隊風格不一樣的程式，或忽略 Git commit 格式。

把規矩寫進 `AGENTS.md` 並 commit 進 Git，全班或團隊的 AI 就會遵守同一套標準。

---

## 2. 動手實作小範例：一測就有感的專案規範

不用等大專案，現在就用一個 3 分鐘的小範例，親眼看 `AGENTS.md` 如何改變 AI 的行為。

### 步驟 1：在專案根目錄建立 `AGENTS.md`

在練習資料夾根目錄建立 `AGENTS.md`（或請 AI 幫你寫入），貼上這三條**一眼就能驗證**的規矩：

```markdown
# 練習專案規範

1. **溝通格式**：一律使用繁體中文條列式回覆，並在每次回覆的最後一行加上「✅ 已遵守專案規範」。
2. **程式寫法**：所有 Python 函式都必須加上型別標註（Type Hints）與繁體中文說明註解（docstring）。
3. **自動補測試**：每次建立新的 `.py` 檔案時，必須同時建立對應的 `test_<檔名>.py` 測試檔。
```

### 步驟 2：下達任務測試

開啟 `agy`（如果已經開著，重新開啟新對話讓它讀取根目錄的 `AGENTS.md`），輸入：

```text
請幫我寫一個計算商品打折後價格的小程式 discount.py。
```

### 步驟 3：檢查 AI 有沒有乖乖照做

觀察結果，你會發現 AI 主動做了三件「沒寫在指令裡、但寫在 `AGENTS.md` 裡」的事：

- 產出 `discount.py` 時，自動加上了型別標註（如 `price: float`）與繁體中文註解。
- 主動多生出一個 `test_discount.py` 測試檔。
- 回覆的最後一行出現 `✅ 已遵守專案規範`。

> [!TIP]
> 這就是 `AGENTS.md` 和一般對話最大的差別：**寫進去一次，以後每一輪對話 AI 都會自動遵守，不用每次重複提醒。**

---

## 3. 進階產生方式：一句話請 AI 自動掃描產生（推薦）

如果是一個已經有程式的現成專案，不用自己從頭寫，啟動 `agy` 後直接請它掃描專案並建立：

```text
請讀一下這個專案的結構與設定檔，幫我在根目錄建立一份繁體中文的 AGENTS.md，寫清楚套件管理、執行程式與跑測試的方式。
```

產生後**自己打開讀一遍**，不對或漏掉的地方直接用中文請 AI 修改，確認沒問題再 commit 進 Git。

---

## 4. Python 專案完整範本（可直接套用）

正式開發 Python 專案時，可以直接參考這份範本，貼到專案根目錄的 `AGENTS.md`：

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

## 5. 規則可以放在哪裡？（區域 vs 全域）

| 範圍 | 位置 | 適合放什麼 |
| :--- | :--- | :--- |
| **所有專案（全域）** | `~/.gemini/config/AGENTS.md` | 個人習慣，例如「一律用繁體中文回覆」 |
| **這個專案（區域）** | 專案根目錄的 `AGENTS.md`（或 `GEMINI.md`） | 全專案共同的規矩，每次對話都會載入（建議 commit 進 Git） |
| **某個子資料夾** | 該資料夾裡的 `AGENTS.md` | 只適用那個資料夾（例如 `frontend/AGENTS.md`），AI 處理那裡的檔案時才載入 |
| **拆成多個規則檔** | `.agents/rules/*.md`（專案）或 `~/.gemini/config/rules/*.md`（全域） | 規則太多時，可依主題拆開（例如測試規範、文件規範） |

> [!TIP]
> 大多數專案**只要根目錄一份 `AGENTS.md` 就夠了**，不需要一開始就拆成多個檔案。

### 小範例：只在寫特定檔案時才載入的規則（`rules/*.md`）

放在 `rules/` 資料夾裡的 `.md` 檔，可以在最開頭加上 `trigger` 指定何時載入：

| `trigger` 的值 | 何時載入 | 範例用途 |
| :--- | :--- | :--- |
| `always_on` | 每一輪對話都載入 | 全專案通用的基本要求 |
| `model_decision` | AI 判斷跟任務有關時才讀（需加寫 `description`） | 只有改資料庫時才需要的規範 |
| `glob` | 碰到符合條件的檔案時才讀（需加寫 `globs`） | 只針對測試檔或文件檔的規則 |

**動手試試**：建立 `.agents/rules/docs-style.md`，讓 AI 只有在編輯 `docs/` 底下的 Markdown 檔時才套用：

```markdown
---
trigger: glob
globs: ["docs/**/*.md"]
---

- 每份文件開頭必須包含「## 學習目標」小節。
- 重要提醒請使用 GitHub Alert（`> [!NOTE]` 或 `> [!TIP]`）。
```

接著對 `agy` 輸入「`請幫我在 docs/intro.md 寫一份 10 行以內的專案簡介`」，就能看到 `docs/intro.md` 自動出現「## 學習目標」與 Alert 區塊！

---

## 6. 進階：用 Hook 強制執行自動化腳本（`hooks.json`）

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

1. **新增 Hook**：在 `.agents/hooks.json` 加入規則（每次 AI 執行完 `run_command` 後，自動印出檢查提醒）：

```json
{
  "my-check-hook": {
    "PostToolUse": [
      {
        "matcher": "run_command",
        "hooks": [
          {
            "type": "command",
            "command": "echo '🔍 Hook 觸發：終端機指令執行完成，請確認結果是否正常！'",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

> 在 `agy` 對話框輸入 **`/hooks`**，可以查看目前所有已載入的 Hook；接著請 AI 執行一個簡單指令（例如「`幫我執行 ls 看一下目前目錄`」），就能看到 Hook 自動觸發。

2. **停用 Hook**：不想刪除設定、只想暫時關閉時，加上 `"enabled": false`（改回 `true` 或刪掉這行即可重新啟用）：

```json
{
  "my-check-hook": {
    "enabled": false,
    "PostToolUse": [ ... ]
  }
}
```

3. **刪除 Hook**：從 `.agents/hooks.json` 移除 `"my-check-hook"` 這個區塊；如果只有這一個 Hook，也可以直接刪除 `.agents/hooks.json` 檔案（或請 AI 幫你刪掉）。

---

## 7. 確認 AI 有讀到規則

套用大型專案範本後，在對話框問一句話就能確認：

```text
請說明這個專案的套件安裝方式與測試指令是什麼。先不要修改任何檔案。
```

AI 回答「使用 `uv add` 安裝、用 `uv run pytest` 跑測試」，就代表規則已經生效了！

---

## ✅ 自我檢查

- [ ] 實際做完第 2 節的 `discount.py` 小範例，確認 AI 有遵守 `AGENTS.md` 的三條規矩
- [ ] 在練習專案用 AI 產生或套用 `AGENTS.md`，並自己讀過一遍
- [ ] 說得出 `AGENTS.md`（每次都載入的規矩）和 [Skill](05-skills.md)（用到才翻開的工作手冊）的差別

---

[← 05 Skill 配置](05-skills.md)　｜　[章節首頁](README.md)　｜　下一站：[07 Subagent 子代理 →](07-subagents.md)
