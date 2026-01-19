# Market Sales Logic
def calculate_daily_sales(sale_list):
    total = sum(sale_list)
    count = len(sale_list)
    average = total / count if count > 0 else 0
    return total, average