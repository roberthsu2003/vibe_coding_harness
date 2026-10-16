# 04　設定與主題

> ★★★ 深入　｜　[← 03 搭配 AI 與 Herdr](03-ai-workflow.md)　｜　[章節首頁](README.md)　｜　📚 [參數速查與疑難排解](reference.md)

**這一站你會學到**：讓 Glow 每次都自動用分頁模式、固定行寬、換配色。

---

## 1. 打開設定檔

最簡單的方式是讓 Glow 幫你開：

```bash
glow config
```

Glow 會用你設定的編輯器（環境變數 `EDITOR`）打開設定檔；檔案不存在時會自動建立。

| 作業系統 | 設定檔位置 |
| :--- | :--- |
| macOS | `~/Library/Preferences/glow/glow.yml` |
| Linux | `~/.config/glow/glow.yml` |

> 不確定位置？執行 `glow --help`，`--config` 那一行會顯示你電腦上的預設路徑。

## 2. 推薦設定

```yaml
# 配色：auto（自動）、dark、light、pink、dracula、tokyo-night、notty
style: "auto"
# 每次都使用分頁模式，不用再打 -p
pager: true
# 每行最多幾個字元
width: 90
# 瀏覽專案時也顯示隱藏檔
all: false
# 瀏覽專案模式可以用滑鼠
mouse: false
```

## 3. 臨時換配色或行寬

不想改設定檔時，用參數臨時指定：

```bash
glow -s light -p README.md     # 淺色背景的終端機
glow -s dracula -p README.md   # Dracula 配色
glow -w 80 -p README.md        # 每行最多 80 個字元
```

---

## ✅ 自我檢查

- [ ] 執行過 `glow config`，知道設定檔在哪裡
- [ ] 設定 `pager: true` 後，`glow README.md` 會直接進入分頁模式
- [ ] 試過至少兩種配色

> 🎉 完成 Glow 章節！遇到問題時查閱 [參數速查與疑難排解](reference.md)。
