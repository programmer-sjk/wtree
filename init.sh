binary_mode=0

while getopts "b" opt; do
    case "$opt" in
    b) binary_mode=1
       echo "wtree is installed executed program..."
    esac
done

pip install colorama

if [ "${binary_mode}" -eq 1 ]; then
	pip install pyinstaller
    pyinstaller.exe wtree.py
fi