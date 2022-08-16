[[ $1 =~ ^([^\/]+)\/([^\/,]+) ]]
FOLDERPATH="${BASH_REMATCH[1]}/${BASH_REMATCH[2]}"



FILE=$FOLDERPATH/challenge.yml

python "$2/.github/scripts/update.py" "$2" "$FOLDERPATH"





git config --global user.name "minaiscoding"
git config --global user.email "khadir04kh@gmail.com"
git config --global user.name "John Doe"
git add counter.yaml
git commit -m 'updated counter'
git push origin main

retVal=$?
if [ $retVal -eq 1 ]; then
    echo "Error"
fi
exit $retVal
