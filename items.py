from flask import jsonify, request

# In-memory store for items
items_store = {
    1: {"id": 1, "name": "Laptop", "price": 1200.00},
    2: {"id": 2, "name": "Phone", "price": 800.00},
}
next_id = 3  # ID for the next new item

def get_items():
    """
    GET /items
    Returns a list of all items in the store.
    """
    return jsonify(list(items_store.values()))

def get_item(item_id):
    """
    GET /items/{item_id}
    Returns a specific item by ID.
    """
    item = items_store.get(item_id)
    if not item:
        return {"error": "Item not found"}, 404
    return jsonify(item)

def add_item():
    """
    POST /items
    Adds a new item to the store.
    Requires 'write' scope.
    """
    global next_id
    data = request.json
    new_item = {"id": next_id, "name": data["name"], "price": data["price"]}
    items_store[next_id] = new_item
    next_id += 1
    return jsonify(new_item), 201

def update_item(item_id):
    """
    PUT /items/{item_id}
    Updates an existing item.
    Requires 'write' scope.
    """
    if item_id not in items_store:
        return {"error": "Item not found"}, 404
    data = request.json
    items_store[item_id].update(data)
    return jsonify(items_store[item_id])

def delete_item(item_id):
    """
    DELETE /items/{item_id}
    Deletes an item by ID.
    Requires 'delete' scope.
    """
    if item_id not in items_store:
        return {"error": "Item not found"}, 404
    del items_store[item_id]
    return "", 204
