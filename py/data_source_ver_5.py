import csv

def get_categories(*args, **kwargs):
    # args and kwargs are for future project development
    yield (0,"Прочие устройтсва")
    yield (1,"Климатическая техника")
    yield (2,"Красота и здоровье")
    yield (3,"Садовая техника")
    yield (4,"Техника для дома")
    yield (5,"Техника для кухни")
    yield (6,"Крупная бытовая техника")

def get_products(csv_file):
    with open(csv_file, newline='', encoding="utf-8") as f_csv:
        data_file = csv.DictReader(f_csv, delimiter=";")
        for rec in data_file:
            rec["product_id"] = int(rec["product_id"])
            rec["price"] = int(rec["price"])
            rec["category"] = int(rec["category"])
            yield(rec)
