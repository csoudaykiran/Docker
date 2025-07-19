from flask import jsonify, request

items = {}
next_id = 1

def get_items():
    return jsonify(list(items.values())), 200

def add_item():
    global next_id
    item_data = request.json
    item_data["id"] = next_id
    items[next_id] = item_data
    next_id += 1
    return jsonify(item_data), 201

def get_item(item_id):
    item = items.get(item_id)
    if item:
        return jsonify(item), 200
    return {"message": "Item not found"}, 404

def update_item(item_id):
    if item_id in items:
        updated_data = request.json
        updated_data["id"] = item_id
        items[item_id] = updated_data
        return jsonify(updated_data), 200
    return {"message": "Item not found"}, 404

def delete_item(item_id):
    if item_id in items:
        del items[item_id]
        return '', 204
    return {"message": "Item not found"}, 404
