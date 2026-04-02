import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
input_path = project_root / "data" / "raw" / "abs_population.xlsx"
output_dir = project_root / "data" / "clean"
output_dir.mkdir(parents=True, exist_ok=True)

# Read header rows so the year columns are correctly identified
header_rows = pd.read_excel(input_path, sheet_name="Table 1", header=None, nrows=6)
column_names = header_rows.iloc[5, :10].tolist() + header_rows.iloc[4, 10:].tolist()

# Read the actual data starting after the header rows
df = pd.read_excel(input_path, sheet_name="Table 1", header=None, skiprows=6)
df.columns = column_names

# Identify year columns from 2001 to 2025
year_cols = [col for col in column_names if isinstance(col, (int, float)) and 2001 <= int(col) <= 2025]

# Land area values in km² for the suburbs
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


def build_density_table(suburb_name: str, area_val: float | None):
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

    if area_val is not None:
        suburb_long["Density"] = suburb_long["Population"] / area_val
    else:
        suburb_long["Density"] = None
        print(f"WARNING: area_km2 is not set for {suburb_name}, density will be None.")

    return suburb_long

suburbs = ["Sunshine", "Bundoora - East", "Coburg - East", "Brunswick East"]

all_tables = []
for suburb in suburbs:
    table = build_density_table(suburb, area_km2.get(suburb))
    all_tables.append(table)

    file_name = normalize_file_name(suburb)
    target_path = output_dir / f"{file_name}_density.csv"
    table.to_csv(target_path, index=False)
    print(f"Saved {suburb} density table to {target_path}")
    print(table)

combined_table = pd.concat(all_tables, ignore_index=True)
combined_output_path = output_dir / "all_suburbs_density.csv"
combined_table.to_csv(combined_output_path, index=False)
print("\nCombined density table for all four suburbs saved to:", combined_output_path)
print(combined_table)
 