# 05　Skill 配置

> ★★ 進階　｜　[← 04 環境配置](04-config.md)　｜　[章節首頁](README.md)　｜　下一站：[06 專案規範與規則 →](06-agents-md.md)

**這一站你會學到**：Skill 是什麼、放在哪裡、`SKILL.md` 怎麼寫，以及如何建立、使用和管理自己的 Skill。

![Skill 的運作方式](assets/skill-flow.svg)

---

## 1. Skill 是什麼？

**Skill 就像交給 AI 的一份工作手冊。** 你把某件事的做法寫下來，之後 AI 遇到這件事就會翻開手冊照做，你不用每次重新交代。

| | `AGENTS.md`（規則） | Skill（工作手冊） |
| :--- | :--- | :--- |
| **何時載入** | 每次對話都載入 | 用到時才載入 |
| **適合內容** | 永遠要遵守的規矩 | 特定工作的步驟 |
| **例子** | 一律用繁體中文回覆 | 怎麼寫週報、怎麼部署網站 |

> [!TIP]
> 同一件事交代 AI 超過兩次，就值得做成 Skill。

---

## 2. Skill 放在哪裡？

| 範圍 | 位置 | 誰能用 |
| :--- | :--- | :--- |
| **專案** | `<專案根目錄>/.agents/skills/<skill 名稱>/` | 這個專案，可用 Git 分享給同學 |
| **全域** | `~/.gemini/config/skills/<skill 名稱>/` | 你電腦上的所有專案 |
| **外掛** | `~/.gemini/config/plugins/<外掛名稱>/skills/` | 用 `agy plugin` 安裝後自動載入 |

> [!NOTE]
> 資料夾名稱是 `.agents`，有 **s**，而且前面有一個點，所以 Finder 預設看不到。

---

## 3. 方法一：一句話請 AI 建立（推薦）

不用自己寫檔案，用中文說明你要什麼：

```text
請幫我在這個專案建立一個 skill，名稱叫 weekly-report，用途是把我這週做的事整理成繁體中文週報，分成「完成事項」「遇到問題」「下週計畫」三段。
```

AI 會建立 `.agents/skills/weekly-report/SKILL.md`。完成後請做兩件事：

1. **確認內容**：打開檔案看一下，不滿意就繼續用中文要求修改。
2. **重新載入**：在對話框輸入下面的指令。

```text
/skills reload
```

接著就能試用了：

```text
/weekly-report 這週完成了登入頁面，但部署時遇到權限錯誤，下週要做購物車
```

想做成所有專案都能用的 Skill，把「在這個專案」改成「在全域」就可以了。

---

## 4. 方法二：自己動手建立

自己寫一次，就會知道 Skill 的結構。以下做一個幫你寫 commit 訊息的 Skill。

### 步驟 1：建立資料夾和檔案

```bash
mkdir -p .agents/skills/commit-message
touch .agents/skills/commit-message/SKILL.md
```

### 步驟 2：寫入 `SKILL.md`

````markdown
---
name: commit-message
description: 依照團隊格式撰寫繁體中文 Git commit 訊息。當使用者要寫 commit 訊息或整理變更內容時使用。
---

# 撰寫 Commit 訊息

## 步驟

1. 判斷變更類型：新功能用 `feat`、修錯誤用 `fix`、改文件用 `docs`。
2. 第一行格式為 `類型: 一句話摘要`，摘要使用繁體中文。
3. 只輸出訊息本身，不要執行 `git commit`。

## 範例

```text
feat: 新增會員登入頁面
```
````

### 步驟 3：重新載入並測試

```text
/skills reload
```

然後用兩種方式測試：

| 測試 | 輸入 | 預期結果 |
| :--- | :--- | :--- |
| 手動呼叫 | `/commit-message 我新增了登入頁面` | `feat: 新增登入頁面` |
| 自動觸發 | `幫我替「修正購物車金額計算錯誤」寫一則 commit 訊息` | `fix: 修正購物車金額計算錯誤` |

---

## 5. 看懂 `SKILL.md`

### Skill 資料夾的結構

```text
.agents/skills/commit-message/
├── SKILL.md       # 必要：說明與步驟
├── scripts/       # 選用：輔助腳本
├── examples/      # 選用：參考範例
├── resources/     # 選用：範本或資料檔
└── references/    # 選用：比較長的參考文件
```

大多數 Skill 只需要 `SKILL.md`。

### 開頭的設定欄位

`SKILL.md` 最上面兩條 `---` 之間的內容叫做 frontmatter：

| 欄位 | 必填 | 說明 |
| :--- | :---: | :--- |
| `name` | 建議填寫 | Skill 名稱，用小寫英文和連字號，也就是 `/` 後面的名字 |
| `description` | ✅ | **最重要的欄位**：這個 Skill 做什麼、什麼時候用 |
| `disable-slash-command` | | 設為 `true` 時不會出現在 `/` 選單，但 AI 仍可自動使用 |

### `description` 決定 AI 會不會用它

AI 平常只看得到 `description`，寫得太模糊，AI 就不知道該用它。

| | 範例 | 問題 |
| :---: | :--- | :--- |
| ❌ | `處理文字` | 沒說做什麼，也沒說何時用 |
| ❌ | `週報` | 太短，AI 難以判斷 |
| ✅ | `把使用者這週做的事整理成繁體中文週報。當使用者要寫週報或總結本週進度時使用。` | 清楚說明「做什麼」和「何時用」 |

---

## 6. 使用 Skill 的三種方式

| 方式 | 怎麼做 | 範例 |
| :--- | :--- | :--- |
| **自動觸發** | 正常說話，AI 判斷符合就使用 | `幫我寫這週的週報` |
| **點名使用** | 在句子裡提到名稱 | `請用 weekly-report 這個 skill 整理進度` |
| **斜線呼叫** | 輸入 `/` 加上 Skill 名稱 | `/weekly-report 這週完成了登入頁面` |

進階：非互動模式也能使用。

```bash
agy -p "/commit-message 我修正了登入錯誤"
```

---

## 7. 管理與分享 Skill

| 想做的事 | 小範例／做法 |
| :--- | :--- |
| **查看**已載入的 Skill | 在對話框輸入 `/skills` |
| **新增** Skill | 建立 `.agents/skills/my-skill/SKILL.md`（或用 `/learn` 整理），再輸入 `/skills reload` |
| **停用** Skill | 暫時將該資料夾移出 `skills/`（或將 `SKILL.md` 改名為 `SKILL.md.bak`），再輸入 `/skills reload` |
| **刪除** Skill | 刪除資料夾（`rm -rf .agents/skills/my-skill`），再輸入 `/skills reload` |
| **分享**給同學 | 把 `.agents/skills/` commit 進 Git，同學 pull 後就能用 |

> [!CAUTION]
> Skill 可以包含腳本，AI 會照著裡面的指示做事。安裝別人的 Skill 之前，請先看過內容，確認來源可信。

### 什麼是 Plugin（外掛）？

如果說 **Skill** 是一份單獨的工作手冊，那 **Plugin（外掛）** 就是一個**把多種自訂功能打包在一起的擴充套件包**（就像手機 App 或 VS Code 擴充功能）。

一個 Plugin 可以同時包含：
- **Skills**：工作手冊與斜線指令（例如 `/firebase`）
- **MCP 伺服器**：連接外部服務的工具
- **Subagents**：專屬子代理角色
- **Rules & Hooks**：預設規則與自動化腳本

**啟用時整包一起生效，停用時整包一起關閉。** 例如官方的 `chrome-devtools`、`firebase` 外掛，就是把該領域需要的 Skill、MCP 與工具打包在一起，安裝後就能直接使用。

**怎麼新增、停用與刪除 Plugin？**

- **在 `agy` 對話框**：輸入 **`/plugin`**（別名 `/plugins`），即可開啟互動式外掛市集與管理面板，瀏覽、安裝、停用或解除安裝外掛。
- **在終端機**（以 `firebase` 外掛為例）：
  ```bash
  # 新增（安裝）外掛
  agy plugin install firebase

  # 查看已安裝的外掛
  agy plugin list

  # 停用 / 重新啟用外掛（保留設定，暫時關閉）
  agy plugin disable firebase
  agy plugin enable firebase

  # 刪除（解除安裝）外掛
  agy plugin uninstall firebase
  ```

---

## 8. 好 Skill 的四個原則

1. **一個 Skill 只做一件事**：「寫週報」和「部署網站」請分開。
2. **主檔保持精簡**：詳細資料放進 `references/`，AI 需要時才會讀。
3. **寫出驗證方式**：告訴 AI 怎麼確認做對了，例如「執行 `npm test` 並確認全部通過」。
4. **不寫 AI 已經會的事**：只寫你的流程裡特別的地方，「要寫乾淨的程式碼」這種話不用寫。

---

## 9. 常見問題

| 狀況 | 檢查方向 |
| :--- | :--- |
| 輸入 `/` 加名稱卻找不到 | 輸入 `/skills reload`，或確認路徑是 `.agents/skills/<名稱>/SKILL.md` |
| 資料夾打錯 | 確認是 `.agents`（有 s），檔名是全大寫的 `SKILL.md` |
| Skill 載入失敗 | 確認檔案第一行就是 `---`，且 `description` 有填寫 |
| AI 沒有自動使用 | 把 `description` 寫得更具體，或直接用 `/` 加名稱呼叫 |
| AI 沒照步驟做 | 把步驟拆得更短、更明確，並加上範例 |

---

## 10. 動手練習

做一個屬於你自己的 Skill：

1. 想一件你常請 AI 做的事，例如「把筆記整理成重點」或「解釋程式碼給初學者聽」。
2. 用一句話請 AI 建立這個 Skill。
3. 輸入 `/skills reload`，再輸入 `/skills` 確認有出現。
4. 分別用「自動觸發」和「斜線呼叫」各試一次。
5. 依照結果，用中文請 AI 修改 Skill，直到你滿意為止。

---

[← 04 環境配置](04-config.md)　｜　[章節首頁](README.md)　｜　下一站：[06 專案規範與規則 →](06-agents-md.md)
