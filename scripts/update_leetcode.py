#!python
from pathlib import Path
import re

pwd = Path.cwd()
print("Currently in ", pwd.name)

if pwd.name != "leetcode":
    print(
        "Must be inside leetcode directory. This is to prevent overriding other readme"
    )
    exit(1)

section = " ".join([w.capitalize() for w in pwd.parent.name.split("_")[1:]])
print("Updating readme for", section, "leetcode problems")
readme = "# " + section + " Leetcode Problems 👨‍💻\n\n"
for folder, dirs, files in pwd.walk():
    if folder.name == "leetcode":
        continue
    title = None
    solution_count = 0
    for file in files:
        m = re.search(r"solution(\d+)", file)
        if m:
            solution_count = max(solution_count, int(m.group(1)))
        if file == "README.md":
            with open(folder / file, "r") as f:
                title = f.readline().replace("#", "-").strip()
    if title:
        readme += title
        if solution_count > 0:
            readme += " " + "✅" * solution_count
        else:
            readme += " 🔴"
        readme += "\n"

with open("README.md", "w") as f:
    _ = f.write(readme)
