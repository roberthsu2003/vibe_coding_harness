# OpenCode CLI 操作指南

查核日期：**2026-10-13**。本頁採 **OpenCode V2** 官方文件。OpenCode 是可在終端中執行的開源 AI coding agent；你提供任務與專案脈絡，它透過工具讀取檔案、修改程式與執行指令。[官方介紹](https://opencode.ai/v2/docs/)

延伸閱讀：[設定與自訂命令](configuration.md)｜[來源與更新](updates.md)｜[搭配 Herdr](../herdr/opencode-integration.md)

## 1. 安裝與確認版本

以下方式**擇一**。macOS 若已使用 Homebrew：

```bash
brew install anomalyco/tap/opencode-v2
```

macOS / Linux 官方安裝腳本：

```bash
curl -fsSL https://opencode.ai/v2/install | bash
```

已安裝 Node.js 與 npm：

```bash
npm install -g @opencode/cli
```

Windows 的 V2 文件目前提供獨立 binary，並註明 Windows 套件管理器尚未支援；請從官方頁面選擇符合架構的下載項目。[V2 安裝方式](https://opencode.ai/v2/docs/)

安裝後在 shell 執行：

```bash
opencode --version
opencode --help
```

## 2. 第一次對話

在你的專案根目錄執行；使用這個 repo 時，先進入 `vibe_coding_harness`：

```bash
cd /path/to/vibe_coding_harness
opencode
```

這會開啟 TUI，也就是終端中的互動介面。亦可用 `opencode /path/to/project` 指定其他專案。[CLI 入門](https://opencode.ai/v2/docs/cli/)

接下來的 `/` 指令輸入在 **OpenCode 對話框**，不要輸入在 shell：

```text
/connect
/models
```

依 `/connect` 的畫面選擇 provider 並完成登入或 API key 設定，再用 `/models` 選模型。可用模型、登入方式與額度依 provider 而異。[連接 provider](https://opencode.ai/v2/docs/)｜[TUI 命令](https://opencode.ai/v2/docs/cli/tui/)

輸入這段練習提示，按 Enter：

```text
請閱讀這個 repo，使用繁體中文解釋 opencode 與 herdr 資料夾各自的用途。
先只做說明，不修改檔案。
```

確認它能讀取正確的專案，且回覆符合需求，就是第一次對話的驗收點。

## 3. 日常互動

| 操作 | 用法 |
| --- | --- |
| 加入檔案脈絡 | 輸入 `@` 搜尋檔案，例如 `請檢查 @README.md` |
| 列出內建操作 | 輸入 `/`，或按 `Ctrl+P` 開啟命令面板 |
| 建立新對話 / 切換對話 | `/new` / `/sessions` |
| 選擇 agent | `/agents` |
| 撤回 / 重做 | `/undo` / `/redo` |
| 提示換行 | `Ctrl+J`，也可使用終端支援的 `Shift+Enter` 等組合 |
| 執行 shell 指令 | 在空提示開頭輸入 `!`，例如 `!git status` |

任務執行期間按 Enter 會引導目前的任務；要將新提示排到稍後執行，按 `Ctrl+X` 再按 Enter。[官方 TUI 操作](https://opencode.ai/v2/docs/cli/tui/)

建議把「目標、範圍、驗收」放進提示，例如：

```text
請改善 @herdr/README.md 的初學者操作流程。
範圍：只修改這份 Markdown；保留官方來源與查核日期。
驗收：每個步驟說明在哪裡輸入指令，並檢查相對連結是否有效。
完成後列出修改內容與檢查結果。
```

需要規劃時，先用 `/agents` 選擇可用的規劃 agent，再切回執行 agent；可用 agent 與權限請依目前設定確認。[Agents 文件](https://opencode.ai/v2/docs/agents/)

完成修改後，在 shell 檢查實際變更：

```bash
git status --short
git diff
```

撤回功能適合對話中修正方向，Git diff 則用來核對最終檔案內容。

## 4. 非互動 CLI

以下指令在 **shell** 執行，適合單次任務或腳本。`run` 不開啟 TUI：

```bash
opencode run "請用繁體中文說明這個 repo 的文件結構"
opencode run --continue "請補充建議的閱讀順序"
opencode run --file README.md "請檢查這份文件的文字與連結"
opencode run --format json "請列出 README.md 中需要改進的項目"
opencode run --help
```

`--format json` 輸出換行分隔的 JSON 事件，腳本應逐行解析。若要指定模型，先以 `opencode models` 查詢，再傳入 `--model provider/model`；不要直接沿用別人的模型 ID。[CLI commands](https://opencode.ai/v2/docs/cli/commands/)

V2 預設連接或啟動同一位使用者的共用背景 server。若任務需要獨立 server，可使用 `opencode run --standalone "你的任務"`；CI 中尤其要注意 API key 應傳入實際執行任務的 server 環境。[背景服務](https://opencode.ai/v2/docs/cli/)｜[CI 範例](https://opencode.ai/v2/docs/cli/commands/)

## 5. 常用管理指令

| shell 指令 | 用途 |
| --- | --- |
| `opencode auth list` | 查看已設定的 provider |
| `opencode models` | 列出模型 |
| `opencode session list` | 列出對話 session |
| `opencode mcp list` | 查看 MCP server |
| `opencode service status` | 查看共用背景服務 |
| `opencode debug config` | 查詢設定來源 |
| `opencode debug paths` | 查詢資料、設定與 log 路徑 |
| `opencode upgrade` | 更新 CLI |

每個命令的完整旗標請加上 `--help` 查閱。[官方 CLI reference](https://opencode.ai/v2/docs/cli/commands/)

## 6. 常見問題

| 問題 | 處理方式 |
| --- | --- |
| 找不到 `opencode` | 重新開啟 shell，檢查安裝目錄是否在 PATH；macOS / Linux 可用 `command -v opencode` 查看目前執行檔 |
| 出現不認得的參數 | 核對 `--version`，確認文件與 binary 都是 V2，再看該子命令的 `--help` |
| 無法使用模型 | 查看 `auth list` 與 `models`，回到 `/connect` 確認 provider 登入、額度與權限 |
| CLI 更新後行為沒改變 | V2 更新不會自動重啟既有 server；完成目前工作後再重啟背景服務 |
| Herdr 看不到正確的工作狀態 | 參考 [整合教學](../herdr/opencode-integration.md)，確認使用完整 TUI 與最新整合 |

更新與服務行為依 [Config 文件](https://opencode.ai/v2/docs/config/) 與 [CLI 文件](https://opencode.ai/v2/docs/cli/commands/)；完整排錯入口為 [官方 Troubleshooting](https://opencode.ai/v2/docs/troubleshooting/)。本頁指令經文件核對，尚未做本機端到端測試。
