# juice

what's the juice? which fruits are currently in season, about to go out of season, or coming in soon — based on your region

## usage

```
./juice.py

# will be prompted to input your region
select your region:
 1. west
 2. pacific northwest
 3. southwest
 4. southeast
 5. midwest
 6. northeast
 7. mountain west
enter a number (1–7):

# sample output
region: pacific northwest
month: may

🍓 in season!
strawberries, avocados, lemons, bananas

🍂 going out of season soon :(
avocados

🌱 will be in season soon!
blueberries, blackberries, cherries
```

## data
`juice` approximates store availability using California/Mexico data, adjusted by region because California dominates U.S. fruit production. Much of the national grocery supply of fresh produce comes from California (and Mexico), but "seasonality" varies by region, microclimates, cultivars, and climate shifts, so the data is tweaked per region with simple month shifts (`REGION_OFFSETS`) to roughly reflect differences in local harvest timing.
