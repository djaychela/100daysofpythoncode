import cProfile
profiler = cProfile.Profile()
profiler.disable()

import research_v2


def main():
    print("Weather research for Seattle, 2014-2015")
    print()
    profiler.enable()
    research_v2.init()

    hot_days = research_v2.hot_days()
    cold_days = research_v2.cold_days()
    wet_days = research_v2.wet_days()

    profiler.disable()

    print("The hottest 5 days:")
    for idx, d in enumerate(hot_days[:5]):
        print("{}. {} F on {}".format(idx+1, d.actual_max_temp, d.date))
    print()
    print("The coldest 5 days:")

    for idx, d in enumerate(cold_days[:5]):
        print("{}. {} F on {}".format(idx+1, d.actual_min_temp, d.date))
    print()
    print("The wettest 5 days:")

    for idx, d in enumerate(wet_days[:5]):
        print("{}. {} inches of rain on {}".format(idx+1, d.actual_precipitation, d.date))


if __name__ == '__main__':
    for i in range(100):
        main()

    profiler.print_stats(sort='cumtime')
