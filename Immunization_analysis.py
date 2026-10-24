
import csv

# Open the sample immunization dataset
with open("data/sample_Immunization.csv", "r", newline="") as file:
    data = csv.DictReader(file)

    total_children = 0
    total_vaccinated = 0

    print("SAMPLE IMMUNIZATION DATA ANALYSIS")
    print("--------------------------------")

    for row in data:
        region = row["Region"]
        surveyed = int(row["Children_Surveyed"])
        vaccinated = int(row["Children_Vaccinated"])

        coverage = (vaccinated / surveyed) * 100

        print(f"{region}: {coverage:.1f}% coverage")

        total_children += surveyed
        total_vaccinated += vaccinated

    overall_coverage = (total_vaccinated / total_children) * 100

    print("--------------------------------")
    print(f"Total children surveyed: {total_children}")
    print(f"Total vaccinated: {total_vaccinated}")
    print(f"Overall coverage: {overall_coverage:.1f}%")
