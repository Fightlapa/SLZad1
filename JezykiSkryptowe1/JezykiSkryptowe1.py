import inspect
import time

SIZE = 0x1ffff
EXTREME_VALUE = 0xfffffffff

def generate_test_data():
    with open("TestData.txt", "w") as fout:
        for i in range (-SIZE - 0x1, SIZE + 0x1):
            fout.write(f"{i},{oct(i)},")
        extreme_value = 0xfffffffff
        fout.write(f"{EXTREME_VALUE},{oct(EXTREME_VALUE)}")


def measure(func):
    empty_loop_start = time.clock()
    for i in range (-SIZE - 0x1, SIZE + 0x1):
        this_is_to_avoid_negative_time = "Problem exists probably because of the cycles required to perform both loops and it occurs, that empty one executes slower."
    empty_loop_end = time.clock()
    loop_start = time.clock()
    for i in range (-SIZE - 0x1, SIZE + 0x1):
        this_is_to_avoid_negative_time = "Problem exists probably because of the cycles required to perform both loops and it occurs, that empty one executes slower."
        value = func(i)
    loop_end = time.clock()
    return (loop_end - loop_start) - (empty_loop_end - empty_loop_start)

def my_oct(value: int):
    oct_value = ""
    if value < 0:
        oct_prefix = "-0o"
        value = - value
    elif value > 0:
        oct_prefix = "0o"
    else:
        return "0o0"
    while value > 0:
        character = str(value & 0b111)
        value = value >> 3
        oct_value = character + oct_value
    return (oct_prefix + oct_value)

def test():
    for i in range (-SIZE - 0x1, SIZE + 0x1):
        if my_oct(i) != oct(i):
            raise Exception()
    if my_oct(EXTREME_VALUE) != oct(EXTREME_VALUE):
            raise Exception()


if __name__ == "__main__":
    generate_test_data()
    test()
    print(measure(oct))
    print(measure(my_oct))
    input()

