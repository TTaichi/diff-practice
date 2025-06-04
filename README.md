# diff-practice
かめさんGit動画講座diff練習用

## 環境設定とインストール

Python 3.8 以上が推奨です。任意のディレクトリで仮想環境を作成し、依存パッケージをインストールします。

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install transformers torch
```

## Chatbot Example

`chatbot.py` は、[`transformers`](https://github.com/huggingface/transformers) ライブラリを使用したシンプルな生成AIチャットボットのデモです。実行するには、`transformers` パッケージと関連モデルのダウンロードが必要です。

```
python chatbot.py
```

`quit` と入力するまで対話を続けられます。
