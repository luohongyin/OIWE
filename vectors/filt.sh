#lhy
#2015.5

python filterVocab.py fullVocab.txt < text8.txt > filtVectors.txt
gzip filtVectors.txt filtVectors.txt.gz
cp filtVectors.txt.gz ../../eval-vectors/
cd ../../eval-vectors/
python wordsim.py filtVectors.txt.gz
