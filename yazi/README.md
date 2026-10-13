# Yazi：在終端機裡逛檔案

Yazi 是用鍵盤操作的檔案管理工具。它可以在終端機裡列出資料夾、預覽 Markdown 或程式碼，也能快速複製檔案路徑。你可以把它想成「不用離開命令列的小型檔案總管」。[Yazi 官方快速入門](https://yazi-rs.github.io/docs/quick-start/)

## 用一個 prompt 安裝整套設定

如果你已經開啟 Codex CLI，請把下面整段貼進去。這份 prompt 會安裝 Yazi、`bat` 彩色文字預覽工具，以及 piper、預覽放大外掛和 Catppuccin Latte 淺色主題；也會設定 Markdown／文字檔行號、預覽捲動與放大快捷鍵。

```text
請在這台電腦安裝並設定 Yazi 檔案管理工具，先確認作業系統與套件管理器，再採用適合此系統的安裝方式。如果是 macOS 且有 Homebrew，請安裝 yazi 和 bat；其他系統請查閱 Yazi 官方安裝文件，選擇對應方法。不要安裝 Herdr 或 AI CLI，它們由我另外安裝。

安裝後請完成這些設定：
1. 使用 Yazi 官方套件命令安裝 yazi-rs/plugins:piper、yazi-rs/plugins:toggle-pane，以及 yazi-rs/flavors:catppuccin-latte。
2. 設定 Yazi 固定使用 Catppuccin Latte 淺色主題。
3. Markdown 和 txt 預覽使用 bat 的 GitHub 淺色配色並顯示行號；保留既有設定，不要整份覆蓋我的設定檔。
4. 設定 Shift+T 放大／還原預覽。預覽使用 Shift+J / Shift+K 上下捲動（若這是 Yazi 預設快捷鍵，請保留預設即可）。
5. 寫入前先查看現有 Yazi 設定；若需要修改，先備份並合併必要設定，不要刪除無關設定。
6. 完成後檢查 yazi、bat 和套件是否可用，列出啟動方式、安裝了哪些項目、修改了哪些設定檔，以及目前沒有成功的步驟。不要只描述命令，請實際執行安裝與設定。

Yazi 套件與設定請以官方文件為準：https://yazi-rs.github.io/docs/installation/ 、https://yazi-rs.github.io/docs/configuration/ 和 https://github.com/yazi-rs/plugins 。遇到需要管理員密碼或權限確認時，先告訴我原因與將執行的命令。
```

這個 prompt 假設你使用支援工具操作的 Codex CLI，並已開啟可安裝軟體的權限。貼上後仍要閱讀 CLI 顯示的命令和結果；若你的系統不是 macOS，安裝命令會依官方文件調整。

## 開啟和離開

在終端機輸入：

```bash
yazi
```

按 `q` 離開。可以先在 shell 用 `cd` 進入想看的專案，再輸入 `yazi`。

## 先記住這幾個按鍵

| 想做什麼 | 按鍵 |
| --- | --- |
| 上下移動檔案 | `↑` / `↓`，或 `k` / `j` |
| 開啟資料夾或檔案 | `Enter` 或 `l` |
| 回上一層資料夾 | `←` 或 `h` |
| 上下捲動右側預覽 | `Shift+J` / `Shift+K` |
| 複製目前檔案的完整路徑 | 依序按 `c`、`c` |
| 選取檔案後複製檔案 | `y`；到目的地按 `p` 貼上 |
| 放大／還原預覽 | `Shift+T`，需要前述設定 |
| 離開 Yazi | `q` |

注意：`c`、`c` 是先按一次 `c`，放開後再按一次 `c`。`c`、`d` 則複製目前資料夾路徑。`Shift+J`、`Shift+K` 捲動右邊的預覽，不會移動左邊的檔案選取位置。[Yazi 快速入門與快捷鍵](https://yazi-rs.github.io/docs/quick-start/)

## 在 Herdr 裡切換分頁

Herdr 的預設 prefix 是 `Ctrl+B`。按下後放開，再按下一個按鍵：[Herdr 官方快捷鍵](https://herdr.dev/docs/keyboard/)

| 想做什麼 | 按法 |
| --- | --- |
| 新增分頁 | `Ctrl+B`，放開，再按 `c` |
| 下一個分頁 | `Ctrl+B`，放開，再按 `n` |
| 上一個分頁 | `Ctrl+B`，放開，再按 `p` |
| 直接切到第 1 到 9 個分頁 | `Ctrl+B`，放開，再按數字 `1` 到 `9` |

例如，在一個 Herdr 分頁跑 Codex CLI，按 `Ctrl+B` 再按 `c` 開新分頁，然後在新分頁輸入 `yazi`。之後用 `Ctrl+B`、`n` 和 `Ctrl+B`、`p` 在兩個分頁間切換。

若快捷鍵和自己的設定不同，在 Herdr 按 `Ctrl+B`，放開後按 `?`，即可查看目前生效的快捷鍵。

## 官方資料

- [Yazi 安裝](https://yazi-rs.github.io/docs/installation/)
- [Yazi 快速入門與預設快捷鍵](https://yazi-rs.github.io/docs/quick-start/)
- [Yazi 設定](https://yazi-rs.github.io/docs/configuration/)
- [Herdr 快捷鍵](https://herdr.dev/docs/keyboard/)

查核日期：2026-10-13。Yazi 與 Herdr 仍會更新；快捷鍵和安裝方式以官方文件及本機 `--help`／快捷鍵說明為準。
