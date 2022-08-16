[[ $1 =~ ^([^\/]+)\/([^\/,]+) ]]
FOLDERPATH="$2"


if [ ! -f $FOLDERPATH/challenge.yml ]; then
    echo "challenge.yml file is missing!"
    exit 1
fi

FILE=$FOLDERPATH/challenge.yml

python "$2/.github/scripts/challenge.py" "$2" "$FOLDERPATH"



retVal=$?
if [ $retVal -eq 1 ]; then
    echo "Error"
fi
exit $retVal
