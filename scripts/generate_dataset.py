import pandas as pd
import numpy as np
import random
import os

# Define breed ranges

breeds = {
    "Chihuahua": {"weight": (2, 4), "chest": (25, 35), "neck": (15, 25)},
    "Beagle": {"weight": (9, 14), "chest": (40, 55), "neck": (30, 40)},
    "German Shepherd": {"weight": (22, 40), "chest": (65, 85), "neck": (40, 55)},
    "Golden Retriever": {"weight": (25, 35), "chest": (65, 80), "neck": (38, 50)},
    "Bulldog": {"weight": (18, 25), "chest": (55, 70), "neck": (35, 45)},
    "Labrador": {"weight": (25, 36), "chest": (65, 85), "neck": (38, 50)},
    "Poodle": {"weight": (15, 25), "chest": (45, 60), "neck": (30, 40)},
    "Rottweiler": {"weight": (35, 60), "chest": (75, 100), "neck": (45, 60)},
    "Dachshund": {"weight": (7, 15), "chest": (35, 50), "neck": (25, 35)},
    "Boxer": {"weight": (25, 32), "chest": (60, 75), "neck": (35, 45)},
}

activity_levels = ["Low", "Medium", "High"]

# Harness size logic

def get_harness_size(weight, chest):
    if chest < 35:
        return "XS"
    elif chest < 50:
        return "S"
    elif chest < 65:
        return "M"
    elif chest < 80:
        return "L"
    else:
        return "XL"

# Data generator

def generate_dog_data(n=10000):
    data = []
    for _ in range(n):
        breed = random.choice(list(breeds.keys()))
        ranges = breeds[breed]

        weight = round(np.random.uniform(*ranges["weight"]), 1)
        chest = round(np.random.uniform(*ranges["chest"]), 1)
        neck = round(np.random.uniform(*ranges["neck"]), 1)
        boot_size = random.randint(1, 7)
        age = random.randint(1, 120)  # in months
        activity = random.choice(activity_levels)
        harness = get_harness_size(weight, chest)

        data.append([breed, weight, chest, neck, boot_size, age, activity, harness])

    df = pd.DataFrame(data, columns=[
        "Breed", "Weight", "Chest", "Neck", "BootSize", "Age", "Activity", "HarnessSize"
    ])
    return df

# Inject Real-World Messiness

def inject_messiness(df):
    # Introduce missing values randomly (1-3% of data)
    for col in ["Weight", "Chest", "Neck", "Age"]:
        df.loc[df.sample(frac=0.02).index, col] = np.nan

    # Introduce outliers
    df.loc[df.sample(frac=0.01).index, "Weight"] *= 5   # overweight dogs
    df.loc[df.sample(frac=0.01).index, "Chest"] *= 3    # unrealistic chest sizes

    # Duplicates
    duplicates = df.sample(frac=0.02)
    df = pd.concat([df, duplicates], ignore_index=True)

    # Wrong categories
    df.loc[df.sample(frac=0.005).index, "Activity"] = "Unknown"

    return df

# Run Script

if __name__ == "__main__":
    df = generate_dog_data(10000)
    df = inject_messiness(df)

    # Ensure folders exist
    os.makedirs("data/raw", exist_ok=True)

    # Save CSV
    df.to_csv("data/raw/dog_data_raw.csv", index=False)

    print("Messy dataset generated: data/raw/dog_data_raw.csv")
    print(df.head())
