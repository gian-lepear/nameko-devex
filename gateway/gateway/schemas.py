from marshmallow import Schema, fields


class CreateOrderDetailSchema(Schema):
    product_id = fields.Str(required=True)
    price = fields.Decimal(as_string=True, required=True)
    quantity = fields.Int(required=True)


class CreateOrderSchema(Schema):
    order_details = fields.Nested(
        CreateOrderDetailSchema, many=True, required=True
    )


class GetOrderSchema(Schema):

    class OrderDetail(Schema):

        class Product(Schema):
            id = fields.Str()
            title = fields.Str()
            maximum_speed = fields.Int()
            in_stock = fields.Int()
            passenger_capacity = fields.Int()

        id = fields.Int()
        quantity = fields.Int()
        product_id = fields.Str()
        image = fields.Str()
        price = fields.Decimal(as_string=True)
        product = fields.Nested(Product, many=False)

    id = fields.Int()
    order_details = fields.Nested(OrderDetail, many=True)
