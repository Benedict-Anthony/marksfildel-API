from housing.models import Address, House, HouseFeatures, HouseType,Images
from rest_framework import serializers

from serializers.public.shared import AddressSerializer, CategorySerializer, OwnerReadOnlySerializer


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ("id", "image")


class HouseFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseFeatures
        fields = ("id", "number_of_bedrooms", "number_of_bathrooms", "number_of_packing_space", "balcony")


class HouseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseType
        fields = ("id","type",)



class HouseListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    type = HouseTypeSerializer()
    
    class Meta:
        model = House
        fields =("id", "title", "price","banner", "type","category",  "slug", "created_at", "updated_at",  )

class HouseDetailSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, source="house_images") 
    category = CategorySerializer()
    type = HouseTypeSerializer()
    features = HouseFeaturesSerializer()
    address = AddressSerializer()
    manager = OwnerReadOnlySerializer(read_only=True, source="owner.user_profile")
    class Meta:
        model = House
        fields =("id", "title", "description", "price","banner", "type","category", "is_available", "is_sold", "is_negotiable", "slug","manager","features", "address","images", "created_at", "updated_at",)

class HouseSearchSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    type = HouseTypeSerializer()
    features = HouseFeaturesSerializer()
    address = AddressSerializer()
    class Meta:
        model = House
        fields =("id", "title", "description", "price","banner", "type","category", "is_available", "is_sold", "is_negotiable", "slug","features", "address", "created_at", "updated_at",)


class HouseCRUDSerializer(serializers.ModelSerializer):
    house_images = ImagesSerializer(many=True) 
    features = HouseFeaturesSerializer()
    address = AddressSerializer()
    class Meta:
        model = House
        fields =("id", "title", "description", "price","banner", "type","category", "is_available", "is_sold", "is_negotiable", "slug","features", "address", "house_images","created_at", "updated_at",)
    
    
    def create(self, validated_data):
        address = validated_data.pop("address")
        features = validated_data.pop("features")

        # DEAL WITH IMAGES LATER
        images = validated_data.pop("house_images")

        address = Address.objects.create(**address)

        house = House.objects.create(**validated_data, address=address)

        if features:
            features = HouseFeatures.objects.create(**features)
            house.features=features
            house.save()
        
        return house
    

    def update(self, instance, validated_data):
        # new_address = validated_data.pop("address")
        # new_features = validated_data.pop("features")

        return super().update(instance, validated_data)

    # "features": {
	# 	"id": "a30793670a",
	# 	"number_of_bedrooms": 4,
	# 	"number_of_bathrooms": 3,
	# 	"number_of_packing_space": 2,
	# 	"balcony": true
	# },