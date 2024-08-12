def individual_serial_user(user) -> dict:
    return {
        "name": user.get("name"),
        "email": user.get("email"),
        "phone": user.get("phone", None),
        "address": [
            {
                "line1": address.get("line1"),
                "line2": address.get("line2", None),
                "district": address.get("district"),
                "state": address.get("state"),
                "pincode": address.get("pincode")
            }
            for address in user.get("address", [])
        ] if user.get("address") else None,
        "orders": user.get("orders", []),
        "wishlist": user.get("wishlist", [])
    }

def list_serial_user(users) -> list:
    return [individual_serial_user(user) for user in users]
