# 第 0 關：認識窗格

← [回到關卡地圖](../README.md)

## 學習目標

用一句中文 prompt，請 Supervisor（agy）幫你：

1. 在旁邊開一個新窗格。
2. 在新窗格執行指令。
3. 把結果「讀回來」告訴你。
4. 用完把窗格關掉。

這就是 Supervisor 指揮別人的基本功：**開窗格 → 執行 → 讀回結果 → 收尾**。之後每一關都會用到。

## 前置條件

完成 [開始前的準備](../README.md#開始前的準備只需做一次)：`~/herdr-lab` 裡有 `SUPERVISOR.md`，並且已在 Herdr 裡啟動 agy。

---

## 動手做

### 步驟 1：輸入 prompt

在 agy 裡輸入（可以直接複製）：

```text
請先閱讀 SUPERVISOR.md。然後幫我在右邊開一個新窗格，在裡面執行 ls -a 和 python3 --version，把看到的結果告訴我，最後把那個窗格關掉。
```

### 步驟 2：允許 herdr 指令

agy 要執行 `herdr` 指令時會問你，選 **2**（本次對話都允許 herdr 開頭的指令）。可能會問一到兩次。

### 步驟 3：觀察

一邊看 agy 的回覆，一邊注意畫面變化：

- 右邊是不是**多出一個窗格**，裡面出現了 `ls -a` 的結果？
- 你的游標有沒有被搶走？（應該沒有，還留在 agy 這邊）
- 最後那個窗格是不是**自己消失了**？

## 預期結果

agy 會回報類似這樣的內容：

```text
1. 開啟右側新窗格：執行了 herdr pane split ...，建立了窗格（ID 為 w1:p3）
2. 在新窗格執行指令：herdr pane run w1:p3 "ls -a && python3 --version"
3. 讀取窗格畫面輸出：herdr pane read w1:p3 ...
4. 關閉窗格：herdr pane close w1:p3

看到的結果
• ls -a：.  ..  SUPERVISOR.md
• python3 --version：Python 3.14.6
```

## 想一想

- agy 是怎麼「看到」另一個窗格的內容的？（提示：看它回報的第 3 步）
- 每個窗格都有一個 ID（像 `w1:p3`）。為什麼 Supervisor 需要知道這個 ID？

---

## 變化題（換個要求再做 2～3 次）

1. ```text
   幫我在下方開一個新窗格，執行 date 和 whoami，告訴我結果後關掉窗格。
   ```
2. ```text
   幫我開兩個窗格，一個執行 pwd，另一個執行 python3 -c "print(1+1)"，分別告訴我結果，最後兩個都關掉。
   ```
3. ```text
   幫我開一個窗格，執行 sleep 5; echo 全部完成，等它真的印出「全部完成」之後再告訴我，然後關掉窗格。
   ```
   想一想：Supervisor 怎麼知道要「等」？

完成後 → [第 1 關：第一次派工](../01-first-subagent/README.md)

---

## 🔧 進階：自己下指令（選修）

想知道 agy 背後到底執行了什麼？在 Herdr 的另一個 shell 窗格裡，親手做一次一樣的事。

> 需要 `jq`（用來從 JSON 取出資料）：沒有的話先執行 `brew install jq`。

```bash
# 1. 開右側窗格，取出新窗格的 ID
WORKER=$(herdr pane split --current --direction right --no-focus | jq -r '.result.pane.pane_id')
echo $WORKER                     # 例如 w1:p3

# 2. 在那個窗格執行指令
herdr pane run $WORKER "ls -a; python3 --version"

# 3. 把輸出讀回來
herdr pane read $WORKER --source recent-unwrapped --lines 10

# 4. 等某段文字出現再讀（--timeout 單位是毫秒）
herdr pane run $WORKER "sleep 3; echo 全部完成"
herdr pane wait-output $WORKER --match "全部完成" --timeout 10000

# 5. 收尾
herdr pane close $WORKER
```

| 參數 | 意思 |
| :--- | :--- |
| `--current` | 以「你現在所在的窗格」為基準分割 |
| `--no-focus` | 不要把游標移到新窗格 |
| `--source recent-unwrapped` | 讀最近的輸出，並把被自動換行切斷的長行接回來 |

> [!IMPORTANT]
> Pane ID 一定要從指令回傳的 JSON 讀出來，不要自己猜。關掉的窗格 ID 不會重複使用。

| 錯誤訊息 | 原因與解法 |
| :--- | :--- |
| `echo $WORKER` 是空的 | 沒有安裝 `jq`，或 split 指令打錯 |
| `pane_not_found` | ID 打錯，或窗格已關閉。用 `herdr pane list` 查看所有窗格 |
| `wait-output` 一直等不到 | `--match` 的文字和實際輸出不一樣（全半形都要一致） |
