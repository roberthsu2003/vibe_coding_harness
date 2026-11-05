# 03　完整流程

> ★★ 進階　｜　[← 02 目錄與原理](02-structure.md)　｜　[章節首頁](README.md)　｜　下一站：[04 合併與衝突 →](04-merge-conflict.md)

**這一站你會學到**：worktree 從建立到清理的 6 個步驟、每一步怎麼跟 AI 說，以及怎麼確認自己在哪個 worktree。

---

![Worktree 的完整流程](assets/git-worktree-lifecycle.svg)

下面的範例用 [OpenCode](../opencode/README.md) 當 AI，其他 AI 工具的說法也一樣。

## 步驟 1：建立（在母目錄）

在專案的母目錄啟動 AI，然後說：

```text
請建立一個 worktree 來開發登入功能，放在 .worktrees/ 底下。如果專案有 .env，請複製一份過去；需要安裝套件的話也一起裝好。
```

> [!IMPORTANT]
> **後半句很重要。** `.env`、`.venv`、`node_modules` 這些被忽略的檔案不會自動出現在新的 worktree，少了它們專案可能跑不起來。

## 步驟 2：檢視（在母目錄）

```text
請列出目前所有的 worktree 和它們的分支。
```

應該會看到兩筆：母目錄（`main`）和新的 worktree（`feature/login`）。

## 步驟 3：讓 AI 開發（在 worktree）

開一個新的終端機視窗，在專案的母目錄輸入這一行，讓另一個 AI 在 worktree 裡工作：

```bash
opencode .worktrees/feature-login
```

確認 OpenCode 畫面下方顯示 `.worktrees/feature-login:feature/login`，再交代工作：

```text
請幫這個專案新增登入功能。
```

AI 在這裡改的檔案都只在 `feature/login` 分支上，main 的檔案不會變動。

> 想同時開好幾個視窗，可以搭配 [Herdr](../herdr/README.md)。

## 步驟 4：驗收並提交（在 worktree）

```text
請列出你改了哪些檔案、跑測試確認沒問題，然後 commit。
```

> 所有 worktree 共用同一個 `.git`，這裡的 commit 在母目錄**馬上看得到**，不需要 push / pull。

## 步驟 5：回到母目錄合併

切回母目錄的 AI，說：

```text
請把 feature/login 合併進 main。合併前先告訴我會多出哪些 commit。
```

詳細的合併步驟與衝突處理見 [04 合併與衝突](04-merge-conflict.md)。

## 步驟 6：清理（在母目錄）

先把 worktree 裡的 AI 關掉，然後對母目錄的 AI 說：

```text
請移除 feature-login 這個 worktree 和它的分支。移除前先檢查裡面有沒有被忽略、但我還需要的檔案，例如只改在那邊的 .env。
```

> [!WARNING]
> 移除 worktree 時，Git 只會擋下**修改過或未追蹤**的檔案。**被忽略的檔案（例如 `.env`）會直接刪除，不會警告。** 所以移除前要先檢查。

> [!WARNING]
> AI 回報分支「沒有完全合併」時，代表還有 commit 沒合併。先回到步驟 5，**不要要求 AI 強制刪除**，否則那些工作很難找回來。

---

## 💡 我現在在哪一個 worktree？

開了好幾個 worktree 後很容易搞混。三個方法：

1. **看 OpenCode 畫面下方**：顯示 `資料夾:分支`，例如 `.worktrees/feature-login:feature/login`。
2. **問 AI**：「我現在在哪個資料夾、哪個分支？這裡是母目錄還是 worktree？」
3. **看終端機提示字元**：很多設定（例如 Oh My Zsh、Starship）會顯示目前分支。

---

## ✅ 動手練習

在一個新的空資料夾裡啟動 AI：

1. 說：「請把這個資料夾變成 Git 專案，把 `.worktrees/` 加進 `.gitignore`，再加一個 README，然後做第一次 commit。」
2. 說：「請建立一個叫 practice 的 worktree。」
3. 開新視窗，用 `opencode .worktrees/practice` 進入 worktree，請 AI 新增一個檔案並 commit。
4. 回到母目錄的 AI，請它把 `practice` 合併進 main。
5. 請它移除 worktree 和分支，並確認只剩母目錄。

> 一定要先做第 1 步。專案還沒有任何 commit 時，建立 worktree 不會報錯，但會產生一條沒有歷史的分支。

---

## 進階（選修）：自己打指令

```bash
# 1. 建立（在母目錄）
git worktree add .worktrees/feature-login -b feature/login
cp .env .worktrees/feature-login/      # 有 .env 才需要

# 2. 檢視
git worktree list

# 3. 開發（在 worktree）
cd .worktrees/feature-login
uv sync                                # 依專案調整，例如 npm install
opencode

# 4. 驗收並提交（在 worktree）
git status
git diff
uv run pytest                          # 依專案調整
git add .
git commit -m "feat: 新增登入功能"

# 5. 合併（回到母目錄）
cd ../..                               # 要在 worktree 的最上層執行才正確
git merge feature/login

# 6. 清理（在母目錄）
git -C .worktrees/feature-login status --ignored   # 先看有哪些被忽略的檔案
git worktree remove .worktrees/feature-login
git branch -d feature/login
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
| 路徑裡有 `.git/worktrees/`，例如 `.../.git/worktrees/feature-login` | 🌿 worktree：`feature-login` |
| `.git`，或以 `/.git` 結尾的路徑（在子資料夾執行時） | ✅ 母目錄 |

> `git worktree list` 會列出所有 worktree，但**不會標示你在哪一個**。

> 下一站：[04 合併與衝突 →](04-merge-conflict.md)
