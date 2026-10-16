# 03　AGENTS.md 專案規則

> ★★ 進階　｜　[← 02 基本操作](02-basics.md)　｜　[章節首頁](README.md)　｜　下一站：[04 實戰情境 →](04-scenarios.md)

**這一站你會學到**：用 `AGENTS.md` 告訴 AI 這個專案的規矩，讓它照你的方式工作。

---

## 1. 為什麼需要 AGENTS.md？

OpenCode 啟動時會自動讀取專案根目錄的 `AGENTS.md`，把它當成這個專案的規則。沒有這份檔案時，AI 常會：

1. 用 `pip install` 把套件裝到系統的 Python，弄亂電腦環境。
2. 不知道專案用什麼工具跑測試。
3. 寫出和專案風格不一樣的程式。

## 2. 用 /init 自動產生

在專案裡啟動 OpenCode，輸入：

```text
/init
```

OpenCode 會分析專案，在根目錄建立（或更新）`AGENTS.md`。產生後**自己讀一遍**，把不對的地方改掉，然後 commit 進 Git。

## 3. 可以直接套用的範本

Python 專案可以參考這份範本，貼到專案根目錄的 `AGENTS.md`：

```markdown
# 專案協作規範

## 1. 溝通
- 一律使用繁體中文回覆。
- 修改檔案前先說明要改哪些地方。
- 修改後主動執行測試，並檢查 git diff。

## 2. Python 環境與套件（uv）
- 本專案使用 uv 管理虛擬環境與套件。
- 安裝套件：uv add <套件名稱>，禁止使用 pip install。
- 開發用套件：uv add --dev <套件名稱>。
- 執行程式：uv run python <檔案.py>
- 執行測試：uv run pytest

## 3. Git
- 不要把沒有驗證過的程式直接 commit 到 main。
- 多個任務同時進行時，使用 git worktree，放在 .worktrees/ 底下。
```

## 4. 確認 AI 有讀到

```text
請說明這個專案的虛擬環境工具和套件安裝方式。先不要修改任何檔案。
```

AI 回答「使用 uv、用 `uv add` 安裝」就代表它讀到了。

> [!WARNING]
> 如果你用另一個 AI 當「主管」指揮 OpenCode（見 [Herdr 多 Agent 協同](../herdr/06-supervisor-subagent.md)），**主管的規則不要寫在 AGENTS.md**。OpenCode 也會讀到，會以為自己是主管而卡住。

---

## ✅ 自我檢查

- [ ] 用 `/init` 產生過 `AGENTS.md`，並自己讀過、修改過
- [ ] AI 能正確說出專案的套件管理方式

> 下一站：[04 實戰情境 →](04-scenarios.md)
