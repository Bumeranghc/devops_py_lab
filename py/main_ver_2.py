# import data_source_ver_N as ds
import markdown2output_ver_1 as m2o
import data_source_ver_2 as ds

tmpl_category_file="tmpl/category_ver_1.md"
tmpl_slides_file="tmpl/slides_ver_2.md"

out_md_file="out/slides_ver_2.md"
out_pptx_file="out/slides_ver_2.pptx"

products = ds.get_products()
#print(*products)
with open(tmpl_slides_file, encoding="UTF-8") as file:
    product_template = file.read()

filenames = []

for product in products:
    current_product_template = product_template
    current_template_file = "out/version_2." + str(product['product_id']) + ".md"
    filenames.append(current_template_file)
    for key, value in product.items():
        current_product_template = current_product_template.replace('{'+key+'}', str(value))
        with open(current_template_file, "w") as outfile:
            outfile.write(current_product_template)

with open(out_md_file, "w", encoding="UTF-8") as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(infile.read())
        outfile.write("\n")
    #for key in product.keys():
    #    print(key)
    #    print(product[key])
    #    test = product_template.replace('{'+key+'}', str(product[key]))
    #    print(test)

#for product in products:
#    print(product)
#    product_template.format(**product)

# объединить файлы в один в директории out 
#filenames = [tmpl_category_file, tmpl_slides_file]
#with open(out_md_file, "w") as outfile:
#    for fname in filenames:
#        with open(fname) as infile:
#            for line in infile:
#                outfile.write(infile.read())
#        outfile.write("\n")

# преобразовать в pptx 
m2o.convert_to_pptx(out_md_file, out_pptx_file) 
