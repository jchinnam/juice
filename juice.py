#!/usr/bin/env python3

from datetime import datetime

# core fruit seasonality (approximate, for CA)
# Uuses California and Mexico-imported availability as the “default” (since it’s what most people in U.S. stores see).
BASE_SEASONAL_FRUIT = {
    "apples": (8, 11),
    "apricots": (5, 7),
    "avocados": (1, 3),
    "bananas": (1, 12),
    "blackberries": (6, 8),
    "blueberries": (5, 8),
    "cantaloupe": (6, 9),
    "cherries": (6, 7),
    "clementines": (11, 2),
    "cranberries": (9, 11),
    "dates": (9, 12),
    "figs": (6, 9),
    "grapefruit": (1, 5),
    "grapes": (8, 10),
    "guava": (8, 11),
    "honeydew": (7, 10),
    "kiwi": (10, 5),
    "lemons": (1, 5),
    "limes": (5, 10),
    "lychee": (6, 7),
    "mangoes": (3, 7),
    "mulberries": (5, 6),
    "nectarines": (6, 8),
    "oranges": (12, 4),
    "papayas": (1, 12),
    "peaches": (5, 9),
    "pears": (8, 11),
    "persimmons": (10, 12),
    "pineapples": (1, 12),
    "plums": (5, 9),
    "pomegranates": (9, 12),
    "raspberries": (6, 9),
    "starfruit": (7, 2),
    "strawberries": (3, 6),
    "tangerines": (11, 1),
    "watermelon": (6, 9),
}

# region offsets: shifts in start/end month
REGION_OFFSETS = {
    "west": (0, 0),
    "pacific_northwest": (1, -1),
    "southwest": (-1, 0),
    "southeast": (0, 1),
    "midwest": (1, 1),
    "northeast": (1, 1),
    "mountain_west": (1, 1),
}

REGION_NAMES = {
    "1": "west",
    "2": "pacific_northwest",
    "3": "southwest",
    "4": "southeast",
    "5": "midwest",
    "6": "northeast",
    "7": "mountain_west",
}

def choose_region():
    print("select your region:")
    for number, key in REGION_NAMES.items():
        print(f" {number}. {key.replace('_', ' ')}")
    choice = input("enter a number (1–7): ").strip()
    return REGION_NAMES.get(choice, "west")  # default to "west"

def apply_region_offset(base_seasons, offset):
    adjusted = {}
    for fruit, (start, end) in base_seasons.items():
        new_start = (start + offset[0] - 1) % 12 + 1
        new_end = (end + offset[1] - 1) % 12 + 1
        adjusted[fruit] = (new_start, new_end)
    return adjusted

def is_in_season(start, end, month):
    return start <= month <= end if start <= end else month >= start or month <= end

def main():
    region = choose_region()
    offset = REGION_OFFSETS.get(region, (0, 0))
    seasonal_data = apply_region_offset(BASE_SEASONAL_FRUIT, offset)

    current_month = datetime.now().month
    next_month = current_month % 12 + 1

    in_season = []
    leaving_soon = []
    coming_soon = []

    for fruit, (start, end) in seasonal_data.items():
        if is_in_season(start, end, current_month):
            in_season.append(fruit)
            if not is_in_season(start, end, next_month):
                leaving_soon.append(fruit)
        elif is_in_season(start, end, next_month):
            coming_soon.append(fruit)

    print(f"\nregion: {region.replace('_', ' ')}")
    print(f"month: {datetime.now().strftime('%B').lower()}\n")

    print("🍓 in season!")
    print(", ".join(in_season) if in_season else "None")

    print("\n🍂 going out of season soon :(")
    print(", ".join(leaving_soon) if leaving_soon else "None")

    print("\n🌱 will be in season soon!")
    print(", ".join(coming_soon) if coming_soon else "None")

if __name__ == "__main__":
    main()
