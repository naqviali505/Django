from rest_framework.serializers import HyperlinkedModelSerializer
from .models import OrderUser,Order,OrderItem,ProductCategory,Product


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = OrderUser
        fields = '__all__'
class OrderSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ProductSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductCategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
class OrderItemSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

