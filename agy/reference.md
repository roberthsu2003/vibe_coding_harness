# 📚 參考：維護指令與疑難排解

> 📚 參考　｜　[章節首頁](README.md)

本頁整理 Antigravity CLI (`agy`) 的常用維護指令與常見狀況排解指南。

---

## 1. 常用管理指令

| 指令 | 用途說明 |
| :--- | :--- |
| `agy update` | 檢查並更新 `agy` 到最新版本 |
| `agy changelog` | 查看版本更新歷史與 Release Notes |
| `agy models` | 列出所有可用模型與推理等級 |
| `agy agent` | 列出目前環境支援的代理角色 |
| `agy mcp list` | 列出所有已配置的 MCP 伺服器狀態 |
| `agy mcp enable <name>` | 啟用指定的 MCP 伺服器 |
| `agy mcp disable <name>` | 停用指定的 MCP 伺服器 |
| `agy plugin list` | 列出目前已安裝的所有外掛模組 |
| `agy plugin install <target>` | 安裝指定外掛 |
| `agy install` | 配置 Shell 環境變數與路徑設定 |

斜線指令請見 [03 斜線指令](03-slash-commands.md)。

### 設定檔位置

| 檔案 | 用途 |
| :--- | :--- |
| `~/.gemini/antigravity-cli/settings.json` | CLI 設定：模型、模式、權限 |
| `~/.gemini/antigravity-cli/keybindings.json` | 快捷鍵 |
| `~/.gemini/config/AGENTS.md` | 全域個人規則 |
| `~/.gemini/config/skills/<名稱>/SKILL.md` | 全域 Skill |
| `~/.gemini/config/mcp_config.json` | MCP 伺服器 |
| `AGENTS.md` | 專案規則 |
| `.agents/rules/*.md` | 專案規則（拆成多檔） |
| `.agents/skills/<名稱>/SKILL.md` | 專案 Skill |

---

## 2. 疑難排解（Troubleshooting）

| 狀況 | 可能原因與解決方法 |
| :--- | :--- |
| **找不到 `agy` 指令** | 執行檔尚未加入系統 PATH。請執行 `~/.local/bin/agy install`，或檢查 `~/.zshrc`（或 `~/.bashrc`）確認 `~/.local/bin` 已加入 PATH，並重新啟動終端機。 |
| **身分認證失效或 401 錯誤** | 登入憑證過期。直接重新執行 `agy`，依終端提示重新完成瀏覽器登入授權。 |
| **出現 429 或配額上限錯誤** | 請求頻率過高或特定模型額度已達上限。可使用 `agy models` 檢視其他可用模型，並改用 `--model gemini-3.8-flash-medium` 繼續工作。 |
| **Skill 找不到或沒有自動使用** | 確認路徑是 `.agents/skills/<名稱>/SKILL.md`，輸入 `/skills reload`，並把 `description` 寫得更具體。詳見 [05 Skill 配置](05-skills.md#9-常見問題)。 |
| **AI 未遵守專案自訂規則** | 確認專案根目錄有名為 `AGENTS.md` 的檔案，且內容格式符合 Markdown 規範。在提問時可使用 `@AGENTS.md` 明確提醒 AI 參照。 |
| **MCP 工具無法連線或逾時** | 執行 `agy mcp list` 檢查伺服器狀態。若為特定 MCP 服務異常，可先以 `agy mcp disable <name>` 暫時停用，避免阻礙主流程。 |
| **執行指令卡住或長時間無回應** | 隨時按下 `Ctrl+C` 中斷目前呼叫。若對話上下文過大，輸入 `/compact` 壓縮歷史，或輸入 `/clear` 開新對話。 |

---

← [章節首頁](README.md)　｜　[回到專案首頁](../README.md)

