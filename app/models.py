from app.database import mongo

class Item:
    @staticmethod
    def to_dict(item):
        return {
            "id": str(item["_id"]),
            "name": item["name"],
            "description": item.get("description", ""),
        }
