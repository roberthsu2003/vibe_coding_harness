# Herdr 版本、來源與更新紀錄

最近上網查核：**2026-10-13**。操作方式依當日官方文件，未查核本機 binary；各功能是否已收錄在你的 stable 版本，仍需透過 `--help` 確認。

## 查核時的發行狀態

官方 GitHub Releases 當日將 **v0.9.3** 標為 Latest，發布時間為 **2026-09-29**；列表另有 **preview-2026-10-12-6d697e1e75ff**。Preview 是另一個更新管道，不應直接當成 stable 最新版。[官方 Releases](https://github.com/herdrdev/herdr/releases)

官方文件目前列出 macOS、Linux、Windows stable 安裝與 OpenCode V2 integration 支援；部分搜尋結果仍會找到較早的 README，因此本文採官方當日安裝與整合文件。[Install](https://herdr.dev/docs/install/)｜[Integrations](https://herdr.dev/docs/integrations/)

## 更新方式

| 原本安裝方式 | 更新方式 |
| --- | --- |
| Herdr 官方 installer | `herdr update` |
| Homebrew | `brew update` 後執行 `brew upgrade herdr` |
| mise / Nix | 使用原套件管理器的更新流程 |

`herdr update` 適用 Herdr 自己的 installer 安裝；套件管理器安裝請走原管理器。[官方安裝與更新說明](https://herdr.dev/docs/install/)

官方 installer 的管道可用以下指令查閱：

```bash
herdr channel show
```

一般教學先使用 stable；確實需要 preview 功能時，再查閱 `herdr channel` 與相關文件。本文不預設切換管道。[官方 CLI reference](https://herdr.dev/docs/cli-reference/)

更新不保證所有既有程序永遠不中斷：相容 server 可持續執行，需重啟的 server 可能必須停止；`--handoff` 是額外的實驗機制。更新前先讀該版本說明，分清楚 detach、restart restore 與 live handoff。[官方 Session state](https://herdr.dev/docs/session-state/)

## 如何維護這份教學

1. 記錄 `herdr --version` 與更新管道。
2. 對照官方 Releases，核對 stable / preview 與發行日期。
3. 查閱 Install、Keyboard、CLI、Integrations 的變更。
4. 用本機命令群組說明核對旗標，再在練習 session 測試分割、讀取與 detach。
5. 搭配 OpenCode 時，重新核對整合相容性、安裝位置與需重啟的程序。
6. 修改文件並更新本頁紀錄；沒有做實機驗證時，明確標記「文件查核」。

## 官方來源索引

| 主題 | 來源 |
| --- | --- |
| 文件入口 | [Docs](https://herdr.dev/docs/) |
| 安裝與更新 | [Install](https://herdr.dev/docs/install/) |
| 初次操作 | [Quick start](https://herdr.dev/docs/quick-start/) |
| 快捷鍵 | [Keyboard](https://herdr.dev/docs/keyboard/) |
| 支援的 agents | [Agents](https://herdr.dev/docs/agents/) |
| CLI 指令 | [CLI reference](https://herdr.dev/docs/cli-reference/) |
| Agent 協調 | [Agent automation](https://herdr.dev/docs/agent-automation/) |
| OpenCode plugin | [Integrations](https://herdr.dev/docs/integrations/#opencode) |
| 持續執行與恢復 | [Session state](https://herdr.dev/docs/session-state/) |
| 發行版本 | [GitHub Releases](https://github.com/herdrdev/herdr/releases) |

## 查核紀錄

| 日期 | 本次確認 | 驗證層級 |
| --- | --- | --- |
| 2026-10-13 | Latest 標記為 v0.9.3；核對安裝、快捷鍵、窗格／agent CLI、OpenCode V2 整合與 Mini/headless 限制 | 官方網站與 Releases 文件查核；未啟動或控制 session |
