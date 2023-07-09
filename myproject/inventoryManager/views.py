from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from inventoryManager.models import Item
from inventoryManager.serializers import ItemSerializer

# Create your views here.

@csrf_exempt
def itemAPI(request):
    match request.method:
        case 'GET': return listItems()
        case 'POST': return addItem(request)
        case 'PUT': return updateItem(request)
        case 'DELETE': return deleteItem(request)
        case _: return JsonResponse({"message": "Method not allowed"}, status=405)
    
def listItems():
    items = Item.objects.all()
    items_serializer = ItemSerializer(items, many = True)
    return JsonResponse(items_serializer.data, safe=False)

def addItem(request):
    items_data = JSONParser().parse(request)
    added_items = []
    max_items = 50  # Maximum allowed items

    if len(items_data) > max_items:
        return JsonResponse({"message": "Exceeded maximum item limit of 50"}, status=400)

    for item_data in items_data:
        if len(added_items) >= max_items:
            break  # Stop adding items if the maximum limit is reached

        items_serializer = ItemSerializer(data=item_data)
        if items_serializer.is_valid():
            items_serializer.save()
            added_items.append(items_serializer.data)

    if added_items:
        return JsonResponse({"message": "Items added successfully", "items": added_items}, safe=False)
    else:
        return JsonResponse({"message": "Failed to add items"}, safe=False)


def updateItem(request):
    item_data = JSONParser().parse(request)
    item = Item.objects.get(item_id = item_data['item_id'])
    items_serializer = ItemSerializer(item, data=item_data)
    if items_serializer.is_valid():
        items_serializer.save()
        return JsonResponse('Item Updated',safe= False )
    return JsonResponse("Failed to Update")

def deleteItem(request):
    item_id = request.GET.get('id')
    
    if item_id is None:
        return JsonResponse({"message": "Item ID is required"}, status=400)
    
    try:
        item = Item.objects.get(item_id=item_id)
        item.delete()
        return JsonResponse({"message": "Item deleted successfully"})
    except Item.DoesNotExist:
        return JsonResponse({"message": "Item not found"}, status=404)