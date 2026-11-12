# 09　指令模式與 Herdr

> ★★★ 深入　｜　[← 08 權限設定與沙盒](08-permissions.md)　｜　[章節首頁](README.md)　｜　下一站：[10 實戰情境 →](10-scenarios.md)

**這一站你會學到**：不進入對話畫面，直接用一行指令叫 `agy` 做事（`agy -p`）；以及搭配 Herdr 同時跑好幾個工作。

---

## 1. `agy -p`：一行指令完成一件事

有時候你只想快速問個問題、請 AI 檢查一個檔案，或是把 AI 的回答交給下一個終端機指令處理。這時可以用 **`-p`**（`--print`）非互動模式，跑完就會直接印出結果並回到終端機：

```bash
# 問一個問題，結果直接印在終端機
agy -p "請用繁體中文說明 README.md 的重點，並列出三個改進建議"

# 指定模型與思考強度
agy -p "檢查 src/auth.py 有沒有明顯的安全問題" --model gemini-4-argon-high --effort high

# 接著上一次的對話繼續問
agy -p "根據剛才找到的問題，幫我寫出對應的測試案例" -c

# 輸出成 JSON 格式，方便給其他程式或腳本讀取
agy -p "列出這個專案所有的 API 路徑" --output-format json
```

### 常用命令列參數

| 參數 | 縮寫 | 用途 |
| :--- | :--- | :--- |
| `--print` | `-p` | 一行指令模式，印出回答後直接結束（別名：`--prompt`） |
| `--prompt-interactive` | `-i` | 啟動時先跑這句指令，跑完**留在對話畫面**繼續聊 |
| `--continue` | `-c` | 接續最近一次的對話 |
| `--model` | | 指定這次要用的模型（如 `gemini-4-argon-high`） |
| `--effort` | | 指定思考強度（`low`、`medium`、`high`、`xhigh`、`max`） |
| `--mode` | | 指定執行模式（`plan`、`accept-edits`、`auto`） |
| `--output-format` | | 輸出格式：`text`（預設）、`json` 或 `stream-json` |
| `--print-timeout` | | 設定最長等待時間（例如 `300s`） |

> 💡 **搭配 [Glow](../glow/README.md) 閱讀排版好的長回答**：
> ```bash
> agy -p "說明這個專案的架構" | glow -p
> ```

---

## 2. 搭配 Herdr 多工開發

AI 在改程式或跑測試時通常要花一點時間。搭配終端機多工工具 [Herdr](../herdr/README.md)，你可以把畫面切開，一邊讓 `agy` 工作，一邊看測試結果或瀏覽檔案：

1. 在 Herdr 的左側窗格執行 `agy` 寫程式。
2. 按 `prefix+v` 切出右邊的窗格，再按 `prefix+s` 上下切開：
   - **右上窗格**：跑 `uv run pytest` 或啟動本地伺服器，隨時看結果。
   - **右下窗格**：開 [Yazi](../yazi/README.md) 看 AI 改了哪些檔案，或跑 `git status`。
3. 看一眼 Herdr 的狀態燈號，就能知道 `agy` 是在工作（🟡）、等你同意權限（🔴），還是已經做完了（🟢）。

```text
+-----------------------+-----------------------+
|                       |  uv run pytest        |
|                       |                       |
|  agy                  +-----------------------+
|                       |  yazi / git status    |
|                       |                       |
+-----------------------+-----------------------+
```

如果要同時做好幾個新功能，還可以搭配 [Git Worktree](../worktree/README.md)，在 Herdr 的不同分頁各開一個 `agy`，讓多個 AI 同時動工互不干擾！

> 詳細操作請見 [Herdr 教材](../herdr/README.md)。

---

## ✅ 自我檢查

- [ ] 用 `agy -p "你好"` 在終端機直接拿到 AI 的回答
- [ ] 說得出 `agy -p`（印完就結束）和 `agy -i`（問完繼續留在對話框）的差別
- [ ] 試過把 `agy -p` 的輸出接給 `glow -p` 閱讀（如果有安裝 Glow）

---

[← 08 權限設定與沙盒](08-permissions.md)　｜　[章節首頁](README.md)　｜　下一站：[10 實戰情境 →](10-scenarios.md)
