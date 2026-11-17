# 06　AGENTS.md 專案規則

> ★★ 進階　｜　[← 05 Skill 配置](05-skills.md)　｜　[章節首頁](README.md)　｜　下一站：[07 Subagent 子代理 →](07-subagents.md)

**這一站你會學到**：用 `AGENTS.md` 告訴 AI 這個專案的規矩，讓它照你的方式工作。

---

## 開始前：建立本節練習資料夾

先完成[課堂練習準備](../practice/README.md)的工具確認與教材下載，再在**一般終端機**逐行執行：

```bash
python3 ~/terminal-ai-course/practice/prepare.py ~/terminal-ai-labs/opencode/06
cd ~/terminal-ai-labs/opencode/06
opencode
```

看到目的資料夾已存在時，直接 `cd` 進去接續；要重做則把路徑最後一段改成 `06-retry`。本節的程式、筆記與初始 Git commit 都已準備好。

---

## 1. 為什麼需要 AGENTS.md？

OpenCode 會自動讀取 `AGENTS.md`，把它當成這個專案的規則。沒有這份檔案時，AI 常會：

1. 用 `pip install` 把套件裝到系統的 Python，弄亂電腦環境。
2. 不知道專案用什麼工具跑測試。
3. 寫出和專案風格不一樣的程式。

## 2. 用 /init 自動產生

在專案裡啟動 OpenCode，輸入：

```text
/init 請用繁體中文撰寫
```

OpenCode 會分析專案，在根目錄建立（或更新）`AGENTS.md`。後面那句話是你的要求，可以依需要改寫。

> 如果選單裡沒有 `/init`，等幾秒再打一次。這類指令會在啟動後才載入。

產生後**自己讀一遍**，不對的地方用中文請 AI 改，然後 commit 進 Git。

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
- 執行測試：uv run pytest tests/

## 3. Git
- 不要把沒有驗證過的程式直接 commit 到 main。
- 多個任務同時進行時，使用 git worktree，放在 .worktrees/ 底下。
```

## 4. 確認 AI 有讀到

```text
請說明這個專案的虛擬環境工具和套件安裝方式。先不要修改任何檔案。
```

AI 回答「使用 uv、用 `uv add` 安裝」就代表它讀到了。

## 5. 規則可以放在哪裡？

| 範圍 | 位置 | 適合放什麼 |
| :--- | :--- | :--- |
| **所有專案** | `~/.config/opencode/AGENTS.md` | 個人習慣，例如「一律用繁體中文回覆」 |
| **這個專案** | 專案根目錄的 `AGENTS.md` | 全專案共同的規矩，建議 commit 進 Git |
| **某個資料夾** | 該資料夾裡的 `AGENTS.md` | 只適用那部分的規矩。AI 讀到那裡的檔案時才載入 |

規則太長時可以拆成多個檔案，在 `opencode.json` 用 `instructions` 引用：

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["CONTRIBUTING.md", "docs/規範/*.md"]
}
```

> [!NOTE]
> OpenCode 2 **只認 `AGENTS.md`**，不會讀 `CLAUDE.md`。之前寫在 `CLAUDE.md` 的規則要搬過來。

> [!WARNING]
> 如果你用另一個 AI 當「主管」指揮 OpenCode（見 [Herdr 多 Agent 協同](../herdr/06-supervisor-subagent.md)），**主管的規則不要寫在 AGENTS.md**。OpenCode 也會讀到，會以為自己是主管而卡住。

---

## 完整小範例：從產生規則到驗證行為

1. 依第 2 節執行 `/init 請用繁體中文撰寫`，打開新產生的 `AGENTS.md`，確認測試指令與 README 一致。
2. 在檔案最後追加下列規則並存檔：

```markdown
## 課堂驗證規則
- 每次回覆最後一行加上「✅ 已遵守課堂規則」。
- 新建 Python 函式要有型別標註與繁體中文 docstring。
- 每次新增 Python 功能，同時新增對應的 unittest 測試。
```

3. 輸入 `/reload`，開新對話後送出：

```text
請建立 discount.py，提供 discounted_price(price, rate) 回傳 price * rate，並依規則補上測試：100 元乘 0.8 應是 80。測試檔命名 test_discount.py，執行 python3 -m unittest test_discount -v。
```

**驗收**：`discount.py` 有型別與中文 docstring，`test_discount.py` 存在且測試 `OK`，AI 回覆有指定結尾。若規則尚未載入，離開再啟動重做；不要只問 AI「你有遵守嗎」。

### 再試拆分規則檔

在一般終端機執行：

```bash
mkdir -p docs/規範
```

用編輯器新增 `docs/規範/筆記.md`，內容為：

```markdown
- 新增 docs/ 底下的 Markdown 文件時，開頭必須有「## 學習目標」。
```

將 `"instructions": ["docs/規範/*.md"]` 合併到專案 `opencode.json`，輸入 `/reload` 後開新對話，送出 `請建立 docs/intro.md，介紹本練習專案的用途。`。**驗收**：實際檔案包含「## 學習目標」。本題未建立 `CONTRIBUTING.md`，因此不需引用它。

想測試全域規則時，備份既有 `~/.config/opencode/AGENTS.md`，追加「一律用繁體中文回覆」，再從另一個空資料夾啟動 OpenCode，送出 `Explain coding agents in one sentence.`。**驗收**：使用繁體中文回答；練完移除本次追加的規則，還原原內容。

想套用第 3 節的 uv 範本，先依[練習準備](../practice/README.md)安裝 uv，在本章資料夾執行 `uv sync`，再讓 AI 執行 `uv run pytest tests/`，應 4 個測試通過；`broken/` 為另一道修復題，不在本次測試範圍。

## ✅ 自我檢查

- [ ] 用 `/init` 產生過 `AGENTS.md`，並自己讀過、修改過
- [ ] AI 能正確說出專案的套件管理方式
- [ ] 說得出 `AGENTS.md` 和 [Skill](05-skills.md) 的差別

> 下一站：[07 Subagent 子代理 →](07-subagents.md)
