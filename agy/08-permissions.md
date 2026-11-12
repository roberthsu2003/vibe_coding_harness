# 08　權限設定與沙盒

> ★★★ 深入　｜　[← 07 Subagent 子代理](07-subagents.md)　｜　[章節首頁](README.md)　｜　下一站：[09 指令模式與 Herdr →](09-cli-run.md)

**這一站你會學到**：設定檔位置、終端安全沙盒（Sandbox）機制、工具執行授權，以及 MCP 與外掛的安全管理。

---

## 1. 為什麼需要權限與沙盒？

AI coding agent 擁有執行 Shell 指令、讀寫檔案與調用外部工具的能力。如果沒有安全圍欄，可能會因為模型誤判而執行破壞性指令（如遞迴刪除檔案、變更系統權限或意外送出敏感資料）。

`agy` 提供了嚴謹的權限確認機制與終端沙盒防護。

---

## 2. 權限規則

在對話中輸入 `/permissions` 就能管理權限。規則會存放在 `~/.gemini/antigravity-cli/settings.json` 的 `permissions` 裡（設定檔的完整介紹請見 [04 環境配置](04-config.md)）：

```json
{
  "permissions": {
    "allow": ["command(git)", "read_url(google.com)"],
    "deny": ["command(sudo)", "write_file(.git/)"],
    "ask": ["command(*)"]
  }
}
```

| 清單 | 意思 |
| :--- | :--- |
| `allow` | 直接執行，不詢問 |
| `ask` | 每次都先問你 |
| `deny` | 一律禁止 |

規則衝突時的優先順序是 **deny > ask > allow**。規則也優先於[執行模式](02-basics.md#4-執行模式)。

| 寫法 | 比對對象 |
| :--- | :--- |
| `command(git)` | 開頭是 `git` 的指令 |
| `command(regex:npm run (build\|lint\|test))` | 符合正規表達式的指令 |
| `read_url(google.com)` | 該網域與其子網域 |
| `mcp(linter/*)` | `linter` 伺服器的所有工具 |
| `command(*)` | 所有指令 |

---

## 3. 安全沙盒模式（`--sandbox`）

如果你在不受信任的目錄或需要嚴格限制 AI 對系統主機的存取，可以使用沙盒模式啟動：

```bash
agy --sandbox
```

在沙盒模式下：
- **終端機限制**：限制 Shell 指令的執行範圍與網路存取。
- **檔案系統保護**：防止存取工作空間以外的敏感系統目錄（如 `/etc`、`~/.ssh`）。

---

## 4. 自動批准旗標（`--dangerously-skip-permissions`）

預設情況下，當 AI 要執行可能具有變更性的操作時，會向使用者請求確認。如果你正在執行已受版本控制的自動化腳本或夜間批次測試，可以使用此旗標：

```bash
agy --dangerously-skip-permissions
```

> [!CAUTION]
> 此選項會**自動允許所有工具執行請求且不跳出確認提示**。請確保專案已完整 commit 進 Git，並避免在包含機密環境變數的環境中盲目開啟。

---

## 5. MCP 伺服器與外掛權限管理

`agy` 內建完整的 MCP（Model Context Protocol）與 Plugin 外掛管理指令：

### 管理 MCP 工具伺服器

```bash
# 查看所有已設定的 MCP 伺服器
agy mcp list

# 啟用特定伺服器
agy mcp enable <server-name>

# 暫時停用伺服器
agy mcp disable <server-name>
```

### 管理外掛（Plugins）

```bash
# 列出目前安裝的外掛
agy plugin list

# 停用特定外掛
agy plugin disable <plugin-name>
```

透過精細管理各個 MCP 與 Plugin，可以確保 agent 只獲得完成工作所必需的最小權限集合。

---

← [← 07 Subagent 子代理](07-subagents.md)　｜　[章節首頁](README.md)　｜　下一站：[09 指令模式與 Herdr →](09-cli-run.md)

