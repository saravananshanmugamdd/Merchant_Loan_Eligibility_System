import os

PROJECT_ROOT=os.getcwd()

raw_data_path=os.path.join(PROJECT_ROOT, "data", "raw")
interim_data_path=os.path.join(PROJECT_ROOT, "data","interim")
processed_data_path=os.path.join(PROJECT_ROOT, "data", "processed")

output_dir=os.path.join(PROJECT_ROOT, "outputs")

log_dir=os.path.join(PROJECT_ROOT, "logs")

for directory in [
    raw_data_path,
    interim_data_path,
    processed_data_path,
    output_dir,
    log_dir
]:
    os.makedirs(directory, exist_ok=True)
