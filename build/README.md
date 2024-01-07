# Developer readme

This file explains how the mod is made, in case anyone is interested in that.

## Creating the .pak file

Making the .pak file is currently a manual process, which is assisted by the scripts in this directory:

1. Use FModel to extract `DT_GameCharacterCustomization` as .json.

   * For this you will need a mapping file for Wild Life, e.g. the latest one from here: https://github.com/WL-Mechanics/mappings

2. Specify the paths you would like to add in `DT_GameCharacterCustomization_extensions.json`.

   * The script `generate_extension_dt.py` can programatically generate a template for this file.

3. Alter the file from Step 1 so that it incorporates the additions from Step 2.

   * The script `merge_fmodel_dt.py` can be used to merge the two files.

4. Convert the file from Step 3 to the format expected by Unreal Editor.

   * The script `fmodel2ue.py` can perform this conversion.

5. In Unreal Editor:

   * Create a blank C++ project and name it `WildLifeC`.

   * Use `Tools > New C++ Class` to create a blank C++ class at `Source/WildLifeC/FGameCharacterCustomizationData`. Replace the content of the auto-generated header file with the content from the header file that's in the same directory as this README.

   * Build the C++ project.

   * Use Unreal Editor to create a DataTable at `DataTables/NPC/DT_GameCharacterCustomization`; as row struct choose the `GameCharacterCustomizationData` from the previous step.

   * Edit the created DataTable and populate it by importing the .json file from Step 4.

   * If you want to make it easy for others to override the added paths, create a placeholder image for each one and add those placeholder images into the Unreal project at the right paths.

     - The script `generate_placeholder_images.py` can be used to generate the placeholder images. It is meant to be used with the file from Step 2.

   * Make sure that the DataTable and placeholder textures get put into a separate .pak when the project is packaged. This can be done by creating a PrimaryAssetLabel in the root of the Content browser with "apply recursively" checked. See also https://docs.unrealengine.com/4.26/en-US/SharingAndReleasing/Patching/GeneralPatching/ChunkingExample/

   * Package the project.

   * Rename the outputted .pak containing the DataTable and placeholder textures to the naming convention used by this mod: `$DT_GameCharacterCustomization_Extended_Vx_P.pak`

## Background information

The idea for this mod came from recreating/reversing the `GameCharacterCustomizationData` struct that Wild Life uses. This was done by inspecting `DT_GameCharacterCustomization.uasset` in FModel and UassetGUI and noting the fields used by each row: HairMeshes, BeardMeshes, SkinTextures etc. A similar approach might work for other DataTables used by the game.
