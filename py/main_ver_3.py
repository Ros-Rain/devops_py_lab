import os
import markdown2output_ver_1 as m2o
import file_tools as ft
import format_tools as frmt
import data_source_ver_3 as ds

# путь запуска 
home_abspath = os.path.dirname(os.path.abspath(__file__))

# путь к рабочим файлам относительно пути запуска
tmpl_category_file = os.path.abspath(home_abspath + "/../tmpl/category_ver_1.md")
tmpl_slides_file = os.path.abspath(home_abspath + "/../tmpl/slides_ver_3.md")
out_md_file = os.path.abspath(home_abspath + "/../out/slides_ver_3.md")
out_pptx_file = os.path.abspath(home_abspath + "/../out/slides_ver_3.pptx")

# категории
category_list = dict(ds.get_categories())

# данные по скидкам
discount_dict = { "Candy":10, "BBK":20 }

# продукты
prod_list = ds.get_products()

# имена временных файлы
out_mdfiles = []

# текст шаблона слайда
with open(tmpl_slides_file) as f_templ:
    templ_text = f_templ.read()

# обработка списка продуктов
for prod in prod_list:
    # добавляем дополнительные данные по категории и скидкам
    # категория -> текст по словарю категорий
    prod["category"] = category_list.get(prod["category"], category_list[0])
    # + discout из словаря discount_dict по названию вендора
    prod.setdefault("discout", discount_dict.get(prod["vendor"], 0))
    # + discounted_price
    prod.setdefault("discounted_price", 
                    round(prod["price"] * (1 - prod["discout"]/100)))
    
    # имя выходного MD файла
    out_mdfiles.append(out_md_file + "." + str(prod['product_id']) + ".md")
    
    # заполнение шаблона из словаря
    md_text = frmt.format_md_text(templ_text, prod)
    
    # запись во временный файл
    with open(out_mdfiles[len(out_mdfiles)-1], "w") as f_out:
        f_out.write(md_text)

# объединить файлы в один в директории out
ft.cat_txtfiles(out_md_file, *out_mdfiles)

# конвертирование md в pptx
m2o.convert_to_pptx(out_md_file, out_pptx_file)  # преобразовать в pptx 

