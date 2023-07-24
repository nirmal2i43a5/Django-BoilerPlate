from django.urls import  path
from .views import (UserRoleCreate, UserRoleUpdate,UserRoleMange,UserPermissionCreate,
                                   user_permission_manage,save_permission)

app_name = 'role_app'

urlpatterns = [
    path('role/add/',UserRoleCreate.as_view(),name = 'add_role'),
    path('role/edit/<str:pk>/',UserRoleUpdate.as_view(),name = 'edit_role'),
    path('index/role/',UserRoleMange.as_view(),name = 'manage_role'),
     path('permission/add/',UserPermissionCreate.as_view(),name = 'add_permission'),
    # path('edit_permission/<str:pk>/',UserRoleUpdate.as_view(),name = 'edit_permission'),
      path('index/permission/',user_permission_manage,name = 'manage_permission'),
      path('save_permission/',save_permission,name = 'save_permission'),
      path('permission-management/', UserRoleMange.as_view(),name = 'permission-management'),
]