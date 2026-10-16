# 01　安裝與第一次啟動

> ★ 入門　｜　[章節首頁](README.md)　｜　下一站：[02 基本操作 →](02-basics.md)

**這一站你會學到**：安裝 Herdr、確認版本、第一次進入與離開。

---

## 1. 安裝

依作業系統選一種方式：

| 作業系統 | 安裝指令 |
| :--- | :--- |
| macOS（Homebrew，推薦） | `brew install herdr` |
| macOS / Linux（官方腳本） | `curl -fsSL https://herdr.dev/install.sh \| sh` |
| Windows（PowerShell） | `powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 \| iex"` |

## 2. 確認安裝成功

```bash
herdr --version
```

看到版本號（例如 `herdr 0.9.3`）就成功了。

> 找不到 `herdr` 指令？重新開一個終端機視窗，或執行 `source ~/.zshrc` 後再試一次。

## 3. 第一次進入

先進入你的專案資料夾，再啟動 Herdr：

```bash
cd ~/my-project
herdr
```

畫面會變成 Herdr 的介面：左邊是**工作區側欄**，右邊是可以輸入指令的**窗格**。

> [!TIP]
> 專案資料夾如果有 `.git`（是 Git 專案），Herdr 會自動用專案名稱命名工作區，並在側欄顯示目前的分支與改動狀態。

## 4. 離開與回來

| 想做的事 | 操作 |
| :--- | :--- |
| 暫時離開（裡面的程式**繼續跑**） | 按 `Ctrl+B`，放開，再按 `q` |
| 回到剛才的畫面 | 在終端機再輸入一次 `herdr` |

這個「先按 `Ctrl+B` 再按別的鍵」的操作叫做 **Prefix 快捷鍵**，下一站會詳細說明。

---

## ✅ 自我檢查

- [ ] `herdr --version` 有顯示版本號
- [ ] 能進入 Herdr，看到左側欄和窗格
- [ ] 能用 `Ctrl+B` 放開再按 `q` 離開，再用 `herdr` 回來

> 下一站：[02 基本操作 →](02-basics.md)
