from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    仅管理员用户可进行修改
    其他用户仅可查看
    """
    def has_permission(self, request, view):
        # 对所有人允许 GET, HEAD or OPTIONS 请求.
        if request.method in permissions.SAFE_METHODS:
            return True
        # 仅管理员可进行其他操作
        return request.user.is_superuser

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    允许对象的所有者进行编辑，其他用户仅可查看
    """
    def has_object_permission(self, request, view, obj):
        # 对所有人允许 GET, HEAD or OPTIONS 请求.
        if request.method in permissions.SAFE_METHODS:
            return True
        # 仅对象的所有者可进行其他操作
        return obj.author == request.user

class IsAuthenticatedAndOwner(permissions.BasePermission):
    """
    仅允许经过身份验证的用户且是对象的所有者进行操作
    """
    def has_object_permission(self, request, view, obj):
        # 用户必须经过身份验证且是对象的所有者
        return request.user.is_authenticated and obj.author == request.user

class RoleBasedPermission(permissions.BasePermission):
    """
    基于用户角色的权限控制
    """
    def has_permission(self, request, view):
        # 假设用户模型有一个角色字段
        if request.user.is_authenticated:
            if request.user.role == 'admin':
                return True  # 管理员有所有权限
            elif request.user.role == 'editor':
                return request.method in permissions.SAFE_METHODS or request.method == 'POST'
            elif request.user.role == 'user':
                return request.method in permissions.SAFE_METHODS
        return False

# 其他常见权限
class AllowAny(permissions.AllowAny):
    """
    允许任何用户访问，无论请求是否经过身份验证
    """
    pass
class IsAuthenticated(permissions.IsAuthenticated):
    """
    仅允许经过身份验证的用户访问
    """
    pass

class IsAdminUser(permissions.IsAdminUser):
    """
    仅允许管理员用户访问
    """
    pass

class IsAuthenticatedOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """
    允许未认证用户进行只读操作，而认证用户可以进行读写操作
    """
    pass

class DjangoModelPermissions(permissions.DjangoModelPermissions):
    """
    基于Django模型的权限，要求用户对模型具有适当的权限
    """
    pass

class DjangoModelPermissionsOrAnonReadOnly(permissions.DjangoModelPermissionsOrAnonReadOnly):
    """
    未认证用户可以进行只读操作，认证用户需要具有模型权限
    """
    pass
#这些类的实现通常不需要额外的代码，因为它们的功能已经在Django REST Framework中定义好了。你只需要在视图中引用这些权限类即可。

