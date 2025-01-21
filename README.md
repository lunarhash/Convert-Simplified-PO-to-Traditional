# PO檔案簡繁轉換工具

這是一個用於將PO檔案中的簡體中文轉換為繁體中文的工具。本工具特別適用於需要處理大量翻譯文件的場景，可以保持原始檔案結構的同時，準確地將簡體中文轉換為繁體中文。

## 功能特點

- 完整保持PO檔案的原始結構
- 只轉換翻譯文本（msgstr部分）
- 使用OpenCC確保高品質的簡繁轉換
- 支援大型PO檔案處理（10000行以上）
- 保持檔案的行數和格式完全一致
- 使用方便的命令列介面

## 安裝說明

1. 確保已安裝Python 3.6或更高版本
2. 克隆此專案：
```bash
git clone https://github.com/yourusername/po-converter.git
cd po-converter
```

3. 安裝依賴套件：
```bash
pip install -r requirements.txt
```

## 使用方法

### 基本用法

```bash
python po_converter.py input.po -o output.po
```

### 參數說明

- `input.po`：輸入的PO檔案路徑（必需）
- `-o output.po`：輸出檔案路徑（可選，如果不指定將自動生成）

### 使用範例

1. 基本轉換：
```bash
python po_converter.py messages.po -o messages_tw.po
```

2. 不指定輸出檔案（將自動生成）：
```bash
python po_converter.py messages.po
```

## 注意事項

1. 轉換過程會保持以下內容不變：
   - 檔案結構
   - 註釋
   - msgid（原文）
   - 檔案格式和編碼

2. 只會轉換 msgstr 開頭的行中的中文文本

3. 建議在轉換前先備份原始檔案

## 常見問題

Q: 為什麼要選擇這個工具？
A: 本工具特別注重保持PO檔案的原始結構，這對於版本控制和差異比對特別重要。

Q: 支援多大的檔案？
A: 本工具已經過測試，可以處理超過10000行的大型PO檔案。

Q: 轉換是否準確？
A: 使用OpenCC進行轉換，這是一個成熟的開源簡繁轉換引擎，具有較高的準確性。

## 貢獻指南

歡迎提交問題報告和改進建議！請遵循以下步驟：

1. Fork 本專案
2. 創建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟一個 Pull Request

## 授權協議

本專案採用 MIT 授權協議 - 詳見 [LICENSE](LICENSE) 檔案

## 聯絡方式

如有任何問題或建議，歡迎通過以下方式聯絡：

- 提交 Issue
- 發送 Pull Request

## 致謝

感謝 OpenCC 專案提供優質的中文轉換引擎。
