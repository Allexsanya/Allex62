import decimal
from pywebio.input import slider, FLOAT, NUMBER

from pywebio.input import input as pw_input

from pywebio.output import put_html, put_success

CHEESE_PRICE = decimal.Decimal(286.35)
POTATO_PRICE = decimal.Decimal(40.32)


# HEADER
put_html("<h1>Welcome to our shops</h1>")


# INPUT SECTION

cheese_weight = slider(
    "Cheese", type=FLOAT, min_value=0, max_value=5, value=0.15, required=True
)
cheese_weight = decimal.Decimal(cheese_weight)
potato_weight = pw_input(
    "Potato", type=NUMBER, required=True, min_value=0, max_value=10, value=3
)
potato_weight = decimal.Decimal(potato_weight)
print("Selected cheese weight:", cheese_weight)
print("Selected potato weight:", potato_weight)

cheese_cost = cheese_weight * CHEESE_PRICE
potato_cost = potato_weight * POTATO_PRICE

total_cost = cheese_cost + potato_cost
put_success(f"Total cost: {cheese_cost=} {potato_cost=} {total_cost}")


pass
