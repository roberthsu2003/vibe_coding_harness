# Harness 是什麼

AI coding agent 可以拆成兩個部分：

```text
AI coding agent = 模型 + Harness
```

- **模型**：負責思考和產生內容的「大腦」，但碰不到你的專案。
- **Harness**：把模型接上真實開發環境的那一層，包含工具、工作規則和權限設定。

有了 Harness，AI 才不只是回答問題，還能讀寫專案檔案、執行終端指令，並根據結果繼續修正。[OpenCode](opencode/README.md) 和 [Antigravity CLI](agy/README.md) 都屬於這類工具。

> 建議先用過其中一個工具，再回來看這一頁，比較容易對照。

## Harness 核心的五大職責

| 核心職責 | 領域 / 英文 | 說明與主要功能 |
| :--- | :--- | :--- |
| **工具連接與環境控制** | Tools & MCP | 提供檔案讀寫、終端機執行、Git 操作以及 MCP (Model Context Protocol) 伺服器介接能力，把大腦與真實開發環境連接起來。 |
| **上下文治理與持久化** | Context & State Management | 自動載入專案規範（如 AGENTS.md、架構設定）、過濾過大檔案或 lockfile 避免爆 token，並維護 session 狀態與對話交接（Handoff）。 |
| **權限約束與安全圍欄** | Constrain & Permissions | 透過設定檔（如 opencode.json）定義哪些操作可以直接執行（auto-run）、哪些需要人類確認（ask），防止危險指令破壞系統。 |
| **自動化驗證與修正迴圈** | Verify & Self-Correction | 代碼生成後自動掛載測試或 Linter 執行，並把失敗日誌餵回給模型修復，無需人類來回複製貼上終端機錯誤。 |
| **多 Agent 協同與分工** | Agent Orchestration | 支援主代理（Supervisor）與子代理（Subagent）拆分規劃、撰寫與評審（Auto-review）任務，避免單一模型包辦全部而失控。 |

← [回到專案首頁](README.md)
