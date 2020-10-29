import csv

from config import PIN_INPUT_FILE

labels = {}

with open(PIN_INPUT_FILE) as csvfile:
    input_reader = csv.reader(csvfile, delimiter=";")
    index_row, index_col, index_label, index_category = -1,-1,-1, -1
    indexes_determined = False
    for row in input_reader:
        if not indexes_determined:
            for i, element in enumerate(row):
                if "Row position" in element:
                    index_row = i
                if "Column position" in element:
                    index_col = i
                if "Label" in element:
                    index_label = i
                if "Category" in element:
                    index_category = i
                if index_row != -1 and index_col != -1 and index_label != -1:
                    indexes_determined = True
                    break
        else:
            labels[str(row[index_row] + row[index_col])] = {
                "label": row[index_label],
                "category": row[index_category]
            } 


def get_label_and_cat(index: int) -> (str, str):
    try:
        label = labels[index]["label"].strip()
        category = labels[index]["category"].strip()
    except KeyError:
        label, category = "", ""
        
    return label, category
