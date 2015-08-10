#Interpretable Word Embeddings

##Overview
This tool provide a method of interpretable word embeddings, which is based on OIWE-IPG model in our paper, Online Learning of Interpretable Word Embeddings.

##Usage

####In Directory word2nve-c/:
Use command "make" to compile sourse files in directory. OIWE model is realized in word2nvec.c

####In Directory bin/:
The command to run OIWE model is in launcher.sh. Configurations in launcher.sh can be modified. Use "sh launcher.sh" to run the model.

format:
./word2vec -train <train file> -output <wordvectors file> -size <number of vector dimension> -threads <number of threads> -binary <save as binary: 0 or 1> -cbow 0

##Experiments

####Data
* text8 corpus from word2vec website: https://code.google.com/p/word2vec/
* Test datasets on wordvectors.org


####Word Similarty Task

| Task name     | Word pairs    | Pairs found  | OIWE-IPG | OIWE-NPG | Skip-gram | RNN |
| ------------- |:-------------:| -----:| ------:| ----------:| ----------:| ----------:|
| WS-353        | 353 | 351 | *0.6415* | 0.5833 | 0.6380 | 0.3675 |
| WS-353-SIM    | 203 | 202 | *0.7174* | 0.6371 | 0.6735 | 0.4928 |
| WS-353-REL    | 252 | 251 | 0.6032 | 0.5788 | *0.6039* | 0.2925 |
| MC-30         | 30 | 30 | *0.6245* | 0.5245 | 0.5041 | 0.5826 |
| RG-65        | 65 | 65 | *0.5716* | 0.5685 | 0.5049 | 0.5019 |
| Rare-Word        | 2034 | 951 | 0.3379 | 0.2544 | 0.3694 | *0.3904* |
| MEN        | 3000 | 2987 | *0.5760* | 0.5668 | 0.5256 | 0.4344 |
| MTurk-287        | 287 | 284 | *0.6054* | 0.5350 | 0.5848 | 0.5093 |
| MTurk-771        | 771 | 769 | *0.4981* | 0.4147 | 0.4965 | 0.3990 |
| YP-130        | 139 | 118 | 0.3066 | 0.1808 | 0.2493 | *0.4021* |


####Spearman Coefficient - dimension
| Dimension Number        | OIWE           | Skip-gram  |
| ------------- |:-------------:| -----:|
| 100      | 62.851 | 64.724 |
| 200      | 66.45  | 64.387 |
| 300      | 71.74  | 67.35  |
| 400      | 66.74  | 64.82  |
| 500      | 64.118 | 66.046 |

####Word Intrusion
| Model         | Precision(%)  |
| ------------- |:-------------:|
| Skip-gram     | 32.62         |
| NNSE          | 92.00         |
| OIWE-NPG      | 61.40         |
| OIWE-IPG      | 94.80         |

