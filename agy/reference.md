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

---

## 2. 疑難排解（Troubleshooting）

| 狀況 | 可能原因與解決方法 |
| :--- | :--- |
| **找不到 `agy` 指令** | 執行檔尚未加入系統 PATH。請執行 `agy install` 或檢查 `~/.zshrc`（或 `~/.bashrc`）確認 Antigravity bin 路徑已匯入，並重新啟動終端機。 |
| **身分認證失效或 401 錯誤** | 登入憑證過期。直接重新執行 `agy`，依終端提示重新完成瀏覽器登入授權。 |
| **出現 429 或配額上限錯誤** | 請求頻率過高或特定模型額度已達上限。可使用 `agy models` 檢視其他可用模型，並改用 `--model gemini-3.8-flash-medium` 繼續工作。 |
| **AI 未遵守專案自訂規則** | 確認專案根目錄有名為 `AGENTS.md` 的檔案，且內容格式符合 Markdown 規範。在提問時可使用 `@AGENTS.md` 明確提醒 AI 參照。 |
| **MCP 工具無法連線或逾時** | 執行 `agy mcp list` 檢查伺服器狀態。若為特定 MCP 服務異常，可先以 `agy mcp disable <name>` 暫時停用，避免阻礙主流程。 |
| **執行指令卡住或長時間無回應** | 隨時按下 `Ctrl+C` 中斷目前呼叫。若對話上下文過大，輸入 `/compact` 壓縮歷史或開新對話。 |

---

← [章節首頁](README.md)　｜　[回到專案首頁](../README.md)

