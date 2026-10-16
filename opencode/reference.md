# 📚 參考：維護指令與疑難排解

> 📚 參考　｜　[章節首頁](README.md)

本頁以 OpenCode 1.19.2 的 `opencode --help` 與[官方文件](https://opencode.ai/docs)為準。

![OpenCode 常用指令速查卡](assets/opencode-shortcuts.svg)

---

## 1. 常用管理指令

| 指令 | 用途 |
| :--- | :--- |
| `opencode --version` | 查看版本 |
| `opencode upgrade` | 升級到最新版 |
| `opencode providers list` | 查看已連接的供應商（`opencode auth list` 也可以） |
| `opencode providers login` | 在終端機登入供應商 |
| `opencode models` | 列出所有可用模型 |
| `opencode session list` | 列出歷史對話 |
| `opencode agent list` | 列出所有代理 |
| `opencode mcp list` | 列出 MCP 伺服器 |
| `opencode stats` | 查看 token 用量與費用 |
| `opencode debug config` | 查看最後實際使用的設定 |

---

## 2. 疑難排解

| 狀況 | 解法 |
| :--- | :--- |
| 找不到 `opencode` 指令 | 重新開終端機；用 `which opencode` 確認安裝路徑在 `$PATH` 裡 |
| 出現 401 錯誤 | 登入資訊失效。輸入 `/connect` 重新連接，或用 `opencode providers list` 檢查 |
| 出現 429 錯誤 | 請求太頻繁或額度用完，稍後再試或換模型 |
| 免費模型出現 `Endpoint is unavailable` | 伺服器忙碌，換成 `opencode/nemotron-3.5-lightning-free` |
| AI 一直用 `pip install` | 確認專案根目錄有 `AGENTS.md`（見 [03](03-agents-md.md)），並在對話中用 `@AGENTS.md` 提醒它 |
| 設定好像沒有生效 | 執行 `opencode debug config` 查看實際使用的設定 |
| 升級後還是舊版 | 關掉所有 OpenCode 視窗後重新啟動；用 `opencode --version` 確認 |
| 想換介面主題或快捷鍵 | 輸入 `/themes`；快捷鍵寫在 `tui.json` |
