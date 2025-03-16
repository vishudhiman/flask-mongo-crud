from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from bson.objectid import ObjectId
from app.database import mongo
from app.models import Item

api_blueprint = Blueprint("api", __name__)

# Display all items (API + HTML)
@api_blueprint.route("/", methods=["GET"])
def index():
    items = list(mongo.db.items.find())

    if request.headers.get('Accept') == 'application/json':
        return jsonify([Item.to_dict(item) for item in items])

    return render_template('index.html', items=[Item.to_dict(item) for item in items])

# Create an item (API + HTML)
@api_blueprint.route("/items", methods=["POST", "GET"])
def create_item():
    if request.method == "POST":
        data = request.json if request.is_json else request.form
        item = {"name": data["name"], "description": data.get("description")}
        result = mongo.db.items.insert_one(item)

        if request.is_json:
            return jsonify({"id": str(result.inserted_id), **item}), 201
        
        return redirect(url_for("api.index"))

    # Display add item form (GET)
    return render_template('add_item.html')

# Update an item (API + HTML)
@api_blueprint.route("/items/<string:item_id>", methods=["PUT", "POST", "GET"])
def update_item(item_id):
    item = mongo.db.items.find_one({"_id": ObjectId(item_id)})

    if request.method in ["POST", "PUT"]:
        data = request.json if request.is_json else request.form
        update_data = {"$set": {"name": data.get("name"), "description": data.get("description")}}
        mongo.db.items.update_one({"_id": ObjectId(item_id)}, update_data)

        if request.is_json:
            updated_item = mongo.db.items.find_one({"_id": ObjectId(item_id)})
            return jsonify(Item.to_dict(updated_item))

        return redirect(url_for("api.index"))

    # Display update form (GET)
    return render_template('update_item.html', item=Item.to_dict(item))

# Delete an item (API + HTML)
@api_blueprint.route("/items/<string:item_id>/delete", methods=["POST", "GET"])
def delete_item(item_id):
    item = mongo.db.items.find_one({"_id": ObjectId(item_id)})

    if request.method == "POST":
        mongo.db.items.delete_one({"_id": ObjectId(item_id)})

        if request.is_json:
            return jsonify({"message": "Item deleted successfully"})

        return redirect(url_for("api.index"))

    # Display delete confirmation form (GET)
    return render_template('delete_item.html', item=Item.to_dict(item))
