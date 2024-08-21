### Scripts to download

Note: Downloading with these scripts requires `aws cli`. 

```bash

# Metadata
DATAPATH="/dat/raw/abc_atlas/"
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/metadata/MERFISH-C57BL6J-638850/20230830 $DATAPATH/abc_atlas/metadata/MERFISH-C57BL6J-638850/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/metadata/MERFISH-C57BL6J-638850-CCF/20230830 $DATAPATH/abc_atlas/metadata/MERFISH-C57BL6J-638850-CCF/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/metadata/Allen-CCF-2020/20230630 $DATAPATH/abc_atlas/metadata/Allen-CCF-2020/20230630
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/metadata/WMB-10X/20230830 $DATAPATH/abc_atlas/metadata/WMB-10X/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/metadata/WMB-10X/20230830 $DATAPATH/abc_atlas/metadata/WMB-10X/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/metadata/WMB-taxonomy/20230830 $DATAPATH/abc_atlas/metadata/WMB-taxonomy/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/metadata/WMB-neighborhoods/20230830 $DATAPATH/abc_atlas/metadata/WMB-neighborhoods/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/metadata/Zhuang-ABCA-1/20230830 $DATAPATH/abc_atlas/metadata/Zhuang-ABCA-1/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/metadata/Zhuang-ABCA-1-CCF/20230830 $DATAPATH/abc_atlas/metadata/Zhuang-ABCA-1-CCF/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/metadata/Zhuang-ABCA-2/20230830 $DATAPATH/abc_atlas/metadata/Zhuang-ABCA-2/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/metadata/Zhuang-ABCA-2-CCF/20230830 $DATAPATH/abc_atlas/metadata/Zhuang-ABCA-2-CCF/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/metadata/Zhuang-ABCA-3/20230830 $DATAPATH/abc_atlas/metadata/Zhuang-ABCA-3/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/metadata/Zhuang-ABCA-3-CCF/20230830 $DATAPATH/abc_atlas/metadata/Zhuang-ABCA-3-CCF/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/metadata/Zhuang-ABCA-4/20230830 $DATAPATH/abc_atlas/metadata/Zhuang-ABCA-4/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/metadata/Zhuang-ABCA-4-CCF/20230830 $DATAPATH/abc_atlas/metadata/Zhuang-ABCA-4-CCF/20230830

# Image volumes
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/image_volumes/Allen-CCF-2020/20230630 ../data/abc_atlas/image_volumes/Allen-CCF-2020/20230630
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/image_volumes/MERFISH-C57BL6J-638850-CCF/20230630 ../data/abc_atlas/image_volumes/MERFISH-C57BL6J-638850-CCF/20230630

# Expression matrices
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/expression_matrices/MERFISH-C57BL6J-638850/20230830 ../data/abc_atlas/expression_matrices/MERFISH-C57BL6J-638850/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/expression_matrices/MERFISH-C57BL6J-638850-sections/20230630 ../data/abc_atlas/expression_matrices/MERFISH-C57BL6J-638850-sections/20230630
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/expression_matrices/WMB-10Xv2/20230630 ../data/abc_atlas/expression_matrices/WMB-10Xv2/20230630
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/expression_matrices/WMB-10Xv3/20230630 ../data/abc_atlas/expression_matrices/WMB-10Xv3/20230630
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/expression_matrices/WMB-10XMulti/20230830 ../data/abc_atlas/expression_matrices/WMB-10XMulti/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/expression_matrices/Zhuang-ABCA-1/20230830 ../data/abc_atlas/expression_matrices/Zhuang-ABCA-1/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/expression_matrices/Zhuang-ABCA-2/20230830 ../data/abc_atlas/expression_matrices/Zhuang-ABCA-2/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/expression_matrices/Zhuang-ABCA-3/20230830 ../data/abc_atlas/expression_matrices/Zhuang-ABCA-3/20230830
aws s3 sync --no-sign-request s3://allen-brain-cell-atlas/expression_matrices/Zhuang-ABCA-4/20230830 ../data/abc_atlas/expression_matrices/Zhuang-ABCA-4/20230830
```

```
35 directories, 200 files
422G	./expression_matrices
662M	./image_volumes
5.7G	./metadata
429G	.
```

### Downloaded directory structure

```bash
.
├── expression_matrices
│   ├── MERFISH-C57BL6J-638850
│   │   └── 20230830
│   │       ├── C57BL6J-638850-log2.h5ad
│   │       └── C57BL6J-638850-raw.h5ad
│   ├── MERFISH-C57BL6J-638850-sections
│   │   └── 20230630
│   │       ├── C57BL6J-638850.01-log2.h5ad
│   │       ├── C57BL6J-638850.01-raw.h5ad
│   │       ├── C57BL6J-638850.02-log2.h5ad
│   │       ├── C57BL6J-638850.02-raw.h5ad
│   │       ├── C57BL6J-638850.03-log2.h5ad
│   │       ├── C57BL6J-638850.03-raw.h5ad
│   │       ├── C57BL6J-638850.04-log2.h5ad
│   │       ├── C57BL6J-638850.04-raw.h5ad
│   │       ├── C57BL6J-638850.05-log2.h5ad
│   │       ├── C57BL6J-638850.05-raw.h5ad
│   │       ├── C57BL6J-638850.06-log2.h5ad
│   │       ├── C57BL6J-638850.06-raw.h5ad
│   │       ├── C57BL6J-638850.08-log2.h5ad
│   │       ├── C57BL6J-638850.08-raw.h5ad
│   │       ├── C57BL6J-638850.09-log2.h5ad
│   │       ├── C57BL6J-638850.09-raw.h5ad
│   │       ├── C57BL6J-638850.10-log2.h5ad
│   │       ├── C57BL6J-638850.10-raw.h5ad
│   │       ├── C57BL6J-638850.11-log2.h5ad
│   │       ├── C57BL6J-638850.11-raw.h5ad
│   │       ├── C57BL6J-638850.12-log2.h5ad
│   │       ├── C57BL6J-638850.12-raw.h5ad
│   │       ├── C57BL6J-638850.13-log2.h5ad
│   │       ├── C57BL6J-638850.13-raw.h5ad
│   │       ├── C57BL6J-638850.14-log2.h5ad
│   │       ├── C57BL6J-638850.14-raw.h5ad
│   │       ├── C57BL6J-638850.15-log2.h5ad
│   │       ├── C57BL6J-638850.15-raw.h5ad
│   │       ├── C57BL6J-638850.16-log2.h5ad
│   │       ├── C57BL6J-638850.16-raw.h5ad
│   │       ├── C57BL6J-638850.17-log2.h5ad
│   │       ├── C57BL6J-638850.17-raw.h5ad
│   │       ├── C57BL6J-638850.18-log2.h5ad
│   │       ├── C57BL6J-638850.18-raw.h5ad
│   │       ├── C57BL6J-638850.19-log2.h5ad
│   │       ├── C57BL6J-638850.19-raw.h5ad
│   │       ├── C57BL6J-638850.24-log2.h5ad
│   │       ├── C57BL6J-638850.24-raw.h5ad
│   │       ├── C57BL6J-638850.25-log2.h5ad
│   │       ├── C57BL6J-638850.25-raw.h5ad
│   │       ├── C57BL6J-638850.26-log2.h5ad
│   │       ├── C57BL6J-638850.26-raw.h5ad
│   │       ├── C57BL6J-638850.27-log2.h5ad
│   │       ├── C57BL6J-638850.27-raw.h5ad
│   │       ├── C57BL6J-638850.28-log2.h5ad
│   │       ├── C57BL6J-638850.28-raw.h5ad
│   │       ├── C57BL6J-638850.29-log2.h5ad
│   │       ├── C57BL6J-638850.29-raw.h5ad
│   │       ├── C57BL6J-638850.30-log2.h5ad
│   │       ├── C57BL6J-638850.30-raw.h5ad
│   │       ├── C57BL6J-638850.31-log2.h5ad
│   │       ├── C57BL6J-638850.31-raw.h5ad
│   │       ├── C57BL6J-638850.32-log2.h5ad
│   │       ├── C57BL6J-638850.32-raw.h5ad
│   │       ├── C57BL6J-638850.33-log2.h5ad
│   │       ├── C57BL6J-638850.33-raw.h5ad
│   │       ├── C57BL6J-638850.35-log2.h5ad
│   │       ├── C57BL6J-638850.35-raw.h5ad
│   │       ├── C57BL6J-638850.36-log2.h5ad
│   │       ├── C57BL6J-638850.36-raw.h5ad
│   │       ├── C57BL6J-638850.37-log2.h5ad
│   │       ├── C57BL6J-638850.37-raw.h5ad
│   │       ├── C57BL6J-638850.38-log2.h5ad
│   │       ├── C57BL6J-638850.38-raw.h5ad
│   │       ├── C57BL6J-638850.39-log2.h5ad
│   │       ├── C57BL6J-638850.39-raw.h5ad
│   │       ├── C57BL6J-638850.40-log2.h5ad
│   │       ├── C57BL6J-638850.40-raw.h5ad
│   │       ├── C57BL6J-638850.42-log2.h5ad
│   │       ├── C57BL6J-638850.42-raw.h5ad
│   │       ├── C57BL6J-638850.43-log2.h5ad
│   │       ├── C57BL6J-638850.43-raw.h5ad
│   │       ├── C57BL6J-638850.44-log2.h5ad
│   │       ├── C57BL6J-638850.44-raw.h5ad
│   │       ├── C57BL6J-638850.45-log2.h5ad
│   │       ├── C57BL6J-638850.45-raw.h5ad
│   │       ├── C57BL6J-638850.46-log2.h5ad
│   │       ├── C57BL6J-638850.46-raw.h5ad
│   │       ├── C57BL6J-638850.47-log2.h5ad
│   │       ├── C57BL6J-638850.47-raw.h5ad
│   │       ├── C57BL6J-638850.48-log2.h5ad
│   │       ├── C57BL6J-638850.48-raw.h5ad
│   │       ├── C57BL6J-638850.49-log2.h5ad
│   │       ├── C57BL6J-638850.49-raw.h5ad
│   │       ├── C57BL6J-638850.50-log2.h5ad
│   │       ├── C57BL6J-638850.50-raw.h5ad
│   │       ├── C57BL6J-638850.51-log2.h5ad
│   │       ├── C57BL6J-638850.51-raw.h5ad
│   │       ├── C57BL6J-638850.52-log2.h5ad
│   │       ├── C57BL6J-638850.52-raw.h5ad
│   │       ├── C57BL6J-638850.54-log2.h5ad
│   │       ├── C57BL6J-638850.54-raw.h5ad
│   │       ├── C57BL6J-638850.55-log2.h5ad
│   │       ├── C57BL6J-638850.55-raw.h5ad
│   │       ├── C57BL6J-638850.56-log2.h5ad
│   │       ├── C57BL6J-638850.56-raw.h5ad
│   │       ├── C57BL6J-638850.57-log2.h5ad
│   │       ├── C57BL6J-638850.57-raw.h5ad
│   │       ├── C57BL6J-638850.58-log2.h5ad
│   │       ├── C57BL6J-638850.58-raw.h5ad
│   │       ├── C57BL6J-638850.59-log2.h5ad
│   │       ├── C57BL6J-638850.59-raw.h5ad
│   │       ├── C57BL6J-638850.60-log2.h5ad
│   │       ├── C57BL6J-638850.60-raw.h5ad
│   │       ├── C57BL6J-638850.61-log2.h5ad
│   │       ├── C57BL6J-638850.61-raw.h5ad
│   │       ├── C57BL6J-638850.62-log2.h5ad
│   │       ├── C57BL6J-638850.62-raw.h5ad
│   │       ├── C57BL6J-638850.64-log2.h5ad
│   │       ├── C57BL6J-638850.64-raw.h5ad
│   │       ├── C57BL6J-638850.66-log2.h5ad
│   │       ├── C57BL6J-638850.66-raw.h5ad
│   │       ├── C57BL6J-638850.67-log2.h5ad
│   │       ├── C57BL6J-638850.67-raw.h5ad
│   │       ├── C57BL6J-638850.68-log2.h5ad
│   │       ├── C57BL6J-638850.68-raw.h5ad
│   │       ├── C57BL6J-638850.69-log2.h5ad
│   │       └── C57BL6J-638850.69-raw.h5ad
│   ├── WMB-10XMulti
│   │   └── 20230830
│   │       ├── WMB-10XMulti-log2.h5ad
│   │       └── WMB-10XMulti-raw.h5ad
│   ├── WMB-10Xv2
│   │   └── 20230630
│   │       ├── WMB-10Xv2-CTXsp-log2.h5ad
│   │       ├── WMB-10Xv2-CTXsp-raw.h5ad
│   │       ├── WMB-10Xv2-HPF-log2.h5ad
│   │       ├── WMB-10Xv2-HPF-raw.h5ad
│   │       ├── WMB-10Xv2-HY-log2.h5ad
│   │       ├── WMB-10Xv2-HY-raw.h5ad
│   │       ├── WMB-10Xv2-Isocortex-1-log2.h5ad
│   │       ├── WMB-10Xv2-Isocortex-1-raw.h5ad
│   │       ├── WMB-10Xv2-Isocortex-2-log2.h5ad
│   │       ├── WMB-10Xv2-Isocortex-2-raw.h5ad
│   │       ├── WMB-10Xv2-Isocortex-3-log2.h5ad
│   │       ├── WMB-10Xv2-Isocortex-3-raw.h5ad
│   │       ├── WMB-10Xv2-Isocortex-4-log2.h5ad
│   │       ├── WMB-10Xv2-Isocortex-4-raw.h5ad
│   │       ├── WMB-10Xv2-MB-log2.h5ad
│   │       ├── WMB-10Xv2-MB-raw.h5ad
│   │       ├── WMB-10Xv2-OLF-log2.h5ad
│   │       ├── WMB-10Xv2-OLF-raw.h5ad
│   │       ├── WMB-10Xv2-TH-log2.h5ad
│   │       └── WMB-10Xv2-TH-raw.h5ad
│   ├── WMB-10Xv3
│   │   └── 20230630
│   │       ├── WMB-10Xv3-CB-log2.h5ad
│   │       ├── WMB-10Xv3-CB-raw.h5ad
│   │       ├── WMB-10Xv3-CTXsp-log2.h5ad
│   │       ├── WMB-10Xv3-CTXsp-raw.h5ad
│   │       ├── WMB-10Xv3-HPF-log2.h5ad
│   │       ├── WMB-10Xv3-HPF-raw.h5ad
│   │       ├── WMB-10Xv3-HY-log2.h5ad
│   │       ├── WMB-10Xv3-HY-raw.h5ad
│   │       ├── WMB-10Xv3-Isocortex-1-log2.h5ad
│   │       ├── WMB-10Xv3-Isocortex-1-raw.h5ad
│   │       ├── WMB-10Xv3-Isocortex-2-log2.h5ad
│   │       ├── WMB-10Xv3-Isocortex-2-raw.h5ad
│   │       ├── WMB-10Xv3-MB-log2.h5ad
│   │       ├── WMB-10Xv3-MB-raw.h5ad
│   │       ├── WMB-10Xv3-MY-log2.h5ad
│   │       ├── WMB-10Xv3-MY-raw.h5ad
│   │       ├── WMB-10Xv3-OLF-log2.h5ad
│   │       ├── WMB-10Xv3-OLF-raw.h5ad
│   │       ├── WMB-10Xv3-PAL-log2.h5ad
│   │       ├── WMB-10Xv3-PAL-raw.h5ad
│   │       ├── WMB-10Xv3-P-log2.h5ad
│   │       ├── WMB-10Xv3-P-raw.h5ad
│   │       ├── WMB-10Xv3-STR-log2.h5ad
│   │       ├── WMB-10Xv3-STR-raw.h5ad
│   │       ├── WMB-10Xv3-TH-log2.h5ad
│   │       └── WMB-10Xv3-TH-raw.h5ad
│   ├── Zhuang-ABCA-1
│   │   └── 20230830
│   │       ├── Zhuang-ABCA-1-log2.h5ad
│   │       └── Zhuang-ABCA-1-raw.h5ad
│   ├── Zhuang-ABCA-2
│   │   └── 20230830
│   │       ├── Zhuang-ABCA-2-log2.h5ad
│   │       └── Zhuang-ABCA-2-raw.h5ad
│   ├── Zhuang-ABCA-3
│   │   └── 20230830
│   │       ├── Zhuang-ABCA-3-log2.h5ad
│   │       └── Zhuang-ABCA-3-raw.h5ad
│   └── Zhuang-ABCA-4
│       └── 20230830
│           ├── Zhuang-ABCA-4-log2.h5ad
│           └── Zhuang-ABCA-4-raw.h5ad
├── image_volumes
│   ├── Allen-CCF-2020
│   │   └── 20230630
│   │       ├── annotation_10.nii.gz
│   │       ├── annotation_boundary_10.nii.gz
│   │       └── average_template_10.nii.gz
│   └── MERFISH-C57BL6J-638850-CCF
│       └── 20230630
│           ├── resampled_annotation_boundary.nii.gz
│           ├── resampled_annotation.nii.gz
│           └── resampled_average_template.nii.gz
└── metadata
    ├── MERFISH-C57BL6J-638850
    │   └── 20230830
    │       ├── cell_metadata.csv
    │       ├── gene.csv
    │       └── views
    │           ├── cell_metadata_with_cluster_annotation.csv
    │           └── example_genes_all_cells_expression.csv
    ├── WMB-10X
    │   └── 20230830
    │       ├── cell_metadata.csv
    │       ├── gene.csv
    │       ├── region_of_interest_metadata.csv
    │       └── views
    │           ├── cell_metadata_with_cluster_annotation.csv
    │           └── example_genes_all_cells_expression.csv
    └── WMB-taxonomy
        └── 20230830
            ├── cl.df_CCN202307220.xlsx
            ├── cluster_annotation_term.csv
            ├── cluster_annotation_term_set.csv
            ├── cluster.csv
            ├── cluster_to_cluster_annotation_membership.csv
            └── views
                ├── cluster_annotation_term_with_counts.csv
                ├── cluster_to_cluster_annotation_membership_color.csv
                └── cluster_to_cluster_annotation_membership_pivoted.csv

```
