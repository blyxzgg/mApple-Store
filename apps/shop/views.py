from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Product, Category, Favorite, Cart, CartItem


def shop_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    category_id = request.GET.get('category')

    if category_id:
        products = products.filter(category_id=category_id)

    favorite_ids = set()
    cart_product_ids = set()

    if request.user.is_authenticated:
        favorite_ids = set(
            Favorite.objects.filter(user=request.user).values_list('product_id', flat=True)
        )

        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_product_ids = set(
                cart.items.values_list('product_id', flat=True)
            )

    context = {
        'products': products,
        'categories': categories,
        'favorite_ids': favorite_ids,
        'cart_product_ids': cart_product_ids,
    }

    return render(request, 'shop/shop.html', context)


@login_required
@require_POST
def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favorite, created = Favorite.objects.get_or_create(
        user=request.user, product=product
    )
    if not created:
        favorite.delete()

    return redirect(request.POST.get('next', 'shop:home'))


@login_required
@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(
        cart=cart, product=product
    )
    if not created:
        item.quantity += 1
        item.save()

    return redirect(request.POST.get('next', 'shop:home'))


@login_required
def favorites_page(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('product')

    cart = Cart.objects.filter(user=request.user).first()
    cart_product_ids = set()
    if cart:
        cart_product_ids = set(
            cart.items.values_list('product_id', flat=True)
        )

    context = {
        'favorites': favorites,
        'cart_product_ids': cart_product_ids,
    }

    return render(request, 'shop/favorites.html', context)


@login_required
def cart_page(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.items.select_related('product')

    total = sum(item.total_price for item in items)

    context = {
        'items': items,
        'total': total,
    }

    return render(request, 'shop/cart.html', context)


@login_required
@require_POST
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()

    return redirect(request.POST.get('next', 'shop:cart'))


@login_required
@require_POST
def increase_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.quantity += 1
    item.save()

    return redirect(request.POST.get('next', 'shop:cart'))


@login_required
@require_POST
def decrease_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect(request.POST.get('next', 'shop:cart'))


@login_required
@require_POST
def remove_from_cart_by_product(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    CartItem.objects.filter(cart=cart, product_id=product_id).delete()

    return redirect(request.POST.get('next', 'shop:home'))
