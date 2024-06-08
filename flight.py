#!/usr/bin/env python3

import sys
import json
from collections import defaultdict


def mapper():
    for line in sys.stdin:
        try:
            flight_number, date, passengers, max_capacity = line.strip().split(",")
            if flight_number == "flight_number":  # Skip header
                continue
            key = f"{flight_number}_{date}"
            value = {"passengers": int(passengers), "maxCapacity": int(max_capacity)}
            print(f"{key}\t{json.dumps(value)}")
        except ValueError:
          
            continue


# Reducer function
def reducer():
    current_key = None
    values = []
    for line in sys.stdin:
        try:
            key, value = line.strip().split("\t", 1)
            value = json.loads(value)  
            if current_key != key:
                if current_key:
                    process_key(current_key, values)
                values = []
                current_key = key
            values.append(value)
        except ValueError:
           
            continue
    if current_key:
        process_key(current_key, values)


def process_key(key, values):
    min_occupancy = min(value["passengers"] / value["maxCapacity"] for value in values)
    max_occupancy_freq = sum(value["passengers"] == value["maxCapacity"] for value in values)
    print(f"{key}\tminOccupancy\t{min_occupancy}")
    print(f"{key}\tmaxOccupancyFrequency\t{max_occupancy_freq}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "mapper":
        mapper()
    else:
        reducer()
