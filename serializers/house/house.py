from housing.models import Address, House, Features, HouseType,Images
from rest_framework import serializers

from serializers.public.shared import AddressSerializer, CategorySerializer, OwnerReadOnlySerializer


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ("id", "image")

    def create(self, validated_data):
        print(validated_data)
        house = House.objects.all()[3]
        image = Images.objects.create(**validated_data, house=house)
        return image
    


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ("id", "bedrooms", "bathrooms", "packing_space", "balcony")


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
    features = FeaturesSerializer()
    address = AddressSerializer()
    manager = OwnerReadOnlySerializer(read_only=True, source="owner.user_profile")
    class Meta:
        model = House
        fields =("id", "title", "description", "price","banner", "type","category", "is_available", "is_sold", "is_negotiable", "slug","manager","features", "address","images", "created_at", "updated_at",)

class HouseSearchSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    type = HouseTypeSerializer()
    features = FeaturesSerializer()
    address = AddressSerializer()
    class Meta:
        model = House
        fields =("id", "title", "description", "price","banner", "type","category", "is_available", "is_sold", "is_negotiable", "slug","features", "address", "created_at", "updated_at",)


class HouseCRUDSerializer(serializers.ModelSerializer):
    house_images = ImagesSerializer(many=True) 
    features = FeaturesSerializer()
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
            features = Features.objects.create(**features)
            house.features=features
            house.save()
        
        for img in images:
            Images.objects.create(*img, house=house)
            
        
        return house
    
    def validate_house_images(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Invalid image format")
        if len(value) > 6:
            raise serializers.ValidationError("number of images must not be more than six")
        if len(value) <3:
            raise serializers.ValidationError("number of images must be at least three")

        return value

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

