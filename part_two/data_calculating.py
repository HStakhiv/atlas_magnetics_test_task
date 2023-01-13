import math
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


def mean_calculating(data: list[int], round_digits: int) -> float:
    return round(sum(data) / len(data), round_digits)


def statistic_mean_calculating(data: list[int], round_digits: int) -> float:
    return round(statistics.mean(data), round_digits)


def median_calculating(data: list[int]) -> int | float:
    data_set_len = len(data)
    index = data_set_len // 2

    if data_set_len % 2:
        return sorted(data)[index]

    return sum(sorted(data)[index - 1:index + 1]) / 2


def statistic_median_calculating(data: list[int]) -> int | float:
    return statistics.median(data)


def mode_calculating(data: list[int]) -> list:
    seen_dict = dict()

    for item in data:
        if item in seen_dict:
            seen_dict[item] += 1
        else:
            seen_dict[item] = 1

    return [
        key
        for key in seen_dict.keys()
        if seen_dict[key] == max(seen_dict.values())
    ]


def statistic_mode_calculating(data: list[int]) -> list:
    return statistics.multimode(data)


def stdev_calculating(data: list[int], round_digits: int) -> float:
    deviations = [
        (x - mean_calculating(data, round_digits)) ** 2 for x in data
    ]
    variance = sum(deviations) / len(data)

    return round(math.sqrt(variance), round_digits)


def statistic_stdev_calculating(data: list[int], round_digits: int) -> float:
    return round(statistics.stdev(data), round_digits)


if __name__ == "__main__":
    print("Mean:", mean_calculating(DATA, ROUND_DIGITS))
    print(
        "Mean from statistics:", statistic_mean_calculating(DATA, ROUND_DIGITS)
    )
    print("Median:", median_calculating(DATA))
    print("Median from statistics:", statistic_median_calculating(DATA))
    print("Mode:", mode_calculating(DATA))
    print("Mode from statistics:", statistic_mode_calculating(DATA))
    print("Standard deviation:", stdev_calculating(DATA, ROUND_DIGITS))
    print(
        "Standard deviation from statistics:",
        statistic_stdev_calculating(DATA, ROUND_DIGITS),
    )
