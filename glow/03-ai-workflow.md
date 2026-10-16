# 03　搭配 AI 與 Herdr

> ★★ 進階　｜　[← 02 四種閱讀方式](02-reading.md)　｜　[章節首頁](README.md)　｜　下一站：[04 設定與主題 →](04-config.md)

**這一站你會學到**：檢閱 AI 產出的文件，並讓 Glow 和 AI 並排工作。

---

## 1. 為什麼 AI 開發需要 Glow？

AI 不只會寫程式，還會寫很多 Markdown 文件：規格書（`spec.md`）、架構說明（`ARCHITECTURE.md`）、專案規則（`AGENTS.md`）、更新紀錄（`CHANGELOG.md`）。

| 閱讀方式 | 問題 |
| :--- | :--- |
| `cat` | 標題、表格、程式碼全擠成一團，很難讀 |
| 編輯器或瀏覽器 | 要切換視窗、拿滑鼠，打斷工作 |
| **Glow** | ✅ 在原本的終端機就能讀到排好版的文件 |

---

## 2. 實戰情境

### 情境 A：檢閱 AI 寫的規格書

AI 寫好 `docs/spec.md` 後，直接閱讀：

```bash
glow -p docs/spec.md
```

表格對齊、程式碼有顏色，逐段確認後按 `q` 離開，再告訴 AI 要修改哪裡。

### 情境 B：AI 的回答太長，來不及看

讓 OpenCode 用指令模式回答，再交給 Glow 分頁閱讀：

```bash
opencode run "請用 Markdown 條列說明這個專案的架構" | glow -p
```

### 情境 C：看某次 commit 的文件長什麼樣子

```bash
git show HEAD~1:README.md | glow -p      # 上上次 commit 的 README
```

---

## 3. 和 Herdr 並排工作

1. 啟動 Herdr，在第一個窗格執行 AI（例如 `opencode`）。
2. 按 `prefix+v` 向右切一個窗格。
3. AI 寫好文件後，在右邊執行 `glow -p 檔名.md` 檢閱。

> Herdr 的操作見 [Herdr 章節](../herdr/README.md)。

---

## ✅ 自我檢查

- [ ] 能用 `glow -p` 檢閱一份 AI 寫的文件
- [ ] 能把其他指令的輸出接到 `| glow -p`

> 下一站：[04 設定與主題 →](04-config.md)
