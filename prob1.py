class Solution:
    def city_revenue(self, orders):
        revenue_dict = {}

        # Calculate total revenue per city
        for order in orders:
            city = order["city"]
            amount = order["amount"]

            if city in revenue_dict:
                revenue_dict[city] += amount
            else:
                revenue_dict[city] = amount

        # Find city with highest revenue
        highest_city = max(revenue_dict, key=revenue_dict.get)

        return revenue_dict, highest_city