#!/usr/bin/env python3

from pathlib import Path
import os, sys, re
from subprocess import call, check_call, check_output
from glob import glob

PLANNER_IDS = list(range(1, 35))
PLANNER_IDS.remove(5)  # not needed (team registered more repos then required)
PLANNER_IDS.remove(6)  # not needed (team registered more repos then required)
PLANNER_IDS.remove(9)  # not needed (team registered more repos then required)
PLANNER_IDS.remove(11) # no content by submission deadline
PLANNER_IDS.remove(12) # no content by submission deadline
PLANNER_IDS.remove(24) # not needed (team registered more repos then required)
PLANNER_IDS.remove(26) # not needed (team registered more repos then required)
PLANNER_IDS.remove(27) # not needed (team registered more repos then required)
PLANNER_IDS.remove(31) # unregistered
PLANNER_IDS.remove(33) # unregistered

SCRIPT_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
SUBMISSIONS_DIR = SCRIPT_DIR / ".." / "submissions"
IMAGES_DIR = SCRIPT_DIR / ".." / "images"
BUILD_IMAGE_SCRIPT = SCRIPT_DIR / "apptainer_builder" / "safe_build.sh"

def clone_and_update_repo(planner_id, warnings):
    src = f"git@github.com:ipc2023-classical/planner{planner_id}.git"
    target = SUBMISSIONS_DIR/f"planner{planner_id}"
    if not target.exists():
        check_call(["git", "clone", src, str(target)])

    assert target.exists()
    check_call(["git", "-C", target, "fetch"])
    has_ipc_branch = call(["git", "-C", target, "checkout", "ipc2023-classical"]) == 0
    if has_ipc_branch:
        check_call(["git", "-C", target, "pull"])
        return target
    else:
        warnings.append(f"Branch 'ipc2023-classical' not found in planner{planner_id}")
        return None

def get_revision(repo):
    try:
        return check_output(["git", "-C", repo, "rev-parse", "HEAD"]).decode()
    except:
        return None

def read_file(filename, default):
    try:
        with open(filename) as f:
            return f.read()
    except:
        return default

def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

def build_image(recipe_file, rev, warnings):
    assert os.path.basename(recipe_file).startswith("Apptainer.")
    shortname = os.path.basename(recipe_file)[len("Apptainer."):]
    rev_file = IMAGES_DIR / f"{shortname}.last_successful_build"

    last_successful_rev = read_file(rev_file, "<None>")
    if rev == last_successful_rev:
        warnings.append(f"Skipping {recipe_file}. Image already up to date.")
        return

    if call([BUILD_IMAGE_SCRIPT, recipe_file]) != 0:
        warnings.append(f"Could not build {recipe_file}.")
    elif not os.path.exists(IMAGES_DIR / (shortname + ".img")):
        warnings.append(f"Image does not exist after building {recipe_file}.")
    else:
        write_file(rev_file, rev)

def build_all_images(repo, warnings):
    rev = get_revision(repo)
    for recipe in glob(str(repo / "Apptainer.*")):
        build_image(recipe, rev, warnings)

def update_and_build(planner_id, warnings):
    repo = clone_and_update_repo(planner_id, warnings)
    if repo:
        build_all_images(repo, warnings)

def update_and_build_all(planner_ids, recipe_files, warnings):
    for planner_id in planner_ids:
        print(f"Building planner {planner_id}")
        import time
        time.sleep(10)
        update_and_build(planner_id, warnings)

    for recipe_file in recipe_files:
        planner_name = os.path.basename(os.path.dirname(recipe_file))
        planner_id = int(planner_name[len("planner"):])
        repo = clone_and_update_repo(planner_id, warnings)
        if repo:
            rev = get_revision(repo)
            build_image(recipe_file, rev, warnings)


if __name__ == "__main__":
    planner_ids = []
    recipe_files = []

    for arg in sys.argv[1:]:
        if re.match(r"^(\d+)", arg):
            planner_ids.append(int(arg))
        elif re.match(r"^planner(\d+)", arg):
            planner_ids.append(int(arg[len("planner"):]))
        else:
            recipe_file = Path(arg)
            if not re.match(r".*/planner\d+/Apptainer\..*", str(recipe_file)):
                print(f"Did not recognize '{arg}' as a path to build.")
                sys.exit(1)
            recipe_files.append(recipe_file)

    if not planner_ids and not recipe_files:
        planner_ids = PLANNER_IDS

    warnings = []
    update_and_build_all(planner_ids, recipe_files, warnings)
    if warnings:
        print("\nWarnings:\n" + "\n".join(warnings))

