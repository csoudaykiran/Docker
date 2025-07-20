from flask import jsonify, request

# In-memory data store with default items
items_store = {
    1: {"id": 1, "name": "Laptop", "price": 50000},
    2: {"id": 2, "name": "Smartphone", "price": 20000},
    3: {"id": 3, "name": "Headphones", "price": 1500}
}

# The next ID should be set to the next available integer
next_id = max(items_store.keys()) + 1 if items_store else 1

def get_items():
    return jsonify(list(items_store.values()))

def get_item(item_id):
    item = items_store.get(item_id)
    if not item:
        return {"error": "Item not found"}, 404
    return jsonify(item)

def add_item():
    global next_id
    data = request.json
    new_item = {"id": next_id, "name": data["name"], "price": data["price"]}
    items_store[next_id] = new_item
    next_id += 1
    return jsonify(new_item), 201

def update_item(item_id):
    data = request.json
    if item_id not in items_store:
        return {"error": "Item not found"}, 404
    items_store[item_id].update(data)
    return jsonify(items_store[item_id])

def delete_item(item_id):
    if item_id not in items_store:
        return {"error": "Item not found"}, 404
    del items_store[item_id]
    return "", 204
