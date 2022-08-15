
[[ $1 =~ ^([^\/]+)\/([^\/,]+) ]]

if [ ! -f "$2/challenge.yml" ]; then
    echo "challenge.yml file is missing!"
    exit 1
fi

FILE="$2/challenge.yml"

python "$2"



retVal=$?
if [ $retVal -eq 1 ]; then
    echo "Error"
fi
exit $retVal
