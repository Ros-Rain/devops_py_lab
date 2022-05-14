import os
import markdown2output_ver_1 as m2o

home_abspath = os.path.dirname(os.path.abspath(__file__))

tmpl_category_file = os.path.abspath(home_abspath + "/../tmpl/category_ver_1.md")
tmpl_slides_file = os.path.abspath(home_abspath + "/../tmpl/slides_ver_1.md")

out_md_file=os.path.abspath(home_abspath + "/../out/slides_ver_1.md")
out_pptx_file=os.path.abspath(home_abspath + "/../out/slides_ver_1.pptx")

# объединить файлы в один в директории out
tmpl_files = []
tmpl_files.append(tmpl_category_file)
tmpl_files.append(tmpl_slides_file)

with open(out_md_file, "w") as out_file:
    for f in tmpl_files:
        with open(f) as in_file:
            out_file.write(in_file.read())

m2o.convert_to_pptx(out_md_file, out_pptx_file)  # преобразовать в pptx 

