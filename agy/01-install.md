# 01　安裝與登入

> ★ 入門　｜　[章節首頁](README.md)　｜　下一站：[02 基本操作 →](02-basics.md)

**這一站你會學到**：安裝 Antigravity CLI (`agy`)、進行身分認證登入，以及查看可用模型。

---

## 1. 安裝與設定環境

`agy` 是 Antigravity 的終端命令列工具。可透過官方安裝工具或套件管理工具安裝，安裝後可透過內建指令配置 Shell 環境：

```bash
# 配置環境路徑與 Shell 自動補全
agy install
```

## 2. 確認安裝成功

執行以下指令確認 `agy` 指令已正確加入至 PATH：

```bash
which agy
```

看到執行路徑（例如 `/Users/.../.gemini/antigravity/bin/agy`）且可以執行 `agy help` 即代表安裝成功。

---

## 3. 登入與身分認證

在專案目錄下啟動 `agy`：

```bash
cd ~/my-project
agy
```

如果是第一次執行，`agy` 會在終端機中顯示認證提示：
1. 終端機會顯示登入連結或驗證碼。
2. 依照指示在瀏覽器中完成 Google 帳號授權。
3. 授權成功後，終端機會自動儲存憑證並進入互動對話介面。

---

## 4. 查看與選擇模型

`agy` 支援多種強大的大型語言模型與快速推理模型。

### 列出所有可用模型

在一般終端機中執行：

```bash
agy models
```

輸出範例：

```text
gemini-4-argon-medium     Gemini 4 Argon (Medium)
gemini-4-argon-high       Gemini 4 Argon (High)
gemini-3.8-flash-high     Gemini 3.8 Flash (High)
gemini-3.8-flash-medium   Gemini 3.8 Flash (Medium)
claude-sonnet-5-5-medium  Claude Sonnet 5.5 (Medium)
```

### 啟動時指定模型

如果想針對複雜重構或快速修復選用特定模型，可在啟動時透過 `--model` 指定：

```bash
# 使用高推理強度模型
agy --model gemini-4-argon-high

# 使用快速響應模型
agy --model gemini-3.8-flash-medium
```

也可以設定推理事實強度（Reasoning Effort）：

```bash
agy --model gemini-3.8-flash-high --effort high
```

---

← [章節首頁](README.md)　｜　下一站：[02 基本操作 →](02-basics.md)

