import json
import os
import random
import struct
import sys
from zlib import crc32, compress
from io import BytesIO


placeholder_width = 32
placeholder_height = 32
fallback_color = (255, 0, 0)


def generate_placeholder_png(width, height, color):
    bit_depth = 8
    color_type = 2

    def write_chunk(out, chunk_type, data):
        checksum = crc32(data, crc32(chunk_type))
        out.write(struct.pack(">I", len(data)))
        out.write(chunk_type)
        out.write(data)
        out.write(struct.pack(">I", checksum))

    out = BytesIO()
    
    # Signature
    out.write(b"\x89PNG\r\n\x1A\n")

    # IHDR
    ihdr = struct.pack('>2I5B', width, height, bit_depth, color_type, 0, 0, 0)
    write_chunk(out, b"IHDR", ihdr)

    # IDAT
    data = bytearray()
    for _ in range(height):
        data.append(0) # filter
        for _ in range(width):
            for byte in color:
                data.append(byte)
    write_chunk(out, b"IDAT", compress(data))

    # IEND
    write_chunk(out, b"IEND", b"")

    return out.getvalue()


def random_bright_color():
    result = [255, random.randint(0, 255), 0]
    random.shuffle(result)
    return result


def gather_png_paths(fmodel_json):
    def to_path(asset_path_name):
        package, _ = asset_path_name.split(".")
        return package.lstrip("/Game/") + ".png"

    fields = ["SkinTextures", "EyeLinerTextures", "EyeShadowTextures"]
    result = set()
    rows = fmodel_json[0]["Rows"]
    for struct in rows.values():
        for field in fields:
            arr = struct.get(field, [])
            for sop in arr:
                result.add(to_path(sop["AssetPathName"]))
    return result


def main():
    if len(sys.argv) != 2:
        print("Unexpected number of arguments provided.")
        print(f"Usage: python {sys.argv[0]} DT_GameCharacterCustomization_extensions.json")
        sys.exit(1)

    fmodel_json = []
    with open(sys.argv[1]) as f:
        fmodel_json = json.load(f)
    
    png_paths = gather_png_paths(fmodel_json)

    folders = set()
    for path in png_paths:
        folders.add(os.path.dirname(path))
    
    for folder in folders:
        os.makedirs(folder)
    
    count = 0
    
    for path in png_paths:
        color = fallback_color
        if "SkinTextures" in path:
            color = random_bright_color()
        with open(path, "wb") as out:
            out.write(generate_placeholder_png(placeholder_width, placeholder_height, color))
        count += 1
    
    print(f"Successfully generated {count} placeholder .png images.")
    

if __name__ == "__main__":
    main()
