from django.shortcuts import render

# Create your views here.
def equipments(request):
    # Fetch Equipments information from database and pass it in the context. The format should be as follows:
    context = {
        "equipments": [
            {"name": "Equipment 1", "field1": "Field1 1", "field2": "Field2 1", "field3": "Field3 1", "field4": "Field4 1", "details": "Details 1"},
            {"name": "Equipment 2", "field1": "Field1 2", "field2": "Field2 2", "field3": "Field3 2", "field4": "Field4 2", "details": "Details 2"},
            {"name": "Equipment 3", "field1": "Field1 3", "field2": "Field2 3", "field3": "Field3 3", "field4": "Field4 3", "details": "Details 3"},
            {"name": "Equipment 4", "field1": "Field1 4", "field2": "Field2 4", "field3": "Field3 4", "field4": "Field4 4", "details": "Details 4"},
        ]
    }

    return render(request, "equipments.html", context)

def add_equipment(request):
    return render(request, "addequipment.html")
