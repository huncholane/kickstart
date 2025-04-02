from pathlib import Path, PosixPath


def dfs(root: Path):
    if root is None:
        return 0
    size = 0  # preorder init
    if root.is_file():
        size = root.stat().st_size

    for f in root.glob("*"):
        size += dfs(f)
    return size  # postorder result


print(dfs(Path("filesizetest")))
