from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment

from django.contrib.auth.decorators import login_required


def home_page(request):
    query = request.GET.get('q')
    search = request.GET.get('search', '')

    products = Product.objects.filter(name__icontains=search)

    if query:
        if query == 'expensive':
            products = products.order_by('-new_price')
        elif query == 'cheap':
            products = products.order_by('new_price')
        elif query == 'rating':
            products = products.order_by('-rating')
        elif query == 'new-arrivals':
            products = products.order_by('-created')

    context = {
        'products': products,
        'search': search,
        'is_home_page': True,
    }

    return render(request, 'index.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        comment = request.POST.get('comment')
        
        if len(comment.strip()) >= 10:
            new_comment = Comment.objects.create(
                owner=request.user,
                product=product,
                body=comment
            )
            new_comment.save()
            return redirect(f'/detail/{product_id}#comments-section')

    context = {
        'product': product,
        'last_3_comments': product.comment_set.all()[::-1][:3]
    }

    return render(request, 'detail.html', context)


@login_required(login_url='login')
def add_cart(request, product):

    if request.method == 'POST':
        product = request.POST.get('product')
        owner = request.user.id
        quantity = request.POST.get('product')

    return redirect('detail', product=product)