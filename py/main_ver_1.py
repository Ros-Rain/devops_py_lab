import os
import markdown2output_ver_1 as m2o
import file_tools as ft

# путь запуска 
home_abspath = os.path.dirname(os.path.abspath(__file__))

# путь к рабочим файлам относительно пути запуска
tmpl_category_file = os.path.abspath(home_abspath + "/../tmpl/category_ver_1.md")
tmpl_slides_file = os.path.abspath(home_abspath + "/../tmpl/slides_ver_1.md")
out_md_file=os.path.abspath(home_abspath + "/../out/slides_ver_1.md")
out_pptx_file=os.path.abspath(home_abspath + "/../out/slides_ver_1.pptx")

# объединить файлы в один в директории out
ft.cat_files(out_md_file, tmpl_category_file, tmpl_slides_file)

# конвертирование md в pptx
m2o.convert_to_pptx(out_md_file, out_pptx_file)  # преобразовать в pptx 

