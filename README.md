# 🧬 Health Lab Visualizer

A local-first Python tool for turning raw medical lab JSON exports into clean, structured, and analyzable time-series data.

Designed for personal health data exploration, longitudinal tracking, and AI-ready exports.

---

## ✨ Features

- Parses nested lab report JSON (CBC, TSH, and other panels)
- Extracts individual biomarkers from observations
- Normalizes data into clean time-series format
- Generates per-biomarker trend plots
- Exports:
  - 📊 CSV (spreadsheet / analysis ready)
  - 🤖 AI-ready JSON (structured for LLMs)

---

## 📦 Installation (using uv)

```bash
uv sync
```

## 🚀 Usage
Run all features:

`uv run labviz input.json --export all --plot --summary`

## 📊 View summary statistics
`uv run labviz input.json --summary`

## 📈 Generate plots
`uv run labviz input.json --plot`

This produces a separate time-series plot for each biomarker (e.g., Hemoglobin, TSH, Leukocytes).

## 📁 Export cleaned data
CSV (for Excel, pandas, etc.)

`uv run labviz input.json --export csv`

AI-ready JSON (structured biomarker timelines)

`uv run labviz input.json --export ai-json`


## 🧠 Output format

CSV structure
```
obs_code	obs_name	date	value	unit	reference_range
718-7	Hemoglobin	2023-10-15	147	g/L	116–148
```

AI JSON structure
```
{
  "Hemoglobin": [
    {
      "date": "2023-10-15 01:59:00+00:00",
      "value": 147,
      "unit": "g/L"
    }
  ]
}
```

This format is optimized for:

LLM analysis

trend interpretation

clinical summarization


## 🔒 Privacy
This tool is fully local-first:

No network calls

No cloud uploads

No telemetry

All processing stays on your machine

You are responsible for your own medical data handling and storage.


## 🧪 Data model
The tool expects JSON structured like:

```
Report
 └── Observations[]
      ├── observationCode
      ├── observationCodeDisplay
      ├── resultValueQuantity
      ├── resultValueUnits
      ├── effectiveDate
```

Each observation becomes a single row in the dataset.


## ⚠️ Notes
Uses observationCode as the primary biomarker identifier (important for correctness)

Panels like CBC are split into individual lab measurements

Invalid or missing values are automatically ignored


