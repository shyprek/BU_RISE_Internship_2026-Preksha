import os
import random
import shutil
from pathlib import Path

def sample_images(num_samples, output_dir="sampled_images"):
    # Target the local data/imgs directory directly
    img_root = Path("MM-SafetyBench_data")
    
    if not img_root.exists():
        print(f"Error: The directory '{img_root.resolve()}' could not be found.")
        print("Please make sure you run this script from the folder containing the 'data' directory.")
        return

    allowed_types = {"SD", "SD_TYPO"}
    all_matching_images = []
    
    # Traverse through all scenario subfolders
    for scenario_dir in img_root.iterdir():
        if scenario_dir.is_dir():
            for img_type in allowed_types:
                target_subfolder = scenario_dir / img_type
                if target_subfolder.exists() and target_subfolder.is_dir():
                    # Collect jpg and png images
                    images = list(target_subfolder.glob("*.jpg")) + list(target_subfolder.glob("*.png"))
                    all_matching_images.extend(images)

    total_found = len(all_matching_images)
    print(f"Found {total_found} total images within 'SD' and 'SD_TYPO' folders.")

    if total_found == 0:
        return

    # Caps the sample size if it's larger than the available images
    if num_samples > total_found:
        print(f"Requested {num_samples} images, but only {total_found} exist. Sampling all available.")
        num_samples = total_found

    # Randomly select X images
    sampled_images = random.sample(all_matching_images, num_samples)

    # Create the output folder
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    print(f"Copying {num_samples} images to '{output_dir}'...")
    
    for img in sampled_images:
        # Prepend scenario and type to prevent filename collisions
        scenario_name = img.parent.parent.name
        img_type = img.parent.name
        new_name = f"{scenario_name}_{img_type}_{img.name}"
        
        shutil.copy(img, out_path / new_name)

    print("Done!")

if __name__ == "__main__":
    # Set your desired number of samples here
    X = 10  
    
    sample_images(num_samples=X)
