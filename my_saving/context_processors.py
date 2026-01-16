
# myapp/context_processors.py
def breadcrumbs(request):
    # Логика получения крошек (например, из URL-а или модели)
    # Здесь может быть обращение к MPTT или разбор URL
    crumbs = []

    if request.resolver_match:
        path = request.resolver_match.route
        parts = path.split('/')
        current_url = ''
        for part in parts:
            if part:
                current_url += '/' + part
                # Здесь нужно получить название для этой части пути
                # Для простоты, назовем ее частью пути
                crumbs.append((current_url, part.capitalize()))
    return {'breadcrumbs': crumbs}