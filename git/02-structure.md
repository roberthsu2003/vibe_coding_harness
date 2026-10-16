# 02　目錄與原理

> ★ 入門　｜　[← 01 為什麼需要 Worktree](01-why-worktree.md)　｜　[章節首頁](README.md)　｜　下一站：[03 完整流程 →](03-lifecycle.md)

**這一站你會學到**：worktree 建議放在哪裡、為什麼要加進 `.gitignore`，以及它為什麼幾乎不佔空間。

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

| 比較 | 專案內 `.worktrees/`（推薦） | 專案外 `../my-project-xxx/` |
| :--- | :--- | :--- |
| 整齊度 | 全部收在專案裡 | 上一層資料夾散落一堆 |
| Herdr 辨識 | 自動歸在同一個專案下 | 要自己分辨 |
| 需要注意 | **必須把 `.worktrees/` 加進 `.gitignore`** | 不需要 |

> [!IMPORTANT]
> 在專案根目錄的 `.gitignore` 加入這一行，否則主目錄的 `git status` 會把整個 `.worktrees/` 當成新檔案：
> ```gitignore
> .worktrees/
> ```

---

## 2. 為什麼幾乎不佔空間？

建立 worktree 時，Git **不會**複製整個專案的歷史。

- **母目錄**：有完整的 `.git/` 資料夾。
- **每個 worktree**：裡面的 `.git` 是**一個檔案**（不是資料夾），內容只有一行，指向母目錄：

```text
gitdir: /path/to/my-project/.git/worktrees/feature-login
```

所以不管開幾個 worktree，歷史紀錄都只存一份。每個 worktree 只多出它自己的工作檔案。

> 自己確認：在 worktree 裡執行 `cat .git`，就會看到上面這一行。

---

## ✅ 自我檢查

- [ ] 專案的 `.gitignore` 已加入 `.worktrees/`
- [ ] 能說出 worktree 裡的 `.git` 是檔案還是資料夾、裡面寫了什麼

> 下一站：[03 完整流程 →](03-lifecycle.md)
