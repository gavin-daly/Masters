import os

# Generate list of model files in steps of 10
model_files = [f"sed_model_incl_{i}.txt" for i in range(0, 181, 10)]

for f1 in model_files:
    print(f"Running comparison with {f1}...")
    os.system(f"python compare_seds.py {f1}")
