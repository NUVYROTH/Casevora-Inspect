# Casevoras 衛生缺失追蹤助手（品牌名稱統一為 Casevoras）

## 兩個版本，每次修改都要一起更新

| 版本 | 位置 | 說明 |
|---|---|---|
| 網址版 | GitHub 倉庫 `NUVYROTH/Casevora-Inspect` 的 `main` → https://nuvyroth.github.io/Casevora-Inspect/ | 公開，沒有 AI 分析 |
| claude.ai 版 | https://claude.ai/artifact/LyD33BcGzozJwyHXEVQG77 | 私人，只給擁有者與品管使用（不分享給朋友），有「產生分析」 |

- 原始檔只有一份：`index.html`。
- **每次修改都要兩邊一起更新。claude.ai 版一律用上面同一個網址更新（Artifact 工具帶 `url`），不要建立新的 artifact。**
- 更新 claude.ai 版的步驟：
  1. `python3 tools/build_claude_html.py <暫存資料夾>/hygiene-claude.html`
  2. 用 Artifact 工具發布該檔案，`url` 填上面的 claude.ai 版網址。
  3. capabilities 維持 `{"sample": {}, "downloads": true}`。**不要宣告 `db`**（資料只存在各自瀏覽器）。

## 修改流程

1. 先開 `preview-xxx` 分支修改並推上去（GitHub Pages 只發布 `main`，所以不影響網站）。
2. 用假資料測試（例：王小明、作業員 A、包裝區積水），電腦與手機尺寸都測。
3. 擁有者確認「可以上線」後才合併到 `main`，並同步更新 claude.ai 版。

## 不能改變的原則

- 程式碼裡不能有任何金鑰（API key、`service_role` 等）。
- AI 分析用「使用者自己的 Claude 帳號」（`claude.use('sample')`），不串 API 金鑰；照片不送給 AI。
- AI 分析建議只顯示在右欄，**不自動儲存**；「套用這張缺失單」會套用類別、描述、等級，要使用者按鈕並確認，再按儲存。
- AI 依 `toolkit/缺失等級判定規則.md` **建議**缺失等級並說明依據，最終由品管人員確認；建議改善期限不自動填入；AI 不判定結案、不寫人名。
- claude.ai 不顯示 alert／confirm 視窗、不能列印：一律用頁面內的 `ask()`／`say()`；列印功能在 claude.ai 版提示改用網址版。
- 頁面上的誠實文案（本機儲存、僅在此裝置此瀏覽器有效）不能拿掉。
- 照片存在 IndexedDB（資料庫名稱 `qaHygienePhotos`），案件資料只記 `ph:編號`；備份檔要放照片本身（data URL），還原時再搬回 IndexedDB。照片不可存到雲端（不用 `assets`／`db`）。
- 安安的條件：claude.ai 版只給擁有者與品管使用；要給朋友時另外做工具包（提示詞＋說明），不分享這個工具。

## 待辦

- 工具包（`toolkit/`）：販售前要再整理，並依安安建議只賣提示詞＋說明。
- 「缺失類別」清單有變動時，`index.html` 的 `TYPES` 與 `toolkit/缺失類別清單.md` 要一起改。
