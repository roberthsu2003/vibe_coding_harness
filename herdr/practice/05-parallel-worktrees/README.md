# 第 5 關：平行開發

← [回到關卡地圖](../README.md)　｜　上一關：[第 4 關](../04-worktree-review/README.md)

## 學習目標

- 讓**兩個小模型同時工作**，各自在自己的 worktree 裡，互不干擾。
- 看主管**分別驗收**兩份成果，再依序**合併回 main**。
- 看到完整的收尾：兩個 worktree、兩個分支都清理乾淨，只剩 main。

這一關把前面學過的全部組合起來：任務卡（第 1 關）、退回修改（第 2 關）、測試（第 3 關）、worktree（第 4 關），再加上**平行派工**。

---

## 對 agy 說

```text
幫我開一個新的 git 專案，同時讓兩個小模型工作：一個寫簡單的統計程式（平均數和中位數），一個寫這個專案的說明文件。各自用自己的 worktree，你檢查完都沒問題就合併回 main，最後把 worktree 清乾淨。
```

## 你會看到什麼

### 1. 任務卡

分工的部分有兩個小模型：

```text
## 分工
  • SubAgent 1：coder
      • 工作目錄：work/stats/.worktrees/code
      • 分支：feature/stats-code
  • SubAgent 2：writer
      • 工作目錄：work/stats/.worktrees/docs
      • 分支：feature/stats-docs
## 驗收標準
  1. 程式：uvx pytest -q checks/stats/test_stats.py 全部通過
  2. 文件：必要段落都在、範例正確
```

確認後回覆「好，開始」。

### 2. 平行工作（大約 3～5 分鐘）

- 畫面上會**同時出現兩個小模型窗格**，兩個都亮 🟡。
- agy 先把任務送給 coder，**不等它做完**就接著送給 writer，然後才分別等待兩個完成。這就是「平行派工」。
- 和第 4 關一樣會有很多 git 指令的確認畫面，選 **2** 即可。

### 3. 回報

最精彩的是合併圖：

```text
git log --oneline --graph
*   3ee135a (HEAD -> main) merge: 合併文件分支 feature/stats-docs
|\
| * 69919ff docs: 新增統計工具專案 README 說明文件     ← writer 的成果
* | 73f98c6 feat: 實作平均數與中位數統計計算函式       ← coder 的成果
|/
* 03bb4e2 chore: 初始化專案與 .gitignore

git worktree list
.../work/stats  3ee135a [main]     ← 兩個 worktree 都清理乾淨了
```

兩條線從同一點分開（平行開發），最後匯合回 main（合併）。

---

## 想一想

1. 兩個小模型同時工作，為什麼不會互相改到對方的檔案？
2. 如果兩個小模型都修改了同一個檔案（例如都改了 `README.md`），合併時可能會發生什麼事？
3. 比較第 4 關和這一關的 `git log --graph`，為什麼這一關多了一個 `merge` 的 commit？

## 變化題（換句話再做 2～3 次）

- 「開一個新的 git 專案，同時讓兩個小模型工作：一個寫簡單的溫度轉換程式，一個寫 BMI 計算程式，你各自寫測試檢查，都通過後合併回 main 並清理 worktree。」
- 「開一個新的 git 專案，讓三個小模型同時各寫一份工具介紹（Yazi、Herdr、Git），用 worktree 隔離，檢查後全部合併並清理。」
- 故意製造衝突：「讓兩個小模型在不同 worktree 都修改 README.md 的第一行，然後合併，看看會發生什麼事。」agy 遇到衝突時應該會停下來告訴你。

🎉 恭喜完成全部 6 關！你已經會用一句話指揮主管 AI，讓多個小模型平行工作、驗收、合併了。

---

## 🔧 進階：自己下指令（選修）

平行派工的關鍵：送出任務時**不加 `--wait`**，送完再分別等待。

```bash
herdr agent prompt coder  "你是 SubAgent……寫 stats.py……"     # 送出後立刻回來
herdr agent prompt writer "你是 SubAgent……寫 README.md……"    # 不用等 coder
herdr agent wait coder  --timeout 600000                      # 再分別等待
herdr agent wait writer --timeout 600000
herdr agent list                                              # 隨時查看所有 Agent 的狀態
```

合併與清理：

```bash
cd ~/herdr-lab/work/stats
git merge feature/stats-code
git merge feature/stats-docs
git worktree remove .worktrees/code && git branch -d feature/stats-code
git worktree remove .worktrees/docs && git branch -d feature/stats-docs
git log --oneline --graph
```
