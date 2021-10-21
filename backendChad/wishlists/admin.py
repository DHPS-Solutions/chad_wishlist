from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from wishlists.models import ItemsOnWishlist, Wishlist


#admin.site.register(ItemsOnWishlist)

class ItemsOnWishlistInline(admin.TabularInline):
    model = ItemsOnWishlist

@admin.register(Wishlist)
class WishlistAdmin(ModelAdmin):
    base_model = Wishlist
    inlines = [
        ItemsOnWishlistInline,
    ]


