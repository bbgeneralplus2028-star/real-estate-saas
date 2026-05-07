# ============================================
# AI UNIVERSAL REPO FIXER
# Drop into ANY GitHub repo
# File name: ai_repo_fixer.py
# ============================================

import os
import subprocess
import shutil
from pathlib import Path

print("\n===================================")
print("AI UNIVERSAL REPO FIXER STARTED")
print("===================================\n")

ROOT = os.getcwd()

# --------------------------------------------
# SAFE FILE WRITER
# --------------------------------------------

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[CREATED] {path}")

# --------------------------------------------
# CREATE MISSING FOLDERS
# --------------------------------------------

folders = [
    "backend",
    "frontend",
    "logs",
    "uploads",
    "templates",
    "static"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# --------------------------------------------
# CREATE .gitignore
# --------------------------------------------

if not os.path.exists(".gitignore"):

    gitignore = """
__pycache__/
node_modules/
.env
venv/
dist/
build/
*.pyc
"""

    write_file(".gitignore", gitignore)

# --------------------------------------------
# CREATE requirements.txt
# --------------------------------------------

if not os.path.exists("requirements.txt"):

    requirements = """
fastapi
uvicorn
openai
python-dotenv
requests
jinja2
aiofiles
flask
gunicorn
watchdog
"""

    write_file("requirements.txt", requirements)

# --------------------------------------------
# CREATE runtime.txt
# --------------------------------------------

if not os.path.exists("runtime.txt"):

    runtime = "python-3.11.9"

    write_file("runtime.txt", runtime)

# --------------------------------------------
# CREATE package.json
# --------------------------------------------

if not os.path.exists("package.json"):

    package_json = """
{
  "name": "ai-project",
  "version": "1.0.0",
  "scripts": {
    "start": "node server.js"
  }
}
"""

    write_file("package.json", package_json)

# --------------------------------------------
# CREATE server.js
# --------------------------------------------

if not os.path.exists("server.js"):

    server_js = """
const express = require("express");
const app = express();

app.get("/", (req, res) => {
    res.send("AI SERVER RUNNING");
});

app.listen(3000, () => {
    console.log("Server running");
});
"""

    write_file("server.js", server_js)

# --------------------------------------------
# CREATE main.py
# --------------------------------------------

if not os.path.exists("main.py"):

    main_py = """
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "AI FIXER ACTIVE"}
"""

    write_file("main.py", main_py)

# --------------------------------------------
# CREATE .env
# --------------------------------------------

if not os.path.exists(".env"):

    env = """
OPENAI_API_KEY=
DATABASE_URL=
STRIPE_SECRET_KEY=
"""

    write_file(".env", env)

# --------------------------------------------
# SCAN PYTHON IMPORTS
# --------------------------------------------

detected_packages = set()

print("\nScanning project imports...\n")

for root, dirs, files in os.walk(ROOT):

    for file in files:

        if file.endswith(".py"):

            filepath = os.path.join(root, file)

            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    code = f.read()

                    checks = {
                        "fastapi": "fastapi",
                        "uvicorn": "uvicorn",
                        "openai": "openai",
                        "flask": "flask",
                        "requests": "requests",
                        "dotenv": "python-dotenv",
                        "jinja2": "jinja2",
                        "aiofiles": "aiofiles",
                        "pandas": "pandas",
                        "numpy": "numpy"
                    }

                    for key, package in checks.items():

                        if key in code:
                            detected_packages.add(package)

            except:
                pass

# --------------------------------------------
# UPDATE requirements.txt
# --------------------------------------------

if detected_packages:

    print("Detected packages:")
    print(detected_packages)

    with open("requirements.txt", "a") as f:

        for package in detected_packages:
            f.write(package + "\n")

# --------------------------------------------
# INSTALL PYTHON DEPENDENCIES
# --------------------------------------------

print("\nInstalling Python packages...\n")

subprocess.run(
    ["pip", "install", "-r", "requirements.txt"],
    shell=False
)

# --------------------------------------------
# INSTALL NODE DEPENDENCIES
# --------------------------------------------

if os.path.exists("package.json"):

    print("\nInstalling Node packages...\n")

    subprocess.run(
        ["npm", "install"],
        shell=False
    )

# --------------------------------------------
# GIT AUTO COMMIT
# --------------------------------------------

try:

    print("\nSaving fixes to GitHub...\n")

    subprocess.run(["git", "add", "."])
    subprocess.run(
        ["git", "commit", "-m", "AI auto repair fix"]
    )
    subprocess.run(["git", "push"])

except:
    print("Git push skipped")

# --------------------------------------------
# RENDER START FILE
# --------------------------------------------

if not os.path.exists("render.yaml"):

    render_yaml = """
services:
  - type: web
    name: ai-app
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port 10000
"""

    write_file("render.yaml", render_yaml)

# --------------------------------------------
# AUTO START SCRIPT
# --------------------------------------------

if not os.path.exists("auto_fix_loop.py"):

    loop_script = '''
import time
import subprocess

while True:
    subprocess.run(["python", "ai_repo_fixer.py"])
    time.sleep(300)
'''

    write_file("auto_fix_loop.py", loop_script)

# --------------------------------------------
# FINISHED
# --------------------------------------------

print("\n===================================")
print("AI UNIVERSAL REPO FIX COMPLETE")
print("===================================\n")
