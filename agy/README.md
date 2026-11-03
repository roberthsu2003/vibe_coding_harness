# Antigravity CLI (agy)：在終端機裡和 AI 代理協同開發

**Antigravity CLI (`agy`)** 是 Google Antigravity 的終端機 AI coding agent。它直接在終端機中執行，能讀懂專案脈絡、自主分析架構、編修程式碼、執行終端指令，並支援進階的多代理（Subagents）與外掛生態系。

- 用繁體中文說出需求，它能主動讀寫檔案、規劃任務並驗證成果。
- 支援多種旗艦與快速模型（如 Gemini 4 Argon、Gemini 3.8 Flash、Claude Sonnet 等）。
- 內建靈活的專案規則（`AGENTS.md` / `GEMINI.md`）、子代理分工與安全沙盒機制。
- 提供豐富的斜線指令（如 `/plan`、`/goal`、`/browser` 等）與強大的非互動指令模式（`agy -p`）。

---

## 學習路線

| 站 | 主題 | 難度 | 你會學到 |
| :---: | :--- | :---: | :--- |
| 01 | [安裝與登入](01-install.md) | ★ | 安裝 agy、身分認證、查看與切換模型 |
| 02 | [基本操作](02-basics.md) | ★ | 啟動與離開、輸入方式、常用斜線指令與快捷操作 |
| 03 | [專案規範與規則](03-agents-md.md) | ★★ | 使用 AGENTS.md 讓 AI 遵守團隊開發規範 |
| 04 | [實戰情境](04-scenarios.md) | ★★ | 任務中斷、長對話壓縮、Plan 模式與高品質 Prompt |
| 05 | [Subagent 子代理](05-subagents.md) | ★★★ | 主子代理協同分工、內建代理與自訂專屬代理 |
| 06 | [權限設定與沙盒](06-permissions.md) | ★★★ | 設定檔、終端沙箱安全與工具執行授權 |
| 07 | [指令模式與 Herdr](07-cli-run.md) | ★★★ | `agy -p` 一行指令執行、搭配 Herdr 多工開發 |

> [!TIP]
> **時間不多？** 讀完 01、02 就能立即上手；03、04 讓 AI 回覆與產出更加穩定；05～07 則是打造進階自動化與團隊工作流的關鍵。

---

## 📚 參考資料

| 文件 | 用途 |
| :--- | :--- |
| [維護指令與疑難排解](reference.md) | 常用 CLI 子指令、設定檔位置與常見問題排解 |
| [官方網站與文件](https://antigravity.google/docs) | Google Antigravity 官方技術文件 |
| [在 Herdr 中使用 agy](../herdr/README.md) | 搭配 Herdr 多工開發環境 |

← [回到專案首頁](../README.md)

