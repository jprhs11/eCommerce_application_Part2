from rest_framework import viewsets, permissions, serializers
from .models import Store, Product, Review
from .serializers import StoreSerializer, ProductSerializer, ReviewSerializer
from .permissions import IsVendorUser, IsOwnerOrReadOnly

# Import the twitter utility functions
from .twitter_utils import tweet_new_store, tweet_new_product


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsVendorUser,
        IsOwnerOrReadOnly,
    ]

    def perform_create(self, serializer):
        # 1. Save the store and assign the logged-in vendor
        store = serializer.save(vendor=self.request.user)

        # 2. Trigger the Tweet
        try:
            tweet_new_store(store.name, store.description)
        except Exception as e:
            # Prints to console if API keys are wrong or permissions fail
            print(f"Twitter API Error (Store): {e}")


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsVendorUser,
        IsOwnerOrReadOnly,
    ]

    def perform_create(self, serializer):
        # 1. Get the store selected in the request
        store = serializer.validated_data.get("store")

        # 2. Validation: Ensure the logged-in user actually owns this store
        if store.vendor != self.request.user:
            raise serializers.ValidationError(
                {
                    "detail": "You cannot add products to a store you "
                    "do not own."
                }
            )

        # 3. Save the product
        product = serializer.save()

        # 4. Trigger the Tweet
        try:
            tweet_new_product(store.name, product.name, product.description)
        except Exception as e:
            print(f"Twitter API Error (Product): {e}")


class ReviewViewSet(viewsets.ReadOnlyModelViewSet):
    """Retrieval only as per instructions"""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
