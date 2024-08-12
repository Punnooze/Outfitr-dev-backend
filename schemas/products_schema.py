def individual_serial_product(product) -> dict:
    return {
        "seller": product.get("seller"),
        "brand": product.get("brand"),
        "product_id": product.get("product_id"),
        "product_url": product.get("product_url"),
        "cover_image": product.get("cover_image"),
        "images": product.get("images", []),
        "product_name": product.get("product_name"),
        "sizes_available": product.get("sizes_available", []),
        "price": product.get("price"),
        "primary_colour": product.get("primary_colour"),
        "secondary_colour": product.get("secondary_colour"),
        "material": product.get("material"),
        "fit": product.get("fit"),
        "occasion": product.get("occasion"),
        "season": product.get("season"),
        "theme": product.get("theme"),
        "gender": product.get("gender"),
        "pattern": product.get("pattern"),
        "master_category": product.get("master_category"),
        "sub_category": product.get("sub_category"),
        "LLM_desc": product.get("LLM_desc"),
        "others": product.get("others")
    }

def list_serial_product(products) -> list:
    return [individual_serial_product(product) for product in products]
