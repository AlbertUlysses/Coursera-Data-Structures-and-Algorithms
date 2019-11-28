# python3
import sys


def compute_min_refills(distance, tank, stops):
    refills = 0
    stop_num = 0
    potential_distance = tank
    stops = [0] + stops + [distance] 
    while stop_num < len(stops)-1 and potential_distance < distance:
        last_stop = stop_num
        while stop_num < len(stops)-1:
            if stops[stop_num] == potential_distance or stops[stop_num] < potential_distance < stops[stop_num +1]:
                break
            stop_num += 1
        potential_distance = tank + stops[stop_num]
        refills += 1
        if potential_distance < stops[stop_num+1]:
            return -1
    if potential_distance >= distance:
        return refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
