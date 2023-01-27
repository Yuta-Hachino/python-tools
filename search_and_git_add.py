# 任意で指定されたディレクトリ内を検索し、一致したファイル群にgit addを実行する。
# ※対象ファイルが存在し且つ変更がある場合

import sys
import glob
import git

searchTargetPath = sys.argv[1]
print("searchTargetPath:", searchTargetPath)
searchWord = sys.argv[2]
print("searchWord:", searchWord)

files = glob.glob(searchTargetPath + searchWord, recursive=True)

repo = git.Repo(searchTargetPath)

# 変更があった場合のみAddする
if repo.git.diff() == '':
    for name in files:
        print(name)
        repo.git.add(name)
