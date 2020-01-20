from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from jobhunter_api.views import *

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'jobs', Job)
router.register(r'contacts', Contact)
router.register(r'companys', Company)
router.register(r'stages', Stage)




urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^register$', register_user),
    url(r'^login$', login_user),
]
