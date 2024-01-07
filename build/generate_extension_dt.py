import json
from collections import OrderedDict
from copy import deepcopy


num_custom = 100

path_prefix = "/Game/Textures/UserProvided/Character"

data_table_template = {
    "Type": "DataTable",
    "Name": "DT_GameCharacterCustomization",
    "Class": "UScriptClass'DataTable'",
    "Properties": {
      "RowStruct": {
        "ObjectName": "ScriptStruct'GameCharacterCustomizationData'",
        "ObjectPath": "/Script/WildLifeC"
      }
    },
    "Rows": OrderedDict()
}

struct_template = OrderedDict([
    ("HairMeshes", []),
    ("BeardMeshes", []),
    ("SkinTextures", []),
    ("PubicHairMasks", []),
    ("IrisTextures", []),
    ("WingMaterials", []),
    ("PhysicsAssets", []),
    ("EyeLinerTextures", []),
    ("EyeShadowTextures", []),
    ("LipstickTextures", []),
    ("TanlineTextures", [])
])

extension_targets = set([
    "SkinTextures",
    "EyeLinerTextures",
    "EyeShadowTextures",
    "LipstickTextures"
])

row_names = [
    "HumanFemaleStandard",
    "Sethro",
    "Bol",
    "Max",
    "IlJah",
    "Yason",
    "Shey",
    "Minotaur",
    "KerpaliStandard",
    "Kral",
    "Rasha",
    "Rawn",
    "Tali",
    "Gulhragg",
    "Karra",
    "Chakkar",
    "MinotaurNew",
    "Frank",
    "Ziad",
    "Ishtra",
    "Vark",
    "Scrof",
    "Sadora",
    "Yanu_Kerpali",
    "Goatman",
    "Fingers"
]


def generate_soft_object_path(row_name, field_name, asset_name):
    asset_path_name = f"{path_prefix}/{row_name}/{field_name}/{asset_name}.{asset_name}"
    return {
        "AssetPathName": asset_path_name,
        "SubPathString": ""
    }


def generate_struct(row_name):
    result = deepcopy(struct_template)

    for field_name, arr in result.items():
        if field_name in extension_targets:
            for i in range(1, num_custom + 1):
                asset_name = f"Custom{i:03}"
                arr.append(generate_soft_object_path(row_name, field_name, asset_name))
    
    return result


def main():
    data_table = deepcopy(data_table_template)

    rows = data_table["Rows"]

    for row_name in row_names:
        rows[row_name] = generate_struct(row_name)
    
    result = [data_table]
    
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
