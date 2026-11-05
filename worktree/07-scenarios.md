# 07　實戰情境

> ★★★ 深入　｜　[← 06 Worktree 完整流程](06-worktree-lifecycle.md)　｜　[章節首頁](README.md)　｜　📚 [指令速查與疑難排解](reference.md)

**這一站你會學到**：八種用 AI 工作時常見的狀況，以及最省事的處理方式。

| 主題 | 情境 |
| :--- | :--- |
| **Branch** | [A. AI 直接改在 main 上](#情境-aai-直接改在-main-上)　｜　[B. 切換分支被擋下](#情境-b切換分支被擋下)　｜　[C. 刪錯分支](#情境-c刪錯分支) |
| **Worktree** | [D. 緊急修正](#情境-d講義寫到一半突然要緊急修正)　｜　[E. 誤刪 worktree](#情境-e不小心刪掉了-worktree-資料夾)　｜　[F. 新 worktree 少了資料](#情境-f新的-worktree-少了資料)　｜　[H. 搭配 Herdr](#情境-h搭配-herdr同時指揮多個-ai) |
| **兩者都會遇到** | [G. Commit 漏了檔案](#情境-gai-剛-commit-完才發現漏了檔案) |

---

## 情境 A：AI 直接改在 main 上

> 你想新增「交叉驗證」的講義。說完需求才發現忘了開分支，AI 已經直接改在 main 上了。

先看改動有沒有 commit，兩種救法不一樣。

### 還沒 commit

改動還沒有被存進 main，開新分支時會一起帶過去。

**自己打指令**

```bash
git switch -c feature/cross-validation   # 開新分支，改動會跟著過來
git add .
git commit -m "docs: 新增交叉驗證講義"
```

**請 AI 做**

```text
剛才的改動不小心做在 main 上，還沒 commit。請開一條新分支 feature/cross-validation，把這些改動帶過去並 commit，然後確認 main 沒有變動。
```

### 已經 commit、還沒 push

**自己打指令**

```bash
git log --oneline -3                  # 先確認要移動幾個 commit
git branch feature/cross-validation   # 讓新分支指向目前的 commit
git reset --keep HEAD~1               # main 退回 1 個 commit，移動 2 個就改成 HEAD~2
git switch feature/cross-validation   # 切到新分支繼續工作
```

**請 AI 做**

```text
剛才的 commit 不小心做在 main 上，還沒 push。請把它移到一條新分支 feature/cross-validation，讓 main 回到改動之前。動手前先告訴我會移動哪些 commit，等我同意。
```

> [!WARNING]
> **已經 push 了，就不要退回 main**，否則會和 GitHub 上的版本對不起來。請改用新的 commit 抵銷，做法和[復原已 push 的合併](03-merge-conflict.md#6-合併完才發現不對)類似。

## 情境 B：切換分支被擋下

> 你在補充過擬合的例子，改到一半想切去看另一條分支的同一份講義，Git 拒絕切換：

```text
error: Your local changes to the following files would be overwritten by checkout:
	terms/overfitting.md
Please commit your changes or stash them before you switch branches.
```

```text
錯誤: 您對下列檔案的本機修改將被簽出動作覆蓋：
	terms/overfitting.md
請在切換分支前提交或貯存您的修改。
```

這是 Git 在保護你還沒 commit 的改動。先看改了什麼，再決定怎麼處理。

**自己打指令**

```bash
git status                       # 看哪些檔案還沒 commit
git diff                         # 看改了什麼，按 q 離開

# 下面三選一
git add . && git commit -m "docs: 補充過擬合的例子"   # 改動告一段落：commit
git stash                                             # 先暫存，之後用 git stash pop 拿回來
git restore terms/overfitting.md                      # 不要了：放棄改動，救不回來
```

**請 AI 做**

```text
切換分支被擋下了。請告訴我還沒 commit 的改動是什麼，建議我該 commit、先暫存還是放棄，等我決定再處理。
```

> 如果改動已經告一段落，直接 commit 最簡單，不容易忘記。

## 情境 C：刪錯分支

> 上週刪掉 `experiment/qa-format`，今天同學說：「那個問答式的講義其實很好背。」或者你剛才強制刪除時，刪錯了分支。

已經 commit 的內容通常還救得回來，越早處理越好。

**自己打指令**

```bash
git reflog                                       # 找出分支最後一個 commit 的編號
git branch experiment/qa-format <commit 編號>     # 用這個 commit 重建分支
git log experiment/qa-format --oneline -3        # 確認內容
```

> 刪除分支時，訊息裡的 `(was a035bc3)` 就是 commit 編號，有留著的話不用查 reflog。

**請 AI 做**

```text
我想救回被刪除的 experiment/qa-format 分支。請從刪除訊息或 Git 的操作紀錄（reflog）找出它最後一個 commit，用它重新建立分支，建立前先讓我確認內容。
```

> ⚠️ 沒有 commit 過的改動救不回來。Git 也會定期清理沒有分支指向的 commit，時間拖太久就可能找不到。

## 情境 D：講義寫到一半，突然要緊急修正

> 梯度下降的講義寫到一半，同學傳訊息：「講義裡準確率的公式是錯的，那是精確率的公式！明天就要考試了！」

**以前的做法**：把改到一半的檔案先藏起來（`git stash`），修完再拿回來，常常發生衝突。

**用 worktree**：原本的資料夾完全不動，從 main 另外開一個資料夾來修。

**自己打指令**

```bash
# 在母目錄
git worktree add .worktrees/hotfix-accuracy -b hotfix/accuracy-formula main

# 到新的 worktree 修正
cd .worktrees/hotfix-accuracy
echo '準確率 = 預測正確的筆數 ÷ 全部筆數' > terms/accuracy.md
git add .
git commit -m "fix: 修正準確率公式"

# 回母目錄合併
cd ../..
git merge hotfix/accuracy-formula
```

**請 AI 做**

對母目錄的 AI 說：

```text
我要緊急修正準確率的公式。請從 main 建立一個新的 worktree 來修，分支叫 hotfix/accuracy-formula，放在 .worktrees/hotfix-accuracy。
```

然後開新視窗，用 `opencode .worktrees/hotfix-accuracy` 進去，告訴 AI 正確的公式：

```text
terms/accuracy.md 的公式寫錯了。正確的公式是「準確率 = 預測正確的筆數 ÷ 全部筆數」。請修正後 commit。
```

合併後，同學馬上就能拿到正確的講義。回到梯度下降時，再把最新的 main 合併進那條分支就好。

## 情境 E：不小心刪掉了 worktree 資料夾

> 你覺得 `.worktrees/` 裡的檔案太亂，順手刪掉了 `feature-neural-network`，才想起講義還沒寫完。

先別慌，看你的工作有沒有 commit 過：

| 內容 | 還在嗎 |
| :--- | :--- |
| ✅ 已經 commit 的 | **還在**，它們存在分支上 |
| ❌ 沒有 commit 的 | **救不回來**，所以做完一段就要 commit |

**自己打指令**

```bash
git worktree prune                                                    # 清掉失效的紀錄
git worktree add .worktrees/feature-neural-network feature/neural-network   # 用原本的分支重建
```

> 如果沒先執行 `prune`，重建時會出現 `missing but already registered worktree`。不需要這個 worktree 了，只要執行 `git worktree prune` 就好。

**請 AI 做**

```text
我不小心刪掉 .worktrees/feature-neural-network 資料夾了。請清掉失效的 worktree 紀錄，再用原本的分支把它重新建立回來。
```

> 下次要刪除時，請用 `git worktree remove`，不要直接刪資料夾。

## 情境 F：新的 worktree 少了資料

> 你請 worktree 裡的 AI 參考老師的投影片，它卻回答：「找不到 `references/slides.md`。」

這通常是被忽略的檔案沒有帶過來（見 [05 站](05-worktree-structure.md#3-什麼隔離了什麼還是共用)）。

**自己打指令**

```bash
# 在母目錄
cp -R references .worktrees/feature-neural-network/
```

**請 AI 做**

對 worktree 裡的 AI 說：

```text
這個 worktree 找不到老師的投影片。請比對母目錄，看是不是少了 references 資料夾，然後幫我複製過來。
```

> 之後寫程式時，出現找不到模組、缺少環境變數這類錯誤，通常也是同樣的原因：少了 `.env` 或還沒安裝套件。

## 情境 G：AI 剛 commit 完，才發現漏了檔案

> AI 寫完神經網路講義並 commit，你一看才發現激活函數的補充講義沒有放進去。

不需要再多一個「補檔案」的 commit，直接補進前一個 commit。

**自己打指令**

```bash
git add terms/activation-function.md   # 把漏掉的檔案加進暫存區
git commit --amend --no-edit           # 併入前一個 commit，訊息不變
```

**請 AI 做**

```text
剛才的 commit 漏掉了 terms/activation-function.md，請把它加進來，合併進前一個 commit。
```

> ⚠️ `git commit --amend` 只適合**還沒 push** 的 commit。已經 push 的 commit 改用新的 commit 補上。

## 情境 H：搭配 Herdr，同時指揮多個 AI

> 期中考前要趕出神經網路和梯度下降兩份講義，你想一個人管兩個 AI。

先建立兩個 worktree：

**自己打指令**

```bash
git worktree add .worktrees/feature-neural-network -b feature/neural-network
git worktree add .worktrees/feature-gradient-descent -b feature/gradient-descent
```

**請 AI 做**

```text
請建立兩個 worktree：feature/neural-network 放在 .worktrees/feature-neural-network，feature/gradient-descent 放在 .worktrees/feature-gradient-descent。
```

再用 Herdr 分頁，讓每個 AI 待在自己的資料夾：

| Herdr 分頁 | 位置 | 做什麼 |
| :--- | :--- | :--- |
| 分頁 1 | 母目錄 | 維護 main、最後合併 |
| 分頁 2 | `.worktrees/feature-neural-network` | OpenCode 寫神經網路講義 |
| 分頁 3 | `.worktrees/feature-gradient-descent` | 另一個 AI 寫梯度下降講義 |

看 Herdr 側欄的狀態燈號（🟡 工作中、🔴 等你回應、🟢 做完了），一個人就能同時管好幾個 AI。

> 兩個 AI 都會在 `README.md` 目錄的最後加一行，第二條分支合併時很可能發生衝突。這兩行互不相關，兩行都留下就好，見 [03 站第 4 節](03-merge-conflict.md#4-處理衝突)。

> 想讓主管 AI 自動完成這整套流程？見 [Herdr 動手練習第 5 關](../herdr/practice/05-parallel-worktrees/README.md)。

---

## ✅ 動手練習

回到 `ml-notes` 資料夾，把最後兩份講義補齊。

### 練習一：情境 A，改動做在 main 上

#### 第 1 步：不小心直接改在 main 上

**自己打指令**

```bash
cd ~/ml-notes
git switch main
cat > terms/cross-validation.md <<'EOF'
# 交叉驗證

- **定義**：把資料分成多份，輪流當驗證資料，評估模型的表現。
- **白話比喻**：同一份教材輪流出不同範圍的模擬考。
- **例子**：5 折交叉驗證會訓練並評估模型 5 次。
EOF
echo '- [交叉驗證](terms/cross-validation.md)' >> README.md
git status
```

**請 AI 做**

```text
請新增 terms/cross-validation.md，說明交叉驗證，並加進目錄。先不要 commit。
```

#### 第 2 步：把改動帶到新分支

**自己打指令**

```bash
git switch -c feature/cross-validation
git add .
git commit -m "docs: 新增交叉驗證講義"
git switch main
git status      # main 應該沒有未提交的改動
```

**請 AI 做**

```text
剛才的改動不小心做在 main 上，還沒 commit。請開一條新分支 feature/cross-validation，把這些改動帶過去並 commit，然後確認 main 沒有變動。
```

#### 第 3 步：合併並刪除分支

**自己打指令**

```bash
git merge feature/cross-validation
git branch -d feature/cross-validation
```

**請 AI 做**

```text
請把這條分支合併進 main，再刪除它。
```

### 練習二：情境 D，寫到一半要緊急修正

#### 第 1 步：建立梯度下降的 worktree

**自己打指令**

```bash
git worktree add .worktrees/feature-gradient-descent -b feature/gradient-descent
```

**請 AI 做**

```text
請建立一個 worktree 來寫梯度下降講義，分支叫 feature/gradient-descent，放在 .worktrees/feature-gradient-descent。
```

#### 第 2 步：開始寫，但先不要 commit

**自己打指令**

開新的終端機視窗：

```bash
cd ~/ml-notes/.worktrees/feature-gradient-descent
cat > terms/gradient-descent.md <<'EOF'
# 梯度下降

- **定義**：沿著讓誤差下降最快的方向，一步步調整模型參數。
- **白話比喻**：在濃霧中下山，每一步都往最陡的下坡走。
- **例子**：訓練神經網路時，用它來更新權重。
EOF
echo '- [梯度下降](terms/gradient-descent.md)' >> README.md
git status
```

**請 AI 做**

開新的終端機視窗，用 `opencode .worktrees/feature-gradient-descent` 進入 worktree，說：

```text
請新增 terms/gradient-descent.md，說明梯度下降，並加進目錄。先不要 commit。
```

#### 第 3 步：在另一個 worktree 緊急修正

**自己打指令**

回到原本的視窗：

```bash
cd ~/ml-notes
git worktree add .worktrees/hotfix-accuracy -b hotfix/accuracy-formula main
cd .worktrees/hotfix-accuracy
echo '準確率 = 預測正確的筆數 ÷ 全部筆數' > terms/accuracy.md
git add .
git commit -m "fix: 修正準確率公式"
cd ../..
```

**請 AI 做**

回到母目錄的 AI，說：

```text
我要緊急修正準確率的公式。請從 main 建立一個新的 worktree，分支叫 hotfix/accuracy-formula，放在 .worktrees/hotfix-accuracy，把 terms/accuracy.md 的公式改成「準確率 = 預測正確的筆數 ÷ 全部筆數」並 commit。
```

#### 第 4 步：合併修正，清理 worktree

**自己打指令**

```bash
git merge hotfix/accuracy-formula
git worktree remove .worktrees/hotfix-accuracy
git branch -d hotfix/accuracy-formula
```

**請 AI 做**

```text
請把 hotfix/accuracy-formula 合併進 main，再移除這個 worktree 和它的分支。
```

#### 第 5 步：回去完成梯度下降

公式應該已經是正確的。

**自己打指令**

回到梯度下降的視窗：

```bash
cd ~/ml-notes/.worktrees/feature-gradient-descent
git add .
git commit -m "docs: 新增梯度下降講義"
git merge --no-edit main
cat terms/accuracy.md
```

**請 AI 做**

回到梯度下降的 AI，說：

```text
內容沒問題，請 commit，再把最新的 main 合併進來，並顯示 terms/accuracy.md 的內容。
```

#### 第 6 步：合併梯度下降

**自己打指令**

回到原本的視窗：

```bash
cd ~/ml-notes
git merge feature/gradient-descent
```

**請 AI 做**

回到母目錄的 AI，說：

```text
請把 feature/gradient-descent 合併進 main。
```

#### 第 7 步：清理並確認成果

應該只剩 main，`terms` 裡有 6 份講義。

**自己打指令**

```bash
git worktree remove .worktrees/feature-gradient-descent
git branch -d feature/gradient-descent
git branch
ls terms
```

**請 AI 做**

關掉 worktree 裡的 AI，再說：

```text
請移除這個 worktree 和它的分支，然後列出所有分支和 terms 裡的檔案。
```

**恭喜，這份講義可以拿來準備考試了！**

---

## ✅ 自我檢查

- [ ] 發現 AI 改在 main 上時，知道先確認有沒有 commit、有沒有 push
- [ ] 知道切換分支被擋下時，Git 在保護什麼
- [ ] 能用 `git reflog` 救回刪錯的分支，也知道什麼救不回來
- [ ] 能用 worktree 處理「寫到一半要緊急修正」
- [ ] 知道刪掉 worktree 資料夾後，哪些內容救得回來、要用哪個指令清理紀錄
- [ ] 知道新 worktree 少了資料時先檢查什麼
- [ ] 知道 `--amend` 只適合還沒 push 的 commit

> 🎉 完成 Branch 與 Worktree 章節！遇到問題時查閱 [指令速查與疑難排解](reference.md)。
