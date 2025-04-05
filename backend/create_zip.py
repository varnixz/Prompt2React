import zipfile
import shutil 
import os
import logging

def create_zip_from_code(project_files: dict, zip_filename="react_project.zip") -> str:
    """Create a ZIP file with the generated React project, following the folder structure provided by the API."""
    project_dir = "./react_project"
    zip_path = os.path.join("./", zip_filename)

    # Delete existing project directory and ZIP file if they exist
    if os.path.exists(project_dir):
        shutil.rmtree(project_dir)  # Delete the entire directory
        logging.info(f"Deleted existing project directory: {project_dir}")
    if os.path.exists(zip_path):
        os.remove(zip_path)  # Delete the existing ZIP file
        logging.info(f"Deleted existing ZIP file: {zip_path}")

    # Create the project directory
    os.makedirs(project_dir, exist_ok=True)

    # Write all files to the project directory
    for file_path, content in project_files.items():
        # Skip empty file paths
        if not file_path:
            continue
            
        full_path = os.path.join(project_dir, file_path)

        # Skip if the path is a directory (ends with "/" or is exactly a directory name)
        if file_path.endswith("/") or os.path.isdir(full_path):
            os.makedirs(full_path, exist_ok=True)
            continue

        # Create parent directories if they don't exist
        parent_dir = os.path.dirname(full_path)
        if parent_dir:  # Only create if there is a parent directory
            os.makedirs(parent_dir, exist_ok=True)

        # Write the file content
        with open(full_path, "w") as f:
            f.write(content)

    # Create a ZIP file from the project directory
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(project_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, project_dir))

    return zip_filename
