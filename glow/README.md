# Glow 終端 Markdown 閱讀指南

Glow 是由 Charmbracelet 以 Go 語言打造的現代終端 Markdown 渲染器與閱讀工具。在以 AI 為核心的開發環境（Vibe Coding Harness）中，Glow 是讓開發者**「雙手不離終端、心流不被打斷」**檢閱 AI 產出的架構規格、PRD、README 與開發日誌不可或缺的終端利器。

---

## 導覽目錄

1. [為什麼 AI 輔助開發需要 Glow？（在 Harness 中的定位）](#1-為什麼-ai-輔助開發需要-glow在-harness-中的定位)
2. [安裝與確認版本](#2-安裝與確認版本)
3. [核心模式：CLI 直接閱讀 vs 互動式 TUI 探索](#3-核心模式cli-直接閱讀-vs-互動式-tui-探索)
4. [日常操作與常用參數速查（分級掌握）](#4-日常操作與常用參數速查分級掌握)
5. [實戰情境與解決方案（在 Harness 中的妙用）](#5-實戰情境與解決方案在-harness-中的妙用)
6. [搭配 Herdr 終端多工工作流](#6-搭配-herdr-終端多工工作流)
7. [設定檔與主題風格客製（Style & Config）](#7-設定檔與主題風格客製style--config)
8. [常見疑難排解（FAQ）](#8-常見疑難排解faq)

---

## 1. 為什麼 AI 輔助開發需要 Glow？（在 Harness 中的定位）

在現代 AI 協同開發（Vibe Coding）的過程中，AI Agent（如 OpenCode、Claude Code）不僅產出程式碼，還會產出大量的 Markdown 文件，例如：
* 系統架構規劃（`ARCHITECTURE.md`）
* 產品需求與規格書（`PRD.md`、`spec.md`）
* 任務代辦清單與驗收標準（`TODO.md`、`AGENTS.md`）
* 更新日誌與功能發布手冊（`CHANGELOG.md`）

很多初學者會問：「我有 VS Code Markdown 預覽外掛，甚至瀏覽器也能開，為什麼要在終端機看 Markdown？」

痛點對比如下：

| 閱讀方式 | 傳統作法與缺點 | Glow 終端解法 |
| :--- | :--- | :--- |
| **`cat` / `less`** | 純文字混亂，標題 `#` 未解析、表格嚴重跑版、代碼區塊無語法著色，長文難以閱讀。 | 將 Markdown 轉化為雜誌級排版，表格自動對齊、代碼區塊多色彩高亮。 |
| **IDE / 瀏覽器** | 頻繁切換視窗（Context Switching），需要拿起滑鼠點擊，打斷終端全鍵盤操作心流。 | 就地於終端指令即開即讀，全鍵盤快捷鍵翻頁，讀完按 `q` 立即回到 Shell。 |
| **遠端 SSH / 容器** | 無 GUI 桌面環境，根本無法開啟圖形預覽器。 | 完全原生終端運作，輕量高效，任何終端皆可隨開隨用。 |

![Glow 終端 Markdown 閱讀器對比與工作流程](assets/glow-workflow.svg)

---

## 2. 安裝與確認版本

Glow 支援 macOS、Linux 與 Windows 等各大作業系統平台：

### macOS (Homebrew 推薦)
```bash
brew install glow
```

### Linux (套件管理或 Snap)
```bash
# Ubuntu / Debian
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://repo.charm.sh/apt/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/charm.gpg
echo "deb [signed-by=/etc/apt/keyrings/charm.gpg] https://repo.charm.sh/apt/ * *" | sudo tee /etc/apt/sources.list.d/charm.list
sudo apt update && sudo apt install glow

# Arch Linux
sudo pacman -S glow

# Fedora
sudo dnf install glow

# Snap 跨發行版通用
sudo snap install glow
```

### Windows (winget 或 Scoop)
```powershell
# winget
winget install charmbracelet.glow

# Scoop
scoop install glow
```

安裝完成後，輸入下列指令檢查版本確認安裝成功：
```bash
glow --version
```

---

## 3. 核心模式：CLI 直接閱讀 vs 互動式 TUI 探索

Glow 提供四種靈活的使用型態，能滿足從單一檔案閱讀到全專案文件管理的各種需求：

### 模式 A：分頁閱讀模式（日常最推薦：`glow -p`）
當閱讀較長的文件時，使用 `-p`（或 `--pager`）參數會啟用內建的分頁器（基於現代分頁技術，類似 `less` 但保留完整顏色排版）：
```bash
glow -p README.md
```
- **操作方式**：按方向鍵或 `j`/`k` 上下滾動，按 `Space` 向下翻頁，按 **`q`** 隨時退出返回命令列。

### 模式 B：直接渲染輸出（終端流管線：`glow <file>`）
如果檔案篇幅較短，或是你想直接在終端輸出渲染後的內容，直接帶入檔案即可：
```bash
glow CHANGELOG.md
```
內容會直接印在目前畫面上，不進入分頁器，非常適合快速確認小片段內容。

### 模式 C：互動式 TUI 探索模式（直接輸入 `glow`）
不安裝任何參數直接執行 `glow`，會開啟全螢幕的 TUI（文字使用者介面）：
```bash
glow
```
- 自動搜尋當前目錄與子目錄下的所有 Markdown 檔案。
- 支援方向鍵挑選、按 `Enter` 進入閱讀、按 `/` 全文搜尋。
- 支援查看本地書籤（Bookmarks）與 GitHub 雲端星標文件。

### 模式 D：讀取遠端 GitHub 或網路 URL
無需手動複製或下載，Glow 能直接抓取網路上的 Markdown 並美麗呈現：
```bash
# 讀取 GitHub Repo 的 README
glow github.com/charmbracelet/glow

# 讀取特定 Raw URL
glow https://raw.githubusercontent.com/user/project/main/spec.md
```

---

## 4. 日常操作與常用參數速查（分級掌握）

### 4.1 核心 CLI 參數指令

| 指令範例 | 說明 | 推薦使用場景 |
| :--- | :--- | :--- |
| `glow -p <file.md>` | **啟用分頁器閱讀**（Pager） | 閱讀長篇規範、PRD、README 必備 |
| `glow -w 100 <file.md>` | **指定行寬為 100 字元**（Word Wrap） | 寬螢幕終端避免字行過長導致閱讀疲勞 |
| `glow -s light <file.md>` | **強制使用淺色主題**（Light Style） | 在白底或亮色系終端模擬最佳對比度 |
| `glow -s dark <file.md>` | **強制使用深色主題**（Dark Style） | 深色系終端預設樣式 |
| `glow` | **進入全功能 TUI 瀏覽器** | 尋找當前專案中散落在各資料夾的 docs |
| `git diff README.md \| glow` | **透過管線接收 Markdown** | 審查 Git 版本變更後的排版長相 |

### 4.2 分頁器（Pager）與 TUI 鍵位操作

在 `glow -p` 或全螢幕 TUI 模式中，支援 Vim 與標準鍵位：

| 按鍵 | 功能說明 |
| :--- | :--- |
| `↓` / `j` | 向下捲動一行 |
| `↑` / `k` | 向上捲動一行 |
| `Space` / `PageDown` | 向下翻整頁 |
| `b` / `PageUp` | 向上翻整頁 |
| `g` | 快速回到文件頂部（首行） |
| `G` | 快速跳至文件尾部（末行） |
| `/` | 搜尋關鍵字（TUI 模式） |
| `Esc` | 取消搜尋 / 返回上一層目錄 |
| **`q`** | **退出 Glow 閱讀模式，返回終端** |

---

## 5. 實戰情境與解決方案（在 Harness 中的妙用）

#### 情境一：審核 AI Agent 剛產出的系統規格或 PRD
* **問題**：讓 Agent 撰寫了一份詳細的 `docs/architecture.md`，裡面包含多張表格、步驟清單與代碼範例。若用 `cat` 看，排版混亂極難閱讀；若開 VS Code 又打斷雙手敲鍵盤的心流。
* **解法**：在終端直接下達：
  ```bash
  glow -p docs/architecture.md
  ```
  表格井然有序、色塊分明，按 `j`/`k` 快速逐條驗收，滿意後按 `q` 繼續下達後續指令。

#### 情境二：審查 Git Diff 或變更中的 Markdown 檔案
* **問題**：想看這次 commit 究竟把說明文件改成什麼樣子，但 `git diff` 顯示的是 `+` / `-` 混雜的純文字語法。
* **解法**：將特定版本的檔案透過管道餵給 Glow：
  ```bash
  git show HEAD:README.md | glow -p
  ```
  直接檢視當前最新提交的完整排版渲染結果！

#### 情境三：管線接收 AI 指令的即時 Markdown 輸出
* **問題**：有些終端 AI CLI 工具會輸出長篇 Markdown 回應，刷屏過快來不及看。
* **解法**：透過管線將結果串接給 `glow -p`：
  ```bash
  ai-tool "請分析此專案架構並給出重構建議" | glow -p
  ```
  輸出會整齊呈現在分頁器中，不洗版且能隨意上下翻閱。

---

## 6. 搭配 Herdr 終端多工工作流

在 [Herdr](../herdr/README.md) 中，推薦配置為左、右雙窗格工作流：

1. **左側窗格（PANE 1）**：啟動 AI Agent（如 `opencode`），下達指令要求建立或維護功能。
2. **右側窗格（PANE 2）**：當 Agent 產出或修改 `README.md`、`AGENTS.md` 時，在右側窗格輸入：
   ```bash
   glow -p AGENTS.md
   ```
3. 左邊看 AI 思考寫作，右邊即時驗收精美渲染成果，雙手完全無需拿起滑鼠，終端開發體驗極致流暢！

---

## 7. 設定檔與主題風格客製（Style & Config）

若你希望每次執行 `glow` 都自動啟用分頁器，或想固定字體行寬與配色主題，可以建立自訂設定檔：

### 設定檔路徑
* **macOS / Linux**：`~/.config/glow/glow.yml`
* **Windows**：`%APPDATA%\glow\glow.yml`

### 推薦設定範例（`glow.yml`）
```yaml
# 預設永遠啟用分頁器（省去每次手動加 -p）
pager: true

# 風格主題：可選 auto, dark, light, pink, dracula, notty
style: "auto"

# 預設自適應排版寬度（避免全螢幕時每行過長造成視覺疲勞）
width: 90

# 是否顯示行號（預設 false）
showAllFiles: false
```

---

## 8. 常見疑難排解（FAQ）

### Q1：文字顏色怪異或變成黑白純文字？
* **原因**：部分終端機未宣告支援 TrueColor（真彩色）。
* **解法**：在你的 `~/.zshrc` 或 `~/.bashrc` 中加入環境變數：
  ```bash
  export COLORTERM=truecolor
  ```
  然後重新載入配置或重啟終端機即可。

### Q2：在寬螢幕顯示器上，字行拉得太長很難讀？
* **解法**：使用 `-w`（width）參數限制最大寬度，例如：
  ```bash
  glow -w 80 -p README.md
  ```
  或在 `~/.config/glow/glow.yml` 中寫入 `width: 80`。

### Q3：如何快速退出 Glow？
* 在分頁（Pager）或全螢幕模式下，直接按鍵盤上的字母 **`q`** 或 **`Ctrl+C`** 即可立即回到 Shell。
