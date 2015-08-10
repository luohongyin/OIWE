#Interpretable Word Embeddings

##Overview
This tool provide a method of interpretable word embeddings, which is based on OIWE-IPG model in our paper, Online Learning of Interpretable Word Embeddings.

##Experiments

####Data
* text8 corpus from word2vec website: https://code.google.com/p/word2vec/
* Test datasets on http://wordvectors.org


####Word Similarty Task

######OIWE-IPG
| Task name     | Word pairs    | Pairs found  | Correlation |
| ------------- |:-------------:| -----:| ------:|
| WS-353        | 353 | 351 | 0.6415 |
| WS-353-SIM    | 203 | 202 | 0.7174 |
| WS-353-REL    | 252 | 251 | 0.6032 |
| MC-30         | 30 | 30 | 0.6245 |
| RG-65        | 65 | 65 | 0.5716 |
| Rare-Word        | 2034 | 951 | 0.3379 |
| MEN        | 3000 | 2987 | 0.5760 |
| MTurk-287        | 287 | 284 | 0.6054 |
| MTurk-771        | 771 | 769 | 0.4981 |
| YP-130        | 139 | 118 | 0.3066 |

######OIWE-NPG
| Task name     | Word pairs    | Pairs found  | Correlation |
| ------------- |:-------------:| -----:| ------:|
| WS-353        | 353 | 351 | 0.5833 |
| WS-353-SIM    | 203 | 202 | 0.6371 |
| WS-353-REL    | 252 | 251 | 0.5788 |
| MC-30         | 30 | 30 | 0.5245 |
| RG-65        | 65 | 65 | 0.5685 |
| Rare-Word        | 2034 | 951 | 0.2544 |
| MEN        | 3000 | 2987 | 0.5668 |
| MTurk-287        | 287 | 284 | 0.5350 |
| MTurk-771        | 771 | 769 | 0.4147 |
| YP-130        | 139 | 118 | 0.1808 |

######Skip-gram
| Task name     | Word pairs    | Pairs found  | Correlation |
| ------------- |:-------------:| -----:| ------:|
| WS-353        | 353 | 351 | 0.6380 |
| WS-353-SIM    | 203 | 202 | 0.6735 |
| WS-353-REL    | 252 | 251 | 0.6039 |
| MC-30         | 30 | 30 | 0.5041 |
| RG-65        | 65 | 65 | 0.5049 |
| Rare-Word        | 2034 | 951 | 0.3694 |
| MEN        | 3000 | 2987 | 0.5256 |
| MTurk-287        | 287 | 284 | 0.5848 |
| MTurk-771        | 771 | 769 | 0.4965 |
| YP-130        | 139 | 118 | 0.2493 |

######RNN
| Task name     | Word pairs    | Pairs found  | Correlation |
| ------------- |:-------------:| -----:| ------:|
| WS-353        | 353 | 351 | 0.3675 |
| WS-353-SIM    | 203 | 202 | 0.4928 |
| WS-353-REL    | 252 | 251 | 0.2925 |
| MC-30         | 30 | 30 | 0.5826 |
| RG-65        | 65 | 65 | 0.5019 |
| Rare-Word        | 2034 | 951 | 0.3904 |
| MEN        | 3000 | 2987 | 0.4344 |
| MTurk-287        | 287 | 284 | 0.5093 |
| MTurk-771        | 771 | 769 | 0.3990 |
| YP-130        | 139 | 118 | 0.4021 |

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

