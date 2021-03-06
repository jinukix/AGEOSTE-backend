from django.urls import path, include
from .views      import SignUpView, SignInView, AccountView, EmailAuthView, ActivateView, CouponView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/account', AccountView.as_view()),
    path('/account/coupon', CouponView.as_view()),
    path('/emailauth', EmailAuthView.as_view()),
    path('/emailauth/activate/<str:uidb64>/<str:token>', ActivateView.as_view())
]
