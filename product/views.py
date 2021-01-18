from django.views     import View
from django.http      import JsonResponse
from django.db.models import Count, Avg

from .models          import Product

class ProductListView(View):
    def get(self, request, menu, sub_category):
        try:
            page     = int(request.GET.get('page', 1))
            products = Product.objects.filter(
                sub_category__name = sub_category, 
                sub_category__main_category__menu__name=menu
            ).prefetch_related('productcolorimages__image', 'reviews').annotate(score_avg = Avg('reviews__score'),color_count=Count('colors', distinct=True)) 

            PAGE_COUNT = 20
            end_page   = page * PAGE_COUNT
            start_page = end_page - PAGE_COUNT
            
            product_list = [{
                'id'               : product.id,
                'name'             : product.name,
                'price'            : product.price,
                'discount_rate'    : product.discount_rate,
                'review_score_avg' : product.score_avg,
                'thumbnail'        : product.productcolorimages.all()[0].image.image_url,
                'color_count'      : product.color_count,
            } for product in products[start_page:end_page]]

            return JsonResponse({
                'PRODUCT_COUNT' : products.count(),
                'PRODUCT_LIST'  : product_list},
                status = 200
            )
        except Exception as e:
            return JsonResponse({'MESSAGE' : (e.args[0])}, status=400)


class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product          = Product.objects.get(id=product_id)
            review_score_avg = product.reviews.aggregate(review_score_avg = Avg('score'))

            color_images = [{
                'color_name' : color_image.color.name,
                'image_url'  : color_image.image.image_url
            } for color_image in product.productcolorimages.select_related('color','image')]

            review = [{
                'user_name'   : review.user.name,
                'image_url'   : review.image_url, 
                'score'       : review.score,
                'description' : review.description,
                'created_at'  : review.created_at,
            } for review in product.reviews.select_related('user')]

            product_info = {
                "name"             : product.name,
                "code"             : product.code,
                "description"      : product.description,
                "price"            : product.price,
                "sail_percent"     : product.discount_rate,
                "review_score_avg" : int(round(review_score_avg['review_score_avg'],0)),
                "hashtags"         : [hashtag.name for hashtag in product.hashtags.all()],
                "sizes"            : [size.name for size in product.sizes.all()],
                "color_images"     : color_images,
                "review"           : review,
            }
            
            return JsonResponse({'PRODUCT_INFO' : product_info},status = 200)
        except Product.DoesNotExist():
            return JsonResponse({'MESSAGE' : "Product doest not exist"}, status=401)
        except Exception as e:
            return JsonResponse({'MESSAGE' : (e.args[0])}, status=400)


class ProductSearchView(View):
    def get(self, request):
        try:
            page = int(request.GET.get('page', 1))
            word = request.GET.get('word', None)

            filter_set = {
                'name__icontains'    : word,
                'hashtags__name__in' : request.GET.getlist('hashtags', None)
            }

            products = Product.objects.filter(**filter_set
            ).prefetch_related(
                'productcolorimages__image', 'reviews'
            ).annotate(score_avg = Avg('reviews__score'),color_count=Count('colors', distinct=True)) 

            PAGE_COUNT = 20
            end_page   = page * PAGE_COUNT
            start_page = end_page - PAGE_COUNT

            product_list = [{
                'id'               : product.id,
                'name'             : product.name,
                'price'            : product.price,
                'discount_rate'    : product.discount_rate,
                'review_score_avg' : product.score_avg,
                'thumbnail'        : product.productcolorimages.all()[0].image.image_url,
                'color_count'      : product.color_count,
            } for product in products[start_page:end_page]]

            return JsonResponse({
                'PRODUCT_COUNT' : products.count(),
                'PRODUCT_LIST'  : product_list},
                status = 200
            )

        except Exception as e:
            return JsonResponse({'MESSAGE' : (e.args[0])}, status=400)