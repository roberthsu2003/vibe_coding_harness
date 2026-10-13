# Herdr 操作指南

查核日期：**2026-10-13**。Herdr 是供 coding agent 使用的終端多工工具：同一個介面中可管理多個專案與終端，並顯示 agent 是否工作中或需要你回應。它也能單純用來跑 shell、測試與開發伺服器。[官方文件](https://herdr.dev/docs/)｜[Agents](https://herdr.dev/docs/agents/)

延伸閱讀：[CLI 操作](cli.md)｜[搭配 OpenCode](opencode-integration.md)｜[版本與更新](updates.md)

## 1. 安裝

macOS / Linux 官方安裝方式：

```bash
curl -fsSL https://herdr.dev/install.sh | sh
```

已使用 Homebrew 的讀者也可選擇：

```bash
brew install herdr
```

Windows 官方目前提供 stable binary 與 PowerShell 安裝方式：

```powershell
powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"
```

Windows 手動解壓縮時須保留包含 ConPTY runtime 的整個目錄。平台限制請閱讀 [Windows support](https://herdr.dev/docs/windows-beta/)。安裝方法與平台支援以 [官方 Install](https://herdr.dev/docs/install/) 為準。

在 shell 確認版本與開啟介面：

```bash
herdr --version
herdr --help
cd /path/to/vibe_coding_harness
herdr
```

`herdr` 會開啟或連接預設背景 session。[官方 CLI reference](https://herdr.dev/docs/cli-reference/)

## 2. 理解介面

| 名稱 | 意義 | 本 repo 的練習例子 |
| --- | --- | --- |
| Workspace（工作區） | 一個專案或工作脈絡 | `vibe_coding_harness` |
| Tab（分頁） | 工作區內的一組終端版面 | 文件編輯、驗證 |
| Pane（窗格） | 真正執行 shell 或程式的終端 | 左邊 OpenCode，右邊 Git diff |
| Agent | 目前占用窗格且被 Herdr 辨識的 coding agent | 窗格內的 OpenCode |

新建工作區或分頁會一併建立第一個窗格；`agent start` 則只在既有空閒 shell 窗格啟動 agent。[官方 Agent automation](https://herdr.dev/docs/agent-automation/)

可以用滑鼠點選窗格、分頁與工作區，拖拉分隔線調整大小，使用右鍵選單分割窗格。初次使用可先靠滑鼠操作。[官方 Keyboard](https://herdr.dev/docs/keyboard/)

## 3. 常用快捷鍵

預設 prefix 是 **Ctrl+B**：先按下、放開，再按下一個鍵。例如 `prefix+c` 是先 Ctrl+B，再按 C。

| 快捷鍵 | 功能 |
| --- | --- |
| `prefix+?` | 查閱目前生效的快捷鍵 |
| `prefix+c` | 新增分頁 |
| `prefix+v` | 向右分割窗格 |
| `prefix+-` | 向下分割窗格 |
| `prefix+h/j/k/l` | 切換至左／下／上／右窗格 |
| `prefix+n/p` | 下一個／上一個分頁 |
| `prefix+w` | 工作區導覽 |
| `prefix+z` | 放大目前窗格 |
| `prefix+q` | Detach，離開介面但持續執行 |

自訂設定可能覆蓋預設鍵，請以 `prefix+?` 為準。[官方快捷鍵](https://herdr.dev/docs/keyboard/)

## 4. 第一次實作

1. 開啟 Herdr，在第一個窗格執行 `pwd`，確認位置是這個 repo。
2. 在該窗格執行 `opencode`，依 [OpenCode 入門](../opencode/README.md) 完成登入與對話。
3. 使用 `prefix+v` 分割右側窗格，點選新的 shell 窗格。
4. 在右側執行 `pwd` 與 `git status --short`；若目錄不同，先 `cd` 回 repo。
5. 左側交付文件任務；右側用 `git diff` 檢查改動。
6. 按 `prefix+q` 離開；在外層 shell 再輸入 `herdr` 回到原本版面。

這是本 repo 的練習流程；分割、滑鼠操作與 detach 的行為依 [Quick start](https://herdr.dev/docs/quick-start/) 與 [Session state](https://herdr.dev/docs/session-state/)。需要精確狀態與 session 恢復時，再設定 [OpenCode integration](opencode-integration.md)。

## 5. 看懂 agent 狀態

| 狀態 | 意義 |
| --- | --- |
| `working` | 正在執行任務 |
| `blocked` | 辨識到需要批准或回答的介面 |
| `idle` | 可接收新輸入 |
| `done` | 工作完成回到可輸入狀態，但尚未被標記為已查看 |
| `unknown` | 有 agent，但 Herdr 無法確定其狀態 |

`done` 是可輸入狀態的查看標記，不是測試通過的證明；`unknown` 也不代表完成。CLI 與各 TUI client 的已查看狀態可能不同。請打開窗格核對實際結果。[官方 Agent automation](https://herdr.dev/docs/agent-automation/)

## 6. Detach 與停止 server

| 操作 | 原有程序是否繼續執行 |
| --- | --- |
| `prefix+q` detach，之後重新 attach | 是，server 仍在執行 |
| 停止並重啟 Herdr server | 否；版面可恢復，程序需重新啟動 |
| 重開機 | 原有程序不會繼續；agent 對話恢復需有效 session 整合 |

一般暫時離開請用 detach。`herdr server stop` 會停止預設 server 與它管理的程序，不適合作為每天離開介面的替代方式。版面還原、畫面歷史與原生 agent session 還原是不同機制。[官方 Session state and restore](https://herdr.dev/docs/session-state/)

## 7. 遇到問題

| 問題 | 先檢查 |
| --- | --- |
| 找不到 `herdr` | 重新開啟終端、檢查 PATH 與安裝方式 |
| 快捷鍵不同 | 用 `prefix+?` 查看實際設定 |
| Agent 顯示 `unknown` | 打開窗格查看畫面，核對整合與 agent 偵測是否支援目前版本 |
| `--current` 失敗 | 指令須在 Herdr 管理的 shell 窗格內執行 |
| 重啟後只剩 shell | 查看是否有官方整合回報的原生 agent session |

詳見 [官方 Troubleshooting](https://herdr.dev/docs/troubleshooting/)。本指南完成文件核對，未在本機啟動或控制 Herdr session。
