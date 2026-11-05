# 06　Worktree 完整流程

> ★★ 進階　｜　[← 05 目錄與原理](05-worktree-structure.md)　｜　[章節首頁](README.md)　｜　下一站：[07 實戰情境 →](07-scenarios.md)

**這一站你會學到**：worktree 從建立到清理的 6 個步驟、每一步怎麼跟 AI 說、為什麼要回母目錄合併，以及怎麼確認自己在哪個 worktree。

---

> **神經網路**的講義開工了。你想讓一個 AI 專心寫，自己的主資料夾保持乾淨。

![Worktree 的完整流程](assets/git-worktree-lifecycle.svg)

下面的範例用 [OpenCode](../opencode/README.md) 當 AI，其他 AI 工具的說法也一樣。

## 步驟 1：建立（在母目錄）

在專案的母目錄啟動 AI，然後說：

```text
請建立一個 worktree 來寫神經網路講義，分支叫 feature/neural-network，放在 .worktrees/feature-neural-network。如果專案有 references 資料夾，請複製一份過去。
```

> [!IMPORTANT]
> **後半句很重要。** 被忽略的檔案不會自動出現在新的 worktree，少了 `references/`，AI 就讀不到老師的投影片。

## 步驟 2：檢視（在母目錄）

```text
請列出目前所有的 worktree 和它們的分支。
```

應該會看到兩筆：母目錄（`main`）和新的 worktree（`feature/neural-network`）。

## 步驟 3：讓 AI 撰寫（在 worktree）

開一個新的終端機視窗，在專案的母目錄輸入這一行，讓另一個 AI 在 worktree 裡工作：

```bash
opencode .worktrees/feature-neural-network
```

確認 OpenCode 畫面下方顯示 `.worktrees/feature-neural-network:feature/neural-network`，再交代工作：

```text
請新增 terms/neural-network.md，說明「神經網路」，包含定義、白話比喻和一個例子，並把它加進 README.md 的目錄。
```

AI 在這裡改的檔案都只在 `feature/neural-network` 分支上，main 的檔案不會變動。

> 想同時開好幾個視窗，可以搭配 [Herdr](../herdr/README.md)。

## 步驟 4：驗收並提交（在 worktree）

```text
請列出你改了哪些檔案，並確認目錄的連結正確。先不要 commit，等我看過內容。
```

對照課本確認定義沒有寫錯，再說：

```text
內容沒問題，請 commit。
```

> 所有 worktree 共用同一個 `.git`，這裡的 commit 在母目錄**馬上看得到**，不需要 push / pull。

## 步驟 5：回到母目錄合併

切回母目錄的 AI，說：

```text
請把 feature/neural-network 合併進 main。合併前先告訴我會多出哪些 commit，等我同意再合併。
```

### 為什麼一定要回母目錄？

`main` 分支已經被母目錄使用中，Git **不允許同一條分支同時在兩個地方使用**。所以在 worktree 裡切換到 main 會失敗：

```text
fatal: 'main' is already used by worktree at '/path/to/ml-notes'
致命錯誤: 「main」已被位於「/path/to/ml-notes」的工作區使用
```

> 反過來就可以：在 worktree 裡把 main 的最新內容合併**進來**是允許的，做法見 [03 站第 5 節](03-merge-conflict.md#5-先把-main-同步進分支)。

合併結果的判讀和衝突處理，都和只用分支時一樣，見 [03 合併與衝突](03-merge-conflict.md)。

## 步驟 6：清理（在母目錄）

先把 worktree 裡的 AI 關掉，然後對母目錄的 AI 說：

```text
請移除 feature-neural-network 這個 worktree 和它的分支。移除前先檢查裡面有沒有被忽略、但我還需要的檔案，例如只放在那邊的 references。
```

> [!WARNING]
> 移除 worktree 時，Git 只會擋下**修改過或未追蹤**的檔案。**被忽略的檔案（例如 `references/`）會直接刪除，不會警告。** 所以移除前要先檢查。

> [!WARNING]
> AI 回報分支「沒有完全合併」時，代表還有 commit 沒合併。先回到步驟 5，**不要要求 AI 強制刪除**，否則那些工作很難找回來。

---

## 💡 我現在在哪一個 worktree？

開了好幾個 worktree 後很容易搞混。三個方法：

1. **看 OpenCode 畫面下方**：顯示 `資料夾:分支`，例如 `.worktrees/feature-neural-network:feature/neural-network`。
2. **問 AI**：「我現在在哪個資料夾、哪個分支？這裡是母目錄還是 worktree？」
3. **看終端機提示字元**：很多設定（例如 Oh My Zsh、Starship）會顯示目前分支。

---

## ✅ 動手練習

回到 [02 站](02-branch-basics.md#-動手練習)的 `ml-notes` 資料夾啟動 AI：

1. 說：「請把 `.worktrees/` 和 `references/` 加進 `.gitignore` 並 commit。然後建立 `references/slides.md`，內容寫『神經網路由輸入層、隱藏層和輸出層組成』，當作老師的投影片。」
2. 說：「請建立一個 worktree 來寫神經網路講義，分支叫 `feature/neural-network`，放在 `.worktrees/feature-neural-network`，並把 `references` 複製過去。」
3. 開新視窗，用 `opencode .worktrees/feature-neural-network` 進入 worktree，說：「請參考 `references/slides.md`，新增 `terms/neural-network.md`，說明神經網路，包含定義、白話比喻和一個例子，並加進 `README.md` 的目錄，然後 commit。」
4. 回到母目錄的 AI，說：「請列出 `terms` 資料夾的檔案。」確認還看不到 `neural-network.md`。
5. 說：「請把 `feature/neural-network` 合併進 main。」
6. 關掉 worktree 裡的 AI，說：「請移除 `feature-neural-network` 這個 worktree 和它的分支，並確認只剩母目錄。」

> 沒做過前面的練習，要從空資料夾開始的話，請先讓 AI 做第一次 commit。專案還沒有任何 commit 時，建立 worktree 不會報錯，但會產生一條沒有歷史的分支。

---

## ✅ 自我檢查

- [ ] 能說出 worktree 的 6 個步驟，以及每一步在哪裡做
- [ ] 知道為什麼在 worktree 裡不能切換到 main
- [ ] 知道移除 worktree 前要先檢查什麼

---

## 進階（選修）：自己打指令

```bash
# 1. 建立（在母目錄）
git worktree add .worktrees/feature-neural-network -b feature/neural-network
cp -R references .worktrees/feature-neural-network/   # 有 references 才需要

# 2. 檢視
git worktree list

# 3. 撰寫（在 worktree）
cd .worktrees/feature-neural-network
opencode

# 4. 驗收並提交（在 worktree）
git status
git diff
git add .
git commit -m "docs: 新增神經網路講義"

# 5. 合併（回到母目錄）
cd ../..                               # 要在 worktree 的最上層執行才正確
git branch --show-current              # 應該顯示 main
git log main..feature/neural-network --oneline   # 預覽會多出哪些 commit
git merge feature/neural-network

# 6. 清理（在母目錄）
git -C .worktrees/feature-neural-network status --ignored   # 先看有哪些被忽略的檔案
git worktree remove .worktrees/feature-neural-network
git branch -d feature/neural-network
git worktree list                      # 確認只剩母目錄
```

> 順序不能反過來：worktree 還在時，`git branch -d` 會出現 `cannot delete branch … used by worktree`。

**確認自己的位置：**

```bash
git rev-parse --show-toplevel    # 目前所在資料夾的根目錄
git branch --show-current        # 目前的分支
git rev-parse --git-dir          # 判斷是母目錄還是 worktree
```

| `git rev-parse --git-dir` 的結果 | 代表 |
| :--- | :--- |
| 路徑裡有 `.git/worktrees/`，例如 `.../.git/worktrees/feature-neural-network` | 🌿 worktree：`feature-neural-network` |
| `.git`，或以 `/.git` 結尾的路徑（在子資料夾執行時） | ✅ 母目錄 |

> `git worktree list` 會列出所有 worktree，但**不會標示你在哪一個**。

> 下一站：[07 實戰情境 →](07-scenarios.md)
