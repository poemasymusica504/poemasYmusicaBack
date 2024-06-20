from django.contrib import admin
from django.urls import include, re_path as url, path
from Api.views import CustomAuthToken, SingIn
from rest_framework import urls
from rest_framework.documentation import include_docs_urls
from Api.urls import router


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', CustomAuthToken.as_view()),
    url(r'^api-auth/', include(urls, namespace='rest_framework')),
    url(r'^docs/', include_docs_urls(title="Poemas Api")),
    url(r'^singIn/', SingIn.as_view()),
    url(r'^', include(router.urls), name="Api"),
]
