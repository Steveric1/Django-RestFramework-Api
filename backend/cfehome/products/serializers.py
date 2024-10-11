from rest_framework import serializers
from .models import Product
from api.serializers import PublicSerializer
from .validators import validate_title, validate_title_no_hello, unique_product_title_no_hello
from rest_framework.reverse import reverse


class UserProductInlineSerializer(serializers.Serializer):
    edit_url = serializers.HyperlinkedIdentityField(
        view_name="product-edit",
        lookup_field="pk",
        read_only=True
    )
    
    title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    owner = PublicSerializer(source='user', read_only=True)
    # related_data = UserProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    # discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.HyperlinkedIdentityField(
        view_name="product-edit",
        lookup_field="pk",
    )
    title = serializers.CharField(
        validators=[validate_title, validate_title_no_hello, unique_product_title_no_hello])
    # name = serializers.CharField(source='title', read_only=True)

    class Meta:
        model = Product 
        fields = [
            'owner',
            'url',
            'edit_url',
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'public',
            # 'discount',
            # 'my_user_data',
            # 'related_data',
        ]
    
    def get_my_user_data(self, obj):
        return {
            "username": obj.user.username
        }

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__exact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value

    def get_url(self, obj):
        # return f"/api/products/{obj.pk}"
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-details", kwargs={"pk": obj.pk}, request=request)

    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
