import datetime as dt

INPUT_FILE = "input.txt"

def get_input(input_file=INPUT_FILE):
    """tranforms input file into a list"""
    input_lines = open(input_file).read().split()
    input_freqs = [int(x) for x in  input_lines]
    return input_freqs

def find_first_repeated_freq(input_freqs, current_freq=0):
    """finds which frequency is reached twice first
    the current frequency is found as the cummulative sum, the input frequencies
    can be read more than once with the starting frequency being the last cummulative
    frequency on the previous pass."""
    found = False
    set_of_sums = {current_freq}
    while not found:     
        for freq in input_freqs:
            current_freq += freq
            if current_freq in set_of_sums:
                found = True
                break
            set_of_sums.add(current_freq)
    return current_freq

    
def main():
    start = dt.datetime.now()

    input_freqs = get_input()
    print("sum of frequencies: ", sum(input_freqs))
    print("frequency reached twice: ", find_first_repeated_freq(input_freqs))
     
    end = dt.datetime.now()
    print("time taken: ", end-start)

if __name__ == "__main__":
    main()
