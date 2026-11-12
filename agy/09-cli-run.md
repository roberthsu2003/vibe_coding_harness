# 10　指令模式與 Herdr

> ★★★ 深入　｜　[← 09 權限設定與沙盒](09-permissions.md)　｜　[章節首頁](README.md)　｜　📚 [維護指令與疑難排解](reference.md)

**這一站你會學到**：不進入互動介面，直接用一行指令讓 agy 執行任務（Print Mode）；以及搭配 Herdr 同步多工作業。

---

## 1. `agy -p`：一行指令完成一件事

有時候你只想快速查詢程式庫結構、審查特定檔案或將代碼重構結果交給其他終端工具處理。這時可以使用 **Print 模式**（`-p` 或 `--print`）：

```bash
# 提出問題，結果直接印在終端機
agy -p "請以繁體中文分析 README.md 的架構並列出三個優化建議"

# 指定模型與推理強度
agy -p "找出 src/auth.py 中的潛在安全性弱點" --model gemini-4-argon-high --effort high

# 接續上一次的工作階段繼續提問
agy -p "依據剛才的分析，產生修復該弱點的測試案例" -c

# 以 JSON 格式輸出，方便供其他自動化腳本解析
agy -p "列出本專案目前所有的 API endpoints" --output-format json
```

### 常用命令列參數

| 參數 | 縮寫 | 用途說明 |
| :--- | :--- | :--- |
| `--print` | `-p` | 非互動模式，執行單次 prompt 後直接印出結果並結束 |
| `--continue` | `-c` | 接續最近一次的對話工作階段 |
| `--model` | | 指定要執行的模型（如 `gemini-4-argon-high`） |
| `--effort` | | 設定模型推理強度（`low`、`medium`、`high`、`xhigh`、`max`） |
| `--output-format` | | 輸出格式：`text`、`json` 或 `stream-json` |
| `--print-timeout` | | 設定最大執行逾時時間（例如 `300s`） |

> 💡 **搭配 [Glow](../glow/README.md) 排版閱讀**：
> ```bash
> agy -p "說明整個專案的核心架構" | glow -p
> ```

---

## 2. 搭配 Herdr 多工開發

在大型專案中，AI 執行任務通常需要一些時間。透過終端機 多工工具 [Herdr](../herdr/README.md)，你可以一邊讓 `agy` 在背景執行，一邊進行其他操作：

1. **左側窗格**：啟動 `agy` 進行功能開發或自動修復。
2. **右上窗格**：持續執行 `uv run pytest -f` 或本地伺服器，觀察改動效果。
3. **右下窗格**：開啟 [Yazi](../yazi/README.md) 快速檢視修改過的檔案，或監控 `git diff`。

```text
+-----------------------+-----------------------+
|                       |  uv run pytest        |
|                       |                       |
|  agy                  +-----------------------+
|                       |  yazi / git status    |
|                       |                       |
+-----------------------+-----------------------+
```

當需要啟動多個針對不同模組的 agent 同步作業時，也可以在 Herdr 的不同 Tab 或 Workspace 中分別啟動 `agy`，並利用 Git Worktree 進行平行開發！

---

← [← 09 權限設定與沙盒](09-permissions.md)　｜　[章節首頁](README.md)　｜　📚 [維護指令與疑難排解](reference.md)

