# 📚 參考：CLI 指令與疑難排解

> [章節首頁](README.md)　｜　相關：[06 多 Agent 協同](06-supervisor-subagent.md)、[07 動手練習](practice/README.md)

本頁指令以 herdr 0.9.3 實測為準。版本不同時，以本機 `herdr --help` 與各指令群組的說明為準（例如執行 `herdr pane`、`herdr agent`）。

---

## 1. 常用維護指令

| 指令 | 用途 |
| :--- | :--- |
| `herdr --version` | 查看版本 |
| `herdr status` | 查看 Herdr 背景服務是否在執行 |
| `herdr update` | 更新到最新版（官方腳本安裝時使用；Homebrew 請用 `brew upgrade herdr`） |
| `herdr server reload-config` | 修改 `config.toml` 後重新載入設定 |
| `herdr server stop` | 完全停止 Herdr 與所有窗格裡的程式 |
| `herdr session list` | 列出所有工作階段 |
| `herdr integration status` | 查看 AI 整合的安裝狀態 |
| `herdr --default-config` | 印出所有預設設定（含快捷鍵） |

---

## 2. 用指令操作窗格與 AI

> 以下指令要在 **Herdr 的窗格裡**執行。先確認：`echo $HERDR_ENV` 顯示 `1`。範例需要 `jq`（`brew install jq`）來讀取 JSON。

### 查看目前狀況

```bash
herdr workspace list                                  # 所有工作區
herdr pane list --workspace "$HERDR_WORKSPACE_ID"     # 目前工作區的窗格
herdr agent list                                      # 所有 AI 與狀態
```

### 開窗格、執行指令、讀回結果

```bash
# 從目前窗格向右切，保留目前資料夾，不搶游標；從回傳的 JSON 取出新窗格 ID
NEW=$(herdr pane split --current --direction right --cwd "$PWD" --no-focus | jq -r '.result.pane.pane_id')

herdr pane run "$NEW" "git status --short"                       # 送出指令並按 Enter
herdr pane wait-output "$NEW" --match "完成" --timeout 60000      # 等畫面出現某段文字（毫秒）
herdr pane read "$NEW" --source recent-unwrapped --lines 80     # 讀回輸出
herdr pane close "$NEW"                                         # 關閉窗格
```

### 啟動 AI、派工、讀回覆

```bash
herdr agent start coder --kind opencode --pane "$NEW" -- -m opencode/muse-spark-1.3-contributor-free
herdr agent prompt coder "請在 hello.py 寫一個印出 Hello 的程式" --wait --timeout 300000
herdr agent get coder                                    # 狀態：idle / working / blocked / done
herdr agent read coder --source recent-unwrapped --lines 60
```

- `agent start` 要在**停在 shell 提示字元**的窗格執行；名字（例如 `coder`）不能和其他執行中的 AI 重複。
- `--` 後面的參數會直接交給該 AI，例如 `-m` 指定模型。
- `--wait` 會等到 AI 停下來（做完或卡住）。回來後要用 `agent get` 確認是哪一種。
- 想同時派工給兩個 AI：`agent prompt` 不加 `--wait`，送完再分別執行 `herdr agent wait <名字>`。

### 重要原則

| 原則 | 原因 |
| :--- | :--- |
| 窗格 ID 一定從 JSON 讀取 | ID 像 `w1:p3`，關掉的 ID 不會重複使用，不能自己猜 |
| 開窗格加 `--no-focus` | 不搶走使用者的畫面 |
| 加 `--current` | 以自己的窗格為基準，避免切到別人正在看的窗格 |
| 不要用建立指令試探說明 | 例如 `herdr workspace create` 沒給參數也會真的建立 |

---

## 3. 疑難排解

| 狀況 | 解法 |
| :--- | :--- |
| 找不到 `herdr` 指令 | 重新開終端機，或 `source ~/.zshrc`；確認安裝路徑（如 `~/.local/bin`、`/opt/homebrew/bin`）在 `$PATH` 裡 |
| 快捷鍵沒反應 | Prefix 要**先按 `Ctrl+B` 放開，再按功能鍵**，不是三鍵一起按；忘記時按 `prefix+?` |
| AI 一直顯示 🟣 `unknown` | 安裝該 AI 的整合（`herdr integration install <名稱>`），再重新啟動 AI |
| AI 亮 🔴 很久 | 切到那個窗格，看它在等你批准什麼或問什麼 |
| `agent_blocked` 錯誤 | AI 正在等人回應，先 `herdr agent read <名字> --source visible` 看畫面 |
| `agent_name_taken` 錯誤 | 名字已被使用，換一個名字或先關掉舊窗格 |
| `pane_not_found` 錯誤 | 窗格 ID 打錯或已關閉，用 `herdr pane list` 查看 |
| 派工後小模型沒反應 | 窗格可能太窄，把終端機視窗放大後重新派工 |
| 想離開但 AI 要繼續跑 | 按 `prefix+q`，**不要**用 `killall herdr` |
| 想完全結束 | `herdr server stop` |

---

## 官方文件

| 主題 | 連結 |
| :--- | :--- |
| CLI 指令 | [CLI reference](https://herdr.dev/docs/cli-reference/) |
| AI 協調 | [Agent automation](https://herdr.dev/docs/agent-automation/) |
| 工作區與 worktree | [CLI：Workspaces / Worktrees](https://herdr.dev/docs/cli-reference/) |
| 遠端機器與 SSH | [Connecting machines](https://herdr.dev/docs/connecting-machines/) |
