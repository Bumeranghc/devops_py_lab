import csv

def get_categories(*args, **kwargs):
    # args and kwargs are for future project development
    yield (1,"Климатическая техника")
    yield (2,"Красота и здоровье")
    yield (3,"Садовая техника")
    yield (4,"Техника для дома")
    yield (5,"Техника для кухни")
    yield (6,"Крупная бытовая техника")

def get_products(file_csv):
    # считать данные из файла CSV
    with open(file_csv, newline='', encoding="utf-8") as file:
        products_file = csv.DictReader(file, delimiter=";")
        for product in products_file:
            product["product_id"] = int(product["product_id"])
            product["category"] = int(product["category"])
            product["price"] = int(product["price"])
            yield(product)