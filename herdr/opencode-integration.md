# 📚 參考：在 Herdr 中使用 OpenCode

> 📚 參考　｜　[章節首頁](README.md)　｜　相關：[03 AI 狀態燈號](03-agents.md)、[OpenCode 操作指南](../opencode/README.md)

**分工**：OpenCode 負責 AI 寫程式，Herdr 負責版面、狀態燈號與背景持續執行。本頁以 macOS / Linux 為例。

---

## 1. 先讓兩個工具各自可用

```bash
opencode --version
herdr --version
```

第一次使用 OpenCode 時，先單獨啟動 `opencode`，完成 `/connect` 與模型選擇，確認可以對話後再離開。這一步也會建立 OpenCode 的設定資料夾，後面安裝整合時會用到。

## 2. 安裝 Herdr 官方整合（建議）

> [!NOTE]
> **不安裝也能用**：實測（herdr 0.9.3）中，沒有安裝整合時 Herdr 仍能從畫面辨識 OpenCode，也能正確判斷 `idle`／`working`。安裝整合後狀態更準確，並支援 Herdr 重啟後恢復對話。

在 Herdr 的窗格裡執行：

```bash
herdr integration install opencode
herdr integration status            # 確認顯示為已安裝
```

整合會在 OpenCode 的全域設定資料夾寫入 plugin 檔案。安裝後**重新啟動 OpenCode** 才會生效。[官方說明](https://herdr.dev/docs/integrations/#opencode)

## 3. 試一次

在 Herdr 的窗格執行 `opencode`，輸入一個簡單的任務，例如：

```text
請閱讀 README.md，列出初學者可能看不懂的地方，先不要修改檔案。使用繁體中文回覆。
```

觀察左側欄的燈號是否依序變成 🟡 `working` → 🟢 `done`。也可以在另一個窗格執行 `herdr agent list` 查看狀態。

## 4. 用指令啟動 OpenCode

讓其他 AI 或腳本在指定窗格啟動 OpenCode 時，用 `--` 後面的參數指定模型：

```bash
herdr agent start coder --kind opencode --pane <窗格ID> -- -m opencode/muse-spark-1.3-contributor-free
```

本教材使用的免費模型：

| 用途 | 模型 | 實測（寫一個小函式） |
| :--- | :--- | :--- |
| 預設 | `opencode/muse-spark-1.3-contributor-free` | 約 10 秒 |
| 備用 | `opencode/nemotron-3.5-lightning-free`（NVIDIA） | 約 80 秒 |

完整範例見 [CLI 指令與疑難排解](cli.md#啟動-ai派工讀回覆)。

## 5. 限制

- **只支援完整的 `opencode` TUI**：OpenCode 的 Mini 版與 headless 模式不會載入這個 plugin，無法回報狀態。[官方說明](https://herdr.dev/docs/integrations/#opencode)
- **恢復對話不等於恢復程式**：Herdr 重啟後可恢復 OpenCode 對話，但 shell、測試、伺服器等程式要重新啟動。暫離（`prefix+q`）則一切照常執行。[Session state](https://herdr.dev/docs/session-state/)
- **不要在專案放主管規則的 `AGENTS.md`**：OpenCode 會自動讀取 `AGENTS.md`。如果你讓另一個 AI 當主管，主管規則請放在主管專用的檔案（例如 agy 讀取的 `GEMINI.md`），詳見 [06 多 Agent 協同](06-supervisor-subagent.md#4-怎麼讓主管-ai-知道要這樣做)。

## 6. 疑難排解

| 狀況 | 解法 |
| :--- | :--- |
| 安裝時說找不到 OpenCode 設定資料夾 | 先單獨啟動一次 OpenCode 並完成登入，再安裝整合 |
| 安裝後燈號沒變化 | 重新啟動 OpenCode；升級過舊版整合時，也要重啟 OpenCode 的背景 server |
| 出現 `Endpoint is unavailable` | 免費模型伺服器忙碌，換成備用模型 |
| 燈號亮 🔴 但看不出原因 | 切到 OpenCode 窗格，看它在等你批准什麼 |
