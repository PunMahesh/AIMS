def sidebar_items(request):
    return {
        'sidebar_items': [
            {'name': 'Dashboard', 'url': 'farmer_home', 'icon': 'house'},
            {'name': 'Crops', 'url': 'crops', 'icon': 'psychiatry'},
            {'name': 'Equipments', 'url': "equipments", 'icon': 'agriculture'},
            {'name': 'Article', 'url': "article", 'icon': 'newspaper'},
            {'name': 'Market', 'url': "404", 'icon': 'store'},

        ]
    }
