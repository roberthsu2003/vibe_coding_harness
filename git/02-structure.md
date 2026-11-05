# 02　目錄與原理

> ★ 入門　｜　[← 01 為什麼需要 Worktree](01-why-worktree.md)　｜　[章節首頁](README.md)　｜　下一站：[03 完整流程 →](03-lifecycle.md)

**這一站你會學到**：worktree 建議放在哪裡、為什麼要加進 `.gitignore`、它為什麼比較省空間，以及哪些東西隔離了、哪些還是共用。

---

## 1. 建議放在專案裡的 `.worktrees/`

```text
my-project/                  ← 母目錄（主專案，停在 main）
├── .git/                    ← 真正的 Git 資料庫（所有歷史都在這）
├── .gitignore               ← 一定要寫入 .worktrees/
├── src/
└── .worktrees/              ← 所有 worktree 都收在這裡
    ├── feature-login/       ← AI A 的工作資料夾
    └── fix-header/          ← AI B 的工作資料夾
```

| 比較 | 專案內 `.worktrees/`（本章使用） | 專案外 `../my-project-xxx/` |
| :--- | :--- | :--- |
| 整齊度 | 全部收在專案裡 | 上一層資料夾散落一堆 |
| 需要注意 | **必須把 `.worktrees/` 加進 `.gitignore`** | 不需要 |

> 兩種放法 Git 都支援。[Git 學習筆記第 07 章](https://github.com/roberthsu2003/git/tree/main/worktree)用的是放在專案旁邊的做法，這裡因為會同時開好幾個 AI，所以集中收在 `.worktrees/`。

> [!IMPORTANT]
> 開始之前先做好這件事，否則主目錄的 Git 會把整個 `.worktrees/` 當成新檔案。對 AI 說：
>
> ```text
> 請把 .worktrees/ 加進 .gitignore 並 commit。
> ```
>
> **一定要 commit。** 新的 worktree 只會拿到已經 commit 的檔案，沒有 commit 的 `.gitignore` 不會跟過去。

---

## 2. 為什麼比較省空間？

建立 worktree 時，Git **不會**複製整個專案的歷史。

- **母目錄**：有完整的 `.git/` 資料夾。
- **每個 worktree**：裡面的 `.git` 是**一個檔案**（不是資料夾），內容只有一行，指向母目錄：

```text
gitdir: /path/to/my-project/.git/worktrees/feature-login
```

所以不管開幾個 worktree，歷史紀錄都只存一份。

> 每個 worktree 還是有自己的一份工作檔案。如果再各自安裝 `.venv`、`node_modules`，也會佔不少空間。

---

## 3. 什麼隔離了？什麼還是共用？

Worktree 隔離的是**專案裡的檔案和目前的分支**，不是整台電腦。

| | 內容 | 要注意什麼 |
| :--- | :--- | :--- |
| ✅ **各自獨立** | 被 Git 追蹤的檔案、目前的分支 | 這就是 worktree 的主要好處 |
| ⚠️ **不會自動帶過去** | 被 `.gitignore` 忽略的檔案，例如 `.env`、`.venv`、`node_modules` | 新 worktree 裡沒有它們，專案可能跑不起來（解法見 [03 站](03-lifecycle.md)） |
| ⚠️ **大家共用** | Git 的 stash 和設定 | 在這個 worktree 做的 `git stash`，換到另一個 worktree 也看得到 |
| ⚠️ **同一台電腦** | 連接埠、資料庫、全域安裝的套件 | 兩個 AI 同時啟動網站，可能搶同一個連接埠，要請它們用不同的連接埠 |

---

## ✅ 自我檢查

- [ ] 專案的 `.gitignore` 已加入 `.worktrees/`，並且 commit 了
- [ ] 能說出 worktree 裡的 `.git` 是檔案還是資料夾、裡面寫了什麼
- [ ] 能說出新 worktree 為什麼沒有 `.env`

---

## 進階（選修）：自己確認

```bash
cat .git                # 在 worktree 裡執行，會看到 gitdir 那一行
git status --ignored    # 看有哪些被忽略的檔案
```

> 下一站：[03 完整流程 →](03-lifecycle.md)
