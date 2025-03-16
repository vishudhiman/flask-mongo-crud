from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from app.database import mongo
from app.models import Item

api_blueprint = Blueprint("api", __name__)

# Create an item
@api_blueprint.route("/items", methods=["POST"])
def create_item():
    data = request.json
    item = {"name": data["name"], "description": data.get("description")}
    result = mongo.db.items.insert_one(item)
    return jsonify({"id": str(result.inserted_id), **item}), 201

# Read all items
@api_blueprint.route("/items", methods=["GET"])
def get_items():
    items = mongo.db.items.find()
    return jsonify([Item.to_dict(item) for item in items])

# Read a single item
@api_blueprint.route("/items/<string:item_id>", methods=["GET"])
def get_item(item_id):
    item = mongo.db.items.find_one({"_id": ObjectId(item_id)})
    if item:
        return jsonify(Item.to_dict(item))
    return jsonify({"error": "Item not found"}), 404

# Update an item
@api_blueprint.route("/items/<string:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.json
    update_data = {"$set": {"name": data.get("name"), "description": data.get("description")}}
    result = mongo.db.items.update_one({"_id": ObjectId(item_id)}, update_data)

    if result.matched_count:
        updated_item = mongo.db.items.find_one({"_id": ObjectId(item_id)})
        return jsonify(Item.to_dict(updated_item))
    return jsonify({"error": "Item not found"}), 404

# Delete an item
@api_blueprint.route("/items/<string:item_id>", methods=["DELETE"])
def delete_item(item_id):
    result = mongo.db.items.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count:
        return jsonify({"message": "Item deleted successfully"})
    return jsonify({"error": "Item not found"}), 404
