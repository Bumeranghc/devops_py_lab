# import data_source_ver_N as ds
import markdown2output_ver_1 as m2o

tmpl_category_file="tmpl/category_ver_1.md"
tmpl_slides_file="tmpl/slides_ver_1.md"

out_md_file="out/slides_ver_1.md"
out_pptx_file="out/slides_ver_1.md"

# объединить файлы в один в директории out 
filenames = [tmpl_category_file, tmpl_slides_file]
with open(out_md_file, "w") as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(infile.read())
        outfile.write("\n")

# преобразовать в pptx 
m2o.convert_to_pptx(out_md_file, out_pptx_file) 

