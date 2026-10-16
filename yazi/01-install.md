# 01　安裝與第一次啟動

> ★ 入門　｜　[章節首頁](README.md)　｜　下一站：[02 瀏覽與預覽 →](02-browse.md)

**這一站你會學到**：安裝 Yazi 和建議的搭配工具，第一次進入與離開。

---

## 1. 安裝

| 作業系統 | 安裝指令 |
| :--- | :--- |
| macOS（Homebrew） | `brew install yazi` |
| Windows（WinGet） | `winget install sxyazi.yazi` |
| Linux（Cargo） | `cargo install --force yazi-build` |

### 建議一起安裝的工具

Yazi 本身就能用，但搭配下面這些工具，搜尋和跳轉的功能才會完整：

```bash
brew install fd ripgrep fzf zoxide
```

| 工具 | 讓 Yazi 能做什麼 |
| :--- | :--- |
| `fd` | 依檔名搜尋（按 `s`） |
| `ripgrep` | 依檔案內容搜尋（按 `S`） |
| `fzf` | 模糊搜尋跳轉（按 `z`） |
| `zoxide` | 跳到常去的資料夾（按 `Z`） |

> 想要預覽圖片、影片、PDF？官方完整的推薦清單見 [Yazi 安裝說明](https://yazi-rs.github.io/docs/installation)。

## 2. 確認安裝成功

```bash
yazi --version
```

看到版本號（例如 `Version: 26.9.1`）就成功了。

## 3. 第一次進入與離開

```bash
cd ~/my-project
yazi
```

| 想做的事 | 按鍵 |
| :--- | :--- |
| 離開 Yazi | `q` |
| 不管在哪，查看所有快捷鍵 | `~` 或 `F1` |

> [!TIP]
> 圖示顯示成方塊或問號？那是終端機字型缺少圖示字元。安裝 Nerd Font 字型（例如 `brew install font-symbols-only-nerd-font`）並在終端機設定中套用即可。

---

## ✅ 自我檢查

- [ ] `yazi --version` 有顯示版本號
- [ ] 能用 `yazi` 進入、用 `q` 離開
- [ ] 按過 `~` 看到快捷鍵說明

> 下一站：[02 瀏覽與預覽 →](02-browse.md)
