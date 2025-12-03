import os

def parse_markdownTree(lines):
    """Markdownの箇条書きからツリー構造を生成する
    ARGS:
        lines (list[str]): インデント付きのMarkdown行

    RETURN:
        list[dict]: ルートノードのリスト。
            各ノードは {"text": str, "children": list} の辞書．
    """
    parent_stack = []  # いまの行の親までのノードを積んでおく
    tree = []
    indent_size = 2  # リストのインデント幅
    
    for line in lines:
        
        # 空行はスキップする
        if not line.strip():
            continue
        
        stripped = line.lstrip()                            # インデント(左側の空白)を消したもの
        level = (len(line) - len(stripped)) // indent_size  # Markdownのスペース数による階層
        node = {"text": stripped.lstrip("- ").strip(), "children": []}

        # スタックの深さを現在のレベルに合わせる
        while len(parent_stack) > level:
            parent_stack.pop()
        
        # 親がいれば親のchildrenに追加，いなければルートに追加
        if parent_stack: #stackの中になんか入っているか(親となるものがあるか)
            parent_stack[-1]["children"].append(node)
        else:
            tree.append(node)
        
        # 自分が次，親になるかもしれないのでstackの末尾に追加．
        parent_stack.append(node) 
   
    return tree

def render_tree2txt(tree, prefix=""):
    """ツリー構造をtreeコマンド風のテキストに変換する
    ARGS:
        tree (list[dict]): ネストされたツリー構造
        prefix (str): 行頭の接頭辞（│やスペース）

    RETURN:
        list[str]: 1行ずつの文字列リスト
    """
    output_lines = []

    for i, node in enumerate(tree):
        connector = "└── " if i == len(tree)-1 else "├── "
        output_lines.append(f"{prefix}{connector}{node['text']}")
        if node["children"]: # 子が存在したら再帰呼び出し
            output_lines.extend(render_tree2txt(
                node["children"],
                prefix + ("    " if i == len(tree) - 1 else "│   ")
            )
        )
    
    return output_lines
    

def save_to_txtfile(tree_lines, file_path):
    """ツリー(list)の中身をテキストファイルに出力"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(".\n")
        f.write("\n".join(tree_lines))


def main():
    SCRIPT_DIR      = os.path.dirname(os.path.realpath(__file__))
    MARKDOWN_FILE   = os.path.join(SCRIPT_DIR, "input.md")
    OUTPUT_FILE     = os.path.join(SCRIPT_DIR, "tree_output.txt")
    
    if not os.path.exists(MARKDOWN_FILE):
        print(f"Error: {MARKDOWN_FILE} が見つかりません")
        return

    # ファイルの読み込み
    with open(MARKDOWN_FILE, "r", encoding="utf-8") as f:
        markdown_list = f.readlines()
    
    # Markdownツリー解析，ツリーの生成
    tree = parse_markdownTree(markdown_list)
    text_tree = render_tree2txt(tree)
    
    # ツリーをテキストファイルに出力
    save_to_txtfile(text_tree, OUTPUT_FILE)
    print(f"\nツリーが {OUTPUT_FILE} に保存されました")
    

if __name__ == "__main__":
    main()