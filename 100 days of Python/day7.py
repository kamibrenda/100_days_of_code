
#write a function which returns the time since midnight in milliseconds.
#Input constraints:
#0 <= h <= 23
#0 <= m <= 59
#0 <= s <= 59

def past(h, m, s):
    total_milliseconds = (h * 60 * 60 + m * 60 + s) * 1000
    return total_milliseconds