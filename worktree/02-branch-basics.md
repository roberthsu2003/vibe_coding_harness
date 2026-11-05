# 02　Branch 基本流程

> ★ 入門　｜　[← 01 為什麼需要 Branch](01-why-branch.md)　｜　[章節首頁](README.md)　｜　下一站：[03 合併與衝突 →](03-merge-conflict.md)

**這一站你會學到**：分支從建立到刪除的 5 個步驟、怎麼丟掉失敗的實驗，以及切換分支前為什麼要先 commit。

---

## 1. 完整流程：新增監督式學習講義

> 老師：「下週要教監督式學習。」

下面每一句都是對 AI 說的。

### 步驟 1：建立分支

```text
我要新增監督式學習的講義。請先確認 main 沒有未提交的改動，再從 main 開一條分支 feature/supervised-learning，並切換過去。
```

### 步驟 2：讓 AI 撰寫

```text
請新增 terms/supervised-learning.md，說明「監督式學習」，包含定義、白話比喻和一個例子，並把它加進 README.md 的目錄。
```

### 步驟 3：驗收並提交

```text
請列出你改了哪些檔案，說明每個改動，確認沒問題後先不要 commit，等我看過內容。
```

**自己讀一遍。** AI 可能把專有名詞解釋錯，請對照課本或投影片。想在終端機裡看排版，可以用 [Glow](../glow/README.md)。確認沒問題後說：

```text
內容沒問題，請 commit。
```

**親眼看看分支的效果。** 對 AI 說：

```text
請切回 main，列出 terms 資料夾的檔案，再切回 feature/supervised-learning 列出一次。
```

在 main 上看不到 `supervised-learning.md`，回到分支它又出現了。檔案沒有消失，只是屬於另一條分支。

### 步驟 4：合併回 main

內容確認過，可以放進正式講義了：

```text
請切回 main，把 feature/supervised-learning 合併進來。合併前先告訴我會多出哪些 commit，等我同意再合併。
```

### 步驟 5：刪除分支

```text
請刪除已經合併的 feature/supervised-learning 分支，然後列出剩下的分支。
```

> 刪掉分支不會刪掉成果。講義已經合併進 main，分支只是功成身退。

---

## 2. 實驗失敗了？整條丟掉

> 同學說問答式的講義比較好背，你想試試看。

```text
請從 main 開一條分支 experiment/qa-format，把 terms/overfitting.md 改成問答式，然後 commit。
```

讀完覺得太零碎，定義反而看不清楚：

```text
這條分支不要了。請切回 main，列出 experiment/qa-format 上還沒合併的 commit，等我確認後再刪除。
```

這條分支沒有合併過，Git 一開始會拒絕刪除，並顯示 `not fully merged`（沒有完全合併）。AI 要改用強制刪除才刪得掉。

> [!WARNING]
> 只有**確定整條都不要**時才能強制刪除。不確定的話就先留著，留一條分支幾乎不佔空間。

---

## 3. 切換分支前，先 commit

> 你請 AI 補充過擬合的例子，改到一半，老師又要你先處理別的名詞。這時直接切換分支會發生什麼事？

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

## 5. 把分支備份到 GitHub（選修）

> `ml-notes` 目前只在你的電腦上，本章的練習不需要 GitHub。如果之後想換電腦繼續寫，或和同學共用，才需要這一節。

Commit 只存在你的電腦上，要 push 才會上傳：

```text
請把 feature/supervised-learning push 到 GitHub。
```

合併並刪除分支後，GitHub 上的那條分支還在，要另外刪：

```text
請把 main push 上去，再刪除 GitHub 上的 feature/supervised-learning 分支。
```

---

## ✅ 動手練習

開一個專用的資料夾 `ml-notes`，在裡面啟動 AI，依序說：

1. 「請把這個資料夾變成 Git 專案，主分支叫 main。建立 `terms/overfitting.md`，內容只有一行：『過擬合：模型學得太細。』建立 `terms/accuracy.md`，內容只有一行：『準確率 = 預測為正且正確的筆數 ÷ 預測為正的筆數』。再建立 `README.md` 當講義目錄，連到這兩個檔案。然後做第一次 commit。」
2. 「請開一條分支 `feature/supervised-learning`，新增 `terms/supervised-learning.md`，說明監督式學習，包含定義、白話比喻和一個例子，並加進目錄，然後 commit。」
3. 「請切回 main，列出 `terms` 資料夾的檔案。」確認看不到 `supervised-learning.md`。
4. 「請把 `feature/supervised-learning` 合併進 main，再刪除這條分支。」
5. 「請開一條分支 `experiment/qa-format`，把 `terms/overfitting.md` 改成問答式並 commit。」
6. 「這條分支不要了。請切回 main，列出還沒合併的 commit，等我確認後刪除。」
7. 「請列出所有分支，並顯示 `terms/overfitting.md` 的內容。」應該只剩 main，內容也還是原本那一行。

> `過擬合` 那句定義故意寫得不夠完整，`準確率` 的公式也藏了一個錯誤（其實是精確率的公式）。請先照抄，下一站和第 07 站會修正它們。

**這個資料夾請留著，接下來幾站都會用到。**

---

## ✅ 自我檢查

- [ ] 能說出分支的 5 個步驟
- [ ] 知道切回 main 後看不到新講義是正常的
- [ ] 知道為什麼刪除沒合併的分支要特別小心
- [ ] 知道切換分支前要先處理還沒 commit 的改動

---

## 進階（選修）：自己打指令

```bash
# 1. 建立並切換
git switch main
git status                        # 確認沒有未提交的改動
git switch -c feature/supervised-learning

# 2～3. 撰寫後驗收並提交
git status
git diff
git add .
git commit -m "docs: 新增監督式學習講義"

# 4. 合併
git switch main
git log main..feature/supervised-learning --oneline   # 預覽會多出哪些 commit
git merge feature/supervised-learning

# 5. 刪除
git branch -d feature/supervised-learning
git branch                        # 列出分支，* 是目前所在的分支
```

**丟掉實驗分支：**

```bash
git switch main
git log main..experiment/qa-format --oneline   # 先看會丟掉什麼
git branch -d experiment/qa-format             # 沒合併過，這一行會被擋下
git branch -D experiment/qa-format             # 確定不要了才用 -D（強制）
```

**備份到 GitHub：**

```bash
git push -u origin feature/supervised-learning        # 第一次 push 這條分支
git push origin --delete feature/supervised-learning  # 刪除 GitHub 上的分支
```

> 舊教材常見的 `git checkout` 也能切換分支，`git switch` 是專門用來切換分支的指令，比較不容易用錯。

> 下一站：[03 合併與衝突 →](03-merge-conflict.md)
