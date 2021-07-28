from django.shortcuts import render
from VEGAN_API.VEGAN_API_ACCOUNT.forms import UserModelForm


def checkout(request):

    user_info_form = UserModelForm(instance=request.user)


    context = {
        'info_form'  : user_info_form
    }
    return render(request, 'checkout.html', context)