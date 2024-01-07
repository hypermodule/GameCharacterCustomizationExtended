import json
import sys
from collections import OrderedDict


def parse_soft_object_path(obj):
    asset_path_name = obj["AssetPathName"]
    sub_path_string = obj["SubPathString"]

    package_name = ""
    asset_name = ""
    parts = asset_path_name.split(".")
    if len(parts) == 2:
        package_name, asset_name = parts

    return {
        "AssetPath": {
            "PackageName": package_name,
            "AssetName": asset_name
        },
        "SubPathString": sub_path_string
    }


def parse_row(row_name, fields):
    result = OrderedDict()
    result["Name"] = row_name
    for field_name, soft_object_paths in fields.items():
        result[field_name] = [parse_soft_object_path(sop) for sop in soft_object_paths]
    return result


def parse(objects):
    result = []
    rows = objects[0]["Rows"]
    for name, fields in rows.items():
        result.append(parse_row(name, fields))
    return result


def main():
    if len(sys.argv) != 2:
        print("Unexpected number of arguments provided.")
        print(f"Usage: python {sys.argv[0]} fmodel_export.json")
        sys.exit(1)

    objects = []
    with open(sys.argv[1]) as f:
        objects = json.load(f)

    parsed = parse(objects)

    print(json.dumps(parsed, indent=2))


if __name__ == "__main__":
    main()
