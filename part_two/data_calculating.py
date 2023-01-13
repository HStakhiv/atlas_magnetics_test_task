import statistics

DATA = [
    364,
    373,
    358,
    394,
    378,
    379,
    357,
    364,
    350,
    363,
    392,
    368,
    359,
    375,
    399,
    365,
    379,
    357,
    380,
]

ROUND_DIGITS = 2


def mean_calculating(data: list, round_digits: int) -> float:
    return round(sum(data) / len(data), round_digits)


def statistic_mean_calculating(data: list, round_digits: int) -> float:
    return round(statistics.mean(data), round_digits)


if __name__ == "__main__":
    print(mean_calculating(DATA, ROUND_DIGITS))
    print(statistic_mean_calculating(DATA, ROUND_DIGITS))
