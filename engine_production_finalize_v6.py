import os
import subprocess

# ----------------------------
# PIPELINE ORDER (FINAL)
# ----------------------------

PIPELINE = [
    ("Build Articles", "engineinternational_geo_builder.py"),
    ("Inject Internal Links", "engine_internal_linker_v4.py"),
    ("Generate Sitemap", "engine_geo_sitemap_v2.py"),
    ("SEO Ping System", "engine_seo_control_center_v2.py"),
    ("Health Check", "engine_health_check_v5.py")
]

def run_script(name, script):

    print(f"\n--- {name} ---")

    result = subprocess.run(["python", script])

    if result.returncode != 0:
        print(f"FAILED: {name}")
        exit(1)

    print(f"OK: {name}")

def run_all():

    print("\nSTARTING FULL SEO PRODUCTION PIPELINE\n")

    for name, script in PIPELINE:
        run_script(name, script)

    print("\nPIPELINE COMPLETE - SYSTEM READY FOR DEPLOY")

# ----------------------------
# EXECUTE
# ----------------------------

if __name__ == "__main__":
    run_all()
