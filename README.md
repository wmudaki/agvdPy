## Getting Started

### 1. Signup
```python
import Agvd from agvd
handle = Agvd().signup(
    id='user-id',
    name='Full Name',
    email='john.doe@email.com',
    password='John2022@Doe',
    organization='H3ABioNet'
)
```

### 2. Login
```python
import Agvd from agvd

handle = Agvd().login(
    user_id='user_id', 
    password='user_password'
)

```

### 3 Variant Query
You need to be authenticated for you to query the AGVD. On login, a token shall
be supplied with which you'll submit as an argument to the
query function. 
```python
import Agvd from agvd

handle = Agvd().query(
    token='insert-token-here',
    id='10:188836:A:G'
)
```
Alternatively you can to avoid the initial login step, you can submit your
both your userid and password as parameters as arguments to the 
query function
```python
import Agvd from agvd

handle = Agvd().query(
    user='insert-user-id-here',
    password='insert-your-password-here',
    id='10:188836:A:G'
)
```
#### Allowed Query Parameters

| Allowed Keyword Arguments | Description                                                                                                                                                                                 | Example |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| token | A token supplied after user login; If user doesn't want to log in first before making the query, the user can append their user-id and password as keyword parameters in the query function | |
| user | unique user-id                                                                                                                                                                              | |
| password | user password                                                                                                                                                                               | |
| id | List of IDs, these can be rs IDs (dbSNP) or variants in the format chrom:start:ref:alt                                                                                                      | rs116600158, COSM6350960, 19:7177679:C:T |
| region | List of regions, these can be just a single chromosome name or regions in the format <chromosome>:<start>-<end>                                                                             | chr22, 3:100000-200000 |
| type | List of types, accepted values are SNV, MNV, INDEL, SV, CNV, INSERTION, DELETION                                                                                                            | SNV, INDEL |
| gene | List of genes, most gene IDs are accepted (HGNC, Ensembl gene, ...).                                                                                                                        | BRCA2, BMPR, ENSG00000174173, ENST00000495642 |
| sample | Filter variants where the samples contain the variant (HET or HOM_ALT). Accepts AND ( ; ) and OR ( , ) operators.                                                                           | HG0097,HG00978 |
| cohort | Select variants with calculated stats for the selected cohorts                                                                                                                              | |
| cohortStatsRef | Reference Allele Frequency                                                                                                                                                                  | ALL>0.6 |
| cohortStatsAlt | Alternate Allele Frequency                                                                                                                                                                  | ALL<=4 |
| cohortStatsMaf | Minor Allele Frequency                                                                                                                                                                      | ALL<0.01 |
| cohortStatsMgf | Minor Genotype Frequency                                                                                                                                                                    | COH1<0.1,COH2<0.3 |
| clinicalSignificance | Clinical significance: benign, likely_benign, likely_pathogenic, pathogenic                                                                                                                 | |
