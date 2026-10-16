# 06　離開時切換目錄

> ★★★ 深入　｜　[← 05 搭配 AI 與 Herdr](05-ai-workflow.md)　｜　[章節首頁](README.md)　｜　📚 [快捷鍵總表與疑難排解](reference.md)

**這一站你會學到**：讓 Yazi 變成「找資料夾的工具」——在 Yazi 裡走到某個資料夾，離開後終端機就停在那裡。

---

## 1. 問題

直接執行 `yazi`，按 `q` 離開時，終端機會回到**啟動 Yazi 時的資料夾**。在 Yazi 裡逛到的深層資料夾，離開後就不見了。

## 2. 解法：加入 `y` 指令

把官方提供的這段程式加到 `~/.zshrc`（使用 Bash 的話是 `~/.bashrc`）：

```bash
function y() {
	local tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
	command yazi "$@" --cwd-file="$tmp"
	IFS= read -r -d '' cwd < "$tmp"
	[ "$cwd" != "$PWD" ] && [ -d "$cwd" ] && builtin cd -- "$cwd"
	rm -f -- "$tmp"
}
```

存檔後執行一次：

```bash
source ~/.zshrc
```

## 3. 使用方式

| 想做的事 | 做法 |
| :--- | :--- |
| 啟動 Yazi | 改用 **`y`**（不是 `yazi`） |
| 離開並**停在目前的資料夾** | 按 `q` |
| 離開並**回到原本的資料夾** | 按 `⇧Q` |

> 其他 shell（Fish、PowerShell 等）的寫法見 [官方說明](https://yazi-rs.github.io/docs/quick-start)。

---

## ✅ 自我檢查

- [ ] 已把 `y` 函式加進 `~/.zshrc` 並 `source`
- [ ] 用 `y` 進入 Yazi，走到某個子資料夾，按 `q` 離開後 `pwd` 顯示那個資料夾
- [ ] 知道 `q` 和 `⇧Q` 的差別

> 🎉 完成 Yazi 章節！遇到問題時查閱 [快捷鍵總表與疑難排解](reference.md)。
