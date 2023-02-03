## Jupyter Notebook の設定手順
1. 仮想環境設定
    - venv  
    `python -m venv .venv`
    - アクティベート  
    `. .venv/bin/activate`
2. ライブラリのインストール
    ```
    pip install --upgrade pip
    pip install notebook
    ```
3. ノートの作成  
    (VSCode CommandPallet)  
    Create:New Jupyter Notebook

[Jupyterのサイト](https://python-academia.com/matplotlib-bargraph/)

## Git の設定手順
1. 環境変数設定(最初の1回だけ)
```
git config --global user.name "XXXXX"
git config --global user.email XXXXX@XXXXX
```
2. ローカルリポジトリ作成
```
git init
```
3. Gitの管理対象外を設定
```
touch .gitignore
```

仮想環境のディレクトリを追加する

4. ステージング->コミット
```
git add .
git commit -m "XXXX"
```

5. リモートにプッシュ
```
git push origin master
```
6. リモートからプル(変更をローカルに反映させる)

7. 