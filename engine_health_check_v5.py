import os

REQUIRED_FILES = [
    "engineinternational_geo_builder.py",
    "engine_internal_linker_v4.py",
    "engine_geo_sitemap_v2.py",
    "engine_seo_control_center_v2.py",
    "engine_keyword_cluster_v3.py"
]

FOLDERS = [
    "articles"
]

def check_files():

    print("\n=== FILE CHECK ===")

    missing = []

    for file in REQUIRED_FILES:
        if not os.path.exists(file):
            print("MISSING:", file)
            missing.append(file)
        else:
            print("OK:", file)

    return missing

def check_folders():

    print("\n=== FOLDER CHECK ===")

    for folder in FOLDERS:
        if not os.path.exists(folder):
            print("MISSING FOLDER:", folder)
        else:
            files = os.listdir(folder)
            print(f"{folder}: {len(files)} files")

def check_output():

    print("\n=== OUTPUT CHECK ===")

    if os.path.exists("sitemap.xml"):
        print("OK: sitemap.xml exists")
    else:
        print("MISSING: sitemap.xml")

def run():

    print("STARTING SEO SYSTEM HEALTH CHECK")

    missing = check_files()
    check_folders()
    check_output()

    if missing:
        print("\nSYSTEM STATUS: BROKEN ❌")
    else:
        print("\nSYSTEM STATUS: READY ✅")

if __name__ == "__main__":
    run()
