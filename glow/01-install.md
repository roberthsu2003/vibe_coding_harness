# 01　安裝與第一次使用

> ★ 入門　｜　[章節首頁](README.md)　｜　下一站：[02 四種閱讀方式 →](02-reading.md)

**這一站你會學到**：安裝 Glow，讀你的第一份 Markdown 文件。

---

## 1. 安裝

| 作業系統 | 安裝指令 |
| :--- | :--- |
| macOS（Homebrew） | `brew install glow` |
| Windows（WinGet） | `winget install charmbracelet.glow` |
| Windows（Scoop） | `scoop install glow` |
| Arch Linux | `sudo pacman -S glow` |
| Fedora | `sudo dnf install glow` |

<details>
<summary>Ubuntu / Debian 的安裝方式（點我展開）</summary>

```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://repo.charm.sh/apt/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/charm.gpg
echo "deb [signed-by=/etc/apt/keyrings/charm.gpg] https://repo.charm.sh/apt/ * *" | sudo tee /etc/apt/sources.list.d/charm.list
sudo apt update && sudo apt install glow
```

</details>

## 2. 確認安裝成功

```bash
glow --version
```

看到版本號（例如 `glow version 3.0.0`）就成功了。

## 3. 讀第一份文件

進入任何有 `README.md` 的資料夾：

```bash
glow -p README.md
```

| 想做的事 | 按鍵 |
| :--- | :--- |
| 往下 / 往上捲動 | `j` / `k`（或 `↓` / `↑`） |
| 離開，回到終端機 | `q` |

> 比較看看：先執行 `cat README.md`，再執行 `glow -p README.md`，差別一眼就看得出來。

---

## ✅ 自我檢查

- [ ] `glow --version` 有顯示版本號
- [ ] 能用 `glow -p README.md` 讀文件，並用 `q` 離開

> 下一站：[02 四種閱讀方式 →](02-reading.md)
