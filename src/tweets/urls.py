from django.urls import path, include


from .views import  TweetListView, TweetDetailView

urlpatterns = [
    #path('admin/', admin.site.urls),

    path('', TweetListView.as_view(), name='list'), #/tweet/
    path('(?P <abc>\d+)/', TweetDetailView.as_view(), name='detail'),
]

