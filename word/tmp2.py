target_number = 225568
divisor = 2000

nearest_multiple = (target_number // divisor) * divisor

if target_number % divisor >= divisor / 2:
    nearest_multiple += divisor

print(nearest_multiple)
