# Microsoft Fabric Healthcare Data Solutions Overview

## Introduction

Microsoft Fabric Healthcare Data Solutions provides a pre-built framework for ingesting, transforming, and analyzing healthcare data using standardized healthcare models such as **FHIR** and **OMOP**.

The goal of Healthcare Data Solutions is to simplify the process of building healthcare analytics platforms by providing ready-to-use components including:

- Pre-configured Lakehouses
- Data ingestion pipelines
- Transformation notebooks
- Healthcare semantic models
- Power BI analytics

These components help healthcare organizations quickly build data platforms for analytics, reporting, and AI-driven insights.

---

## Key Components of Healthcare Data Solutions

When deploying Healthcare Data Solutions in Microsoft Fabric, several resources are automatically created.

### Lakehouses

Lakehouses store raw and processed healthcare data.

Examples include:

- Bronze Layer (raw ingestion)
- Silver Layer (cleaned and normalized data)
- Gold Layer (analytics-ready data)

---

### Notebooks

Several PySpark notebooks are deployed to process healthcare data.

Examples from this project:

- `healthcare1_msft_raw_process_movement`
- `healthcare1_msft_sdoh_ingestion`
- `healthcare1_msft_sdoh_bronze_silver_flatten`
- `healthcare1_msft_omop_silver_gold_transform`

These notebooks handle:

- Raw data ingestion
- Data transformation
- Schema standardization
- OMOP model transformations

---

### Pipelines

Fabric pipelines orchestrate the movement of healthcare data between layers.

Example: