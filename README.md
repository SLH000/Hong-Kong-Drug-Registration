# Drug List and Human Albumin Market Analysis

This project processes drug registration data from an XML file, extracts relevant drug information, and then filters and analyzes the market trends of Human Albumin in Hong Kong. The data is visualized using a Tableau dashboard.

## Project Overview

The project is divided into two main parts:

1. **XML Data Extraction**:
   - Extracts drug data from an XML file (`DrugList.xml`), including product name, registration certificate holder, permit number, and active ingredients.
   - Converts the extracted data into a CSV file (`drug_data.csv`).

2. **Market Trend Analysis**:
   - Loads the `drug_data.csv` file and filters it based on specific keywords related to Human Albumin.
   - Creates a filtered dataset of Human Albumin-related drugs (`Registered Albumin.csv`).
   - The filtered data is then used for market trend analysis and visualized in a Tableau dashboard.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Required Python libraries:
  - `pandas`
  - `xml.etree.ElementTree`
  - `Tableau` (for visualization)

To install the required Python libraries, use the following command:

```bash
pip install pandas
