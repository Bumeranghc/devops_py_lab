# import data_source_ver_N as ds
import markdown2output_ver_1 as m2o
import data_source_ver_2 as ds

tmpl_category_file="tmpl/category_ver_1.md"
tmpl_slides_file="tmpl/slides_ver_2.md"

out_md_file="out/slides_ver_2.md"
out_pptx_file="out/slides_ver_2.pptx"

# получить словари с описанием продуктов 
products = ds.get_products()

# использовать файл-шаблон
with open(tmpl_slides_file, encoding="UTF-8") as file:
    product_template = file.read()

# объединить файлы из этого списка в один в директории out
filenames = []
for product in products:
    # подготовить шаблон для продукта к изменениям
    current_product_template = product_template
    # сгенерировать имя для файла шаблона продукта
    current_template_file = "out/version_2." + str(product['product_id']) + ".md"
    # добавить имя файла в список для объединения
    filenames.append(current_template_file)
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
