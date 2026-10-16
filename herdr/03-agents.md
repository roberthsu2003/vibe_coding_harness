# 03　AI 狀態燈號

> ★★ 進階　｜　[← 02 基本操作](02-basics.md)　｜　[章節首頁](README.md)　｜　下一站：[04 實戰情境 →](04-scenarios.md)

**這一站你會學到**：看懂 AI 的狀態燈號、安裝 AI 整合、設定聲音與通知。

---

## 1. 狀態燈號

在窗格裡啟動 AI（例如 `opencode`、`claude`、`agy`），Herdr 會自動認出它，並在左側欄與分頁上顯示燈號：

![AI 狀態燈號](assets/agent-status.svg)

| 燈號 | 狀態 | 你該做什麼 |
| :---: | :--- | :--- |
| 🟢 空心 | `idle` 待命中 | 可以交代新任務 |
| 🟡 | `working` 工作中 | 等它就好，可以去做別的事 |
| 🔴 | `blocked` 等你回應 | **切過去看它在問什麼**，不回應它就不會繼續 |
| 🟢 實心 | `done` 剛做完 | 切過去看成果，看完會變回空心 |
| 🟣 | `unknown` 認不出來 | 安裝該 AI 的整合（見下一節） |

> [!IMPORTANT]
> 🔴 `blocked` 最重要。同時跑好幾個 AI 時，只要盯著側欄有沒有紅燈就好。

---

## 2. 安裝 AI 整合（讓燈號更準確）

Herdr 能直接從畫面辨識多數 AI。安裝官方整合後，AI 會主動回報自己的狀態，燈號更準確；部分整合還支援 Herdr 重啟後恢復 AI 對話。

```bash
herdr integration status                    # 查看哪些整合已安裝
herdr integration install opencode          # 安裝整合（換成你要的名稱）
```

| AI 工具 | 整合名稱 |
| :--- | :--- |
| OpenCode | `opencode`（詳見 [OpenCode 整合](opencode-integration.md)） |
| Claude Code | `claude` |
| Codex CLI | `codex` |
| Antigravity CLI（agy） | `antigravity-cli` |

安裝後，**關掉並重新啟動該 AI**才會生效。完整清單請執行 `herdr integration` 查看。

---

## 3. 聲音與通知

AI 在**背景工作區**變成 🔴 或 🟢 時，Herdr 會播放提示音。可以在 `~/.config/herdr/config.toml` 調整：

```toml
[ui.sound]
enabled = true                       # 開關提示音
# done_path = "sounds/done.mp3"      # 自訂「做完了」的音效（mp3）
# request_path = "sounds/request.mp3" # 自訂「等你回應」的音效（mp3）

[ui.toast]
delivery = "herdr"                   # 跳出通知：off / herdr / terminal / system
```

改完設定後執行：

```bash
herdr server reload-config                                  # 套用新設定
herdr notification show "測試通知" --sound done             # 試聽音效
```

---

## ✅ 自我檢查

- [ ] 在窗格啟動一個 AI，看到側欄出現它的燈號
- [ ] 能說出 🔴 和 🟢 實心各代表什麼、該做什麼
- [ ] 執行過 `herdr integration status`

> 下一站：[04 實戰情境 →](04-scenarios.md)
