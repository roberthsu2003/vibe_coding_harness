# 06　專案規範與規則

> ★★ 進階　｜　[← 05 Skill 配置](05-skills.md)　｜　[章節首頁](README.md)　｜　下一站：[07 實戰情境 →](07-scenarios.md)

**這一站你會學到**：使用 `AGENTS.md` 與專案規則（Rules），讓 AI coding agent 嚴格遵守團隊規範與工程要求。

---

## 1. 為什麼需要專案規範？

當 `agy` 進入一個專案時，如果沒有明確的規則指引，AI 可能會：
- 擅自使用全域 `pip install` 污染系統環境，而非使用專案指定工具（如 `uv` 或 `poetry`）。
- 猜測測試執行方式，或改動程式後忘記跑測試驗證。
- 使用非繁體中文回覆，或是忽略團隊的 Git Commit 格式。

透過在專案根目錄建立 `AGENTS.md`，`agy` 在對話初期就會主動載入這些指示，建立清晰的「行為圍欄」。

---

## 2. 規則存放位置與載入機制

`agy` 支援多層次的規則配置機制：

| 範圍 | 位置 | 說明 |
| :--- | :--- | :--- |
| **專案專屬** | 專案根目錄或子資料夾的 `AGENTS.md`（`GEMINI.md` 亦可） | 本專案共享的工程規則與指令（建議加入 Git） |
| **自訂規則庫** | 專案目錄 `.agents/rules/*.md` | 可依不同領域拆分的細部規則（例如代碼風格、測試規範） |
| **全域設定** | `~/.gemini/config/AGENTS.md` 或 `~/.gemini/config/rules/*.md` | 個人在所有專案中通用的偏好（例如慣用繁體中文） |

`AGENTS.md` 永遠生效；放在 `rules/` 裡的檔案則要在開頭用 `trigger` 指定載入時機：

```markdown
---
trigger: always_on
---

- 一律使用繁體中文撰寫程式註解。
```

| `trigger` 的值 | 何時載入 |
| :--- | :--- |
| `always_on` | 每一輪都載入 |
| `model_decision` | AI 判斷任務相關時才讀取 |
| `glob` | 處理符合條件的檔案時載入 |

---

## 3. 建議的 `AGENTS.md` 範本

在專案根目錄建立 `AGENTS.md`，可參考以下繁體中文規範：

```markdown
# 專案協作規範

## 1. 溝通原則
- 一律使用繁體中文（Traditional Chinese）回答。
- 在進行任何檔案修改前，先說明預計改動的檔案清單與原因。
- 修改完成後，主動執行測試並展示修改成果。

## 2. 套件與環境管理（uv）
- 本專案強制使用 uv 管理虛擬環境與相依套件。
- 禁止直接執行 pip install 或在系統環境安裝套件。
- 新增套件：`uv add <package>`
- 新增開發相依：`uv add --dev <package>`
- 執行測試：`uv run pytest`
- 執行程式：`uv run python main.py`

## 3. 程式碼品質與測試
- 撰寫新功能時，必須在 `tests/` 下補上對應單元測試。
- 修改既有代碼不能破壞現有測試案例。
- 送出前確認通過代碼檢查：`uv run ruff check .`

## 4. Git 版本控制
- 不要在未經測試通過的情況下直接 commit 到 main 分支。
- 每個功能或修復建議建立獨立的 Git branch 或使用 Git worktree。
```

---

## 4. 驗證規則是否生效

在啟動 `agy` 後，可以向 AI 確認：

```text
請檢查當前專案的 AGENTS.md，列出本專案執行的測試指令是什麼？
```

AI 會從讀取的專案脈絡中確認規範，後續指令與自動修正迴圈皆會遵照設定進行。

---

← [← 05 Skill 配置](05-skills.md)　｜　[章節首頁](README.md)　｜　下一站：[07 實戰情境 →](07-scenarios.md)

