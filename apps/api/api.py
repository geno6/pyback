from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.translation import ugettext as _, get_language


@api_view()
def index(request):
    language = get_language()
    return Response({"message": _("Welcome!")})