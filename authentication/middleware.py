apps_name = ['company', 'apartment', 'authentication']

action_list = ['List', 'Create', 'Detail', 'Update', 'Delete']

role_user = ['roller1', 'roller2', 'roller3', 'roller4', 'User']

url_path = ['company', 'apartment', 'authentication']

method = ['GET', 'PUT', 'PATCH', "DELETE"]


# # class Midwave()
#         user_id = request.user.id
#             role_user = request.user.role
#         permissions = role_user.permissions

#
#         for permission in permissions.all():
#                 print(permission)
#
#         part_url = (request.path.split('/')[1] )
#         method =request.method
#
#         if user in apps_name and action in action_list and and role_user inrole_user  part_url = path and method in method:
#                 return True

from django.db.models import F
import re
from django.shortcuts import redirect
# from rest_framework import request
from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied
LOGIN_REDIRECT_URL = '/auth'
LOGIN_URL = '/auth/login/'

LOGIN_EXEMPT_URLS =(
        r'^auth/login/$',
        r'^auth/logout/$',
)


class DemoMiddleware:

        def __init__(self, get_response):
                self.get_response = get_response



        def __call__(self, request):

                print('hello Thao')
                response = self.get_response(request)
                print(response)
                self.test(request)

                return response
        #
        # def process_view(self, request, callback, callback_args, callback_kwargs):
        #         assert  hasattr(request, 'user')
        #         if not request.user.is_authenticated:
        #                 if True:
        #                         return redirect(LOGIN_URL)

        # def process_request(self, request):
        #         user = request.user
        #         # if not (user and user.is_authenticated() and user.email) and request.path in URLS:
        #         #         return redirect('')
        #         if user.role.id != 1:
        #                 raise 403
        #         return None


        def test(self,request):
                exclusion_list = ['/auth/register/', '/auth/login/']
                if request.path not in exclusion_list :
                        user = request.user
                        part_url = (request.path.split('/')[1])
                        method =request.method
                        global role_user
                        role = user.role
                        permissions = [permission for permission in (role.permissions.all())]
                        roler = [x for x in role_user]


                        # if role ==roler :
                        if user and user.is_authenticated and permissions in action_list:
                                return True


                else:
                        return False





