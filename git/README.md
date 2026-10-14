# Git 與 Worktree：AI Agent 平行開發指南

Git 是 AI 開發工作流程中不可或缺的「安全復原網與時間機器」。搭配 `git worktree`，同一個 Git 儲存庫可以同時擁有多個獨立的工作目錄，各自切換分支，徹底解放多 Agent 平行開發的潛力。

---

## 導覽目錄

1. [為什麼 AI Coding 需要 Worktree？（三大核心價值）](#1-為什麼-ai-coding-需要-worktree三大核心價值)
2. [目錄設計與原理解析：為什麼放在專案內的 .worktrees/？](#2-目錄設計與原理解析為什麼放在專案內的-worktrees)
3. [完整操作指令與生命週期（端到端實踐）](#3-完整操作指令與生命週期端到端實踐)
4. [實戰情境與解決方案（新手常見盲點）](#4-實戰情境與解決方案新手常見盲點)
5. [常用指令速查與疑難排解](#5-常用指令速查與疑難排解)

---

## 1. 為什麼 AI Coding 需要 Worktree？（三大核心價值）

在傳統開發中，切換分支需要使用 `git checkout`，同一個目錄在同一時間只能停留在一條分支上。

當搭配 AI Coding Agent 時，我們常常需要讓多個 Agent 同時處理不同任務（例如 Agent A 開發登入功能、Agent B 修復 Header Bug、Agent C 跑效能測試）。這時 `git worktree` 便是最佳武器：

| 核心價值 | 傳統單一目錄痛點 | Worktree 平行架構優勢 |
| :--- | :--- | :--- |
| **多 Agent 絕對隔離** | 多個 Agent 在同個目錄修改程式碼，容易引發檔案覆蓋、中途髒污或衝突 | 每個 Agent 擁有專屬的獨立工作目錄，各做各的、互不干擾 |
| **超高速建立與省硬碟** | 重複 `git clone` 耗時且數百 MB 的歷史紀錄被重複複製多次 | 所有 Worktree **共用母專案同一個 `.git` 資料庫**，毫秒級建立且幾乎零額外空間 |
| **主幹穩定與即時審查** | 切換分支測試時，未完成的改動會被 stash 搞得混亂不堪 | 主專案目錄維持穩定主幹，可隨時開窗切換到各 Worktree 驗收成果 |

---

## 2. 目錄設計與原理解析：為什麼放在專案內的 .worktrees/？

很多開發者會好奇：Worktree 應該建在專案內還是專案外？為什麼手冊推薦放在專案內的 `.worktrees/`？

### 2.1 專案內 vs. 專案外 方案對照

| 評比維度 | 專案內集中管理：`.worktrees/`（推薦 ⭐） | 專案外平級目錄：`../project-worktrees/` |
| :--- | :--- | :--- |
| **目錄整潔度** | **高**。所有分支工作區集中在專案內部的隱藏目錄，自成一格（Self-contained） | **低**。在電腦上一層目錄散落一堆平級資料夾，專案多了難以辨識管理 |
| **工具感知 (Herdr / IDE)** | **極佳**。Herdr 能透過相對路徑直接識別血緣，自動群組聚合在同一個專案樹下 | **稍弱**。不同目錄需要手動個別定位，無法自動關聯母專案 |
| **目錄隱蔽性** | 加點開頭（`.`）為隱藏資料夾，日常終端 `ls` 或檔案總管不干擾雜亂 | 需另開資料夾存放 |
| **關鍵前提條件** | **必須在 `.gitignore` 加上 `.worktrees/`**，避免子目錄被 Git 誤追蹤 | 不需要特別加 gitignore |

### 2.2 建議目錄結構

```text
vibe_coding_harness/              # 主專案目錄（母體）
├── .git/                         # 真正的 Git 物件資料庫（所有歷史與分支都在這）
├── .gitignore                    # 規範忽略 .worktrees/（必備！）
├── src/                          # 程式碼
└── .worktrees/                   # 集中存放所有 Agent 分支工作區的收納箱
    ├── feature-login/            # 專供 Agent A 開發登入功能的獨立工作目錄
    └── fix-header/               # 專供 Agent B 修復 Header 的獨立工作目錄
```

### 2.3 底層原理揭秘：為什麼不會重複佔用空間？

當你在專案內執行 `git worktree add .worktrees/feature-login` 時，Git **並沒有**重新複製整份倉庫！

* **母專案根目錄**：擁有完整的 `.git/` 資料夾（存放所有提交、歷史物件與設定）。
* **`.worktrees/feature-login/` 目錄**：裡面**只有一個極小的 `.git` 檔案**（只有十幾 Bytes，不是資料夾！），裡面只記錄了一行指向母體的路徑指標：
  ```text
  gitdir: /path/to/vibe_coding_harness/.git/worktrees/feature-login
  ```

這意味著不管你開了 3 個還是 10 個 Worktree，它們全都是向母專案借用物件資料庫，建立只需要 **0.1 秒**，而且完全不耗費重複的硬碟空間！

> [!IMPORTANT]
> **必備前置設定**：請務必確認專案根目錄的 `.gitignore` 已加入：
> ```gitignore
> .worktrees/
> ```
> 這樣主目錄的 `git status` 就不會把 `.worktrees/` 當作待提交檔案。

---

## 3. 完整操作指令與生命週期（端到端實踐）

Worktree 的標準生命週期包含：**建立 → 檢視 → 賦予 Agent → 驗收合併 → 清理**。

### 步驟 1：建立存放目錄與分支工作區
```bash
# 1. 確保存放目錄存在
mkdir -p .worktrees

# 2. 建立新分支 feature/login，並將其掛載到 .worktrees/feature-login
git worktree add .worktrees/feature-login -b feature/login
```

### 步驟 2：檢視所有活躍中的 Worktree
```bash
git worktree list
```
輸出範例：
```text
/path/to/vibe_coding_harness                     abc1234 [main]
/path/to/vibe_coding_harness/.worktrees/feature-login   def5678 [feature/login]
```

### 步驟 3：進入 Worktree 啟動 AI Agent
```bash
cd .worktrees/feature-login

# 啟動 OpenCode 或其他 Agent 開始編程
opencode
```
> 此時 Agent 的所有檔案讀寫、安裝依賴（`uv add`）、終端測試，完全隔離在該目錄與 `feature/login` 分支上，主專案的代碼絲毫不受影響！

### 步驟 4：驗收、合併與安全移除 Worktree
當 Agent 完成任務，且你已驗收代碼並在母目錄 merge 完畢後，即可清理該工作區：

```bash
# 1. 先回到母目錄
cd ../..

# 2. 安全移除該 worktree
git worktree remove .worktrees/feature-login

# 3. （選用）整理已過期的中繼紀錄
git worktree prune
```

---

## 4. 實戰情境與解決方案（新手常見盲點）

#### 情境一：主功能改到一半，突然要緊急開另一個 Hotfix 分支
* **痛點**：以往需要 `git stash` 暫存一堆未完成的檔案，修完 bug 回來 `stash pop` 常常遇到衝突。
* **解決方案**：
  直接開一個新 Worktree：
  ```bash
  git worktree add .worktrees/hotfix-auth -b hotfix/auth-crash
  ```
  原本的開發目錄檔案完全不動，直接切換到 `.worktrees/hotfix-auth` 讓 Agent 迅速修復並提交，優雅無痛。

#### 情境二：不小心手動用 `rm -rf` 刪除了 Worktree 資料夾
* **痛點**：手動刪除資料夾後，執行 `git worktree list` 依然看到該項目，或出現警告。
* **解決方案**：
  不要慌張！執行清理指令：
  ```bash
  git worktree prune
  ```
  Git 會自動檢查所有註冊的 Worktree，自動清除磁碟上已不存在的無效指標。

#### 情境三：Agent 剛 Commit 完才發現漏加檔案（善用 Amend）
* **痛點**：Agent 建立了 commit，但測試檔案忘了加入，產生多餘的修正 commit。
* **解決方案**：
  直接請 Agent：
  ```text
  剛才的 commit 漏掉了 tests/test_login.py，請將它加入後，使用 git commit --amend 合併進前一個 commit。
  ```
  這能讓該分支維持簡潔高質量的 Git Commit 歷史。

#### 情境四：搭配 Herdr 實現「多分支多 Agent 視覺化並行」
* **最佳協同模式**：
  1. 在 Herdr 的 Tab 1 開啟主目錄維護主幹代碼。
  2. 在 Tab 2 進入 `.worktrees/feature-login` 啟動 OpenCode 寫功能。
  3. 在 Tab 3 進入 `.worktrees/feature-pay` 啟動 Claude 寫支付模組。
  利用 Herdr 的分頁標籤與即時狀態圖示（🟡 working / 🟢 done），一人同時指揮多個 Agent 平行作戰！

---

## 5. 常用指令速查與疑難排解

### 指令速查表

| 操作需求 | Git 指令語法 | 說明 |
| :--- | :--- | :--- |
| **建立並開新分支** | `git worktree add <路徑> -b <分支名稱>` | 最常用！同時建立獨立目錄與新分支 |
| **掛載既有分支** | `git worktree add <路徑> <現有分支>` | 將遠端已有的分支拉到本地獨立目錄處理 |
| **列出所有工作區** | `git worktree list` | 查看當前所有的 worktree 路徑與分支狀態 |
| **安全移除工作區** | `git worktree remove <路徑>` | 刪除工作目錄並註銷 Git 內部指標（需先 commit） |
| **清理無效參照** | `git worktree prune` | 清除被手動刪除或過期的 worktree 中繼狀態 |

### 常見問題排解 (Troubleshooting)

1. **fatal: '...' is already checked out at '...'**：
   - Git 規定**同一條分支不能同時被兩個 Worktree 簽出（checkout）**。請為新 Worktree 建立新分支（使用 `-b <新分支名>`），或在原目錄切換至其他分支。
2. **Worktree 建立後出現大量的未追蹤檔案**：
   - 請檢查根目錄是否有 `.gitignore`。若有忽略規則，確認在母倉庫中已正常配置。
3. **誤把 `.worktrees/` 提交進 Git 了**：
   - 執行 `git rm -r --cached .worktrees/`，並確認根目錄 `.gitignore` 包含 `.worktrees/`，然後重新 commit。
