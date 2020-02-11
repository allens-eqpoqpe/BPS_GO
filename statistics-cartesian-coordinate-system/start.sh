pwd
Completed_tips="Completed!"
echo "####################"
python3 support_class.py && echo "Building ${Completed_tips}"
rm library.py & echo "Not found" && echo "Delete ${Completed_tips}"
touch library.py && echo "Building ${Completed_tips}"
echo "####################"