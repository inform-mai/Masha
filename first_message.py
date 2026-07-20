from utils import convert_to_decimal, conver_to_chance

p_1 = convert_to_decimal(0.00154)
p_2 = convert_to_decimal(0.2)
p_3 = convert_to_decimal(0.05)
p_4 = convert_to_decimal(0.7)

result = p_1 * p_2 * p_3 * p_4

chance_first_message = conver_to_chance(result, 'Первое сообщение')
print(chance_first_message)