# 📚 參考：版本與更新紀錄

> 📚 參考　｜　[章節首頁](README.md)　｜　相關：[01 安裝與啟動](01-install.md)

---

## 1. 本教材使用的版本

| 項目 | 內容 |
| :--- | :--- |
| 教材驗證版本 | **herdr 0.9.3**（stable） |
| 官方發布日期 | 2026-09-29 |
| 最後實機驗證 | 2026-10-16 |

查看自己的版本與更新管道：

```bash
herdr --version
herdr channel show        # 顯示 stable 或 preview
```

> [!NOTE]
> 官方 [Releases](https://github.com/herdrdev/herdr/releases) 也會列出 **preview** 版。Preview 是另一個測試用的更新管道，不是 stable 最新版。教學一律使用 **stable**。

---

## 2. 如何更新

| 當初的安裝方式 | 更新方式 |
| :--- | :--- |
| 官方安裝腳本 | `herdr update` |
| Homebrew | `brew update && brew upgrade herdr` |
| mise / Nix | 用原本的套件管理器更新 |

> [!WARNING]
> 更新時，背景執行中的 Herdr server 可能需要重啟，窗格裡的程式可能因此中斷。**更新前先讓 AI 完成手上的工作**，並閱讀該版本的更新說明。[官方說明](https://herdr.dev/docs/session-state/)

---

## 3. 官方文件索引

| 主題 | 連結 |
| :--- | :--- |
| 文件首頁 | [Docs](https://herdr.dev/docs/) |
| 安裝與更新 | [Install](https://herdr.dev/docs/install/) |
| 第一次使用 | [Quick start](https://herdr.dev/docs/quick-start/) |
| 快捷鍵 | [Keyboard](https://herdr.dev/docs/keyboard/) |
| 支援的 AI | [Agents](https://herdr.dev/docs/agents/) |
| CLI 指令 | [CLI reference](https://herdr.dev/docs/cli-reference/) |
| AI 協調 | [Agent automation](https://herdr.dev/docs/agent-automation/) |
| OpenCode 整合 | [Integrations](https://herdr.dev/docs/integrations/#opencode) |
| 持續執行與恢復 | [Session state](https://herdr.dev/docs/session-state/) |
| 發行版本 | [GitHub Releases](https://github.com/herdrdev/herdr/releases) |

---

## 4. 給教材維護者：如何更新這份教材

1. 記錄 `herdr --version` 與 `herdr channel show`。
2. 對照官方 Releases，確認 stable 版本與發行日期。
3. 用 `herdr --help`、`herdr pane`、`herdr agent` 等指令群組核對指令與參數。
4. 用 `herdr --default-config` 核對快捷鍵與設定項目（教材裡的 SVG 速查卡也要一起更新）。
5. 在練習用的資料夾實際跑過 [07 動手練習](practice/README.md) 的關卡。
6. 修改文件後，在下方查核紀錄新增一筆；只看文件、沒有實機測試時，標記為「文件查核」。

---

## 5. 查核紀錄

| 日期 | 確認內容 | 驗證方式 |
| :--- | :--- | :--- |
| 2026-10-16 | 章節重整；以本機 0.9.3 核對所有 CLI 指令與預設快捷鍵；實際跑過 6 關練習（agy + OpenCode） | **實機驗證** |
| 2026-10-13 | Latest 為 v0.9.3；核對安裝、快捷鍵、窗格／agent CLI、OpenCode V2 整合與 Mini/headless 限制 | 文件查核 |
