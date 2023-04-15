def sidebar_items(request):
    return {
        'sidebar_items': [
            {'name': 'Dashboard', 'url': 'farmerHome', 'icon': 'house'},
            {'name': 'Crops', 'url': 'crops', 'icon': 'psychiatry'},
            {'name': 'Equipments', 'url': "equipments", 'icon': 'agriculture'},
            {'name': 'Market', 'url': "404", 'icon': 'store'},
            {'name': 'Worker', 'url': "404", 'icon': 'engineering'},
            {'name': 'Feed', 'url': "404", 'icon': 'article'},
        ]
    }
