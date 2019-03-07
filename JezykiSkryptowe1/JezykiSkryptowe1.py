import inspect
import time

SIZE = 0x1ffff
EXTREME_VALUE = 0xfffffffff

def generate_test_data():
    with open("TestData.txt", "w") as fout:
        for i in range (-SIZE, SIZE):
            fout.write(f"{i},{oct(i)},")
        extreme_value = 0xfffffffff
        fout.write(f"{EXTREME_VALUE},{oct(EXTREME_VALUE)}")

def measure(func):
    empty_loop_start = time.clock()
    for i in range (-SIZE, SIZE):
        this_is_to_avoid_negative_time = \
        "Probably because of the instruction pipelining while performing both loops it occurs, that empty one executes slower."
    mid_time = time.clock()

    for i in range (-SIZE, SIZE):
        this_is_to_avoid_negative_time = \
        "Probably because of the instruction pipelining while performing both loops it occurs, that empty one executes slower."
        value = func(i)
    loop_end = time.clock()
    print("Empty loop time:" + str(mid_time - empty_loop_start))
    print("Full time:" + str(loop_end - mid_time))
    return (loop_end - mid_time) - (mid_time - empty_loop_start)

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

if __name__ == "__main__":
    generate_test_data()
    for i in range(0, 3):
        print("Oct summed execution time:" + str(measure(oct)))
        print("My_oct summed func execution time:" + str(measure(my_oct)))
    input()

