# md2tree

`md2tree` は，インデント付きの Markdown 箇条書きを，Unix の `tree` コマンド風のテキストツリーに変換するシンプルな Python スクリプトです．

## Features

- Markdown のリスト構造（スペース + `-`）から階層構造を解析
- ネストされたリストをツリー記法（`├──` / `└──` / `│`）で表示
- 結果を標準出力とファイルの両方に出力可能

## Requirements

- 動作確認済み環境: Python 3.13.2（標準ライブラリのみ使用）

## Files

- `md2tree.py` : メインのスクリプト
- `sample_input.md` : サンプルの Markdown 入力
- `sample_output.txt` : サンプルの出力結果
- `input.md` : 実際に処理したい Markdown（`.gitignore` で無視推奨）
- `tree_output.txt` : 出力されるツリー（`.gitignore` で無視推奨）

## Usage

1. `input.md` に、次のような Markdown の箇条書きを用意します．

   例（`sample_input.md` と同等）:
    ```markdown 
   - Projects  
     - Web  
       - Portfolio  
       - Blog  
     - Scripts  
       - Python  
         - md2tree  
         - file_cleaner  
       - Bash  
   - Notes  
     - University  
       - Research  
       - Assignments  
     - Personal  
       - Ideas  
       - Reading List  
    
2. スクリプトを実行します．

   python md2tree.py

3. カレントディレクトリに `tree_output.txt` が生成され，ターミナルにもツリー構造が表示されます．

## Example

上記のサンプル入力に対して、出力は次のようになります（`sample_output.txt` と同等）:
```text
.
├── Projects
│   ├── Web
│   │   ├── Portfolio
│   │   └── Blog
│   └── Scripts
│       ├── Python
│       │   ├── md2tree
│       │   └── file_cleaner
│       └── Bash
└── Notes
    ├── University
    │   ├── Research
    │   └── Assignments
    └── Personal
        ├── Ideas
        └── Reading List
```
## Notes

- インデントは半角スペース 2 個を 1 レベルとして扱います．
- それ以外の Markdown 記法（番号付きリスト、チェックボックスなど）には対応していません．
- 処理対象のファイル名や出力先を変更したい場合は、`md2tree.py` 内のパス定義を調整してください．
