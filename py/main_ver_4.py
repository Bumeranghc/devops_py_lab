# import data_source_ver_N as ds
from unicodedata import category
import markdown2output_ver_1 as m2o
import data_source_ver_2 as ds

tmpl_category_file="tmpl/category_ver_4.md"
tmpl_slides_file="tmpl/slides_ver_3.md"

out_md_file="out/slides_ver_4.md"
out_md_category_file = "out/category_ver_4.md"
out_pptx_file="out/slides_ver_4.pptx"

# получить словари с описанием продуктов 
products = ds.get_products()

# отсортировать по категориям
sorted_products = list(products)
sorted_products.sort(key=lambda x: x['category'])

# использовать список категория
category_list=["Прочие устройства", "Климатическая техника" "Красота и здоровье", "Садовая техника","Техника для дома","Техника для кухни", "Крупная бытовая техника" ]

# использовать словарь с ценами
discount_dict={ "Candy":10, "BBK":20 }

# использовать файл-шаблон для продуктов
with open(tmpl_slides_file, encoding="UTF-8") as file:
    product_template = file.read()

# использовать файл-шаблон для категорий продуктов
with open(tmpl_category_file, encoding="UTF-8") as file:
    category_template = file.read()

# использовать переменную для хранения текущей категории
current_category = -1

# объединить файлы из этого списка в один в директории out
filenames = []
for product in sorted_products:
    if product["category"] != current_category:
        # подготовить шаблон для категории к изменениям
        current_category_template = category_template
        # сгенерировать имя для файла шаблона категории
        current_category_template_file = "out/version_category_4." + str(product['category']) + ".md"
        # добавить имя файла в список для объединения
        filenames.append(current_category_template_file)
        # произвести замену переменных в шаблоне категории
        current_category_template = current_category_template.replace('{category_name}', category_list[product['category']-1])
        current_category_template = current_category_template.replace('{category_num}', "category_"+str(product['category']))
        # записать отредактированный шаблон в файл
        with open(current_category_template_file, "w") as outfile:
            outfile.write(current_category_template)
        current_category = product['category']
    # подготовить шаблон для продукта к изменениям
    current_product_template = product_template
    # сгенерировать имя для файла шаблона продукта
    current_template_file = "out/version_4." + str(product['product_id']) + ".md"
    # добавить имя файла в список для объединения
    filenames.append(current_template_file)
    # назначить категорию из списка
    product['category']=category_list[product['category']-1]
    # указать скидку в процентах из словаря
    product.setdefault('discount', discount_dict.get(product['vendor'], 0))
    # указать окончательную стоимость со скидкой
    product.setdefault('discounted_price', round(product['price'] * (1 - product['discount']/100)))
    # произвести замену переменных в шаблоне
    for key, value in product.items():
        current_product_template = current_product_template.replace('{'+key+'}', str(value))
        # записать отредактированный шаблон в файл
        with open(current_template_file, "w") as outfile:
            outfile.write(current_product_template)

# объединить файлы
with open(out_md_file, "w", encoding="UTF-8") as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(infile.read())
        outfile.write("\n")

# преобразовать в pptx 
m2o.convert_to_pptx(out_md_file, out_pptx_file) 
