def verifyFilter(filter_form, queryset):

    if not filter_form.is_valid():
        return queryset

    data = filter_form.cleaned_data
    model = queryset.model

    simple_filters = {
        'name': 'name__icontains',
        'description': 'description__icontains',
        'cnpj': 'cnpj__icontains',
        'contact': 'contact__icontains',
        'status': 'status',
    }

    for form_field, filter_expr in simple_filters.items():
        value = data.get(form_field)
        model_field = filter_expr.split("__")[0]

        if value and hasattr(model, model_field):
            queryset = queryset.filter(**{filter_expr: value})


    related_filters = {
        'provider_name': ('provider', 'provider__name__icontains'),
        'provider': ('provider', 'provider__name__icontains'),
        'product_name': ('product', 'product__name__icontains'),
        'product': ('product', 'product__name__icontains'),
        'user_name': ('user', 'user__username__icontains'),
    }

    for form_field, (related_field, filter_expr) in related_filters.items():
        value = data.get(form_field)
        if value and hasattr(model, related_field):
            queryset = queryset.filter(**{filter_expr: value})


    if hasattr(model, 'salePrice'):
        initial_price = data.get('initial_price')
        final_price = data.get('final_price')

        if initial_price is not None:
            queryset = queryset.filter(salePrice__gte=initial_price)

        if final_price is not None:
            queryset = queryset.filter(salePrice__lte=final_price)


    date_fields = ['dueDate', 'orderDate', 'saleDate']
    start_date = data.get('start_date') or data.get('initial_date')
    end_date = data.get('end_date') or data.get('final_date')

    for field in date_fields:
        if hasattr(model, field):
            if start_date:
                queryset = queryset.filter(**{f"{field}__gte": start_date})
            if end_date:
                queryset = queryset.filter(**{f"{field}__lte": end_date})

    return queryset
