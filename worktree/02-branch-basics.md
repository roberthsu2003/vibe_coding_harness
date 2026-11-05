# 02　Branch 基本流程

> ★ 入門　｜　[← 01 為什麼需要 Branch](01-why-branch.md)　｜　[章節首頁](README.md)　｜　下一站：[03 合併與衝突 →](03-merge-conflict.md)

**這一站你會學到**：分支從建立到刪除的 5 個步驟、怎麼丟掉失敗的實驗，以及切換分支前為什麼要先 commit。

---

## 1. 完整流程：幫小豆咖啡加菜單頁

> 老闆：「週末想讓客人看到菜單，幫我加一頁。」

下面每一句都是對 AI 說的。

### 步驟 1：建立分支

```text
我要幫網站加菜單頁。請先確認 main 沒有未提交的改動，再從 main 開一條分支 feature/menu，並切換過去。
```

### 步驟 2：讓 AI 開發

```text
請新增菜單頁 menu.html，列出三種咖啡和價格，並在首頁放一個連到菜單的連結。
```

### 步驟 3：驗收並提交

```text
請列出你改了哪些檔案，說明每個改動，確認沒問題後 commit。
```

**親眼看看分支的效果。** 對 AI 說：

```text
請切回 main，列出目前資料夾的檔案，再切回 feature/menu 列出一次。
```

在 main 上看不到 `menu.html`，回到 `feature/menu` 它又出現了。檔案沒有消失，只是屬於另一條分支。

### 步驟 4：合併回 main

老闆看過，覺得可以上線：

```text
請切回 main，把 feature/menu 合併進來。合併前先告訴我會多出哪些 commit，等我同意再合併。
```

### 步驟 5：刪除分支

```text
請刪除已經合併的 feature/menu 分支，然後列出剩下的分支。
```

> 刪掉分支不會刪掉成果。菜單頁已經合併進 main，分支只是功成身退。

---

## 2. 實驗失敗了？整條丟掉

> 老闆聽朋友說深色主題很流行，想試試看。

```text
請從 main 開一條分支 experiment/dark-theme，把網站改成深色主題，然後 commit。
```

老闆看完皺眉：「太暗了，還是原本的好。」

```text
這條分支不要了。請切回 main，列出 experiment/dark-theme 上還沒合併的 commit，等我確認後再刪除。
```

這條分支沒有合併過，Git 一開始會拒絕刪除，並顯示 `not fully merged`（沒有完全合併）。AI 要改用強制刪除才刪得掉。

> [!WARNING]
> 只有**確定整條都不要**時才能強制刪除。不確定的話就先留著，留一條分支幾乎不佔空間。

---

## 3. 切換分支前，先 commit

> 你請 AI 改首頁標語，改到一半，老闆又說要改別的。這時直接切換分支會發生什麼事？

| 目前的狀態 | 切換分支時會發生什麼 |
| :--- | :--- |
| ✅ 改動已經 commit | 改動安全地留在原本的分支 |
| ⚠️ 還沒 commit，切換時不會互相影響 | 切換成功，但**改動會跟著你到另一條分支**，很容易以為改錯地方 |
| 🛑 還沒 commit，切換時會被覆蓋 | Git 拒絕切換，提醒你先處理這些改動 |

所以交代 AI 切換前，先說這句：

```text
請先告訴我現在在哪條分支、有沒有還沒 commit 的改動。有的話先問我要怎麼處理，不要直接切換。
```

---

## 4. 讓 AI 記住這個習慣

每次都提醒 AI 很麻煩，可以把規則寫進專案的 `AGENTS.md`，OpenCode 開始工作時會讀這個檔案：

```text
請在 AGENTS.md 加一條規則：開始修改檔案前，先確認目前的分支；如果在 main 上，先問我要不要開新分支。然後 commit。
```

> 規則能降低出錯的機率，但不是保證。AI 還是改到 main 上的話，見[情境 A](07-scenarios.md#情境-aai-直接改在-main-上)。

---

## 5. 把分支備份到 GitHub（有遠端時）

> 週末你要帶另一台電腦到店裡，繼續做到一半的功能。

Commit 只存在你的電腦上，要 push 才會上傳：

```text
請把 feature/menu push 到 GitHub。
```

合併並刪除分支後，GitHub 上的那條分支還在，要另外刪：

```text
請把 main push 上去，再刪除 GitHub 上的 feature/menu 分支。
```

---

## ✅ 動手練習

在一個新的空資料夾（例如 `xiaodou-cafe`）裡啟動 AI，依序說：

1. 「請把這個資料夾變成 Git 專案，主分支叫 main。建立 `index.html`，內容是『小豆咖啡』的標題和一行營業時間 08:00-18:00，然後做第一次 commit。」
2. 「請開一條分支 `feature/menu`，新增菜單頁 `menu.html` 並從首頁連過去，然後 commit。」
3. 「請切回 main，列出檔案。」確認看不到 `menu.html`。
4. 「請把 `feature/menu` 合併進 main，再刪除這條分支。」
5. 「請開一條分支 `experiment/dark-theme`，改成深色主題並 commit。」
6. 「這條分支不要了。請切回 main，列出還沒合併的 commit，等我確認後刪除。」
7. 「請列出所有分支，並告訴我 `index.html` 有沒有深色主題。」應該只剩 main，也沒有深色主題。

**這個資料夾請留著，下一站和第 06 站還會用到。**

---

## ✅ 自我檢查

- [ ] 能說出分支的 5 個步驟
- [ ] 知道切回 main 後看不到 `menu.html` 是正常的
- [ ] 知道為什麼刪除沒合併的分支要特別小心
- [ ] 知道切換分支前要先處理還沒 commit 的改動

---

## 進階（選修）：自己打指令

```bash
# 1. 建立並切換
git switch main
git status                        # 確認沒有未提交的改動
git switch -c feature/menu

# 2～3. 開發後驗收並提交
git status
git diff
git add .
git commit -m "feat: 新增菜單頁"

# 4. 合併
git switch main
git log main..feature/menu --oneline   # 預覽會多出哪些 commit
git merge feature/menu

# 5. 刪除
git branch -d feature/menu
git branch                        # 列出分支，* 是目前所在的分支
```

**丟掉實驗分支：**

```bash
git switch main
git log main..experiment/dark-theme --oneline   # 先看會丟掉什麼
git branch -d experiment/dark-theme             # 沒合併過，這一行會被擋下
git branch -D experiment/dark-theme             # 確定不要了才用 -D（強制）
```

**備份到 GitHub：**

```bash
git push -u origin feature/menu    # 第一次 push 這條分支
git push origin --delete feature/menu   # 刪除 GitHub 上的分支
```

> 舊教材常見的 `git checkout` 也能切換分支，`git switch` 是專門用來切換分支的指令，比較不容易用錯。

> 下一站：[03 合併與衝突 →](03-merge-conflict.md)
