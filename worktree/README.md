# Branch 與 Worktree：讓 AI 放心改，多個 AI 同時開發

請 AI 工作最怕兩件事：改壞已經完成的內容，以及多個 AI 互相干擾。

- **Branch（分支）** 把開發中的版本隔開。AI 在分支上改壞了，main 還是好的。
- **Worktree** 把工作資料夾隔開。每個 AI 有自己的資料夾和分支，可以同時工作。

> [!NOTE]
> **這一章從 Branch 教到 Worktree，重點放在怎麼搭配 AI 使用。** 還不熟 commit 的話，請先看 [Git 學習筆記](https://github.com/roberthsu2003/git)的[環境設定](https://github.com/roberthsu2003/git/tree/main/環境安裝與設定)和[第 01 章](https://github.com/roberthsu2003/git/tree/main/開始使用Git)。想更深入了解分支，看[第 03 章 分支與合併](https://github.com/roberthsu2003/git/tree/main/分支)；想把改壞的檔案救回來，看[第 09 章 還原檔案](https://github.com/roberthsu2003/git/tree/main/回復被刪除的檔案或被編輯的內容)。

---

## 貫穿全章的故事：機器學習名詞講義

你正在學機器學習，決定請 AI 幫忙把課堂上的專有名詞整理成講義，每個名詞一個 Markdown 檔。**全程不用寫程式。**

請開一個專用的本地資料夾（本章以 `ml-notes` 為例，準備步驟見[開始之前](#開始之前準備-ml-notes-資料夾)），各站的練習都接著在這裡做。走完全章，你會得到一份真正能複習的講義：

```text
ml-notes/
├── .gitignore                  ← 告訴 Git 哪些檔案不用記錄
├── README.md                   ← 講義目錄
├── references/                 ← 老師的投影片（不放進 Git）
└── terms/                      ← 每個專有名詞一個檔案
    ├── accuracy.md             ← 準確率
    ├── cross-validation.md     ← 交叉驗證
    ├── gradient-descent.md     ← 梯度下降
    ├── neural-network.md       ← 神經網路
    ├── overfitting.md          ← 過擬合
    └── supervised-learning.md  ← 監督式學習
```

| 老師說 | 你遇到的問題 | 學到什麼 | 站 |
| :--- | :--- | :--- | :---: |
| 「下週要教監督式學習。」 | AI 可能改壞已經寫好的講義 | Branch | [01](01-why-branch.md)、[02](02-branch-basics.md) |
| 「過擬合要講原因，也要講現象。」 | 兩條分支改到同一行 | 合併與衝突 | [03](03-merge-conflict.md) |
| 「要開始教神經網路，混淆矩陣的表格也標反了。」 | 想讓兩個 AI 同時做 | Worktree | [04](04-why-worktree.md)、[05](05-worktree-structure.md)、[06](06-worktree-lifecycle.md) |
| 「準確率的公式寫錯了，明天就要考試！」 | 手上的講義還沒寫完 | 實戰情境 | [07](07-scenarios.md) |

---

## 開始之前：準備 ml-notes 資料夾

開始第 01 站前，先把資料夾準備好。**這些步驟只需要做一次。**

每個範例都有兩種做法，全章都一樣。上面的指令要自己打過並看懂；下面的提示句，是實際工作時交給 AI 的說法。

### 步驟 1：建立資料夾

**自己打指令**

```bash
mkdir ~/ml-notes      # 建立資料夾
cd ~/ml-notes         # 進入資料夾
```

**請 AI 做**

AI 要在資料夾裡啟動，所以這一步一定要自己做。上面兩行打完後，再輸入：

```bash
opencode
```

> [!WARNING]
> 不要把 `ml-notes` 建在其他 Git 專案裡面，否則兩個專案的紀錄很容易搞混。

### 步驟 2：初始化 Git

初始化會在資料夾裡建立 `.git`，Git 從此才開始記錄這個資料夾的版本。

**自己打指令**

```bash
git --version                         # 確認已經安裝 Git
git rev-parse --is-inside-work-tree   # 出現 not a git repository，代表還不是 Git 專案
git init -b main                      # 初始化，主分支叫 main
```

**請 AI 做**

```text
請確認電腦已經安裝 Git，並確認這個資料夾還不是 Git 專案。確認後把它初始化成 Git 專案，主分支叫 main。
```

### 步驟 3：檢查 user.name 和 user.email

每個 commit 都會記錄是誰做的。這兩項沒有設定的話，commit 時會出現 `Author identity unknown`（作者身分未知）。

**自己打指令**

```bash
git config user.name     # 檢查名字，沒有輸出代表還沒設定
git config user.email    # 檢查 email，沒有輸出代表還沒設定

# 沒有設定才需要執行，請換成你自己的資料
git config --global user.name "你的名字"
git config --global user.email "you@example.com"
```

**請 AI 做**

```text
請檢查 Git 的 user.name 和 user.email 有沒有設定，並把結果告訴我。如果沒有設定，先問我要填什麼，不要自己編，再設定到這台電腦的全域設定。
```

> [!NOTE]
> - **電腦教室或共用電腦：** 如果顯示的是別人的名字，請拿掉 `--global`，只在這個專案設定，不要改到全域設定。
> - **Email 會被公開：** 之後把 commit push 到 GitHub，這裡的 email 會公開顯示。不想公開的話，可以使用 GitHub 提供的 noreply 信箱。

### 步驟 4：建立 .gitignore

`.gitignore` 列出 Git 不用記錄的檔案。電腦會自動產生一些和講義無關的檔案，例如 macOS 的 `.DS_Store`、Windows 的 `Thumbs.db`，先把它們排除。

**自己打指令**

```bash
printf '.DS_Store\nThumbs.db\n' > .gitignore   # 建立 .gitignore，每行一個規則
cat .gitignore                                  # 確認內容
```

**請 AI 做**

```text
請建立 .gitignore，忽略 .DS_Store 和 Thumbs.db。
```

> 第 06 站還會再加入 `.worktrees/` 和 `references/`，原因在[第 05 站](05-worktree-structure.md)說明。

### 步驟 5：做第一次 commit

專案要先有第一個 commit，後面才能順利開分支。

**自己打指令**

```bash
git add .gitignore                 # 把檔案放進暫存區
git commit -m "chore: 初始化專案"   # 建立 commit
git log --oneline                  # 看 commit 紀錄
git status                         # 看目前的狀態
```

**請 AI 做**

```text
請把 .gitignore 做第一次 commit，然後顯示 commit 紀錄和目前的狀態。
```

### ✅ 確認準備好了

- [ ] 目前的分支是 `main`
- [ ] commit 紀錄裡有一筆，作者是你的名字和 email
- [ ] 目前的狀態沒有未提交的改動

準備好了，就可以從[第 01 站](01-why-branch.md)開始。

---

## 學習路線

![Branch 與 Worktree 學習路線](assets/learning-path.svg)

| 部分 | 站 | 主題 | 難度 | 你會學到 |
| :--- | :---: | :--- | :---: | :--- |
| **Branch** | 01 | [為什麼需要 Branch](01-why-branch.md) | ★ | 分支是什麼、怎麼命名 |
| | 02 | [Branch 基本流程](02-branch-basics.md) | ★ | 建立 → 撰寫 → 提交 → 合併 → 刪除、丟掉失敗的實驗 |
| | 03 | [合併與衝突](03-merge-conflict.md) | ★★ | 安全地合併、解決衝突、合併後反悔 |
| **Worktree** | 04 | [為什麼需要 Worktree](04-why-worktree.md) | ★ | 多個 AI 同時工作的問題、Branch 和 Worktree 怎麼選 |
| | 05 | [目錄與原理](05-worktree-structure.md) | ★ | `.worktrees/` 放哪裡、什麼隔離了、什麼還是共用 |
| | 06 | [Worktree 完整流程](06-worktree-lifecycle.md) | ★★ | 建立 → 撰寫 → 提交 → 回母目錄合併 → 清理 |
| **實戰** | 07 | [實戰情境](07-scenarios.md) | ★★★ | AI 改在 main 上、救回分支、緊急修正、搭配 Herdr |

> [!TIP]
> **一句話記住**：不要直接在 main 上改。一次一個 AI 用 Branch；多個 AI 同時做，每個 AI 再加一個 Worktree。

> [!IMPORTANT]
> **指令和 AI 都要會。** 每個範例都先列出指令，再列出請 AI 做的說法。工程師要看得懂 AI 執行了什麼、出錯時知道怎麼處理，所以請先自己打過指令，再交給 AI。

---

## 📚 參考資料

| 文件 | 用途 |
| :--- | :--- |
| [指令速查與疑難排解](reference.md) | 所有 branch 與 worktree 指令、常見錯誤訊息（中英對照） |
| [Git 學習筆記](https://github.com/roberthsu2003/git) | 從第一筆 commit 開始的 Git 基礎教材 |
| [官方文件：git-branch](https://git-scm.com/docs/git-branch)、[git-switch](https://git-scm.com/docs/git-switch)、[git-worktree](https://git-scm.com/docs/git-worktree) | Git 官方說明 |

← [回到專案首頁](../README.md)
