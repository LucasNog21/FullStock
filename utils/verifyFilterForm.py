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

    return queryset
