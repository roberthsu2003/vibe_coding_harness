# 07　指令模式與 Herdr

> ★★★ 深入　｜　[← 06 權限設定](06-permissions.md)　｜　[章節首頁](README.md)　｜　📚 [維護指令與疑難排解](reference.md)

**這一站你會學到**：不進入對話介面，直接用一行指令叫 OpenCode 做事；以及搭配 Herdr 同時跑好幾個工作。

---

## 1. `opencode run`：一行指令完成一件事

```bash
# 問一個問題，結果直接印在終端機
opencode run "請用繁體中文檢查 README.md 的連結是否正確"

# 附上檔案
opencode run "優化這段程式的效能並加上型別標註" -f main.py

# 指定模型
opencode run "解釋這個專案的架構" -m opencode/muse-spark-1.3-contributor-free

# 接著上一次的對話
opencode run "為剛才修改的函式補上單元測試" -c

# 輸出 JSON，給其他程式使用
opencode run "列出專案裡所有的 TODO" --format json
```

| 參數 | 用途 |
| :--- | :--- |
| `-m`、`--model` | 指定模型（`供應商/模型`） |
| `-f`、`--file` | 附上檔案 |
| `-c`、`--continue` | 接續上一次的對話 |
| `--agent` | 指定代理，例如 `--agent plan` |
| `--format json` | 輸出 JSON |

> 💡 搭配 [Glow](../glow/README.md) 閱讀長回答：`opencode run "說明專案架構" | glow -p`

---

## 2. 搭配 Herdr

想一邊讓 OpenCode 寫程式、一邊跑測試或看檔案，或是同時跑好幾個 OpenCode，可以搭配 [Herdr](../herdr/README.md)：

1. 在 Herdr 的窗格執行 `opencode`。
2. 按 `prefix+v` 切出旁邊的窗格，跑測試、看 `git diff`，或開 [Yazi](../yazi/README.md) 看檔案。
3. Herdr 的狀態燈號會顯示 OpenCode 是在工作（🟡）、等你回應（🔴），還是做完了（🟢）。

（選用）安裝 Herdr 官方整合，狀態顯示會更準確：

```bash
herdr integration install opencode
```

> 詳細說明見 [在 Herdr 中使用 OpenCode](../herdr/opencode-integration.md)；讓主管 AI 指揮多個 OpenCode 見 [Herdr 動手練習](../herdr/practice/README.md)。

---

## ✅ 自我檢查

- [ ] 用 `opencode run` 問過一個問題
- [ ] 用 `-c` 接續過上一次的對話
- [ ] 在 Herdr 裡做出「左邊 OpenCode、右邊測試」的版面

> 🎉 完成 OpenCode 章節！遇到問題時查閱 [維護指令與疑難排解](reference.md)。
