# 01　安裝與登入

> ★ 入門　｜　[章節首頁](README.md)　｜　下一站：[02 基本操作 →](02-basics.md)

**這一站你會學到**：安裝 Antigravity CLI (`agy`)、完成第一次啟動與登入，以及查看和切換模型。

---

## 1. 安裝

依照你的作業系統，複製指令到終端機執行：

**macOS / Linux**

```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
```

**Windows（PowerShell）**

```powershell
irm https://antigravity.google/cli/install.ps1 | iex
```

---

## 2. 確認安裝成功

重新開啟終端機，然後執行：

```bash
agy --version
```

看到版本號就成功了。

> [!NOTE]
> 如果出現「找不到指令」，執行檔可能還沒加入 PATH。macOS / Linux 的預設位置是 `~/.local/bin/agy`，可以用完整路徑執行 `~/.local/bin/agy install` 來設定環境路徑，再重開終端機。

---

## 開始前：建立本節練習資料夾

先完成[課堂練習準備](../practice/README.md)的工具確認與教材下載，再在**一般終端機**逐行執行：

```bash
python3 ~/terminal-ai-course/practice/prepare.py ~/terminal-ai-labs/agy/01
cd ~/terminal-ai-labs/agy/01
```

看到目的資料夾已存在時，直接 `cd` 進去接續；要重做則把路徑最後一段改成 `01-retry`。本節的程式、筆記與初始 Git commit 都已準備好。

## 3. 第一次啟動與登入

進入專案資料夾後啟動：

```bash
cd ~/terminal-ai-labs/agy/01
agy
```

第一次執行時，畫面會一步一步帶你完成：

1. **選擇配色與顯示方式**：不確定就用預設值，之後能用 `/config` 修改。
2. **信任這個資料夾**：確認這是你自己的專案後再同意。
3. **登入**：依照畫面指示，在瀏覽器完成 Google 帳號授權。

完成後就會進入對話畫面。

---

## 4. 查看與選擇模型

### 在 agy 裡切換（推薦）

```text
/model
```

用方向鍵選擇模型，按 `Enter` 確認。

### 列出所有可用模型

在一般終端機中執行：

```bash
agy models
```

輸出範例（實際內容依帳號和版本而定）：

```text
gemini-4-argon-medium     Gemini 4 Argon (Medium)
gemini-4-argon-high       Gemini 4 Argon (High)
gemini-3.8-flash-medium   Gemini 3.8 Flash (Medium)
gemini-3.8-flash-low      Gemini 3.8 Flash (Low)
claude-sonnet-5-5-medium  Claude Sonnet 5.5 (Medium)
```

名稱最後的 `low`、`medium`、`high` 是思考強度：越高想得越深，通常也越慢。

### Orchestrator：自動搭配規劃與執行模型

Google 在 **2026-11-12** 發布 Orchestrator，讓較大的模型負責規劃與檢查，再交給 Gemini 4 Hydrogen 修改檔案、建置與測試；遇到卡關時，會交回規劃模型調整計畫。適合需要「先理解專案，再修改並驗證」的功能開發或除錯。[官方發布公告](https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity)

在對話框輸入 `/model`，選擇帳號可用的 Orchestrator 項目，按 `Enter` 後就能照平常方式交代任務：

```text
請修改 calc.py 的 divide(a, b)：當 b 為 0 時拋出 ValueError("除數不可為零")，其餘行為不變。
在 tests/test_calc.py 補上除數為零的測試，
執行 python3 -m unittest discover -s tests -v，最後整理修改結果。
```

**驗收**：另開終端機進入 `~/terminal-ai-labs/agy/01`，執行 `python3 -m unittest discover -s tests -v`，應至少 5 個測試通過。執行 `git diff -- calc.py tests/test_calc.py`，應看到錯誤處理與新測試；只切換模型而沒有送出上述任務，不會產生改動。

| 選單名稱 | 規劃與檢查 | 修改與測試 | 可用方案 |
| :--- | :--- | :--- | :--- |
| **Orchestrator (Carbon)** | Gemini 4 Carbon | Gemini 4 Hydrogen | Google AI Ultra |
| **Orchestrator (Argon)** | Gemini 4 Argon | Gemini 4 Hydrogen | Google AI Ultra、付費 Google AI Pro，或符合資格的高階裝置試用方案 |

也可以在啟動時指定（名稱含空格，請保留引號）：

```bash
agy --model "Orchestrator (Argon)"
```

> [!NOTE]
> **Orchestrator 使用固定配置，不能用 `/effort` 或 `--effort` 調整思考強度。** 若想自行指定強度，請改選單一模型。找不到選項時，先執行 `agy update`，再用 `agy models` 確認帳號可用清單。

方案與操作依 [官方模型文件](https://antigravity.google/docs/models#orchestrator) 整理，查核日期：**2026-11-17**。想把工作拆給多位代理平行處理，可接著看 [07 Subagent 子代理](07-subagents.md)。

### 啟動時指定模型

```bash
# 複雜的工作：用強一點的模型
agy --model gemini-4-argon-high

# 簡單的工作：用快一點的模型
agy --model gemini-3.8-flash-medium
```

---

## 5. 保持最新版本

```bash
agy update
```

---

## 完整小練習：登入後確認模型能讀檔

1. 在本章練習資料夾啟動 `agy` 並完成登入。
2. 輸入 `/model`，選帳號有額度的模型，按 `Enter`。
3. 在對話框送出：

```text
請閱讀 README.md 與 main.py，用三點繁體中文說明專案用途、執行方式與測試指令，先不要修改檔案。
```

**驗收**：回答應包含 `python3 main.py` 與 `python3 -m unittest discover -s tests -v`。在另一個終端機執行 `git status --short` 應無輸出（若做過 Orchestrator 修改題，則應只列出該題的變更）。離開後再用本章列出的 `agy --model ...` 啟動，送出同一問題，確認選到的模型與回答都正常。

更新練習：離開後執行 `agy --version`，記下版本，再執行 `agy update` 與 `agy --version`。**驗收**：顯示更新成功或已是最新版；版本號可以相同。

## ✅ 自我檢查

- [ ] `agy --version` 顯示版本號
- [ ] 完成 Google 帳號登入，成功進入對話畫面
- [ ] 輸入 `/model` 看過模型清單，並問了 AI 一個問題得到回覆

---

[← 章節首頁](README.md)　｜　下一站：[02 基本操作 →](02-basics.md)
