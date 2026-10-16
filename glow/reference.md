# 📚 參考：參數速查與疑難排解

> 📚 參考　｜　[章節首頁](README.md)

本頁以 Glow 3.0.0 的 `glow --help` 為準。

---

## 1. 常用參數

| 參數 | 功能 | 範例 |
| :--- | :--- | :--- |
| `-p`、`--pager` | 分頁閱讀 | `glow -p README.md` |
| `-t`、`--tui` | 用瀏覽模式開啟 | `glow -t docs/` |
| `-w`、`--width` | 每行最多幾個字元（`0` 為不換行） | `glow -w 80 README.md` |
| `-s`、`--style` | 配色（auto、dark、light、pink、dracula、tokyo-night、notty） | `glow -s light README.md` |
| `-a`、`--all` | 瀏覽模式也顯示隱藏檔 | `glow -a` |
| `-l`、`--line-numbers` | 瀏覽模式顯示行號 | `glow -t -l README.md` |
| `-n`、`--preserve-new-lines` | 保留原本的換行 | `glow -n notes.md` |
| `--config` | 指定設定檔 | `glow --config my.yml README.md` |
| `glow config` | 打開設定檔 | `glow config` |

## 2. 讀取來源

| 來源 | 範例 |
| :--- | :--- |
| 本機檔案 | `glow README.md` |
| 資料夾（瀏覽模式） | `glow docs/` |
| GitHub 專案 | `glow github.com/charmbracelet/glow` |
| 網址 | `glow https://example.com/notes.md` |
| 其他指令的輸出 | `git show HEAD:README.md \| glow -p` |

## 3. 分頁模式按鍵

| 按鍵 | 功能 |
| :--- | :--- |
| `j` / `k` | 往下 / 往上一行 |
| `Space`、`f` / `b` | 往下 / 往上一頁 |
| `d` / `u` | 往下 / 往上半頁 |
| `g` / `⇧G` | 開頭 / 結尾 |
| `?` | 按鍵說明 |
| `q` | 離開 |

---

## 4. 疑難排解

| 狀況 | 解法 |
| :--- | :--- |
| 找不到 `glow` 指令 | 重新開終端機；確認安裝路徑在 `$PATH` 裡 |
| 顏色怪怪的或變成黑白 | 終端機可能沒有宣告支援全彩。在 `~/.zshrc` 加上 `export COLORTERM=truecolor`，重新開終端機 |
| 淺色背景的終端機看不清楚 | 改用 `glow -s light`，或在設定檔寫 `style: "light"` |
| 寬螢幕上一行太長 | 用 `-w 80`，或在設定檔寫 `width: 80` |
| 改了 `~/.config/glow/glow.yml` 沒效果（macOS） | macOS 的設定檔在 `~/Library/Preferences/glow/glow.yml`，用 `glow config` 開啟最保險 |
| 怎麼離開 | 按 `q`，或 `Ctrl+C` |
