if [ $1 == 'test' ] 
then 
    python test.py 
elif [ $1 == 'build' ]
then
    
    rm build -r
    rm dist -r
    rm listcord.py.egg-info -r

    python setup.py sdist bdist_wheel

    if [ $2 == '-u' ]
    then
        python -m twine upload dist/*
    fi

elif [ $1 == 'upload' ]
then
    python -m twine upload dist/*
elif [ $1 == 'commit' ]
then
    echo "Commit Description: "
    read commitln

    git add .
    git commit -m \"$commitln\"
    git push github
else
    echo "Command not found!"
fi