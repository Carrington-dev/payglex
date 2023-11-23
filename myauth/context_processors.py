def show_me(request):
    context = {}
    context['company'] = "Oftmart"    
    context['domain'] = "oftmart.com"    
    context['tel1'] = "+27 67 735 2242"    
    context['tel2'] = "+27 63 859 9481"    
    return context