# 05　目錄與原理

> ★ 入門　｜　[← 04 為什麼需要 Worktree](04-why-worktree.md)　｜　[章節首頁](README.md)　｜　下一站：[06 Worktree 完整流程 →](06-worktree-lifecycle.md)

**這一站你會學到**：worktree 建議放在哪裡、為什麼要加進 `.gitignore`、它為什麼比較省空間，以及哪些東西隔離了、哪些還是共用。

---

## 1. 建議放在專案裡的 `.worktrees/`

```text
ml-notes/                        ← 母目錄（主專案，停在 main）
├── .git/                        ← 真正的 Git 資料庫（所有歷史都在這）
├── .gitignore                   ← 一定要寫入 .worktrees/
├── README.md
├── terms/
└── .worktrees/                  ← 所有 worktree 都收在這裡
    ├── feature-neural-network/  ← AI A 的工作資料夾
    └── fix-supervised-example/  ← AI B 的工作資料夾
```

| 比較 | 專案內 `.worktrees/`（本章使用） | 專案外 `../ml-notes-xxx/` |
| :--- | :--- | :--- |
| 整齊度 | 全部收在專案裡 | 上一層資料夾散落一堆 |
| 需要注意 | **必須把 `.worktrees/` 加進 `.gitignore`** | 不需要 |

> 兩種放法 Git 都支援。[Git 學習筆記第 07 章](https://github.com/roberthsu2003/git/tree/main/worktree)用的是放在專案旁邊的做法，這裡因為會同時開好幾個 AI，所以集中收在 `.worktrees/`。

> [!IMPORTANT]
> 開始之前要先做好這件事，否則主目錄的 Git 會把整個 `.worktrees/` 當成新檔案。**而且一定要 commit**：新的 worktree 只會拿到已經 commit 的檔案，沒有 commit 的 `.gitignore` 不會跟過去。

**自己打指令**

```bash
echo '.worktrees/' >> .gitignore            # 加入 .gitignore，>> 是加在檔案最後
git add .gitignore
git commit -m "chore: 忽略 .worktrees"
```

**請 AI 做**

```text
請把 .worktrees/ 加進 .gitignore 並 commit。
```

---

## 2. 為什麼比較省空間？

建立 worktree 時，Git **不會**複製整個專案的歷史。

- **母目錄**：有完整的 `.git/` 資料夾。
- **每個 worktree**：裡面的 `.git` 是**一個檔案**（不是資料夾），內容只有一行，指向母目錄：

```text
gitdir: /path/to/ml-notes/.git/worktrees/feature-neural-network
```

所以不管開幾個 worktree，歷史紀錄都只存一份。

親眼確認一下（要先有 worktree 才能執行，可以等 [06 站](06-worktree-lifecycle.md)做練習時再試）：

**自己打指令**

```bash
cat .worktrees/feature-neural-network/.git   # 會看到 gitdir 那一行
```

**請 AI 做**

```text
請顯示 .worktrees/feature-neural-network/.git 的內容，並說明它是檔案還是資料夾。
```

> 每個 worktree 還是有自己的一份工作檔案，所以講義本身會各有一份。Markdown 檔案很小，不用擔心；如果放了大型 PDF，就要留意空間。

---

## 3. 什麼隔離了？什麼還是共用？

Worktree 隔離的是**專案裡的檔案和目前的分支**，不是整台電腦。

> 老師的投影片和課本 PDF 有版權，不適合放進 Git。你把它們放在 `references/`，並加進 `.gitignore`。這個資料夾只留在你的電腦上，AI 寫講義時可以參考，但 Git 不會追蹤它。

| | 內容 | 要注意什麼 |
| :--- | :--- | :--- |
| ✅ **各自獨立** | 被 Git 追蹤的檔案（`terms/`、`README.md`）、目前的分支 | 這就是 worktree 的主要好處 |
| ⚠️ **不會自動帶過去** | 被 `.gitignore` 忽略的檔案，例如 `references/` | 新 worktree 裡沒有它們，AI 會找不到參考資料（解法見 [06 站](06-worktree-lifecycle.md)） |
| ⚠️ **大家共用** | Git 的 stash 和設定 | 在這個 worktree 做的 `git stash`，換到另一個 worktree 也看得到 |
| ⚠️ **同一台電腦** | 連接埠、資料庫、全域安裝的套件 | 寫講義不會遇到。之後用 AI 寫程式時，兩個 AI 同時啟動網站可能會搶同一個連接埠 |

想知道專案裡有哪些被忽略的檔案：

**自己打指令**

```bash
git status --ignored
```

**請 AI 做**

```text
請列出這個專案裡被 Git 忽略的檔案。
```

> 之後寫程式的專案也一樣：`.env`、`.venv`、`node_modules` 通常都被忽略，不會自動帶到新的 worktree。

---

## ✅ 自我檢查

- [ ] 知道 `.gitignore` 為什麼要加入 `.worktrees/`，而且一定要 commit
- [ ] 能說出 worktree 裡的 `.git` 是檔案還是資料夾、裡面寫了什麼
- [ ] 能說出新 worktree 為什麼沒有 `references/`
- [ ] 知道怎麼用 `git status --ignored` 查看被忽略的檔案

> 下一站：[06 Worktree 完整流程 →](06-worktree-lifecycle.md)
