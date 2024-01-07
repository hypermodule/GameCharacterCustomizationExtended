#pragma once

#include "CoreMinimal.h"
#include "FGameCharacterCustomizationData.generated.h"

USTRUCT(BlueprintType)
struct WILDLIFEC_API FGameCharacterCustomizationData : public FTableRowBase
{
	GENERATED_BODY()
public:
	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta=(DisplayName="HairMeshes"))
	TArray<FSoftObjectPath> HairMeshes;

	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta=(DisplayName="BeardMeshes"))
	TArray<FSoftObjectPath> BeardMeshes;

	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta=(DisplayName="SkinTextures"))
	TArray<FSoftObjectPath> SkinTextures;

	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta=(DisplayName="PubicHairMasks"))
	TArray<FSoftObjectPath> PubicHairMasks;

	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta=(DisplayName="IrisTextures"))
	TArray<FSoftObjectPath> IrisTextures;

	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta=(DisplayName="WingMaterials"))
	TArray<FSoftObjectPath> WingMaterials;

	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta=(DisplayName="PhysicsAssets"))
	TArray<FSoftObjectPath> PhysicsAssets;

	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta=(DisplayName="EyeLinerTextures"))
	TArray<FSoftObjectPath> EyeLinerTextures;

	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta=(DisplayName="EyeShadowTextures"))
	TArray<FSoftObjectPath> EyeShadowTextures;

	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta=(DisplayName="LipstickTextures"))
	TArray<FSoftObjectPath> LipstickTextures;

	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta=(DisplayName="TanlineTextures"))
	TArray<FSoftObjectPath> TanlineTextures;
};
