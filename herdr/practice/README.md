# Herdr 多 Agent 協同練習：由淺至深 6 關

這組練習帶你學會一個工作循環：

> **聰明的 Supervisor 派工 → 小模型（SubAgent）完成後回報 → Supervisor 檢查 → 不合格就退回修改 → 直到通過**

**你不需要背任何指令。** 你只要用中文寫 prompt（或寫一份任務檔 `task.md`），交給 Supervisor（agy），由它去操作 Herdr、指揮小模型、驗收成果。

每關的任務都很小，每關只多學一個新概念。每關最後都有**變化題**，請換題目再做 2～3 次，練到熟為止。對指令有興趣的同學，每關最下方另有「🔧 進階：自己下指令」。

觀念說明請看 👉 [Supervisor 與 SubAgent 終端協同指南](../supervisor-subagent.md)。

---

## 角色分配

| 角色 | 誰 | 做什麼 |
| :--- | :--- | :--- |
| 🧑‍🎓 **你** | 學生 | 寫 prompt 或任務檔，交代要做什麼、怎麼算合格 |
| 👑 **Supervisor** | agy（Antigravity CLI） | 看懂你的要求，開窗格、派工給小模型、親自驗收 |
| 🛠️ **SubAgent** | OpenCode + 免費模型 | 只負責把被交辦的小任務做完 |

---

## 關卡地圖

| 關 | 主題 | 你要學會的事 | 題材 |
| :--- | :--- | :--- | :--- |
| [第 0 關](00-panes/README.md) | 認識窗格 | 用 prompt 請 Supervisor 開窗格、執行指令、回報結果 | — |
| [第 1 關](01-first-subagent/README.md) | 第一次派工 | 寫任務檔，請 Supervisor 派工給小模型並驗收 | 程式 |
| 第 2 關 | 不合格就退回 | 寫清楚驗收標準，觀察 Supervisor 退回修改 | 文件 |
| 第 3 關 | 自動測試把關 | 用測試檔當驗收標準，多輪修改直到通過 | 程式 |
| 第 4 關 | 隔離與審查 | 讓小模型在獨立分支工作，審查後才合併 | 文件 |
| 第 5 關 | 兩個小模型分工 | 一個寫程式、一個寫說明文件 | 程式＋文件 |

> 第 2～5 關製作中。

---

## 開始前的準備（只需做一次）

### 1. 確認工具都已安裝

在終端機輸入以下指令，每一行都有顯示版本號就可以了：

```bash
herdr --version
opencode --version
agy --version
```

安裝方式請參考 [Herdr 操作指南](../README.md) 與 [OpenCode 操作指南](../../opencode/README.md)。

### 2. 建立練習資料夾，放入 Supervisor 規則檔

```bash
mkdir -p ~/herdr-lab
cd ~/herdr-lab
curl -fsSLO https://raw.githubusercontent.com/roberthsu2003/vibe_coding_harness/main/herdr/practice/SUPERVISOR.md
```

[`SUPERVISOR.md`](SUPERVISOR.md) 是給 agy 看的「主管工作手冊」：告訴它該怎麼派工、怎麼驗收，以及 Herdr 指令怎麼用。**你不用看懂它**，只要放在資料夾裡就好。

> [!IMPORTANT]
> 檔名一定要是 `SUPERVISOR.md`，**不要改名成 `AGENTS.md`**。小模型（OpenCode）會自動讀取 `AGENTS.md`，讀到之後會誤以為自己是主管而卡住。

### 3. 進入 Herdr，啟動 Supervisor

```bash
herdr
```

進入 Herdr 後，在窗格裡（確認目前位置是 `~/herdr-lab`）啟動 agy：

```bash
agy
```

第一次在這個資料夾啟動時，agy 會問 **Do you trust the contents of this project?**，直接按 **Enter**（選 Yes）。若出現其他提示訊息，按 **Esc** 關掉即可。

### 4. 學會一件事：允許 Supervisor 使用 herdr 指令

當 agy 要執行指令時，會跳出確認畫面：

```text
Requesting permission for:
   herdr pane split ...
Run this command?
> 1. Yes, run command
  2. Yes, and always allow in this conversation for commands that start with 'herdr'
  3. Yes, and always allow for commands that start with 'herdr' (Persist to settings.json)
  4. No, cancel
```

請用 **↓** 選 **2**，再按 **Enter**。這表示「這次對話中，herdr 開頭的指令都不用再問我」。之後如果出現其他指令（例如 `python3`），先看清楚它要做什麼，再決定要不要允許。

---

## 寫 prompt 的三個小原則

1. **每次開新的 agy，第一句話先說「請先閱讀 SUPERVISOR.md」**，它才知道自己是主管。
2. **說清楚「要做什麼」和「怎麼算合格」**，例如「結果必須是 32.0 212.0 -40.0」。
3. **說清楚「誰來做」**：要它「開一個 SubAgent 來寫」，不要讓主管自己動手。

---

## 常見狀況

| 狀況 | 怎麼辦 |
| :--- | :--- |
| 右邊窗格出現 `Endpoint is unavailable` | 免費模型伺服器忙碌，不是你的錯。對 agy 說「請換一個免費模型重新派工」 |
| agy 好像停住、沒有反應 | 看看畫面是不是在等你按確認（見準備第 4 步） |
| 窗格太窄，字都擠在一起 | 用滑鼠點一下該窗格，按 `prefix+z` 放大，再按一次還原 |
| 想重新開始 | 按 `prefix+x` 關掉 agy 所在的窗格，再開一個新窗格輸入 `agy`，記得第一句先說「請先閱讀 SUPERVISOR.md」 |
