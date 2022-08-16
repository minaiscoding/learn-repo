[[ $1 =~ ^([^\/]+)\/([^\/,]+) ]]
FOLDERPATH="${BASH_REMATCH[1]}/${BASH_REMATCH[2]}"


if [ ! -f $FOLDERPATH/challenge.yml ]; then
    echo "challenge.yml file is missing!"
    exit 1
fi

FILE=$FOLDERPATH/challenge.yml

python "$2/.github/scripts/challenge.py" "$2" "$2/counter.yaml"



retVal=$?
if [ $retVal -eq 1 ]; then
    echo "Error"
fi
exit $retVal
