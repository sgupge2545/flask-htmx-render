# 🚀 Flask × HTMX Demo 🍏

ようこそ！このリポジトリは、**Flask + HTMX** を組み合わせて、**JavaScript ゼロで非同期通信・動的 DOM 更新を実現**した軽量 Web アプリケーションのサンプルです。

## ✨ このアプリでできること

- ✅ フロントエンドに**JavaScript 一切なし**
- ✅ 入力フォーム → 非同期 POST → 結果をその場で表示
- ✅ 名前によって異なるメッセージを表示
- ✅ スピナー表示（ローディング中の UI 付き）
- ✅ リセットボタンで元の状態に戻せる
- ✅ **Render で簡単にデプロイ可能**

![demo screenshot](https://user-images.githubusercontent.com/your-image-url.png) <!-- Optional: Add screenshot -->

---

## 🔧 使用技術

| 技術                                        | 説明                                          |
| ------------------------------------------- | --------------------------------------------- |
| [Flask](https://flask.palletsprojects.com/) | 軽量 Python Web フレームワーク                |
| [HTMX](https://htmx.org/)                   | HTML 属性で非同期通信などを実現するライブラリ |
| [Render](https://render.com/)               | Flask と相性抜群の無料ホスティングサービス    |

---

## 📦 セットアップ方法（ローカル）

```bash
git clone https://github.com/sgupge2545/flask-htmx-render.git
cd flask-htmx-render
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
