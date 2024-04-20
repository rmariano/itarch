#!/bin/bash
for file in content/blog/*.rst; do
    echo "migrating ${file}"
    python migrate-file.py ${file}
    echo "done for ${file} (written to ${file/.rst/.md})" 
done;
