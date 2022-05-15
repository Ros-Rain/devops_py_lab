import os

from numpy import Infinity
import markdown2output_ver_1 as m2o
import file_tools as ft
import format_tools as frmt
import data_source_ver_3 as ds

# путь запуска 
home_abspath = os.path.dirname(os.path.abspath(__file__))

# путь к рабочим файлам относительно пути запуска
tmpl_category_file = os.path.abspath(home_abspath + "/../tmpl/category_ver_4.md")
tmpl_slides_file = os.path.abspath(home_abspath + "/../tmpl/slides_ver_3.md")
out_md_file = os.path.abspath(home_abspath + "/../out/slides_ver_4.md")
out_md_cat_file = os.path.abspath(home_abspath + "/../out/category_ver_4.md")
out_pptx_file = os.path.abspath(home_abspath + "/../out/slides_ver_4.pptx")

# категории
category_list = dict(ds.get_categories())

# данные по скидкам
discount_dict = {"Candy":10, "BBK":20}

# продукты
prod_list = list(ds.get_products())

# сортировка по категориям
prod_list.sort(key=lambda prod : prod["category"])

# имена временных файлов
out_mdfiles = []

# текст шаблона слайда
with open(tmpl_slides_file) as f_templ:
    templ_text = f_templ.read()

# текст шаблона слайда категории 
with open(tmpl_category_file) as f_templ:
    templ_cat_text = f_templ.read()

# текущая категория по списку продуктов
current_category = Infinity   # prod_list[0]["category"]

# обработка списка продуктов
for prod in prod_list:
    # + category_name текст по словарю категорий
    prod.setdefault("category_name", 
                    category_list.get(prod["category"], category_list[0]))

    # новая категория - выводим слайд заголовка
    if prod["category"] != current_category:
        # формируем слайд категории
        # имя выходного MD файла слайд категории
        out_mdfiles.append(out_md_cat_file + "." + str(prod['category']) + ".md")

        # заполнение шаблона категории из словаря
        md_text = frmt.format_md_text(templ_cat_text, prod)
        
        # запись во временный файл
        with open(out_mdfiles[len(out_mdfiles)-1], "w") as f_out:
            f_out.write(md_text)

        current_category = prod["category"]
    
    # подмена ключа категории на текстовое значение для внесения в слайд продукта
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

