# czexample
## Dataset for evaluating dictionary examples in the Czech language

About the dataset compilation and annotation guidlines read more [here](https://raslan2024.nlp-consulting.net/).

### Requirements
* [Pandas](https://pandas.pydata.org/)
* [NumPy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)
* [Regular expression operations](https://docs.python.org/3/library/re.html)

### Train classification neural network
To pre-process and annotate examples, simply run:
```bash
python main.py --exam_df EXAM_DF --word WORD --stem STEM --freq FREQ --output OUTPUT
```
Example:
```bash
python main.py --exam_df example.csv --word bandaska --stem bandas --freq 1991 --output result.csv
```

