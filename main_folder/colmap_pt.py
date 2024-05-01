import subprocess

def run_colmap_point_triangulator(database_path, image_path, input_path, output_path):
    command = [
        "colmap", "point_triangulator",
        "--database_path", database_path,
        "--image_path", image_path,
        "--input_path", input_path,
        "--output_path", output_path
    ]
    
    try:
        # Run the command
        subprocess.run(command, check=True)
        print("Point triangulation completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Point triangulation failed.")

def run_colmap_bundle_adjuster(input_path, output_path):
    command = [
        "colmap", "bundle_adjuster",
        "--input_path", input_path,
        "--output_path", output_path
    ]
    
    try:
        # Run the command
        subprocess.run(command, check=True)
        print("Bundle adjustment completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Bundle adjustment failed.")

if __name__ == "__main__":
    database_path = "/working/colmap_ws/dataset.db"
    image_path = "/working/colmap_ws/images"
    input_path = "/working/colmap_ws/sparse/it/"
    output_path = "/working/colmap_ws/sparse/it"
    num_iterations = 5

    for i in range(num_iterations):
        print(f"Iteration {i+1}:")
        run_colmap_point_triangulator(database_path, image_path, input_path, output_path)
        #run_colmap_bundle_adjuster(input_path, output_path)
        print("-" * 50)
