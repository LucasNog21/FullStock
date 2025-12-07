def verifyFilter(filter_form, queryset):
    if filter_form.is_valid():

        name = filter_form.cleaned_data.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        description = filter_form.cleaned_data.get('description')
        if description:
            queryset = queryset.filter(description__icontains=description)

        initial_price = filter_form.cleaned_data.get('initial_price')
        if initial_price is not None:
            queryset = queryset.filter(salePrice__gte=initial_price)

        final_price = filter_form.cleaned_data.get('final_price')
        if final_price is not None:
            queryset = queryset.filter(salePrice__lte=final_price)

        initial_date = filter_form.cleaned_data.get('initial_date')
        if initial_date:
            queryset = queryset.filter(dueDate__gte=initial_date)

        final_date = filter_form.cleaned_data.get('final_date')
        if final_date:
            queryset = queryset.filter(dueDate__lte=final_date)

        cnpj = filter_form.cleaned_data.get('cnpj')
        if cnpj:
            queryset = queryset.filter(cnpj__icontains=cnpj)

        contact = filter_form.cleaned_data.get('contact')
        if contact:
            queryset = queryset.filter(contact__icontains=contact)

        provider = filter_form.cleaned_data.get('provider')
        if provider:
            queryset = queryset.filter(provider__icontains=provider)

        product = filter_form.cleaned_data.get('product')
        if product:
            queryset = queryset.filter(product__icontains=product)

        provider_name = filter_form.cleaned_data.get('provider_name')
        if provider_name:
            queryset = queryset.filter(provider__name__icontains=provider_name)

        product_name = filter_form.cleaned_data.get('product_name')
        if product_name:
            queryset = queryset.filter(product__name__icontains=product_name)

        status = filter_form.cleaned_data.get('status')
        if status:
            queryset = queryset.filter(status=status)

        start_date = filter_form.cleaned_data.get('start_date')
        if start_date:
            queryset = queryset.filter(orderDate__gte=start_date)

        end_date = filter_form.cleaned_data.get('end_date')
        if end_date:
            queryset = queryset.filter(orderDate__lte=end_date)

    return queryset
