# Healthcare Appointment Analytics Pipeline in Microsoft Fabric

A complete end-to-end showing how **FHIR-like healthcare appointment data** can be ingested, transformed, modeled, and visualized using **Microsoft Fabric**, **PySpark**, **Lakehouse architecture**, and **Power BI**.

This project was built as a portfolio-style healthcare data engineering demo to showcase how semi-structured healthcare data can be transformed into analytics-ready datasets using a **Medallion Architecture (Bronze → Silver → Gold)** approach.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Context](#business-context)
- [Project Goals](#project-goals)
- [Architecture Overview](#architecture-overview)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Healthcare Data Solutions Exploration](#healthcare-data-solutions-exploration)
- [Custom End-to-End Pipeline Implementation](#custom-end-to-end-pipeline-implementation)
  - [Step 1 - Create Fabric Environment](#step-1---create-fabric-environment)
  - [Step 2 - Prepare Dummy Healthcare Data](#step-2---prepare-dummy-healthcare-data)
  - [Step 3 - Upload Raw Data to Lakehouse](#step-3---upload-raw-data-to-lakehouse)
  - [Step 4 - Read Raw NDJSON in PySpark](#step-4---read-raw-ndjson-in-pyspark)
  - [Step 5 - Bronze Layer](#step-5---bronze-layer)
  - [Step 6 - Silver Layer](#step-6---silver-layer)
  - [Step 7 - Gold Layer](#step-7---gold-layer)
  - [Step 8 - Power BI Semantic Model](#step-8---power-bi-semantic-model)
  - [Step 9 - Power BI Dashboard](#step-9---power-bi-dashboard)
- [Dataset Details](#dataset-details)
- [Data Model](#data-model)
- [PySpark Transformation Logic](#pyspark-transformation-logic)
- [Validation Queries](#validation-queries)
- [Screenshots](#screenshots)
- [How to Reproduce](#how-to-reproduce)
- [Challenges and Learnings](#challenges-and-learnings)
- [Future Improvements](#future-improvements)
- [Conclusion](#conclusion)

---

## Project Overview

Healthcare data is often stored in nested, semi-structured formats such as **FHIR JSON / NDJSON**, which are flexible for interoperability but not ideal for direct analytics.

This project demonstrates how to:

- ingest healthcare-style raw JSON data into a Fabric Lakehouse
- preserve raw records in a **Bronze** layer
- flatten and normalize nested JSON into a structured **Silver** layer using **PySpark**
- create an aggregated **Gold** table for reporting
- build a **semantic model**
- visualize the data in **Power BI**

The goal is to simulate a realistic healthcare data engineering workflow in a simplified and reproducible way.

---

## Business Context

Healthcare systems generate large volumes of data from appointments, clinical encounters, lab results, observations, immunizations, and more.

Much of this data is:
- nested
- semi-structured
- difficult to query directly
- spread across multiple systems

To support reporting, operational monitoring, and downstream analytics, organizations often implement layered data architectures to convert raw clinical data into curated and analytics-ready data products.

This demo focuses on a simplified **Appointment** use case inspired by the **FHIR Appointment resource**.

---

## Project Goals

This project was designed to demonstrate the following:

- working with healthcare-style JSON data in Microsoft Fabric
- implementing **Medallion Architecture**
- parsing nested data using **PySpark**
- creating reusable Lakehouse tables
- exposing curated data to **Power BI**
- documenting the full workflow in a way that is easy to understand and reproduce

---

## Architecture Overview

The final architecture implemented in this repo is:

```text
Raw NDJSON Healthcare Data
        ↓
Fabric Lakehouse Files
        ↓
PySpark Notebook
        ↓
Bronze Table (raw nested JSON)
        ↓
Silver Table (normalized structured columns)
        ↓
Gold Table (aggregated analytics output)
        ↓
Power BI Semantic Model
        ↓
Power BI Dashboard
