[[ $1 =~ ^([^\/]+)\/([^\/,]+) ]]
FOLDERPATH="${BASH_REMATCH[1]}/${BASH_REMATCH[2]}"


if [ ! -f $FOLDERPATH/challenge.yml ]; then
    echo "challenge.yml file is missing!"
    exit 1
fi

FILE=$FOLDERPATH/challenge.yml

# installing the module needed
pip install -U pip setuptools wheel
pip install ruamel.yaml
# run the python script
git status | grep 'add'
retVal=$?
if [ $retVal -eq True ]; then
    python "$2/.github/scripts/challenge.py" "$2" "$FOLDERPATH"
    else
    echo 'The Challenge already exist'
fi




retVal=$?
if [ $retVal -eq 1 ]; then
    echo "Error"
fi
exit $retVal
