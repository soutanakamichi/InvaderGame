# インベーダーゲーム ver.1.0　<img src="https://img.shields.io/badge/Python-yellow?logo=python&logoColor=blue">
![インベーダーデモ](https://github.com/user-attachments/assets/89ca2934-b6a0-4d9c-8bd2-089ee379e505)
![インベーダーデモ2](https://github.com/user-attachments/assets/de36b5d6-1e4b-47f0-b657-49e004f859d2)<br>
かつてのアーケードゲームを彷彿とさせる、古き良きシューティングゲームです。<br>
自分に合った難易度を選んで、ハイスコアを目指しましょう！<br><br>

## 操作方法
[P]　　 　 　　：ゲーム開始（スタート画面のみ）<br>
[←矢印キー]　 ：左に移動（ゲーム画面のみ）<br>
[→矢印キー]　 ：右に移動（ゲーム画面のみ）<br>
[スペースキー]：弾を発射（ゲーム画面のみ）<br>
[Q]　　 　 　　：ゲーム終了<br>
[Enter]　　　　：プレイヤー名の入力完了<br>
<br>

## インストール方法
以下の手順で、プロジェクトをローカル環境にインストールしてください。

```bash
# リポジトリをクローン
git clone https://github.com/soutanakamichi/InvaderGame.git

# ディレクトリに移動
cd InvaderGame

# 依存関係をインストール
pip install -r requirements.txt

# ゲームを実行
python alien_invasion.py
```
<br>

## 工夫した点
1. ハイスコアのファイル保存機能
2. エイリアン（赤）ランダム生成機能
3. 衝突数に応じたベルのカラー変化機能
4. プレイヤー名とスコアのファイル保存機能
5. TOP5のプレイヤー名とスコアの画面表示機能
<br><br>

## ライセンス
当プロジェクトは、MITライセンスのもとで公開されています。<br><br>

## 免責事項
当プロジェクトの利用によって生じたあらゆる不具合やトラブルに対して、制作者は一切の責任を負いません。<br>
自己責任でご利用ください。
