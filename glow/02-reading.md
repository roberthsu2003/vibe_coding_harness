# 02　四種閱讀方式

> ★ 入門　｜　[← 01 安裝](01-install.md)　｜　[章節首頁](README.md)　｜　下一站：[03 搭配 AI 與 Herdr →](03-ai-workflow.md)

**這一站你會學到**：依情況選擇最適合的閱讀方式，以及分頁模式的按鍵。

---

## 1. 四種方式一覽

![Glow 的四種閱讀方式](assets/glow-modes.svg)

| 方式 | 指令 | 什麼時候用 |
| :--- | :--- | :--- |
| **A 分頁閱讀**（推薦） | `glow -p 檔名.md` | 長文件，一頁一頁慢慢讀 |
| **B 直接印出** | `glow 檔名.md` | 短文件，快速確認內容 |
| **C 瀏覽專案** | `glow` | 不知道文件在哪，讓 Glow 幫你找出所有 Markdown |
| **D 讀網址** | `glow github.com/使用者/專案` | 直接讀 GitHub 專案的 README |

### 也可以接收其他指令的輸出

Glow 可以讀「別的指令印出來的 Markdown」，在後面加上 `| glow -p` 就好：

```bash
git show HEAD:README.md | glow -p      # 看上一次 commit 時的 README 長什麼樣子
```

---

## 2. 分頁模式的按鍵

| 按鍵 | 功能 |
| :--- | :--- |
| `j` / `k`（`↓` / `↑`） | 往下 / 往上一行 |
| `Space`、`f` / `b` | 往下 / 往上一整頁 |
| `d` / `u` | 往下 / 往上半頁 |
| `g` / `⇧G` | 跳到開頭 / 結尾 |
| `?` | 顯示按鍵說明 |
| **`q`** | **離開** |

## 3. 瀏覽專案模式（`glow`）的按鍵

| 按鍵 | 功能 |
| :--- | :--- |
| `j` / `k` | 選擇文件 |
| `Enter` | 開啟文件 |
| `/` | 依檔名搜尋 |
| `Esc` | 返回清單 |
| `q` | 離開 |

---

## ✅ 動手練習

1. 在本專案資料夾執行 `glow`，找到 `herdr/README.md` 並開啟。
2. 用 `glow -p yazi/README.md` 閱讀，試試 `Space`、`g`、`⇧G`。
3. 執行 `glow github.com/charmbracelet/glow`，讀 Glow 官方的 README。

> 下一站：[03 搭配 AI 與 Herdr →](03-ai-workflow.md)
