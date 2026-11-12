# 08　權限設定與沙盒

> ★★★ 深入　｜　[← 07 Subagent 子代理](07-subagents.md)　｜　[章節首頁](README.md)　｜　下一站：[09 指令模式與 Herdr →](09-cli-run.md)

**這一站你會學到**：控制 AI 哪些事可以直接做、哪些要先問你、哪些完全禁止，以及用終端機沙盒保護電腦安全。

---

## 1. 為什麼要管權限？

`agy` 能讀寫檔案、執行終端機指令，也能連接外部工具。在預設的 `default` 模式下，AI 做修改或跑指令前都會先問你；但當你常用的安全指令（例如 `git status`、`pytest`）每次都要按同意時會覺得麻煩，而危險的指令（例如 `sudo`、`rm -rf`）則希望永遠禁止。

透過**權限規則**和**沙盒（Sandbox）**，你可以把安全的操作放行，同時把危險的操作擋下來。

---

## 2. 設定權限的三種方式

### 方法一：用 `/permissions` 畫面管理（推薦）

在對話框輸入：

```text
/permissions
```

可以用選單查看與修改目前的允許、詢問和禁止規則。

### 方法二：用一句話請 AI 幫你設定

直接用中文告訴 AI 你想怎麼設：

```text
請幫我在 ~/.gemini/antigravity-cli/settings.json 加上權限規則：git status 和 git diff 直接允許，sudo 和 rm 一律禁止。
```

### 方法三：直接改 `settings.json`

權限規則存放在 `~/.gemini/antigravity-cli/settings.json`（完整設定檔介紹見 [04 環境配置](04-config.md)）：

```json
{
  "toolPermission": "request-review",
  "enableTerminalSandbox": true,
  "permissions": {
    "allow": ["command(git status)", "command(git diff)", "read_url(google.com)"],
    "deny": ["command(sudo)", "command(rm)", "write_file(.git/)"],
    "ask": ["command(*)"]
  }
}
```

---

## 3. 看懂權限規則

### 三種清單

| 清單 | 意思 |
| :--- | :--- |
| `allow` | 直接執行，不詢問 |
| `ask` | 每次都先問你，同意才執行 |
| `deny` | 一律禁止 |

> [!IMPORTANT]
> 當多條規則同時符合時，優先順序是 **`deny`（禁止）> `ask`（詢問）> `allow`（允許）**。也就是說，只要寫進 `deny`，不管在哪種[執行模式](02-basics.md#4-執行模式)下都一定會被擋下來。

### 規則怎麼寫？

| 寫法 | 比對對象 | 例子 |
| :--- | :--- | :--- |
| `command(git)` | 開頭是 `git` 的終端機指令 | `git status`、`git log` |
| `command(regex:npm run (build\|lint\|test))` | 符合正規表達式的指令 | `npm run test` |
| `write_file(.git/)` | 修改指定路徑的檔案 | 禁止直接改 `.git/` 內部檔案 |
| `read_url(google.com)` | 讀取該網域與子網域的網頁 | `docs.google.com` |
| `mcp(linter/*)` | 指定 MCP 伺服器的工具 | `linter` 伺服器的所有工具 |
| `command(*)` | 所有終端機指令 | 搭配 `ask` 當作保底規則 |

### 整體工具授權設定（`toolPermission`）

除了單獨寫規則，`settings.json` 裡的 `toolPermission` 可以設定工具預設的詢問行為：

| 設定值 | 說明 |
| :--- | :--- |
| `request-review`（預設） | 執行指令前先請你確認 |
| `proceed-in-sandbox` | 在沙盒中自動執行，遇到高風險操作才詢問 |
| `always-proceed` | 自動同意執行 |
| `strict` | 最嚴格的審查模式 |

---

## 4. 終端機安全沙盒（Sandbox）

沙盒就像一個隔離的練習場。開啟沙盒後，AI 執行的終端機指令會被限制在專案工作區內，**不能亂動電腦系統的重要資料夾**（例如 `/etc`、`~/.ssh`），網路存取也會受到保護。

### 這次啟動開啟沙盒

```bash
agy --sandbox
```

### 預設永遠開啟沙盒

在 `~/.gemini/antigravity-cli/settings.json` 加上：

```json
{
  "enableTerminalSandbox": true
}
```

（或在 `/config` 選單裡把沙盒打開。）

---

## 5. 完全不詢問旗標（`--dangerously-skip-permissions`）

如果你在跑已經測好、而且有用 Git 備份的自動化腳本，想讓 AI 從頭跑到尾都不跳出詢問視窗，可以在啟動時加上：

```bash
agy --dangerously-skip-permissions
```

> [!CAUTION]
> 這個參數會**跳過所有確認提示，直接讓 AI 執行任何操作**。平時練習請不要使用；真的要用時，務必先 `git commit` 備份，並搭配 `--sandbox` 沙盒保護。

---

## 6. 管理 MCP 與外掛的開關

如果某個外部工具（MCP 伺服器）或外掛（Plugin）暫時用不到，可以把它關掉，讓 AI 只擁有目前需要的工具：

```bash
# 查看與開關 MCP 伺服器
agy mcp list
agy mcp disable <名稱>
agy mcp enable <名稱>

# 查看與開關外掛
agy plugin list
agy plugin disable <名稱>
agy plugin enable <名稱>
```

---

## ✅ 自我檢查

- [ ] 輸入 `/permissions` 看過目前的權限畫面
- [ ] 知道 `deny`、`ask`、`allow` 衝突時誰優先（`deny > ask > allow`）
- [ ] 用 `agy --sandbox` 啟動過一次沙盒模式

---

[← 07 Subagent 子代理](07-subagents.md)　｜　[章節首頁](README.md)　｜　下一站：[09 指令模式與 Herdr →](09-cli-run.md)
