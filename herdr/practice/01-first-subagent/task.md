# 任務：溫度轉換

## 要做什麼
建立 `temperature.py`，裡面寫一個函式 `celsius_to_fahrenheit(c)`，把攝氏溫度轉成華氏溫度。

## 誰來做
請開一個 SubAgent（名字叫 coder）來寫，你不要自己寫。

## 怎麼驗收
執行：
python3 -c "from temperature import celsius_to_fahrenheit as f; print(f(0), f(100), f(-40))"
結果必須是 32.0 212.0 -40.0
