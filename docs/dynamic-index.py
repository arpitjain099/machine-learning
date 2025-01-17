import os

# Path to your 'cvelist' directory
cvelist_dir = '/Users/arpitjain/Downloads/machine-learning/docs/cvelist'

# Generate the dynamic entries for the toctree
dynamic_entries = [f"   cvelist/{filename[:-4]}" for filename in os.listdir(cvelist_dir) if filename.endswith(".rst")]

# Assuming you're appending to or creating a section in index.rst for these entries
with open('/Users/arpitjain/Downloads/machine-learning/docs/dynamic-index.rst', 'w') as index_file:
    index_file.write("\n.. toctree::\n")
    index_file.write("   :maxdepth: 2\n")
    index_file.write("   :caption: CVE List:\n\n")
    index_file.writelines('\n'.join(dynamic_entries))