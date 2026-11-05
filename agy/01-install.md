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

## 3. 第一次啟動與登入

進入專案資料夾後啟動：

```bash
cd ~/my-project
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

← [章節首頁](README.md)　｜　下一站：[02 基本操作 →](02-basics.md)
