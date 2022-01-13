JUPYTER_FOLDER=${1?Must provide first argument as output folder}
BASE_DOCUMENT=${2?Must base document to compile onto}
OUTPUT_PATH=${3}

# Add some styling to the document and a content div
echo "
<style>
body {
  background: #555;
}
.content {
  max-width: 500px;
  margin: auto;
  background: white;
  padding: 10px;
  min-height:100wh;
  border-radius: 10px;
}
</style>
" > index.md
echo '<div class="content">' >> index.md

# Compile out the markdown document
cat $BASE_DOCUMENT >> index.md

mkdir -p $JUPYTER_FOLDER
rm $JUPYTER_FOLDER/*.ipynb

mkdir -p $OUTPUT_PATH
rm $OUTPUT_PATH/*.html

cd $JUPYTER_FOLDER
wget "https://raw.githubusercontent.com/tomasle/data-science-prosjekt/main/notebooks/LesInnCSVtilPandas.tomlev.ipynb"
#wget "https://raw.githubusercontent.com/alexdiem/data-science-python/main/L1_intro_python_data_analysis.ipynb"
#wget "https://raw.githubusercontent.com/alexdiem/data-science-python/main/L2_plotting.ipynb"
#wget "https://raw.githubusercontent.com/alexdiem/data-science-python/main/L3_geopandas.ipynb"
#wget "https://raw.githubusercontent.com/alexdiem/data-science-python/main/L4_time_series.ipynb"

cd ..

jupyter nbconvert --to html --output-dir $OUTPUT_PATH/ $JUPYTER_FOLDER/*.ipynb

echo -e "\n\n" >> index.md


for notebook in $OUTPUT_PATH/*.html

do
  echo "[$notebook](https://tomasle.github.io/data-science-prosjekt/)" | tee -a index.md
  echo -e "\n" >> index.md
done

# Finally we end the document by adding the end of our content outline
echo "</div>" >> index.md
