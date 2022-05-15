#%%
import os
#%%
files = []
files.append(os.path.abspath("../tmpl/category_ver_1.md"))
files.append(os.path.abspath("../tmpl/slides_ver_1.md"))
out_md_file=os.path.abspath("../out/slides_ver_1.md")
# %%
with open(out_md_file, "w") as out_file:
    for file in files:
        with open(file) as in_file:
            out_file.write(in_file.read())


# %%
print(os.path.dirname(os.path.abspath(__file__)))
# %%
