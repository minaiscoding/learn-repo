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
    echo updating.
    git config --global user.name GitHub Action
    git config --global user.email github-action@users.noreply.github.com
    git add counter.yaml
    git commit -m 'updated counter'
    git branch -a
    git push origin main
    else
    echo 'The Challenge already exist'
fi




retVal=$?
if [ $retVal -eq 1 ]; then
    echo "Error"
fi
exit $retVal
