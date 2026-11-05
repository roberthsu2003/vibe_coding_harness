# 03　合併與衝突

> ★★ 進階　｜　[← 02 Branch 基本流程](02-branch-basics.md)　｜　[章節首頁](README.md)　｜　下一站：[04 為什麼需要 Worktree →](04-why-worktree.md)

**這一站你會學到**：怎麼安全地合併、遇到衝突怎麼處理，以及合併完才後悔怎麼辦。

---

## 1. 安全地合併

**自己打指令**

```bash
git switch main                                      # 1. 切到 main
git status                                           # 2. 應該沒有未提交的改動
git pull                                             # 3. （有遠端時）先更新 main
git log main..feature/supervised-learning --oneline  # 4. 預覽分支比 main 多了哪些 commit
git merge feature/supervised-learning                # 5. 合併
git push                                             # 6. （有遠端時）推送
```

**請 AI 做**

```text
請把 feature/supervised-learning 合併進 main。合併前先確認我在 main 上、沒有未提交的改動，並告訴我會多出哪些 commit，等我同意再合併。
```

> [!NOTE]
> **`git merge` 之後跳出編輯器？這不是當機。** main 和分支各有新 commit 時，Git 會請你確認合併訊息，直接存檔離開就好：
> - **nano**（畫面下方有 `^X Exit`）：按 `Ctrl+X`
> - **Vim**：輸入 `:wq`，按 `Enter`
>
> 不想看到編輯器：`git merge --no-edit feature/supervised-learning`。

## 2. 合併的兩種結果

| 結果 | 英文介面 | 中文介面 | 接下來 |
| :--- | :--- | :--- | :--- |
| ✅ 順利合併 | `Fast-forward`，或 `Merge made by the 'ort' strategy.` | 相同 | 完成，可以刪除分支 |
| ⚠️ 發生衝突 | `CONFLICT (content): Merge conflict in 檔名` | `衝突（內容）：合併衝突於 檔名` | 照下面的步驟處理 |

---

## 3. 為什麼會衝突？

> 講義裡過擬合的定義只寫了「模型學得太細」。老師說：「要講原因，也要講現象。」你各開一條分支來改：
>
> - `fix/overfit-cause`：改成「模型連雜訊也學了進去」
> - `fix/overfit-symptom`：改成「訓練資料表現好，新資料表現差」

兩條分支都改了同一行定義。第一條順利合併後，第二條合併時 Git 不知道要留哪個版本，就會停下來問你：

```text
<<<<<<< HEAD
過擬合：模型連雜訊也學了進去。
=======
過擬合：訓練資料表現好，新資料表現差。
>>>>>>> fix/overfit-symptom
```

| 標記 | 意思 |
| :--- | :--- |
| `<<<<<<< HEAD` | 開始：目前分支（main）的版本 |
| `=======` | 分隔線 |
| `>>>>>>> fix/overfit-symptom` | 結束：要合併進來的分支的版本 |

衝突不代表出錯了，只是有一個決定要由人來做。這很常見，不用怕。

---

## 4. 處理衝突

![合併衝突的處理方式](assets/git-merge-conflict.svg)

### 先看懂衝突

**自己打指令**

```bash
git status                  # both modified（雙方修改）的就是衝突的檔案
cat terms/overfitting.md    # 看衝突的內容
```

**請 AI 做**

```text
目前的合併發生衝突。請告訴我衝突在哪裡、兩邊各改了什麼，先不要修改檔案。
```

### 決定內容並完成合併

這句定義該怎麼寫，要由讀過課本的你決定。

**自己打指令**

```bash
nano terms/overfitting.md   # 留下正確的內容，並刪掉三行標記
git add terms/overfitting.md            # 標記為已解決
git commit -m "merge: 合併 fix/overfit-symptom"   # 完成合併
```

**請 AI 做**

```text
原因和現象都要留。定義請改成：「過擬合：模型連雜訊也學了進去，所以訓練資料表現好，新資料表現差。」改完先讓我看結果，我確認後再完成合併。
```

如果兩邊改的內容互不相關，例如兩條分支都在目錄最後加了一行不同的名詞，兩行都留下就好。請 AI 做時可以這樣說：

```text
請幫我解決目前的合併衝突，保留兩邊的內容。改完先讓我看結果，我確認後再完成合併。
```

### 想放棄這次合併

**自己打指令**

```bash
git merge --abort   # 回到合併前的狀態
```

**請 AI 做**

```text
請放棄這次合併，回到合併前的狀態。
```

---

## 5. 先把 main 同步進分支

> 監督式學習的講義還在寫，main 卻已經更新了過擬合的定義和講義目錄。你希望先確定兩邊放在一起沒問題，再正式合併。

切到還在撰寫的分支，再執行：

**自己打指令**

```bash
git switch feature/supervised-learning   # 切到撰寫中的分支
git merge main                           # 把 main 合併進來
```

**請 AI 做**

```text
請把最新的 main 合併進這條分支。如果有衝突先告訴我，解決後確認目錄的連結都正確。
```

衝突在分支上就處理完了，main 全程保持乾淨。接著再把分支合併回 main，就不會遇到同樣的衝突。

---

## 6. 合併完才發現不對

> 剛合併完過擬合的新定義，老師說：「等一下，雜訊那段說法還要再確認。」

| 情況 | 做法 | 結果 |
| :--- | :--- | :--- |
| **還沒 push** | 把 main 退回合併前 | 就像沒合併過，分支還在，修好後可以再合併 |
| **已經 push** | 用一個新的 commit 抵銷這次合併 | 歷史會多一筆「Revert」紀錄，別人不受影響 |

**自己打指令**

```bash
# 還沒 push：退回合併前。要在合併後馬上執行，中間不要做其他合併或 reset
git reset --merge ORIG_HEAD

# 已經 push：新增一個抵銷的 commit
git revert -m 1 HEAD
git push
```

> `-m 1` 用在有產生合併 commit 的情況。如果當時是 `Fast-forward`，就沒有合併 commit，要先用 `git log` 找出要抵銷的 commit，再執行 `git revert <commit 編號>`。

**請 AI 做**

```text
我想復原剛才那次合併。請先告訴我這次合併有沒有 push 過，再用適合的方式復原，復原前讓我確認。
```

> [!WARNING]
> **已經抵銷（revert）過的合併，不能直接再合併一次。** Git 會顯示 `Already up to date`（已經是最新的），改動不會回來。要先請 AI 處理：「我之前 revert 過這次合併，現在要重新把它合併回來。」

---

## ✅ 動手練習

回到 [02 站](02-branch-basics.md#-動手練習)的 `ml-notes` 資料夾，親手製造一次衝突。

### 第 1 步：開兩條分支，改同一行

**自己打指令**

```bash
git switch -c fix/overfit-cause
echo '過擬合：模型連雜訊也學了進去。' > terms/overfitting.md
git add .
git commit -m "fix: 補上過擬合的原因"

git switch main
git switch -c fix/overfit-symptom
echo '過擬合：訓練資料表現好，新資料表現差。' > terms/overfitting.md
git add .
git commit -m "fix: 補上過擬合的現象"

git switch main
```

**請 AI 做**

```text
請從 main 開兩條分支。fix/overfit-cause 把 terms/overfitting.md 的內容改成「過擬合：模型連雜訊也學了進去。」並 commit；fix/overfit-symptom 把同一個檔案的內容改成「過擬合：訓練資料表現好，新資料表現差。」並 commit。先不要合併。
```

### 第 2 步：合併第一條

應該會順利完成，顯示 `Fast-forward`。

**自己打指令**

```bash
git merge fix/overfit-cause
```

**請 AI 做**

```text
請把 fix/overfit-cause 合併進 main。
```

### 第 3 步：合併第二條，遇到衝突

這裡會出現 `CONFLICT`，這是預期中的結果。

**自己打指令**

```bash
git merge fix/overfit-symptom
git status
cat terms/overfitting.md
```

**請 AI 做**

```text
請把 fix/overfit-symptom 也合併進 main。如果有衝突先不要解決，把衝突內容給我看。
```

### 第 4 步：解決衝突

**自己打指令**

```bash
echo '過擬合：模型連雜訊也學了進去，所以訓練資料表現好，新資料表現差。' > terms/overfitting.md
git add terms/overfitting.md
git commit -m "merge: 合併 fix/overfit-symptom"
```

> 這裡為了方便，直接覆蓋整個檔案。檔案內容比較多時，要用編輯器打開，只修改衝突的段落。

**請 AI 做**

```text
定義請改成「過擬合：模型連雜訊也學了進去，所以訓練資料表現好，新資料表現差。」請解決衝突並完成合併。
```

### 第 5 步：刪除分支，看看歷史

**自己打指令**

```bash
git branch -d fix/overfit-cause fix/overfit-symptom
git log --oneline --graph --all
```

**請 AI 做**

```text
請刪除這兩條已經合併的分支，並用圖形顯示 commit 歷史。
```

---

## ✅ 自我檢查

- [ ] 能看懂 `<<<<<<<`、`=======`、`>>>>>>>` 各代表什麼
- [ ] 能自己用指令解決一次衝突
- [ ] 知道解決衝突時，為什麼要由自己決定正確內容
- [ ] 能分辨 `git merge --abort`（合併途中放棄）和 `git reset --merge`／`git revert`（已經合併完才復原）

> 下一站：[04 為什麼需要 Worktree →](04-why-worktree.md)
