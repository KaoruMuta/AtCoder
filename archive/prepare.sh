#!/bin/sh
CURRENT_PATH=$(cd $(dirname $0);pwd)
FOLDER_PATH="${CURRENT_PATH}/$1"
mkdir ${FOLDER_PATH}

if [ $# == 0 ]; then
    echo "Arguments are required in command line"
elif [ $# == 1 ]; then
    # default language: python
    touch "${FOLDER_PATH}/A.py"
    touch "${FOLDER_PATH}/B.py"
    touch "${FOLDER_PATH}/C.py"
    touch "${FOLDER_PATH}/D.py"
    touch "${FOLDER_PATH}/E.py"
    touch "${FOLDER_PATH}/F.py"
elif [ $# == 2 ]; then
    touch "${FOLDER_PATH}/A.$2"
    touch "${FOLDER_PATH}/B.$2"
    touch "${FOLDER_PATH}/C.$2"
    touch "${FOLDER_PATH}/D.$2"
    touch "${FOLDER_PATH}/E.$2"
    touch "${FOLDER_PATH}/F.$2"
elif [ $# == 3 ]; then
    touch "${FOLDER_PATH}/$3.$2"
else
    echo "There are extra arguments in command line"
fi
