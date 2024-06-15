import random

def monte_carlo_cbrt_x2(num_samples):
    total_sum = 0
    for _ in range(num_samples):
        x = random.uniform(0, 1) #mantenha o x entre 0 e 1 para maior precisão
        y = (x**(2/3))
        total_sum += y
    
    estimated_value = total_sum / num_samples
    return estimated_value

num_samples = 1000000
estimated_cbrt_x2 = monte_carlo_cbrt_x2(num_samples)
print(f"Valor estimado de cbrt(x**3): {estimated_cbrt_x2}")