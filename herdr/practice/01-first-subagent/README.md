# 第 1 關：第一次派工

← [回到關卡地圖](../README.md)　｜　上一關：[第 0 關](../00-panes/README.md)

## 學習目標

1. 學會寫一份**任務檔 `task.md`**：說清楚「要做什麼、誰來做、怎麼驗收」。
2. 請 Supervisor（agy）依照任務檔，**派工給小模型（SubAgent）**。
3. 觀察 Supervisor **親自驗收**，而不是只相信小模型說「完成」。

> 💡 為什麼要寫成檔案，而不是直接打一長串 prompt？
> 任務檔可以存下來、修改、重複使用。要換題目時，只要改檔案內容，prompt 都不用變。

## 前置條件

完成 [第 0 關](../00-panes/README.md)。

---

## 動手做

### 步驟 1：準備任務檔

在 `~/herdr-lab` 建立 `task.md`，內容如下（也可以直接下載 [範例檔](task.md)）：

```markdown
# 任務：溫度轉換

## 要做什麼
建立 `temperature.py`，裡面寫一個函式 `celsius_to_fahrenheit(c)`，把攝氏溫度轉成華氏溫度。

## 誰來做
請開一個 SubAgent（名字叫 coder）來寫，你不要自己寫。

## 怎麼驗收
執行：
python3 -c "from temperature import celsius_to_fahrenheit as f; print(f(0), f(100), f(-40))"
結果必須是 32.0 212.0 -40.0
```

下載範例檔的方式：

```bash
cd ~/herdr-lab
curl -fsSLO https://raw.githubusercontent.com/roberthsu2003/vibe_coding_harness/main/herdr/practice/01-first-subagent/task.md
```

> 💡 也可以直接請 agy 幫你建立：「請幫我建立 task.md，內容是……」。

### 步驟 2：輸入 prompt

在 agy 裡輸入（如果是剛開的 agy，記得先加上「請先閱讀 SUPERVISOR.md。」）：

```text
請依照 task.md 完成任務，做完告訴我驗收結果。
```

遇到確認畫面時，`herdr` 指令選 **2**；其他指令（例如 `python3`）看清楚後再允許。

### 步驟 3：觀察三個角色

| 看哪裡 | 你會看到 |
| :--- | :--- |
| 🧑‍🎓 你的 agy 窗格 | agy 說明它開了窗格、啟動了 coder、派了什麼任務 |
| 🛠️ 右邊新窗格 | OpenCode 啟動，小模型開始寫 `temperature.py` |
| 👑 agy 驗收 | 小模型做完後，agy 自己執行驗收指令，比對 `32.0 212.0 -40.0` |

整個過程大約 1～2 分鐘。

## 預期結果

agy 最後會回報類似：

```text
3. 親自驗收：
   • 檢查 temperature.py 內容：
     def celsius_to_fahrenheit(c):
         return c * 9 / 5 + 32
   • 輸出結果為：32.0 212.0 -40.0
4. 清理窗格：關閉剛剛為 SubAgent 開啟的右側窗格。

驗收結論：驗收通過
```

`~/herdr-lab` 裡會多出 `temperature.py`。

## 想一想

- 如果 `task.md` 沒有寫「怎麼驗收」，agy 要怎麼判斷小模型做得對不對？
- 為什麼要叫 agy「不要自己寫」？讓聰明的模型自己寫不是更快嗎？（提示：想想費用，以及「由另一個人檢查」的好處）

---

## 變化題（只改 task.md，prompt 不變）

每次都改寫 `task.md` 的內容，再輸入同一句 prompt：「請依照 task.md 完成任務，做完告訴我驗收結果。」

1. **BMI 計算**
   - 要做什麼：建立 `bmi.py`，函式 `bmi(weight_kg, height_m)` 回傳 BMI，四捨五入到小數第 1 位。
   - 怎麼驗收：`python3 -c "from bmi import bmi; print(bmi(70, 1.75))"` 結果必須是 `22.9`。
2. **成績等第**
   - 要做什麼：建立 `grade.py`，函式 `grade(score)`：90 以上回傳 `"A"`、80～89 回傳 `"B"`、其餘回傳 `"C"`。
   - 怎麼驗收：`python3 -c "from grade import grade; print(grade(95), grade(85), grade(60))"` 結果必須是 `A B C`。
3. **自己出題**：想一個簡單的小函式，自己寫出「要做什麼」和「怎麼驗收」。

> 🎯 **挑戰**：在變化題 1 的 task.md 加一行「請使用 opencode/glm-5.3-flash-free 模型」，看看 agy 會不會照做。

完成後 → 第 2 關：不合格就退回（製作中）

---

## 🔧 進階：自己下指令（選修）

想知道 agy 背後做了什麼？在 Herdr 的另一個 shell 窗格，親手當一次 Supervisor：

```bash
mkdir -p ~/herdr-lab/manual && cd ~/herdr-lab/manual

# 1. 開工作窗格（--cwd 讓新窗格和你在同一個資料夾）
WORKER=$(herdr pane split --current --direction right --cwd "$PWD" --no-focus | jq -r '.result.pane.pane_id')

# 2. 啟動 SubAgent，取名 coder；-- 後面的參數交給 OpenCode，-m 指定模型
herdr agent start coder --kind opencode --pane $WORKER -- -m opencode/deepseek-v4.1-flash-free

# 3. 派工並等它做完（--timeout 單位是毫秒，300000 = 5 分鐘）
herdr agent prompt coder "你是 SubAgent，只負責完成下面的任務，不要執行任何 herdr 指令。請在 temperature.py 寫一個函式 celsius_to_fahrenheit(c)，回傳華氏溫度。完成後回覆「完成」。" --wait --timeout 300000

# 4. 看狀態、讀回覆
herdr agent get coder | jq -r '.result.agent.agent_status'
herdr agent read coder --source recent-unwrapped --lines 40

# 5. 親自驗收
python3 -c "from temperature import celsius_to_fahrenheit as f; print(f(0), f(100), f(-40))"

# 6. 收尾（裡面的 OpenCode 會一起結束）
herdr pane close $WORKER
```

| 狀態 | 意思 | 該做什麼 |
| :--- | :--- | :--- |
| `idle` / `done` | 做完了，等待下一個指令 | 驗收 |
| `working` | 還在做 | `herdr agent wait coder --timeout 300000` |
| `blocked` | 跳出確認或提問畫面 | `herdr agent read coder --source visible` 看它在問什麼 |

| 錯誤訊息 | 原因與解法 |
| :--- | :--- |
| `agent_name_taken` | 已經有叫 `coder` 的 Agent，換個名字或先關掉舊窗格 |
| `agent_blocked` | Agent 正在等人回應，先讀畫面看它在問什麼 |
| `Endpoint is unavailable` | 免費模型忙碌，關掉窗格換模型重新開始 |

> [!WARNING]
> 不要在練習資料夾放 `AGENTS.md`。OpenCode 會自動讀它；如果裡面寫著「你是 Supervisor」，小模型會誤以為自己是主管，跑去用 herdr 查詢自己的狀態而卡住。這也是為什麼主管規則檔要取名為 `SUPERVISOR.md`。
