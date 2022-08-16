


if [ ! -f "$2/challenge.yml" ]; then
    echo "challenge.yml file is missing!"
    exit 1
fi

FILE="$2/challenge.yml"
pip install PyYaml
python3 "$2/.github/scripts/challenge.py" "$2"



retVal=$?
if [ $retVal -eq 1 ]; then
    echo "Error"
fi
exit $retVal
