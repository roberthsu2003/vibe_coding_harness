# 03-E　E 區：調環境 (Config) 與其他指令

> ★ 入門　｜　[← D 區：看成果](d-output.md)　｜　[回到 03 斜線指令總覽](../03-slash-commands.md)　｜　下一站：[04 環境配置 →](../04-config.md)

**這一區解決的問題**：「想換更快或更聰明的 AI 模型？想調整思考深度、修改介面設定，或是下課離開 `agy`？」

（想深入了解設定檔與擴充功能，可接著閱讀 [04 環境配置](../04-config.md) 與 [05 Skill 配置](../05-skills.md)。）

---

## 開始前：建立本節練習資料夾

先完成[課堂練習準備](../../practice/README.md)的工具確認與教材下載，再在**一般終端機**逐行執行：

```bash
python3 ~/terminal-ai-course/practice/prepare.py ~/terminal-ai-labs/agy/03-e
cd ~/terminal-ai-labs/agy/03-e
agy
```

看到目的資料夾已存在時，直接 `cd` 進去接續；要重做則把路徑最後一段改成 `03-e-retry`。本節的程式、筆記與初始 Git commit 都已準備好。

---

## 1. 最常操作的環境指令

### `/model`：切換 AI 模型

```text
/model
```

- **結果**：開啟模型選單，用上下鍵即可切換預設模型（例如快一點的 Flash 模型，或擅長深度推理的模型）。
- **選擇 Orchestrator**：可選 `Orchestrator (Carbon)` 或 `Orchestrator (Argon)`，讓規劃與執行模型自動交接；方案與操作見 [01 Orchestrator 教學](../01-install.md#orchestrator自動搭配規劃與執行模型)。
- **只在這一句換模型**：也可以直接在指令後面指定模型與任務：
  ```text
  /model gemini-4-argon-high 幫我把 draft.md 的文字潤飾得更有說服力
  ```

---

### `/effort`：調整思考強度

覺得某個問題需要 AI 想得更深、更周全時：

```text
/effort high
```

- **結果**：調整模型的思考深度（Thinking Effort）。等級由低到高為 `low`、`medium`、`high`、`xhigh`、`max`（實際可用等級依目前選用的模型而定）。想得越深，回答品質越細膩，但等待時間也會稍微變長。
- **Orchestrator 例外**：它使用固定配置，`/effort` 不適用；想練習調整強度時，請先用 `/model` 選擇支援調整的單一模型。[官方說明](https://antigravity.google/docs/models#select-orchestrator)

---

### `/config`：開啟設定選單

```text
/config
```

- **結果**：開啟互動式設定選單，可以調整執行模式、介面配色、通知等選項。別名：`/settings`。

---

### `/exit`：離開 agy

```text
/exit
```

- **結果**：結束這次的 `agy` 工作階段，回到一般終端機畫面。別名：`/quit`（也可以連按兩次 `Ctrl+D`）。

---

## 2. 進階管理指令（第 04～08 站會用到）

| 指令 | 一句話說明 | 範例與延伸閱讀 |
| :--- | :--- | :--- |
| `/permissions` | 查看或修改 AI 可以執行哪些動作的權限 | 輸入 `/permissions` 開啟畫面。詳見 [08 權限設定與沙盒](../08-permissions.md) |
| `/add-dir` | 讓 AI 也能讀取電腦裡另一個資料夾的筆記 | `/add-dir ~/Documents/my-notes` |
| `/skills` | 瀏覽目前已載入的 Skill（或重新載入） | 輸入 `/skills` 查看，或 `/skills reload` 重新載入。詳見 [05 Skill 配置](../05-skills.md) |
| `/agents` | 查看自訂代理與背景子代理 | 輸入 `/agents` 開啟管理畫面。詳見 [07 Subagent 子代理](../07-subagents.md) |
| `/mcp` | 查看外部工具（MCP 伺服器）連線狀態 | 輸入 `/mcp` 開啟管理畫面。詳見 [04 環境配置](../04-config.md) |
| `/plugin` | 查看或管理已安裝的外掛（詳見 [05 Skill 配置](../05-skills.md#方式-a透過官方社群市集安裝-plugin推薦)） | 輸入 `/plugin` 開啟管理面板，或 `/plugin list` 列出外掛。別名：`/plugins` |

---

## 3. 其他少用指令速查

平時比較少用到，知道有這些功能即可：

| 指令 | 用途 | 小範例 |
| :--- | :--- | :--- |
| `/feedback` | 開啟意見回饋面板 | `/feedback` |
| `/hooks` | 瀏覽目前啟用的 Hook（詳見 [06 專案規範與規則](../06-agents-md.md#6-進階用-hook-強制執行自動化腳本hooksjson)） | `/hooks` |
| `/keybindings` | 修改快捷鍵 | `/keybindings` |
| `/logout` | 登出並移除登入憑證 | `/logout` |
| `/remote-control` | 開關遠端控制 | `/remote-control on` |
| `/statusline` | 自訂底部狀態列 | `/statusline` |
| `/title` | 開關終端機標題更新 | `/title off` |
| `/voice` | 語音對話或語音輸入 | `/voice dictate` |

---

## 完整小範例：模型與管理功能逐一操作

先送出 `請讀 draft.md，回報一句摘要，不修改。`，確保有一段對話。

| 功能 | 準備與操作 | 驗收與收尾 |
| :--- | :--- | :--- |
| `/model` | 記下原模型，選另一個有額度的模型，再送出 `請用一句話摘要 draft.md，不修改。` | 模型名稱改變且有回答；再選回原模型。若只有一個可用模型，記下限制 |
| 單句換模型 | 確認有 Argon 模型才用上面的 `/model ...` 範例，否則換成選單列出的模型 ID | 檢查該輪模型與文字修改結果，不把無權限錯誤當成功 |
| `/effort` | 先用 `/model` 選單一、支援思考強度的模型，記下原強度，再 `/effort high` | 狀態列或提示顯示 high；送出 `請比較 draft.md 的兩種標題寫法` 看回答，再改回原強度 |
| `/config` | 記下配色或通知原值，切換一次、關閉再重開 | 新值保留；練完還原原值 |
| `/permissions`、`/skills`、`/agents`、`/mcp`、`/plugin` | 各開一次面板，記下一項已載入內容或「目前沒有」；看完按 Esc | 要新增實際內容，分別依第 04～08 站完整流程操作 |
| `/add-dir` | 在一般終端機 `mkdir -p ~/terminal-ai-labs/extra-notes`，`printf '外部筆記：週六複習。\n' > ~/terminal-ai-labs/extra-notes/extra.md`；再在 agy 輸入 `/add-dir ~/terminal-ai-labs/extra-notes`，閱讀信任提示後加入 | 送出 `請讀剛加入資料夾的 extra.md，回報內容`，應包含「週六複習」；結束本次對話後檢查工作區清單，移除不再需要的附加目錄 |

### 少用指令也能實測

| 指令 | 完整操作與驗收 |
| :--- | :--- |
| `/feedback` | 開啟回饋面板，閱讀可填欄位後取消返回即可；本練習不需送出回饋 |
| `/hooks` | 先完成 [06 Hook 實作](../06-agents-md.md#6-進階用-hook-強制執行自動化腳本hooksjson)，再查看 my-check-hook，停用後執行 python3 main.py 確認不再觸發 |
| `/keybindings` | 先在 `/config` 設好外部編輯器，開啟快捷鍵檔，找到一項現有快捷鍵並記錄，退出不存檔；不用臆造不明的 action 名稱 |
| `/logout` | 確認對話已完成後登出，再從終端機執行 agy，依登入步驟重新登入；能再次送出「你好」取得回答即完成 |
| `/remote-control` | `/remote-control on`，依畫面指示在自己的瀏覽器登入，確認能看到這段對話；回終端機 `/remote-control off`，確認連線關閉。網址留在自己裝置使用 |
| `/statusline` | 送出 `/statusline 請在狀態列顯示目前模型與工作目錄`，檢查是否顯示；先記錄原設定，練完請它還原原設定 |
| `/title` | 先記原值，`/title off` 後送出一則短訊息，觀察視窗標題不隨任務更新；再 `/title on` 恢復（若原本關閉就設回 off） |
| `/voice` | 有麥克風時 `/voice dictate`，依提示允許麥克風，說「請用三點整理今天的學習」；確認轉錄內容，取消或送出，最後退出語音模式。無麥克風則記下環境限制 |
| `/exit` | 離開回一般終端機，執行 `agy -c` 應能接續本節對話 |

## ✅ 動手練習：切換思考強度與體驗設定選單

這個練習同樣**不寫任何程式**，帶你體驗切換模型設定與完成練習後安全離開：

| 步驟 | 在對話框輸入 | 觀察重點 |
| :---: | :--- | :--- |
| **1** | `/model` | 打開模型選單，看看目前有哪些模型可以選擇（看完可按 `Esc` 關閉或選一個模型） |
| **2** | `/effort high` | 先確認選用支援調整強度的單一模型，再調高強度並觀察狀態列或系統提示；Orchestrator 不適用 |
| **3** | `請幫我建立 summary.md，用一個表格整理今天學到的 5 個最實用的斜線指令` | 讓高思考強度的 AI 幫你整理出一份漂亮的複習筆記 `summary.md` |
| **4** | `/config` | 打開設定選單逛一逛有哪些個人化選項，按 `Esc` 返回 |
| **5** | `/exit` | 結束今天的練習，順利回到終端機！ |

---

[← D 區：看成果](d-output.md)　｜　[回到 03 斜線指令總覽](../03-slash-commands.md)　｜　下一站：[04 環境配置 →](../04-config.md)
