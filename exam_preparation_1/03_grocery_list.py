def shop_from_grocery_list(budgets, grocery_list, *args):
    for item in args:
        current_product = item[0]
        current_price = item[1]
        if current_product not in grocery_list:
            continue
        if float(current_price) > budgets:
            break
        else:
            budgets -= float(current_price)
            grocery_list.remove(current_product)
    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budgets:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
