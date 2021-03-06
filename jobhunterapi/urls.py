from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from jobhunter_api.views import *
from jobhunter_api.models import *

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'job', Job, 'JobModel')
router.register(r'contact', Contact, 'ContactModel')
router.register(r'company', Company, 'CompanyModel')
router.register(r'stage', Stage, 'StageModel')




urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^register$', register_user),
    url(r'^login$', login_user),
]
