from rest_framework import routers

from .views import ProductView, CategoryView, PairsView

app_name = "product"

router = routers.SimpleRouter()
router.register(r"product", ProductView, basename="product")
router.register(r"category", CategoryView, basename="category")
router.register(r"pair", PairsView, basename="pair")

urlpatterns = router.urls
