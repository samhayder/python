phone_prices = {
    'Apple':19500,
    'Samsung':65874,
    'Opp':215,
    'Walton':2548
}

min_prices = min(zip(phone_prices.values(),phone_prices.keys())) #(65874, 'Samsung')
max_prices = max(zip(phone_prices.values(),phone_prices.keys())) #(215, 'Opp')
sort_prices = sorted(zip(phone_prices.values(),phone_prices.keys())) #[(215, 'Opp'), (2548, 'Walton'), (19500, 'Apple'), (65874, 'Samsung')]