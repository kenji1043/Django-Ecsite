from django.contrib import admin
from django.urls import path, include # 追加
from django.conf import settings
from django.conf.urls.static import static # 画像公開

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

# 画像を公開する（アクセス可能にする）
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

