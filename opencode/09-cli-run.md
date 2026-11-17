# 09　指令模式與 Herdr

> ★★★ 深入　｜　[← 08 權限設定](08-permissions.md)　｜　[章節首頁](README.md)　｜　下一站：[10 實戰情境 →](10-scenarios.md)

**這一站你會學到**：不進入對話介面，直接用一行指令叫 OpenCode 做事；以及搭配 Herdr 同時跑好幾個工作。

---

## 開始前：建立本節練習資料夾

先完成[課堂練習準備](../practice/README.md)的工具確認與教材下載，再在**一般終端機**逐行執行：

```bash
python3 ~/terminal-ai-course/practice/prepare.py ~/terminal-ai-labs/opencode/09
cd ~/terminal-ai-labs/opencode/09
opencode
```

看到目的資料夾已存在時，直接 `cd` 進去接續；要重做則把路徑最後一段改成 `09-retry`。本節的程式、筆記與初始 Git commit 都已準備好。

---

## 1. `opencode run`：一行指令完成一件事

素材已附 `main.py`、`calc.py`、`tests/` 與 README。確認已依第 01 站登入後，在一般終端機依序執行：

```bash
# 1. 唯讀提問
opencode run "請讀 README.md，回報用途與測試指令，不要修改"

# 2. 附檔案，產生明確的改動
opencode run "只為 main.py 加上型別或中文註解，保持執行結果 4.0 不變" -f main.py

# 3. 立即接續上一個任務，不要穿插別的 run
opencode run "請把剛才改了什麼與驗證方式寫成 run-summary.md，不再改 Python 檔案" -c

# 4. 指定模型；若 ID 已下架，換成 /models 中選到的可用非中國大陸模型
opencode run "請讀 README.md，只回報測試指令" -m opencode/nemotron-3.5-lightning-free

# 5. 只規劃，不動檔案
opencode run "請規劃在 README.md 新增安裝說明，先不要修改" --agent plan

# 6. 輸出 JSON 事件
opencode run "請只讀 main.py，列出 TODO 註解，不修改" --format json
```

**驗收**：第 2 步後 `python3 main.py` 仍印出 `4.0`，`git diff -- main.py` 可見註解；第 3 步產生 `run-summary.md` 且說明上一輪改動；第 5 步後 `git diff -- README.md` 無輸出。第 6 步為 JSON 輸出，可能包含多筆事件，不要假設一定只有一個 JSON 物件。

若第 08 站設了 `ask`，請依實際提示授權；無法互動授權時回互動式 OpenCode 送出同一任務，不能把權限失敗當成任務成功。

| 參數 | 用途 |
| :--- | :--- |
| `-m`、`--model` | 指定模型（`供應商/模型`） |
| `-f`、`--file` | 附上檔案 |
| `-c`、`--continue` | 接續上一次的對話 |
| `-s`、`--session` | 接續指定的對話 |
| `--agent` | 指定代理，例如 `--agent plan` |
| `--format json` | 輸出 JSON |
| `--auto` | 自動同意沒有被 `deny` 的操作（見 [08](08-permissions.md)） |
| `--standalone` | 不使用背景服務（見 [04](04-config.md#4-環境變數)） |

> [!NOTE]
> **斜線指令在 `opencode run` 裡沒有作用。** `opencode run "/hello 小明"` 會把這串文字原封不動送給 AI。請直接寫出你要它做的事。

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

## 完整小練習：Herdr 左邊修改、右邊驗收

先依 [Herdr 安裝教學](../herdr/01-install.md)完成安裝。兩個窗格都先 `cd ~/terminal-ai-labs/opencode/09`。

1. 左邊啟動 `opencode`，送出 `請為 calc.py 的 divide 加上中文 docstring 與型別標註，不改運算結果，完成後執行 python3 -m unittest discover -s tests -v。`。
2. 右邊執行 `python3 -m unittest discover -s tests -v`，再執行 `git diff -- calc.py`。
3. **驗收**：4 個測試通過，diff 顯示 docstring 與型別。左側的 AI 工作紀錄與右側實際程式結果對得上。

`--session` 選做：先 `opencode session list`，複製本節對話 ID，再執行 `opencode run "請用一句話回顧這個任務，不改檔案" --session 貼上實際ID`，回答應能回顧前文。`--standalone` 可用 `opencode run "只回覆 OK" --standalone` 驗證。`--auto` 為進階參數，本節無需開啟。Glow 選做題先確認 `glow --version`，再使用前面的管線，應看見排版後文字。

## ✅ 自我檢查

- [ ] 用 `opencode run` 問過一個問題
- [ ] 用 `-c` 接續過上一次的對話
- [ ] 在 Herdr 裡做出「左邊 OpenCode、右邊測試」的版面

> 下一站：[10 實戰情境 →](10-scenarios.md)
