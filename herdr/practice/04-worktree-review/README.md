# 第 4 關：隔離與審查

← [回到關卡地圖](../README.md)　｜　上一關：[第 3 關](../03-test-loop/README.md)

## 學習目標

- 理解 **git worktree**：讓小模型在「平行時空」（獨立的資料夾和分支）裡工作，就算改壞了也不會影響主專案。
- 看主管**審查**小模型的改動（`git diff`），確認沒問題才**合併**回 main。
- 看到完整的收尾：**合併 → 移除 worktree → 刪除分支**。

> 想先了解 worktree 是什麼？見 [Git 操作指南](../../../git/)。

---

## 對 agy 說

```text
幫我開一個新的 git 專案，讓小模型在獨立的分支（用 worktree）寫一份 Git 基本指令的筆記，你審查沒問題再合併回 main，最後把 worktree 清乾淨。
```

## 你會看到什麼

### 1. 任務卡

分工的部分多了 worktree 和分支：

```text
## 分工
  • SubAgent：writer
  • 工作目錄：work/git-notes/.worktrees/notes
  • 分支：feature/git-basics
```

確認後回覆「好，開始」。

### 2. 確認畫面會比較多

這一關 agy 會執行很多 git 指令（`git init`、`git worktree add`、`git status`、`git commit`、`git merge`……），**每個都會問你一次**，大約 8～10 次。都是安全的指令，看一眼選 **2** 即可。

> 🔎 趁這個機會，每次確認時唸出指令名稱。做完這關，你就看過一次完整的 git 工作流程了。

### 3. 流程（大約 3 分鐘）

| 階段 | agy 做了什麼 |
| :--- | :--- |
| 準備 | 建立 git 專案、`.gitignore`、第一次 commit |
| 隔離 | `git worktree add` 建立獨立資料夾和分支 |
| 派工 | 小模型在 worktree 裡寫筆記 |
| 審查 | `git status` 確認只新增了筆記檔、執行檢查程式 |
| 合併 | 在 worktree 裡 commit，回到 main 執行 `git merge` |
| 清理 | `git worktree remove`、`git branch -d`，關閉小模型窗格 |

### 4. 回報

最後會附上兩個結果：

```text
git log --oneline --graph
* 4fdcbe6 (HEAD -> main) docs: 新增 Git 基本指令初學者筆記
* cbf739b chore: 初始化專案與 .gitignore

git worktree list
.../work/git-notes  4fdcbe6 [main]     ← 只剩主目錄，代表清理乾淨了
```

---

## 想一想

1. 為什麼要讓小模型在 worktree 裡工作，而不是直接在主專案裡改？
2. 小模型被交代「不要執行 git commit」，那 commit 是誰做的？為什麼要這樣分工？
3. 如果審查時發現小模型偷偷改了別的檔案，主管應該怎麼做？

## 變化題（換句話再做 2～3 次）

- 「在剛才的 git 專案裡，讓小模型用新的 worktree 再寫一份『常見錯誤與解法』，你審查後合併，記得清理。」
- 「讓小模型在 worktree 裡寫一個簡單的猜數字遊戲，你先寫測試，測試通過才合併回 main。」
- 合併完成後問 agy：「幫我用 git log 看看剛才的合併紀錄，並解釋每一行的意思。」

完成後 → [第 5 關：平行開發](../05-parallel-worktrees/README.md)

---

## 🔧 進階：自己下指令（選修）

agy 背後執行的 worktree 指令：

```bash
cd ~/herdr-lab/work/git-notes

git worktree add .worktrees/notes -b feature/git-basics   # 建立獨立資料夾與分支
git worktree list                                         # 查看所有 worktree

git -C .worktrees/notes status                            # 看小模型改了什麼
git -C .worktrees/notes diff                              # 看改動內容
git -C .worktrees/notes add -A
git -C .worktrees/notes commit -m "新增筆記"

git merge feature/git-basics                              # 在主目錄（main）合併
git worktree remove .worktrees/notes                      # 移除 worktree
git branch -d feature/git-basics                          # 刪除已合併的分支
```

> `git -C <路徑>` 的意思是「到那個資料夾執行 git」，不用真的 `cd` 過去。
