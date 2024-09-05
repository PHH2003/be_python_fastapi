def order_serial(order) -> dict:
    return {
        "id":str(order["_id"]),
        "fullName": str(order["fullName"]),
        "phoneNumber": str(order["phoneNumber"]),
        "city": str(order["city"]),
        "district": str(order["district"]),
        "commune": str(order["commune"]),
        "detailAddress": str(order["detailAddress"]),
        "total": float(order["total"]),
        "productName": str(order["productName"]),
        "productPrice": float(order["productPrice"]),
        "productQuantity": float(order["productQuantity"]),
        "payment_methods":str(order["payment_methods"]),
        "editBy": str(order["editBy"]),
        "orderStatus": str(order["orderStatus"]),
        "timestamp": str(order["timestamp"]),
    }

def list_order(orders) -> list:
    return[order_serial(order) for order in orders]