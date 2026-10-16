# 05　搭配 AI 與 Herdr

> ★★★ 深入　｜　[← 04 搜尋與跳轉](04-search.md)　｜　[章節首頁](README.md)　｜　下一站：[06 離開時切換目錄 →](06-cwd-on-exit.md)

**這一站你會學到**：讓 AI 寫程式時，用 Yazi 在旁邊即時查看成果、把檔案路徑交給 AI。

---

## 1. 為什麼 AI 開發需要 Yazi？

| 需求 | 沒有 Yazi 時 | 有 Yazi 時 |
| :--- | :--- | :--- |
| **看 AI 改了什麼** | 切到編輯器或 Finder，打斷思路 | 旁邊的窗格游標掃過去，右欄直接預覽 |
| **告訴 AI 要改哪個檔案** | 手打長長的路徑，容易打錯 | `c` `c` 複製完整路徑，貼進提示 |
| **找隱藏的設定檔** | 圖形介面常把 `.env`、`.worktrees/` 藏起來 | 按 `.` 立刻顯示 |

---

## 2. 和 Herdr 並排工作

![Herdr 中 AI 與 Yazi 並排](assets/herdr-yazi-workflow.svg)

1. 在專案資料夾啟動 Herdr：`herdr`。
2. 在第一個窗格啟動 AI，例如 `opencode`。
3. 按 `prefix+v`（`Ctrl+B` 放開再按 `v`）向右切一個窗格。
4. 在右邊的窗格執行 `yazi`。
5. 左邊交代 AI 工作，右邊隨時看檔案；用 `prefix+h` / `prefix+l` 在左右窗格之間切換。

> Herdr 的操作見 [Herdr 章節](../herdr/README.md)。

---

## 3. 實戰情境

### 情境 A：驗收 AI 剛改好的檔案

AI 說它改了 5 個檔案。切到 Yazi 窗格，用 `j` / `k` 掃過那些檔案，右欄就是最新內容。Yazi 會自動偵測檔案變動，不用重新整理。

### 情境 B：把檔案路徑交給 AI

在 Yazi 把游標移到檔案上，按 `c` `c`；切回 AI 窗格，貼上並接著打字：

```text
請幫我在 /Users/me/app/src/api/auth.py 加上錯誤處理
```

### 情境 C：找不到 `.env` 或 `.worktrees/`

按 `.` 顯示隱藏檔。在 Git worktree 開發時，用這招進入 `.worktrees/` 查看各分支的成果（見 [Git 與 Worktree 章節](../git/README.md)）。

---

## ✅ 自我檢查

- [ ] 能在 Herdr 做出「左邊 AI、右邊 Yazi」的版面
- [ ] 能用 `c` `c` 複製路徑並貼給 AI
- [ ] 能用 `.` 找到隱藏的設定檔

> 下一站：[06 離開時切換目錄 →](06-cwd-on-exit.md)
