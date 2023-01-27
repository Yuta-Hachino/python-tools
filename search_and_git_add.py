import sys
import glob
import git

searchTargetPath = sys.argv[1]
print("searchTargetPath:", searchTargetPath)
searchWord = sys.argv[2]
print("searchWord:", searchWord)

files = glob.glob(searchTargetPath + searchWord, recursive=True)

repo = git.Repo(searchTargetPath)

for name in files:
    print(name)
    repo.git.add(name)
