def verifyFilter(filter_form, queryset):


    if not filter_form.is_valid():
        return queryset

    data = filter_form.cleaned_data

    name = data.get('name')
    if name and queryset.model._meta.get_field('name', None):
        queryset = queryset.filter(name__icontains=name)

    description = data.get('description')
    if description and hasattr(queryset.model, 'description'):
        queryset = queryset.filter(description__icontains=description)

    cnpj = data.get('cnpj')
    if cnpj and hasattr(queryset.model, 'cnpj'):
        queryset = queryset.filter(cnpj__icontains=cnpj)

    contact = data.get('contact')
    if contact and hasattr(queryset.model, 'contact'):
        queryset = queryset.filter(contact__icontains=contact)

    provider = data.get('provider_name') or data.get('provider')
    if provider and hasattr(queryset.model, 'provider'):
        queryset = queryset.filter(provider__name__icontains=provider)

    product = data.get('product_name') or data.get('product')
    if product and hasattr(queryset.model, 'product'):
        queryset = queryset.filter(product__name__icontains=product)

    initial_price = data.get('initial_price')
    if initial_price is not None and hasattr(queryset.model, 'salePrice'):
        queryset = queryset.filter(salePrice__gte=initial_price)

    final_price = data.get('final_price')
    if final_price is not None and hasattr(queryset.model, 'salePrice'):
        queryset = queryset.filter(salePrice__lte=final_price)

    status = data.get('status')
    if status and hasattr(queryset.model, 'status'):
        queryset = queryset.filter(status=status)

    start_date = data.get('start_date') or data.get('initial_date')
    end_date = data.get('end_date') or data.get('final_date')

    if hasattr(queryset.model, 'dueDate'):
        if start_date:
            queryset = queryset.filter(dueDate__gte=start_date)
        if end_date:
            queryset = queryset.filter(dueDate__lte=end_date)

    if hasattr(queryset.model, 'orderDate'):
        if start_date:
            queryset = queryset.filter(orderDate__gte=start_date)
        if end_date:
            queryset = queryset.filter(orderDate__lte=end_date)

    if hasattr(queryset.model, 'saleDate'):
        if start_date:
            queryset = queryset.filter(saleDate__gte=start_date)
        if end_date:
            queryset = queryset.filter(saleDate__lte=end_date)

    user_name = data.get('user_name')
    if user_name and hasattr(queryset.model, 'user'):
        queryset = queryset.filter(user__username__icontains=user_name)

    return queryset
