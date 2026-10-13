# vibe_coding_harness

這個 repo 用繁體中文介紹 **Harness**，以及怎麼透過 OpenCode、Herdr 這些工具，讓 AI 在你的專案裡實際做事。

## Harness 是什麼？

你可能遇過這種情況：請 AI 幫忙改程式，它給了一段答案，你再把程式碼貼進檔案、執行測試，出錯後又把錯誤訊息貼回去。

**Harness 可以想成「讓 AI 動手做事的一整套工作設備與流程」。** 它把模型、專案檔案、工具和操作規則接在一起，讓讀檔、改檔、執行指令、查看結果這些步驟能在同一個工作流程裡完成。

拿做菜來比喻：AI 模型像是負責想菜單的廚師；Harness 像是廚房，裡面有食材、鍋具、爐子，也有使用規則。廚師提出做法，廚房提供實際完成料理的條件。

## 為什麼說 OpenCode 是 Harness？

OpenCode 的推理與回答主要來自它連接的 AI 模型；OpenCode 則負責把模型接到你的專案與工具。從這個角度看，我們可以把它理解成一種 coding agent harness。[OpenCode 官方介紹](https://opencode.ai/v2/docs/)

可以用五件事來理解它的工作：

| 它幫忙處理什麼？ | 用口語說 | 小例子 |
| --- | --- | --- |
| 連接工具 | 讓 AI 有工具可以動手 | 讀取程式、修改檔案、執行終端指令；也能透過 MCP 接上額外工具 |
| 整理工作脈絡 | 告訴 AI 現在做什麼、要遵守什麼 | 讀取 `AGENTS.md` 裡的專案規則，管理對話紀錄，對話太長時整理重點 |
| 管理權限 | 決定哪些事能做、哪些要先問 | 允許讀檔，但修改檔案或執行某些指令前，需要你確認 |
| 檢查與修正 | 讓 AI 看得到自己做完的結果 | 依任務執行測試，把失敗訊息交回模型，再嘗試修正 |
| 分工 | 需要時讓不同 agent 負責不同任務 | 主 agent 處理修改，子 agent 協助檢查問題 |

這五點是方便理解的整理方式；測試要依專案與任務安排，分工也要依需求使用，不代表每次都會自動發生。工具與脈絡功能見官方 [Tools](https://opencode.ai/v2/docs/tools/)、[Instructions](https://opencode.ai/v2/docs/instructions/) 與 [Compaction](https://opencode.ai/v2/docs/compaction/)；權限與分工見 [Permissions](https://opencode.ai/v2/docs/permissions/) 與 [Agents](https://opencode.ai/v2/docs/agents/)。

## 一個小例子：請 AI 改按鈕文字

假設你正在做一個網站，想把「登入」按鈕改成「會員登入」。你可以在 OpenCode 裡說：

```text
請把首頁的「登入」按鈕改成「會員登入」。
保留原本的樣式與功能，修改後執行相關測試，並告訴我結果。
```

這時可以這樣理解整個過程：

1. **模型判斷怎麼改**：找出相關頁面與按鈕，決定需要修改哪裡。
2. **OpenCode 提供動手的工具**：讓模型能讀檔、提出修改，並依權限設定執行。
3. **工具把結果傳回來**：如果專案有相關測試，就執行測試；失敗時，模型可以根據錯誤再調整。
4. **你檢查成果**：看修改差異與測試結果，確認文字和功能都符合需求。

這是示意流程。實際步驟會依專案、提示與權限設定改變；專案沒有測試時，也要清楚回報哪些部分尚未驗證。

## 那 Herdr 在這裡做什麼？

Herdr 可以想成工作桌上的終端管理員：左邊開 OpenCode，右邊看測試或 Git 差異，再用狀態提示知道哪個 agent 正在工作、哪個需要你回答。它在這個 repo 裡負責介紹「怎麼把這些工作安排好」；模型與改程式的流程則由 OpenCode 負責。[Herdr Agents 文件](https://herdr.dev/docs/agents/)

## 開始操作

**最近上網查核：2026-10-13（Asia/Taipei）**。本次依官方文件整理；未在本機安裝工具或實際呼叫模型。文件是一份查核當日的快照，後續更新方式見各工具的更新紀錄。

| 工具 | 用途 | 閱讀入口 |
| --- | --- | --- |
| OpenCode CLI | 在專案中與 AI 對話、分析與修改程式、執行非互動任務 | [OpenCode 操作指南](opencode/README.md) |
| Herdr | 管理終端工作區、分頁與窗格，觀察 coding agent 狀態 | [Herdr 操作指南](herdr/README.md) |
| Yazi | 在終端機用鍵盤瀏覽檔案、預覽文件與複製路徑 | [Yazi 安裝與簡單操作](yazi/README.md) |
| OpenCode + Herdr | 在 Herdr 窗格中執行 OpenCode，加入狀態與 session 整合 | [整合實作](herdr/opencode-integration.md) |

建議先完成 OpenCode 的第一次對話，再學習 Herdr 的分割窗格與 detach，最後設定整合。

## 文件結構

```text
vibe_coding_harness/
├── README.md
├── opencode/
│   ├── README.md                # 安裝、對話、常用 CLI 與排錯
│   ├── configuration.md         # 專案指示、權限、自訂命令
│   └── updates.md               # 來源與更新紀錄
├── herdr/
│   ├── README.md                # 安裝、介面、快捷鍵、持續執行
│   ├── cli.md                   # 工作區、窗格、agent CLI
│   ├── opencode-integration.md  # OpenCode 整合與實作
│   └── updates.md               # 發行版本、來源與更新紀錄
└── yazi/
    └── README.md                # 一段 prompt 安裝、簡單操作與 Herdr 分頁
```

## 版本與指令

本 repo 的 OpenCode 教學統一採 [V2 官方文件](https://opencode.ai/v2/docs/)，包含安裝、操作、設定與整合。

Herdr 的指南採 [官方文件](https://herdr.dev/docs/)，另記錄 stable 與 preview 的差異。實際可用旗標以讀者安裝版本的 `--help` 為準；上游文件可能先於 stable binary 更新。

範例中的 `/path/to/project`、模型 ID 與 session ID 必須換成自己的值。文件只記錄人工查核，不會自動每日更新。
