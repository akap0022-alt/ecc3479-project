#sunshine
import pandas as pd

# Load Excel file
file_path = r"C:\Users\ashit\OneDrive\Desktop\Y3S2\ECC 3479 - Data and Evidence in Economics\ECC3479 - Data Analysis Project\data\raw\abs_population.xlsx"

# Read header rows so the year columns are correctly identified
header_rows = pd.read_excel(file_path, sheet_name="Table 1", header=None, nrows=6)
column_names = header_rows.iloc[5, :10].tolist() + header_rows.iloc[4, 10:].tolist()

# Read the actual data starting after the header rows
df = pd.read_excel(file_path, sheet_name="Table 1", header=None, skiprows=6)
df.columns = column_names

# Filter only Sunshine
sunshine_df = df[df["SA2 name"] == "Sunshine"].copy()
if sunshine_df.empty:
    raise ValueError("Sunshine row not found in the data.")

# Identify year columns from 2001 to 2025
year_cols = [col for col in column_names if isinstance(col, (int, float)) and 2001 <= int(col) <= 2025]

sunshine_df[year_cols] = sunshine_df[year_cols].apply(pd.to_numeric, errors="coerce")

# Convert wide to long
sunshine_long = sunshine_df.melt(
    id_vars="SA2 name",
    value_vars=year_cols,
    var_name="Year",
    value_name="Population"
)

sunshine_long["Year"] = sunshine_long["Year"].astype(int)

# Keep only 2018–2025
sunshine_long = sunshine_long[
    (sunshine_long["Year"] >= 2018) & (sunshine_long["Year"] <= 2025)
].copy()

# Add density using Sunshine area in km²
area = 7.3
sunshine_long["Area_km2"] = area
sunshine_long["Density"] = sunshine_long["Population"] / area

# Save clean output
target_path = r"C:\Users\ashit\OneDrive\Desktop\Y3S2\ECC 3479 - Data and Evidence in Economics\ECC3479 - Data Analysis Project\data\clean\sunshine_density.csv"
sunshine_long.to_csv(target_path, index=False)
print(f"Saved Sunshine density table to {target_path}")
print(sunshine_long)
Year	Population	Area (km²)	Density (people/km²)
2018	10,318	7.3	1413.42
2019	10,306	7.3	1411.78
2020	10,100	7.3	1383.56
2021	9,568	7.3	1310.68
2022	9,601	7.3	1315.21
2023	9,910	7.3	1357.53
2024	10,059	7.3	1377.95
2025	10,151	7.3	1390.55






#bundoora-east 
import pandas as pd
from pathlib import Path

project_root = Path.cwd()
if not (project_root / "data" / "raw").exists():
    project_root = project_root.parent
input_path = project_root / "data" / "raw" / "abs_population.xlsx"
output_dir = project_root / "data" / "clean"
output_dir.mkdir(parents=True, exist_ok=True)

header_rows = pd.read_excel(input_path, sheet_name="Table 1", header=None, nrows=6)
column_names = header_rows.iloc[5, :10].tolist() + header_rows.iloc[4, 10:].tolist()

df = pd.read_excel(input_path, sheet_name="Table 1", header=None, skiprows=6)
df.columns = column_names

year_cols = [col for col in column_names if isinstance(col, (int, float)) and 2001 <= int(col) <= 2025]

suburb_name = "Bundoora - East"
area_km2 = 15.0

suburb_df = df[df["SA2 name"] == suburb_name].copy()
if suburb_df.empty:
    raise ValueError(f"{suburb_name} row not found")

suburb_df[year_cols] = suburb_df[year_cols].apply(pd.to_numeric, errors="coerce")

suburb_long = suburb_df.melt(
    id_vars="SA2 name",
    value_vars=year_cols,
    var_name="Year",
    value_name="Population"
)

suburb_long["Year"] = suburb_long["Year"].astype(int)
suburb_long = suburb_long[
    (suburb_long["Year"] >= 2018) & (suburb_long["Year"] <= 2025)
].copy()
suburb_long["Area_km2"] = area_km2
suburb_long["Density"] = suburb_long["Population"] / area_km2

output_path = output_dir / "bundoora-east_density.csv"
suburb_long.to_csv(output_path, index=False)

print("Bundoora - East population density (2018-2025)")
print(f"Land area: {area_km2} km²")
print(f"Saved table to: {output_path}")
print(suburb_long)
  SA2 name  Year  Population  Area_km2     Density
17  Bundoora - East  2018     10359.0      15.0  690.600000
18  Bundoora - East  2019     10372.0      15.0  691.466667
19  Bundoora - East  2020     10295.0      15.0  686.333333
20  Bundoora - East  2021      9920.0      15.0  661.333333
21  Bundoora - East  2022      9814.0      15.0  654.266667
22  Bundoora - East  2023      9993.0      15.0  666.200000
23  Bundoora - East  2024     10196.0      15.0  679.733333
24  Bundoora - East  2025     10339.0      15.0  689.266667




#brunswick east
import pandas as pd
from pathlib import Path

project_root = Path.cwd()
if not (project_root / "data" / "raw").exists():
    project_root = project_root.parent

input_path = project_root / "data" / "raw" / "abs_population.xlsx"
output_dir = project_root / "data" / "clean"
output_dir.mkdir(parents=True, exist_ok=True)

header_rows = pd.read_excel(input_path, sheet_name="Table 1", header=None, nrows=6)
column_names = header_rows.iloc[5, :10].tolist() + header_rows.iloc[4, 10:].tolist()

df = pd.read_excel(input_path, sheet_name="Table 1", header=None, skiprows=6)
df.columns = column_names

year_cols = [
    col for col in column_names
    if isinstance(col, (int, float)) and 2001 <= int(col) <= 2025
]

suburb_name = "Brunswick East"
area_km2 = 5.2

suburb_df = df[df["SA2 name"] == suburb_name].copy()
if suburb_df.empty:
    raise ValueError(f"{suburb_name} row not found")

suburb_df[year_cols] = suburb_df[year_cols].apply(pd.to_numeric, errors="coerce")

suburb_long = suburb_df.melt(
    id_vars="SA2 name",
    value_vars=year_cols,
    var_name="Year",
    value_name="Population"
)

suburb_long["Year"] = suburb_long["Year"].astype(int)
suburb_long = suburb_long[
    (suburb_long["Year"] >= 2018) & (suburb_long["Year"] <= 2025)
].copy()

suburb_long["Area_km2"] = area_km2
suburb_long["Density"] = suburb_long["Population"] / area_km2

output_path = output_dir / "brunswick-east_density.csv"
suburb_long.to_csv(output_path, index=False)

print("Brunswick East population density (2018-2025)")
print(f"Land area: {area_km2} km²")
print(f"Saved table to: {output_path}")
print(suburb_long)
 SA2 name  Year  Population  Area_km2      Density
17  Brunswick East  2018     12392.0       5.2  2383.076923
18  Brunswick East  2019     12602.0       5.2  2423.461538
19  Brunswick East  2020     13064.0       5.2  2512.307692
20  Brunswick East  2021     12964.0       5.2  2493.076923
21  Brunswick East  2022     13238.0       5.2  2545.769231
22  Brunswick East  2023     13691.0       5.2  2632.884615
23  Brunswick East  2024     14328.0       5.2  2755.384615
24  Brunswick East  2025     14693.0       5.2  2825.576923




#coburg east
import pandas as pd
from pathlib import Path

project_root = Path.cwd()
if not (project_root / "data" / "raw").exists():
    project_root = project_root.parent

input_path = project_root / "data" / "raw" / "abs_population.xlsx"
output_dir = project_root / "data" / "clean"
output_dir.mkdir(parents=True, exist_ok=True)

header_rows = pd.read_excel(input_path, sheet_name="Table 1", header=None, nrows=6)
column_names = header_rows.iloc[5, :10].tolist() + header_rows.iloc[4, 10:].tolist()

df = pd.read_excel(input_path, sheet_name="Table 1", header=None, skiprows=6)
df.columns = column_names

year_cols = [
    col for col in column_names
    if isinstance(col, (int, float)) and 2001 <= int(col) <= 2025
]

suburb_name = "Coburg - East"
area_km2 = 7.0

suburb_df = df[df["SA2 name"] == suburb_name].copy()
if suburb_df.empty:
    raise ValueError(f"{suburb_name} row not found")

suburb_df[year_cols] = suburb_df[year_cols].apply(pd.to_numeric, errors="coerce")

suburb_long = suburb_df.melt(
    id_vars="SA2 name",
    value_vars=year_cols,
    var_name="Year",
    value_name="Population"
)

suburb_long["Year"] = suburb_long["Year"].astype(int)
suburb_long = suburb_long[
    (suburb_long["Year"] >= 2018) & (suburb_long["Year"] <= 2025)
].copy()

suburb_long["Area_km2"] = area_km2
suburb_long["Density"] = suburb_long["Population"] / area_km2

output_path = output_dir / "coburg-east_density.csv"
suburb_long.to_csv(output_path, index=False)

print("Coburg - East population density (2018-2025)")
print(f"Land area: {area_km2} km²")
print(f"Saved table to: {output_path}")
print(suburb_long)
 SA2 name  Year  Population  Area_km2      Density
17  Coburg - East  2018     13379.0       7.0  1911.285714
18  Coburg - East  2019     13397.0       7.0  1913.857143
19  Coburg - East  2020     13265.0       7.0  1895.000000
20  Coburg - East  2021     12675.0       7.0  1810.714286
21  Coburg - East  2022     12901.0       7.0  1843.000000
22  Coburg - East  2023     13482.0       7.0  1926.000000
23  Coburg - East  2024     13887.0       7.0  1983.857143
24  Coburg - East  2025     14457.0       7.0  2065.285714



#merge 
import pandas as pd
from pathlib import Path

project_root = Path.cwd()
if not (project_root / "data" / "raw").exists():
    project_root = project_root.parent

input_path = project_root / "data" / "raw" / "abs_population.xlsx"
output_dir = project_root / "data" / "clean"
output_dir.mkdir(parents=True, exist_ok=True)

header_rows = pd.read_excel(input_path, sheet_name="Table 1", header=None, nrows=6)
column_names = header_rows.iloc[5, :10].tolist() + header_rows.iloc[4, 10:].tolist()

df = pd.read_excel(input_path, sheet_name="Table 1", header=None, skiprows=6)
df.columns = column_names

year_cols = [
    col for col in column_names
    if isinstance(col, (int, float)) and 2001 <= int(col) <= 2025
]

area_km2 = {
    "Sunshine": 7.3,
    "Bundoora - East": 15.0,
    "Coburg - East": 7.0,
    "Brunswick East": 5.2,
}

def normalize_file_name(name: str) -> str:
    return (
        name.lower()
        .replace(" - ", "-")
        .replace(" ", "-")
        .replace("/", "-")
        .replace("--", "-")
    )

def build_density_table(suburb_name: str, area_val: float):
    suburb_df = df[df["SA2 name"] == suburb_name].copy()
    if suburb_df.empty:
        raise ValueError(f"Suburb row not found: {suburb_name}")

    suburb_df[year_cols] = suburb_df[year_cols].apply(pd.to_numeric, errors="coerce")

    suburb_long = suburb_df.melt(
        id_vars="SA2 name",
        value_vars=year_cols,
        var_name="Year",
        value_name="Population"
    )

    suburb_long["Year"] = suburb_long["Year"].astype(int)
    suburb_long = suburb_long[
        (suburb_long["Year"] >= 2018) & (suburb_long["Year"] <= 2025)
    ].copy()

    suburb_long["Area_km2"] = area_val
    suburb_long["Density"] = suburb_long["Population"] / area_val
    suburb_long["Suburb"] = suburb_name

    return suburb_long[["Suburb", "Year", "Population", "Area_km2", "Density"]]

suburbs = ["Sunshine", "Bundoora - East", "Coburg - East", "Brunswick East"]

all_tables = []
for suburb in suburbs:
    table = build_density_table(suburb, area_km2[suburb])
    all_tables.append(table)

    output_path = output_dir / f"{normalize_file_name(suburb)}_density.csv"
    table.to_csv(output_path, index=False)
    print(f"Saved {suburb} density table to {output_path}")

combined_table = pd.concat(all_tables, ignore_index=True)
combined_output_path = output_dir / "all_suburbs_density.csv"
combined_table.to_csv(combined_output_path, index=False)

print(f"\nSaved combined density table to {combined_output_path}")
print(combined_table)