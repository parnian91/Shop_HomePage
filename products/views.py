from django.shortcuts import render, get_object_or_404
from .models import Product, Comment
from products.forms import CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def Store_view(request):
    all_products = Product.objects.all()
    
    all_products = Paginator(all_products, 5) 
    try:    
        page_number = request.GET.get('page')
        all_products = all_products.get_page(page_number)
    except PageNotAnInteger:
        all_products = all_products.get_page(1)
    except EmptyPage:
        all_products = all_products.get_page(1)
    context={'all_products': all_products}
    
    return render(request, 'products/index.html', context)
    # return render(request, 'products/index.html', {'all_products': all_products})



def Product_view(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product  # Set the product field
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment has been posted successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Your comment has not been posted')  

    comments = Comment.objects.filter(product=product, approved=True).order_by('-created_date')
    form = CommentForm()
    context = {'product': product, 'comments': comments, 'form': form}
    return render(request, 'products/product.html', context)

        
