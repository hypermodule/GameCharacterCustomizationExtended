import json
import sys
from collections import OrderedDict
from copy import deepcopy


def merge_soft_object_path_arrays(arr1, arr2):
    result = []

    seen = set()

    for sop in arr1:
        result.append(sop)
        seen.add(sop["AssetPathName"])
    
    for sop in arr2:
        if not sop["AssetPathName"] in seen:
            result.append(sop)
    
    return result


def merge_rows(row1, row2):
    result = OrderedDict()

    for key, arr1 in row1.items():
        arr2 = row2.get(key, [])
        result[key] = merge_soft_object_path_arrays(arr1, arr2)
    
    return result


def merge_data_tables(dt1, dt2):
    rows1 = dt1["Rows"]
    rows2 = dt2["Rows"]

    new_rows = OrderedDict()

    for row_name, row1 in rows1.items():
        row2 = rows2.get(row_name, {})
        new_rows[row_name] = merge_rows(row1, row2)
    
    result = deepcopy(dt1)
    result["Rows"] = new_rows

    return result


def merge_json(json1, json2):
    dt1 = json1[0]
    dt2 = json2[0]

    return [merge_data_tables(dt1, dt2)]


def main():
    if len(sys.argv) != 3:
        print("Unexpected number of arguments provided.")
        print(f"Usage: python {sys.argv[0]} DT_GameCharacterCustomization1.json DT_GameCharacterCustomization2.json")
        sys.exit(1)

    json1 = []
    with open(sys.argv[1]) as f:
        json1 = json.load(f)
    
    json2 = []
    with open(sys.argv[2]) as f:
        json2 = json.load(f)
    
    result = merge_json(json1, json2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
