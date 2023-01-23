import sys
from unityparser import UnityDocument

targetAssetPath = sys.argv[1]

doc = UnityDocument.load_yaml(targetAssetPath)
doc.dump_yaml("./dump.yaml")
targetAsset = doc.entry

print(targetAsset.m_Script)