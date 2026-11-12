# 📚 參考：維護指令與疑難排解

> 📚 參考　｜　[章節首頁](README.md)

本頁整理 Antigravity CLI (`agy`) 的常用終端機管理指令、設定檔位置與常見問題排解。

---

## 1. 常用管理指令（在一般終端機執行）

| 指令 | 用途說明 |
| :--- | :--- |
| `agy update` | 檢查並把 `agy` 更新到最新版本 |
| `agy changelog` | 查看版本更新內容（Release Notes） |
| `agy models` | 列出所有可用的模型與思考強度 |
| `agy agent`（或 `agy agents`） | 列出目前已安裝的代理角色 |
| `agy mcp list` | 列出所有已設定的 MCP 伺服器與狀態 |
| `agy mcp add <name> <command...>` | 新增一個 MCP 伺服器 |
| `agy mcp remove <name>` | 移除指定的 MCP 伺服器 |
| `agy mcp enable <name>` | 啟用指定的 MCP 伺服器 |
| `agy mcp disable <name>` | 停用指定的 MCP 伺服器 |
| `agy plugin list` | 列出目前已安裝的外掛（別名：`agy plugins`） |
| `agy plugin install <target>` | 安裝指定的外掛 |
| `agy plugin enable <name>` | 啟用指定的外掛 |
| `agy plugin disable <name>` | 停用指定的外掛 |
| `agy remote-control status` | 查看遠端控制背景服務的狀態（另有 `start`、`stop`） |
| `agy install` | 自動設定 Shell 的環境變數與 PATH 路徑 |

對話框裡的 `/` 指令請見 [03 斜線指令](03-slash-commands.md)。

### 設定檔位置速查

| 檔案 | 用途 |
| :--- | :--- |
| `~/.gemini/antigravity-cli/settings.json` | CLI 設定：模型、執行模式、權限、沙盒 |
| `~/.gemini/antigravity-cli/keybindings.json` | 自訂快捷鍵 |
| `~/.gemini/config/AGENTS.md` | 全域個人規則（所有專案都生效） |
| `~/.gemini/config/rules/*.md` | 全域個人規則（拆成多個檔案） |
| `~/.gemini/config/skills/<名稱>/SKILL.md` | 全域個人 Skill |
| `~/.gemini/config/mcp_config.json` | MCP 伺服器設定檔 |
| `AGENTS.md`（或 `GEMINI.md`） | 專案規則（放在專案根目錄或子資料夾） |
| `.agents/rules/*.md` | 專案規則（拆成多個檔案） |
| `.agents/skills/<名稱>/SKILL.md` | 專案專屬 Skill |

---

## 2. 疑難排解（Troubleshooting）

| 遇到的狀況 | 可能原因與解決方法 |
| :--- | :--- |
| **終端機顯示「找不到 `agy` 指令」** | 執行檔還沒加進系統 PATH。請執行 `~/.local/bin/agy install`，並**重新打開終端機**（macOS / Linux 預設裝在 `~/.local/bin/agy`）。 |
| **出現 401 或登入認證失效** | 登入憑證過期了。可以在對話框輸入 `/logout` 登出後重新執行 `agy`，照畫面指示在瀏覽器重新登入。 |
| **出現 429 或額度不足（Quota）** | 短時間內問太多次，或該模型的免費／方案額度用完了。先輸入 `/usage` 查看額度，再用 `/model` 換成比較輕量的模型（例如 `gemini-3.8-flash-medium`）繼續做。 |
| **剛寫好的 Skill 找不到或不會自動觸發** | 1. 確認資料夾叫 `.agents/skills/<名稱>/`（`.agents` 有 **s**），檔名是全大寫 `SKILL.md`。<br>2. 輸入 `/skills reload` 重新載入。<br>3. 把 `description` 寫得更具體。詳見 [05 Skill 配置](05-skills.md#9-常見問題)。 |
| **AI 沒有遵守 `AGENTS.md` 的規定** | 確認檔名拼對（全大寫 `AGENTS.md`）且放在專案根目錄。也可以在對話時用 `@AGENTS.md` 點名提醒它參考。 |
| **MCP 伺服器連不上或卡住** | 在終端機執行 `agy mcp list` 查看狀態。如果某個外部服務故障，先跑 `agy mcp disable <名稱>` 把它關掉，就不會卡住對話。 |
| **AI 卡住很久沒反應** | 按 `Ctrl+C` 中斷目前的動作。如果對話已經很長，輸入 `/compact` 壓縮對話，或輸入 `/clear` 開新對話。 |

---

[← 章節首頁](README.md)　｜　[回到專案首頁](../README.md)
