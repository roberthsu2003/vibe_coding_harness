# 02　Branch 基本流程

> ★ 入門　｜　[← 01 為什麼需要 Branch](01-why-branch.md)　｜　[章節首頁](README.md)　｜　下一站：[03 合併與衝突 →](03-merge-conflict.md)

**這一站你會學到**：分支從建立到刪除的 5 個步驟、怎麼丟掉失敗的實驗，以及切換分支前為什麼要先 commit。

> [!NOTE]
> **從這一站開始，請在 `ml-notes` 裡一步一步跟著做。** 每個動作只會出現一次，下一步都接著上一步的結果。內容請 AI 寫，Git 指令先自己打一遍。還沒準備資料夾的話，請先完成[開始之前](README.md#開始之前準備-ml-notes-資料夾)的步驟。

---

## 1. 完整流程：新增監督式學習講義

> 老師：「下週要教監督式學習。」

### 步驟 1：建立分支

**自己打指令**

```bash
git switch main                             # 切到 main
git status                                  # 確認沒有未提交的改動
git switch -c feature/supervised-learning   # 建立分支並切換過去
```

**請 AI 做**

```text
我要新增監督式學習的講義。請先確認 main 沒有未提交的改動，再從 main 開一條分支 feature/supervised-learning，並切換過去。
```

### 步驟 2：撰寫講義

**請 AI 寫**

```text
請新增 terms/supervised-learning.md，說明「監督式學習」，格式和現有的講義一樣，並把它加進 README.md 的索引。先不要 commit。
```

### 步驟 3：驗收並提交

**自己打指令**

```bash
git status                # 看改了哪些檔案
git add .                 # 把改動放進暫存區
git diff --staged         # 看暫存區的內容，按 q 離開
git commit -m "docs: 新增監督式學習講義"
```

**請 AI 做**

```text
請列出你改了哪些檔案，說明每個改動，確認沒問題後先不要 commit，等我看過內容。
```

讀完內容，確認沒問題後再說：

```text
內容沒問題，請 commit。
```

> [!IMPORTANT]
> **AI 寫的內容一定要讀一遍。** AI 可能把專有名詞解釋錯，請對照課本或投影片，確認自己能用自己的話說明這個名詞。想在終端機裡看排版，可以用 [Glow](../glow/README.md)。

**親眼看看分支的效果。**

**自己打指令**

```bash
git switch main                            # 切回 main
ls terms                                   # 看不到 supervised-learning.md
git switch feature/supervised-learning     # 切回分支
ls terms                                   # 又看得到了
```

**請 AI 做**

```text
請切回 main，列出 terms 資料夾的檔案，再切回 feature/supervised-learning 列出一次。
```

檔案沒有消失，只是屬於另一條分支。

### 步驟 4：合併回 main

**自己打指令**

```bash
git switch main                                       # 要合併進哪一條，就先切到哪一條
git log main..feature/supervised-learning --oneline   # 預覽會多出哪些 commit
git merge feature/supervised-learning                 # 合併
```

**請 AI 做**

```text
請切回 main，把 feature/supervised-learning 合併進來。合併前先告訴我會多出哪些 commit，等我同意再合併。
```

### 步驟 5：刪除分支

**自己打指令**

```bash
git branch -d feature/supervised-learning   # 刪除已合併的分支
git branch                                  # 列出分支，* 是目前所在的分支
```

**請 AI 做**

```text
請刪除已經合併的 feature/supervised-learning 分支，然後列出剩下的分支。
```

> 刪掉分支不會刪掉成果。講義已經合併進 main，分支只是功成身退。

---

## 2. 實驗失敗了？整條丟掉

> 同學說問答式的講義比較好背，你想試試看。

先開一條實驗分支：

**自己打指令**

```bash
git switch -c experiment/qa-format
```

**請 AI 做**

```text
請從 main 開一條分支 experiment/qa-format，並切換過去。
```

再請 AI 改寫：

**請 AI 寫**

```text
請把 terms/overfitting.md 改成問答式。先不要 commit。
```

把這次實驗提交到分支上：

**自己打指令**

```bash
git add .
git commit -m "docs: 試做問答式講義"
```

**請 AI 做**

```text
請把這次的改動 commit，訊息是「docs: 試做問答式講義」。
```

讀完覺得太零碎，定義反而看不清楚，決定不要了：

**自己打指令**

```bash
git switch main
git log main..experiment/qa-format --oneline   # 先看會丟掉什麼
git branch -d experiment/qa-format             # 沒合併過，這一行會被擋下
git branch -D experiment/qa-format             # 確定不要了才用 -D（強制刪除）
```

**請 AI 做**

```text
這條分支不要了。請切回 main，列出 experiment/qa-format 上還沒合併的 commit，等我確認後再刪除。
```

這條分支沒有合併過，所以 `-d` 會被拒絕，並顯示 `not fully merged`（沒有完全合併）。

> [!WARNING]
> 只有**確定整條都不要**時才能用 `-D`。不確定的話就先留著，留一條分支幾乎不佔空間。

確認結果：應該只剩 main，過擬合的講義也回到原本的格式，定義還是「模型學得太細。」

**自己打指令**

```bash
git branch
cat terms/overfitting.md
```

**請 AI 做**

```text
請列出所有分支，並顯示 terms/overfitting.md 的內容。
```

---

## 3. 切換分支前，先 commit

> 你在補充過擬合的例子，改到一半，老師又要你先處理別的名詞。這時直接切換分支會發生什麼事？

| 目前的狀態 | 切換分支時會發生什麼 |
| :--- | :--- |
| ✅ 改動已經 commit | 改動安全地留在原本的分支 |
| ⚠️ 還沒 commit，切換時不會互相影響 | 切換成功，但**改動會跟著你到另一條分支**，很容易以為改錯地方 |
| 🛑 還沒 commit，切換時會被覆蓋 | Git 拒絕切換，提醒你先處理這些改動 |

這一節不用改檔案，只要記住這個習慣。切換前，先確認目前的狀態：

**自己打指令**

```bash
git branch --show-current   # 現在在哪條分支
git status                  # 有沒有還沒 commit 的改動
```

**請 AI 做**

```text
請先告訴我現在在哪條分支、有沒有還沒 commit 的改動。有的話先問我要怎麼處理，不要直接切換。
```

---

## 4. 讓 AI 記住這個習慣

每次都提醒 AI 很麻煩，可以把規則寫進專案的規則檔，AI 工具開始工作時會讀這個檔案。本章以 `AGENTS.md` 為例；如果你的工具讀的是其他檔名，請把下面的檔名換掉。這也是請 AI 修改內容，所以一樣先開分支。

**自己打指令**

```bash
git switch -c feature/ai-rules
```

**請 AI 做**

```text
請從 main 開一條分支 feature/ai-rules，並切換過去。
```

接著請 AI 寫規則：

**請 AI 寫**

```text
請在 AGENTS.md 加兩條規則：開始修改檔案前，先確認目前的分支；如果在 main 上，先問我要不要開新分支。新增講義時，要同步更新 README.md 的索引。先不要 commit。
```

確認規則寫對了，再提交並合併：

**自己打指令**

```bash
git add AGENTS.md
git commit -m "docs: 新增 AI 工作規則"
git switch main
git merge feature/ai-rules
git branch -d feature/ai-rules
```

**請 AI 做**

```text
請把 AGENTS.md commit，訊息是「docs: 新增 AI 工作規則」。然後切回 main，把 feature/ai-rules 合併進來，再刪除這條分支。
```

之後 AI 在 main 上被要求修改檔案時，可能會先問你要不要開分支，這就是規則生效了。

> 規則能降低出錯的機率，但不是保證。AI 還是改到 main 上的話，見[情境 A](07-scenarios.md#情境-aai-直接改在-main-上)。

---

## 5. 把分支備份到 GitHub（選修）

> `ml-notes` 目前只在你的電腦上，本章不需要 GitHub，**這一節先看就好，不用執行**。之後想換電腦繼續寫，或和同學共用，才需要這些指令。專案要先連上 GitHub 的遠端才能 push。

Commit 只存在你的電腦上，要 push 才會上傳。下面的 `<分支名稱>` 請換成你正在做的分支。

**自己打指令**（這次不用執行）

```bash
git push -u origin <分支名稱>   # 第一次 push 這條分支
```

**請 AI 做**

```text
請把目前這條分支 push 到 GitHub。
```

合併並刪除分支後，GitHub 上的那條分支還在，要另外刪。

**自己打指令**（這次不用執行）

```bash
git switch main
git push                               # 上傳 main
git push origin --delete <分支名稱>     # 刪除 GitHub 上的分支
```

**請 AI 做**

```text
請把 main push 上去，再刪除 GitHub 上已經合併的那條分支。
```

---

## ✅ 自我檢查

- [ ] 能不看教材打出分支的 5 個步驟
- [ ] 知道 `git switch` 和 `git switch -c` 的差別
- [ ] 知道 `-d` 和 `-D` 的差別，以及為什麼 `-D` 要特別小心
- [ ] 知道切回 main 後看不到新講義是正常的
- [ ] 知道切換分支前要先處理還沒 commit 的改動
- [ ] 能用自己的話說明什麼是監督式學習

> 📍 **目前進度**：只有 `main` 一條分支。`terms` 裡有 `accuracy.md`、`overfitting.md`、`supervised-learning.md`，專案裡多了 `AGENTS.md`。**這個資料夾請留著，接下來幾站都會用到。**

> 舊教材常見的 `git checkout` 也能切換分支，`git switch` 是專門用來切換分支的指令，比較不容易用錯。

> 下一站：[03 合併與衝突 →](03-merge-conflict.md)
