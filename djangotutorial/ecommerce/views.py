from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin, CreateModelMixin, \
    UpdateModelMixin
from .models import Order,OrderItem,OrderUser,Product,ProductCategory
from .serializer import UserSerializer,OrderSerializer,OrderItemSerializer,ProductSerializer,ProductCategorySerializer
# Create your views here.

class OrderUserView(GenericAPIView, ListModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin):
    queryset = OrderUser.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class OrderItemView(GenericAPIView, ListModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class ProductView(GenericAPIView, ListModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ProductCategoryView(GenericAPIView, ListModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class OrderView(GenericAPIView, ListModelMixin,CreateModelMixin,UpdateModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

