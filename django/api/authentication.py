from tastypie.authentication import ApiKeyAuthentication


class CustomAuthentication(ApiKeyAuthentication):

    def is_authenticated(self, request, **kwargs):
        return True if request.method == 'GET' \
            else super().is_authenticated(request, **kwargs)
