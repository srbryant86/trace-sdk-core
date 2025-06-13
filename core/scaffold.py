import os

def run(project_name):
    base_path = os.path.abspath(project_name)
    os.makedirs(base_path, exist_ok=True)

    subdirs = ["src", "tests", "docs"]
    for d in subdirs:
        os.makedirs(os.path.join(base_path, d), exist_ok=True)

    with open(os.path.join(base_path, "README.md"), "w") as f:
        f.write(f"# {project_name}\n\nProject scaffold generated.")

    print(f"✅ Project '{project_name}' scaffold created at {base_path}")
