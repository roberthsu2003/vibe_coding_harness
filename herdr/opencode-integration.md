# 在 Herdr 中使用 OpenCode

查核日期：**2026-10-13**。OpenCode 負責 AI 任務，Herdr 負責終端版面、agent 狀態與持續執行。本頁採 macOS / Linux shell 範例。

## 1. 先讓兩個工具各自可用

依 [OpenCode](../opencode/README.md) 與 [Herdr](README.md) 入門完成安裝。在 shell 查看：

```bash
opencode --version
herdr --version
```

先啟動 OpenCode 並完成 `/connect` 與模型選擇，確認可以對話，再離開 OpenCode 回到 shell。這也讓 OpenCode 完成首次啟動的設定初始化。

## 2. 安裝 Herdr 官方整合

在 Herdr 的 shell 窗格內執行：

```bash
herdr integration install opencode
```

整合會寫入 OpenCode 全域設定目錄的 plugin 檔案，並登記 TUI plugin；設定目錄需已存在。安裝後重新啟動 OpenCode TUI。若先前已有舊整合，更新後也依官方說明重啟共用 OpenCode server，再重開 TUI。[官方 OpenCode integration](https://herdr.dev/docs/integrations/#opencode)

## 3. 開始文件任務

在 Herdr 窗格執行：

```bash
cd /path/to/vibe_coding_harness
opencode
```

在 OpenCode 提示框輸入：

```text
請閱讀 @opencode/README.md，檢查初學者是否能依序完成安裝與第一次對話。
先列出問題，不修改檔案。使用繁體中文回覆。
```

在旁邊的 shell 窗格執行：

```bash
herdr agent list
```

觀察 Herdr 是否辨識 OpenCode，以及開始任務、等待回應、完成時是否有合理的狀態切換。任務完成後閱讀實際回覆，再決定下一個修改任務。[官方 Agents](https://herdr.dev/docs/agents/)

## 4. 這個整合能提供什麼

完整 V2 TUI 的整合由窗格本地回報狀態，即使多個窗格共用同一個 OpenCode server，也以各窗格選定的 session 為範圍。

**V2 Mini 與 headless client 不會載入這個 TUI plugin，無法提供同樣的生命週期回報。** 在 Herdr 中學習狀態追蹤時，先使用完整 `opencode` TUI。[官方整合限制](https://herdr.dev/docs/integrations/#opencode)

Herdr 可利用整合回報的原生 session 參考，在 server 重啟後恢復符合條件的 agent 對話。這需要已回報有效 session，並不表示 shell、測試程序或開發 server 也會恢復成原來的程序。單純 detach 則保留原來的執行程序。[Session restore](https://herdr.dev/docs/session-state/)

## 5. 整合排錯

| 現象 | 處理方式 |
| --- | --- |
| 安裝說找不到 OpenCode 設定目錄 | 先完成 OpenCode 首次啟動與登入，再安裝整合 |
| 安裝後狀態沒改變 | 重新啟動 OpenCode TUI；若升級舊整合，核對是否也需重啟共用 server |
| Mini / `run` 沒有完整 V2 回報 | 換用完整 TUI 驗證 |
| Agent 正在等待你，但 CLI 任務沒完成 | 查看窗格中的批准或問題畫面，依實際內容回應 |

本頁是官方文件整理與練習步驟，未做實機整合測試。
