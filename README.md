# Antibody reliability influences observed mRNA-protein correlations in tumours #


### Data analysis overview:
     
All the figures and statistics are generated in these notebooks
        
Notebook                           | Figures        | Description           |
:---------------------------------------------|:-------------  |:----------------------|
data_sources                                | NA        | Lists the data sources used for this project |
01_assess_TCGA_antibodies                   | Figure 1  | Assess the antibodies used for THE TCGA Pan-Cancer RPPA studies |
02a_assess_mRNA_RPPA_cor (TCGA PanCancer)   | Figure 2  | Investigate the mRNA-protein correlation for TCGA Pan-Cancer studies with respect to antibody validation status |
02b_assess_mRNA_MS_correlation              | Figure 3  | Investigate the mRNA-protein correlation for CPTAC studies with respect to antibody validation status |
02c_validate_results_using_LR               | Figure S1 | Perform Linear regression to understand the variance in mRNA-protein correlation that is explained by antibody validation status |
03_validate_results_using_CCLE              | Figure 4  | Validate the findings using the cancer cell lines data |
04_analyzed_antibody_and_protein_attributes | Figure 5  | Investigate if good and bad antibodies have differing protein or mRNA abundance and measurement reproducibility|
standardised_pipeline_utils.py              | NA        | Contains standardised pipeline applied to all the data before computing correlation |


### To run Jupyter notebooks:
* Obtain external data - sources are listed in data_sources
* Set path to external data in environment.yml (DATA_PATH)
  * Note: this can also be set in the activated environment with: `conda env config vars set external_data=directory_of_choice`
* Create [conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) environment from the environment.yml file: `conda env create -n antibody_quality_limitations -f environment.yml`
* Activate conda environment: `conda activate antibody_quality_limitations`
* Start notebooks: `jupyter notebook`
