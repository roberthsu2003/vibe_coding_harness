# Herdr Desktop 與 Herdr CLI 差異比較

> [章節首頁](README.md)　｜　相關：[01 安裝與第一次啟動](01-install.md)、[CLI 指令與疑難排解](cli.md)

Herdr 推出了全新的原生桌面應用程式 **Herdr Desktop（Herdr App）**。本教材第 01～07 站與實作練習以終端機版的 **Herdr CLI（TUI）** 為主，這頁幫你快速看懂兩者的差別，並選擇適合你的版本。

---

## 1. 一張表看懂：Herdr Desktop vs Herdr CLI（TUI）

| 比較項目 | Herdr Desktop（Herdr App） | Herdr CLI（Herdr TUI） |
| :--- | :--- | :--- |
| **介面型態** | 原生桌面視窗 App（macOS / Windows / Linux） | 終端機內的文字多工介面（類似 tmux） |
| **底層引擎** | `herdr-core`（常駐背景服務） | `herdr server`（常駐背景 Daemon） |
| **關掉視窗時** | 視窗關閉後，Agent 仍在 `herdr-core` 繼續執行 | 暫離（`prefix+q`）或關閉終端機後，Agent 仍在背景繼續執行 |
| **操作與快捷鍵** | 滑鼠點擊 + 桌面快捷鍵，側欄即時顯示各機器與 Agent 狀態 | 全鍵盤操作（`Ctrl+B` Prefix 快捷鍵） |
| **介面客製化** | **可用自然語言請 AI 改介面**：版面、快捷鍵、主題與 Mod 都是 `~/.config/herdr-app/` 裡的純檔案，例如「幫每個分頁加上計時器」 | 修改 `~/.config/herdr/config.toml` 調整設定與快捷鍵 |
| **多機與遠端連線** | 透過 SSH / Tailscale 直接把遠端伺服器、VM 加進同一個側欄管理（`hc machine add`） | 先 SSH 連進遠端機器，再啟動遠端上的 `herdr` |
| **手機連動** | 支援搭配 **Herdr Mobile**（iOS / Android）從手機看狀態、讀終端機輸出並回覆 | 無專屬手機 App（需透過手機 SSH 連回主機） |
| **多 Agent 協同指令** | 使用 `hc` 指令（如 `hc run --bg`、`hc send`） | 使用 `herdr` 指令（如 `herdr pane`、`herdr agent`） |
| **設定檔位置** | `~/.config/herdr-app/` | `~/.config/herdr/` |

---

## 2. 我該選哪一個？

- **選 Herdr Desktop（Herdr App）**，如果你：
  - 喜歡圖形化視窗介面、側欄卡片與拖拉操作。
  - 想用一句話請 AI 幫你改造工作區版面或加上自訂功能（Mod）。
  - 需要同時管理本機、遠端 VPS / VM，或想用手機 **Herdr Mobile** 隨時查看與回覆卡住的 Agent。
- **選 Herdr CLI（Herdr TUI）**，如果你：
  - 習慣在純終端機（例如 iTerm2、Ghostty、Alacritty、VS Code 內建終端機）裡工作。
  - 常在沒有桌面環境的遠端 Linux 伺服器上開發。
  - 要跟著本教材的 **[01～07 站與實作練習](practice/README.md)** 一步步操作 `herdr` 指令。

---

## 3. Herdr Desktop 安裝與常用指令

### 安裝 Herdr Desktop（會一併安裝 `herdr-core`）

| 作業系統 | 安裝方式 |
| :--- | :--- |
| **macOS（Homebrew）** | `brew install --cask herdr-app`（或至 [herdr.dev](https://herdr.dev/) 下載 `Herdr.dmg`） |
| **macOS / Linux（官方腳本）** | `curl -fsSL https://releases.herdr.dev/app/install.sh \| sh` |
| **Windows（PowerShell）** | `powershell -c "irm https://releases.herdr.dev/app/install.ps1 \| iex"` |

> 如果只需要在無桌面環境的伺服器安裝背景引擎與 CLI，可單獨安裝 `herdr-core`：
> `curl -fsSL https://releases.herdr.dev/core/install.sh | sh`

### 常用 `hc` 指令（Herdr Desktop / Core）

| 指令 | 用途 |
| :--- | :--- |
| `hc status` | 查看 `herdr-core` 執行狀態 |
| `hc machine add <名稱>` | 將可透過 SSH 連線的遠端主機加入側欄管理 |
| `hc machine list` | 列出已連接的主機 |
| `hc run --bg <指令>` | 在背景啟動另一個 Agent 或腳本任務 |
| `hc send <目標> "<訊息>"` | 傳送訊息或指示給指定窗格／Agent |

---

← [章節首頁](README.md)　｜　[01 安裝與第一次啟動](01-install.md)　｜　[官方網站 herdr.dev](https://herdr.dev/)

