# 06　Worktree 完整流程

> ★★ 進階　｜　[← 05 目錄與原理](05-worktree-structure.md)　｜　[章節首頁](README.md)　｜　下一站：[07 實戰情境 →](07-scenarios.md)

**這一站你會學到**：Worktree 從建立、多工開發到清理的完整標準流程，並學會輕鬆管理多個 AI 同時工作的視窗。

> 接續 [05 站](05-worktree-structure.md)的 `ml-notes`。目前專案只有 `main` 一條分支。

---

## 💡 先看懂這一切：3 個視窗與分工

很多人覺得 Worktree 很亂，是因為**視窗跳來跳去搞混了**。

這一站我們會開 **3 個終端機視窗**（如果使用 [Herdr](../herdr/README.md) 就是切成 3 個窗格）。只要記住各自的角色，流程就會非常清楚：

| 視窗 | 所在資料夾 | 扮演角色 | 負責做什麼 |
| :--- | :--- | :--- | :--- |
| **視窗 1（主管）** | `ml-notes`（母目錄） | **主管** | 發派任務（建立 worktree）、最後合併成果與清理 |
| **視窗 2（AI A）** | `.worktrees/feature-neural-network` | **小幫手 A** | 專心寫「神經網路」講義 |
| **視窗 3（AI B）** | `.worktrees/fix-supervised-example` | **小幫手 B** | 專心改寫「監督式學習」的例子 |

![Worktree 的完整流程](assets/git-worktree-lifecycle.svg)

---

## 步驟 1：主管建立 Worktree（在視窗 1：母目錄）

我們要請主管為兩位小幫手各自開闢獨立的工作資料夾與分支。神經網路需要參考投影片，所以順便把 `references` 複製過去。

**自己打指令**

```bash
# 建立第一個 worktree 與分支，並複製參考投影片
git worktree add .worktrees/feature-neural-network -b feature/neural-network
cp -R references .worktrees/feature-neural-network/

# 建立第二個 worktree 與分支
git worktree add .worktrees/fix-supervised-example -b fix/supervised-example

# 查看目前所有的 worktree
git worktree list
```

**請 AI 做**

對母目錄的 AI 說：

```text
請建立兩個 worktree：
1. 分支 feature/neural-network 放在 .worktrees/feature-neural-network，並把 references 資料夾複製過去
2. 分支 fix/supervised-example 放在 .worktrees/fix-supervised-example
建立完成後列出目前的 worktree 清單。
```

> [!IMPORTANT]
> **為什麼要手動複製 `references`？**
> 被 `.gitignore` 忽略的檔案不會自動帶到新的 worktree。如果沒複製，小幫手 A 就讀不到裡面的投影片。

---

## 步驟 2：兩位 AI 同時開工（在各自的視窗）

現在主管原地待命，兩位小幫手各自在獨立的視窗開始工作。

### 視窗 2：小幫手 A 寫「神經網路」

開一個新視窗，進入它的資料夾並啟動 AI 工具：

```bash
cd .worktrees/feature-neural-network
```

對視窗 2 的 AI 說：

```text
請參考 references/slides.md，新增 terms/neural-network.md 說明「神經網路」。
格式和現有的講義相同（包含定義、白話比喻、例子），並把連結加進 README.md 索引中。先不要 commit。
```

---

### 視窗 3：小幫手 B 改寫「監督式學習」

再開一個新視窗，進入另一個資料夾並啟動 AI 工具：

```bash
cd .worktrees/fix-supervised-example
```

對視窗 3 的 AI 說：

```text
請檢視 terms/supervised-learning.md，把裡面的「例子」改寫得更生活化、更具體。
其他段落與檔案都不要動。先不要 commit。
```

> 兩位小幫手在各自的平行時空改檔案，彼此互不影響，主管的母目錄也乾乾淨淨。

---

## 步驟 3：驗收並提交 Commit（在各自的視窗）

兩邊都寫完後，檢查成果沒問題，就讓它們各自在自己的分支上 commit。

### 視窗 2 提交（小幫手 A）

**自己打指令**

```bash
git status
git diff
git add .
git commit -m "docs: 新增神經網路講義"
```

**請 AI 做**

對視窗 2 的 AI 說：

```text
內容確認沒問題，請把改動 commit，訊息是「docs: 新增神經網路講義」。
```

---

### 視窗 3 提交（小幫手 B）

**自己打指令**

```bash
git status
git diff
git add .
git commit -m "fix: 改寫監督式學習的例子"
```

**請 AI 做**

對視窗 3 的 AI 說：

```text
內容確認沒問題，請把改動 commit，訊息是「fix: 改寫監督式學習的例子」。
```

> [!NOTE]
> 所有的 worktree 都共用母目錄的 Git 資料庫（`.git`），所以這裡 commit 完，主管在母目錄馬上看得到，不需要 push。

---

## 步驟 4：主管收割成果：合併回 main（在視窗 1：母目錄）

回到**視窗 1（母目錄）**，確認自己在 `main` 分支上，開始驗收並合併兩位小幫手的成果。

### 4-1 合併第一個成果（神經網路）

**自己打指令**

```bash
# 預覽會合併進來的 commit
git log main..feature/neural-network --oneline

# 合併進 main
git merge feature/neural-network
```

**請 AI 做**

對母目錄的 AI 說：

```text
請先列出 feature/neural-network 上有哪些新 commit，確認後幫我合併進 main。
```

---

### 4-2 合併第二個成果（改寫例子）

現在 main 已經有了神經網路的新內容。接著把小幫手 B 的改動也合併進來：

**自己打指令**

```bash
git log main..fix/supervised-example --oneline
git merge fix/supervised-example
```

**請 AI 做**

對母目錄的 AI 說：

```text
請把 fix/supervised-example 也合併進 main。
```

> [!TIP]
> **團隊好習慣（進階選修）**：
> 如果第二個任務改動很大，可以在合併前先到**視窗 3**執行 `git merge main`（把最新的 main 帶進分支測試確認沒衝突），確認沒問題再回母目錄合併。

---

## 步驟 5：主管清理收尾（在視窗 1：母目錄）

合併完成後，兩位小幫手的任務就結束了。關閉視窗 2 與視窗 3，由主管在**視窗 1（母目錄）**把臨時工作區與分支清乾淨：

**自己打指令**

```bash
# 移除第一個 worktree 並刪除分支
git worktree remove .worktrees/feature-neural-network
git branch -d feature/neural-network

# 移除第二個 worktree 並刪除分支
git worktree remove .worktrees/fix-supervised-example
git branch -d fix/supervised-example

# 確認只剩下母目錄
git worktree list
```

**請 AI 做**

對母目錄的 AI 說：

```text
任務已全部合併完成。請幫我移除 feature-neural-network 與 fix-supervised-example 這兩個 worktree，並刪除對應的分支，最後確認只剩母目錄。
```

> [!WARNING]
> **重要順序**：一定要先 `git worktree remove`，才能 `git branch -d`。如果順序顛倒，Git 會警告該分支正在被使用而拒絕刪除。

---

## 💡 常見疑惑與實用秘訣

### Q1：我隨時想知道「我現在在哪個 worktree？」

如果你開了太多視窗忘記了：

```bash
# 顯示目前所在資料夾的根目錄
git rev-parse --show-toplevel

# 顯示目前分支
git branch --show-current
```

- 如果路徑結尾是 `.worktrees/...` $\rightarrow$ 你在小幫手的 worktree 裡。
- 如果路徑是專案母目錄 $\rightarrow$ 你在主管的主目錄裡。

### Q2：為什麼在 worktree 裡不能切換到 main？

因為 `main` 分支已經被母目錄佔用了。Git 嚴格規定：**同一條分支不能在兩個地方同時被 checkout**。
這就是為什麼我們規定「**只有主管在母目錄才能操作 main**」，小幫手只能在各自的分支上工作。

---

## ✅ 自我檢查

- [ ] 清楚 Worktree 的 3 個視窗角色分工（主管 vs 小幫手）
- [ ] 能順暢完成標準 5 步驟：**建立 $\rightarrow$ 開發 $\rightarrow$ 提交 $\rightarrow$ 回母目錄合併 $\rightarrow$ 清理**
- [ ] 知道為什麼移除 worktree 要先 remove 再刪分支（`-d`）
- [ ] 知道如何在終端機確認自己目前的資料夾與分支

> 📍 **目前進度**：只有 `main` 一條分支，也只剩母目錄。`terms` 裡有 4 份講義：`accuracy.md`、`neural-network.md`、`overfitting.md`、`supervised-learning.md`。

> 下一站：[07 實戰情境 →](07-scenarios.md)
