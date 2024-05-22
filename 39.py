int_num = 5
float_num = 4.5
print(float_num + int_num)

bool_val = True
int_val = 7
print(int_val + bool_val)


int_num_sec = 50
float_num_sec = 7.5
print(int_num_sec * float_num_sec)

# NotImplemented - Не реализован функционал умножения целого числа на нецелое
print(int_num_sec.__mul__(float_num_sec))

print(float_num_sec.__rmul__(int_num_sec))

str_val = 'abc'
print(int_num * str_val)
