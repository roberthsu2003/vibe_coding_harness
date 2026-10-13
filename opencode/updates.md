# OpenCode 版本、來源與更新紀錄

最近上網查核：**2026-10-13**。查核依據是當日官方文件，未查核本機 OpenCode binary，也不把文件中的範例版本宣稱為最新發行版本。

## 如何持續更新這份教材

1. 記錄實際使用的 `opencode --version`。
2. 開啟對應版本的官方文件與 [官方 GitHub Releases](https://github.com/anomalyco/opencode/releases)，區分 stable 與 prerelease。
3. 檢查安裝、登入、TUI、權限與 plugin 是否改變；以子命令 `--help` 核對實際可用旗標。
4. 需要更新時執行 `opencode upgrade`；若有共用 server，先完成目前工作，再依官方說明重啟使更新生效。
5. 在隔離的練習專案驗證對話、讀檔與改檔，再修改本 repo 的教學與查核日期。

CLI 更新方式見 [Commands](https://opencode.ai/v2/docs/cli/commands/)，背景 server 不會隨安裝更新自動重啟的行為見 [Config](https://opencode.ai/v2/docs/config/)。

## 官方來源索引

| 主題 | 來源 |
| --- | --- |
| V2 安裝 | [Intro](https://opencode.ai/v2/docs/) |
| 互動與非互動 CLI | [CLI Intro](https://opencode.ai/v2/docs/cli/) |
| TUI 操作 | [TUI](https://opencode.ai/v2/docs/cli/tui/) |
| 指令與參數 | [CLI Commands](https://opencode.ai/v2/docs/cli/commands/) |
| 設定 | [Config](https://opencode.ai/v2/docs/config/) |
| 權限 | [Permissions](https://opencode.ai/v2/docs/permissions/) |
| 專案規則 | [Instructions](https://opencode.ai/v2/docs/instructions/) |
| 自訂提示命令 | [Commands](https://opencode.ai/v2/docs/commands/) |
| 自訂 agent | [Agents](https://opencode.ai/v2/docs/agents/) |

## 查核紀錄

| 日期 | 本次確認 | 驗證層級 |
| --- | --- | --- |
| 2026-10-13 | 核對 V2 安裝、TUI、背景服務與權限格式 | 官方文件查核；未執行安裝或模型任務 |
