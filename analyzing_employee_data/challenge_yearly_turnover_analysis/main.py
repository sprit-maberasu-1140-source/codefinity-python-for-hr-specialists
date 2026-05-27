def print_turnover_rates(years, departures, headcounts):
    # Write your code here
    for year, departure, headcount in zip(years, departures, headcounts):
        turnover_rate = departure / headcount
        output = f"Year: {year} - Turnover Rate: {turnover_rate:.2%}"
        print(output)

years = [2020, 2021, 2022]
departures = [5, 8, 6]
headcounts = [50, 60, 55]

print_turnover_rates(years, departures, headcounts)
