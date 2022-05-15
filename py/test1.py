#%%
from email.policy import default
from turtle import width
from typing import Dict
import data_source_ver_1

prod_list = data_source_ver_1.get_products()
cat_list = data_source_ver_1.get_categories()
# %%
home_abspath = os.path.dirname(os.path.abspath(__file__))
slide_tmpl = os.path.abspath(home_abspath + "/../tmpl/slides_ver_2.md")
# %%
print(slide_tmpl)
# %%
with open(slide_tmpl) as tmpl:
    tmpl_body = tmpl.read()
print(tmpl_body.format(model="Модель",
                       vendor="Гравитон",
                       product_id="8483040",
                       price="Цена"))

# %%
import re

txt="""{model}
{.column }
{.columns}
text
{model}
{name}
asasaSas{width=120px}"""

def repl(match):
    text = match.group(0)
    return '@@@' + text[1:-1] + '@@@'
# md_str = re.compile('\{\..*\}')
# md_str = re.compile('\{\}')
md_str = re.compile('\{(?!model|name).+\}', re.IGNORECASE)
tmp_str = md_str.sub(repl, txt)

d = {"model" : "Модель", "name" : "Имя"}
print(tmp_str.format_map(d))
# %%
r = re.compile('\{(?!model|name).+\}', re.IGNORECASE)
print(r.search(txt).group(0))
# %%
import format_tools as frt
#%%
mdtext = """## {model}
:::::::::::::: {.columns}
::: {.column }
* вендор: {vendor}
* модель: {model}
* артикул: {product_id}
* цена: {price}
:::
::: {.column }

![фото товара](pic/{product_id}.png){width=120px} {hdskjhaksjhd}
:::
::::::::::::::

* * *    """

d = {"model" : "Модель", "product_id" : "Идентификатор продукта", "vendor" : "Вендор", "price" : "Цена"}
print(frt.format_md_text(mdtext, d))

# %%
# задание 3
import data_source_ver_3 as ds

cat = dict(ds.get_categories())
cat.setdefault(999, "Новое значение 2")

print(cat)

# %%
price = 4173
discount = 0
final = price * (1 - discount / 100)
print(final)
print(round(final))
# %%
import data_source_ver_4 as ds

prods = ds.get_products()
print(*prods)

prods = list(ds.get_products())
prods.sort(key=lambda prod : prod["category"])
print(prods[0]["model"])

# %%
import data_source_ver_5 as ds

data = ds.get_products("/Users/rosrain/pylab/csv/wb.csv")
print(list(data))

# %%
