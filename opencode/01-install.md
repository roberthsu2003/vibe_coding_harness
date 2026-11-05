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

## ✅ 自我檢查

- [ ] `opencode --version` 顯示 `2.` 開頭的版本號
- [ ] 用 `/connect` 連接了供應商
- [ ] 用 `/models` 選好模型，並問了它一個問題，得到回覆

> 下一站：[02 基本操作 →](02-basics.md)
