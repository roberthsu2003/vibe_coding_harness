# 01　安裝與連線

> ★ 入門　｜　[章節首頁](README.md)　｜　下一站：[02 基本操作 →](02-basics.md)

**這一站你會學到**：安裝 OpenCode、連接模型供應商、使用免費模型。

---

## 1. 安裝

| 方式 | 指令 |
| :--- | :--- |
| 官方安裝腳本（macOS / Linux） | `curl -fsSL https://opencode.ai/install \| bash` |
| Homebrew | `brew install anomalyco/tap/opencode` |
| npm | `npm install -g opencode-ai` |
| Windows（Scoop） | `scoop install opencode` |

> Windows 官方建議在 WSL 裡使用，體驗最好。

## 2. 確認安裝成功

```bash
opencode --version
```

看到版本號（例如 `1.19.2`）就成功了。

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

1. 選擇供應商。使用 OpenCode 自家的模型（含免費模型）請選 **opencode**。
2. 依畫面指示到 [opencode.ai/auth](https://opencode.ai/auth) 登入，取得 API Key。
3. 把 API Key 貼回 OpenCode。

> 也可以選擇 Anthropic、OpenAI、Google 等其他供應商，依畫面指示登入即可。

## 4. 選擇模型

在輸入框輸入 `/models`，搜尋並選擇模型。本教材推薦的免費模型：

| 用途 | 模型 | 說明 |
| :--- | :--- | :--- |
| 預設 | `opencode/muse-spark-1.3-contributor-free` | Muse Spark 免費版，速度快 |
| 備用 | `opencode/nemotron-3.5-lightning-free` | NVIDIA Nemotron 免費版，速度較慢 |

也可以在啟動時直接指定：

```bash
opencode -m opencode/muse-spark-1.3-contributor-free
```

> 免費模型偶爾會因為伺服器忙碌出現 `Endpoint is unavailable`，換成備用模型即可。

---

## ✅ 自我檢查

- [ ] `opencode --version` 有顯示版本號
- [ ] 用 `/connect` 連接了供應商
- [ ] 用 `/models` 選好模型，並問了它一個問題，得到回覆

> 下一站：[02 基本操作 →](02-basics.md)
