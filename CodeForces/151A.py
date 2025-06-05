n, k, l, c, d, p, nl, np = map(int, input().split())
 
total_drink_ml = k * l
total_lime_slices = c * d
total_salt_grams = p
 
toasts_from_drink = total_drink_ml // (n * nl)
toasts_from_limes = total_lime_slices // n
toasts_from_salt = total_salt_grams // (n * np)
 
max_toasts = min(toasts_from_drink, toasts_from_limes, toasts_from_salt)
 
print(max_toasts)