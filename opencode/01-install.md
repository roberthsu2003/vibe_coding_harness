# 01　安裝與連線

> ★ 入門　｜　[章節首頁](README.md)　｜　下一站：[02 基本操作 →](02-basics.md)

**這一站你會學到**：安裝 OpenCode、連接模型供應商、使用免費模型。

---

## 1. 安裝

選一種方式就好，建議用官方安裝腳本：

| 方式 | 指令 |
| :--- | :--- |
| 官方安裝腳本（macOS / Linux / WSL） | `curl -fsSL https://opencode.ai/v2/install \| bash` |
| Homebrew | `brew install anomalyco/tap/opencode-v2` |
| npm | `npm install -g @opencode/cli` |

> Windows 請在 WSL 裡使用，或到官網下載獨立執行檔。OpenCode 2 不支援 Windows 的套件管理工具（例如 Scoop）。

> [!NOTE]
> **已經裝了舊版 OpenCode 1？** 執行 `opencode upgrade --major` 升級。OpenCode 1 和 2 使用同一個指令名稱，升級時會取代舊版。

## 2. 確認安裝成功

```bash
opencode --version
```

看到 `2.` 開頭的版本號（例如 `2.0.32`）就成功了。

---

## 開始前：建立本節練習資料夾

先完成[課堂練習準備](../practice/README.md)的工具確認與教材下載，再在**一般終端機**逐行執行：

```bash
python3 ~/terminal-ai-course/practice/prepare.py ~/terminal-ai-labs/opencode/01
cd ~/terminal-ai-labs/opencode/01
```

看到目的資料夾已存在時，直接 `cd` 進去接續；要重做則把路徑最後一段改成 `01-retry`。本節的程式、筆記與初始 Git commit 都已準備好。

## 3. 連接模型供應商

OpenCode 要連到 AI 模型才能工作。在專案資料夾啟動：

```bash
opencode
```

在 OpenCode 的輸入框輸入（不是在一般終端機）：

```text
/connect
```

1. 選擇 **OpenCode Console**（OpenCode 自家的服務，含免費模型）。
2. 依畫面指示登入，取得 API Key。
3. 把 API Key 貼回 OpenCode。

> 也可以選擇 Anthropic、OpenAI、Google 等其他供應商，依畫面指示登入即可。已連接的供應商前面會有 ✓。

## 4. 選擇模型

在輸入框輸入 `/models`，打 `free` 搜尋，選一個右邊標示 `Free` 的模型。本教材推薦：

| 用途 | 模型 | 說明 |
| :--- | :--- | :--- |
| 預設 | `opencode/nemotron-3.5-lightning-free` | NVIDIA Nemotron 免費版 |
| 備用 | `opencode/nemotron-3.5-super-vl-free` | 同系列的另一個免費版，速度可能較慢 |

也可以用一行指令，指定模型來試試看：

```bash
opencode run -m opencode/nemotron-3.5-lightning-free "你好"
```

> [!IMPORTANT]
> 本教材**不使用中國大陸的模型**（例如 DeepSeek、GLM、MiMo、Kimi、Qwen、Hy）。清單裡看到它們時請略過。沒有指定模型時，OpenCode 可能自動選到它們，所以建議照 [04 環境配置](04-config.md#固定預設模型)把預設模型固定下來。

> [!NOTE]
> 免費模型的名單會變動，也可能因為伺服器忙碌而無法使用。遇到問題就用 `/models` 換一個，或查看[疑難排解](reference.md#2-疑難排解)。

---

## 完整小練習：連線、選模型、讀取素材

1. 在本章練習資料夾啟動 `opencode`，執行 `/connect` 完成登入。
2. 輸入 `/models`，搜尋 `free`，從目前可用的非中國大陸模型中選擇一個標示 `Free` 的模型；記下完整模型 ID。若沒有符合條件的免費模型，使用自己已有額度的供應商模型。
3. 在對話框送出：

```text
請閱讀 README.md 與 main.py，用三點繁體中文說明用途、執行方式與測試指令。先不要修改任何檔案。
```

**驗收**：輸入框下方顯示剛選的模型；回答包含 `python3 main.py` 與 `python3 -m unittest discover -s tests -v`。另開終端機進入本章資料夾執行 `git status --short`，應無輸出。

最後輸入 `/exit`，在一般終端機執行上面的 `opencode run ... "你好"`。若範例模型 ID 已下架，換成第 2 步記下的 ID；看到文字回答並回到 shell 提示符即完成。

## ✅ 自我檢查

- [ ] `opencode --version` 顯示 `2.` 開頭的版本號
- [ ] 用 `/connect` 連接了供應商
- [ ] 用 `/models` 選好模型，並問了它一個問題，得到回覆

> 下一站：[02 基本操作 →](02-basics.md)
