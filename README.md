
![Logo](https://raw.githubusercontent.com/aurumz-rgb/NOS-TLPlot/main/assets/preview1.png)
[![PyPI](https://img.shields.io/pypi/v/nos-tlplot)](https://pypi.org/project/nos-tlplot/)
[![Python Version](https://img.shields.io/badge/python-3.12+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Streamlit Demo](https://img.shields.io/badge/Streamlit-Demo-orange)](https://nos-tlplot.streamlit.app)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17065214.svg)](https://doi.org/10.5281/zenodo.17065214)
[![JORS](https://img.shields.io/badge/Journal-JORS-blue)](https://doi.org/10.5334/jors.635)


---

**NOS-TLPlot** is an open-source Python package for **visualising Newcastle–Ottawa Scale (NOS) risk-of-bias assessments**.
It converts NOS star ratings into **publication-ready traffic-light plots** and **13 specialized visualizations**, enabling reviewers and readers to interpret study-level risk-of-bias results clearly and reproducibly.

This is the pip-installable package of [NOS-TLPlot](https://github.com/aurumz-rgb/NOS-TLPlot) — same engine, same plots, installable with a single command.

📃 **Software Metapaper (Journal of Open Research Software DOI):** [10.5334/jors.635](https://doi.org/10.5334/jors.635)

---

## ✨ Key Features

- **13 Visualization Types**: Traffic-light plots, radar charts, heatmaps, item heatmaps, stacked star profiles, donut charts, lollipop charts, star matrices, and more
- **Publication-Quality Output**: Export figures in `.png`, `.pdf`, `.svg`, `.tiff` formats
- **Multiple Themes**: Traffic-light, grayscale, ocean-blue, and sage themes for various publication requirements. [See the Themes section](#themes)
- **Interactive Web App**: Built with Streamlit for simple data upload, preview, and figure export
- **Command Line Interface**: For batch processing and automated figure generation
- **Domain-Specific Risk Assessment**: Automatically converts NOS stars (0–9) to categorical RoB (Low/Moderate/High)
- **Customizable Output**: Adjustable figure sizes, line thickness, and color themes
- **Scope-Limited**: Designed exclusively for NOS evaluations of non-randomised studies

---

## 📥 Installation

### Prerequisites
- Requires **Python 3.12+** (developed on Python 3.12.3)
- `pip` package manager

```bash
pip install nos-tlplot
```

To work on the code from a clone instead:

```bash
git clone https://github.com/nos-tlplot/NOS-TLPlot-Package.git
cd NOS-TLPlot-Package
pip install -e ".[dev]"
```

---

## ⚡ Usage

### 1️⃣ Python API

```python
import nos_tlplot

df = nos_tlplot.read_input_file("sample.csv")
df = nos_tlplot.process_detailed_nos(df)

nos_tlplot.plot_nos_visualization(df, "output_nos_plot.png")
nos_tlplot.professional_plot(df, "output.png", theme="gray")
```

Every plot function takes the processed DataFrame, an output file (`.png`, `.pdf`, `.svg` or `.tiff`), and an optional `theme` (`traffic_light` default, `gray`, `ocean` or `sage`). Pass a list of paths to save the same figure in several formats at once.

![Python Result1](https://raw.githubusercontent.com/aurumz-rgb/NOS-TLPlot/main/example/python.png)

---

### 2️⃣ Command Line Interface (For Reviewers to ensure reproducibility and Transparency)

```bash
# Basic usage
nos-tlplot sample.csv output.png

# With theme
nos-tlplot sample.csv output-traffic-light.png gray
```

`python -m nos_tlplot sample.csv output.png [theme]` works the same way.

This generates the traffic-light plot plus the 12 companion figures (`_radar`, `_theme_radar`, `_heatmap`, `_item_heatmap`, `_dot_profile`, `_table`, `_donut`, `_line_ordered`, `_lollipop`, `_pie`, `_stacked_area`, `_nos_plot`) next to the output file.

**Parameters:**

| Parameter     | Description                                         |
| ------------- | --------------------------------------------------- |
| `input_file`  | Path to CSV/Excel file containing NOS data          |
| `output_file` | Output file name and extension                      |
| `theme`       | Optional theme: `traffic_light` (default), `gray`, `ocean` or `sage` |

**Generated Outputs:**

| File                 | Description                             |
| -------------------- | --------------------------------------- |
| `_traffic-light.png` | Classic traffic-light bubble plot       |
| `_radar.png`         | Radar chart of domain scores            |
| `_heatmap.png`       | Color heatmap for domain-level bias     |
| `_item_heatmap.png`  | Item-level star heatmap with domain bands |
| `_dot_profile.png`   | Stacked domain stars per study          |
| `_table.png`         | Summary table with domain scores        |
| `_donut.png`         | Donut chart of overall bias levels      |
| `_line_ordered.png`  | Item-level star ratings matrix          |
| `_lollipop.png`      | Lollipop chart for comparative bias     |
| `_pie.png`           | Proportional risk-of-bias pie           |
| `_stacked_area.png`  | Stacked area visualization over domains |
| `_nos_plot.png`      | NOS visualization plot                  |

---

### 3️⃣ Streamlit Web App

The interactive web app lives in the [main repository](https://github.com/aurumz-rgb/NOS-TLPlot) and installs this package as a dependency. You can try it directly at the [hosted demo](https://nos-tlplot.streamlit.app).

**Features:**

* Upload CSV/Excel files
* Real-time visualization preview
* Choose from 12 plot types
* Download publication-ready figures in multiple formats
* Theme switcher (Traffic-light / Grayscale / Ocean / Sage)

---

##  Input Data Format

Your file should have these columns:

| Column Name                  | Description      | Valid Range           |
| ---------------------------- | ---------------- | --------------------- |
| `Author, Year`               | Study identifier | Text                  |
| `Representativeness`         | Domain 1         | 0–1                   |
| `Non-exposed Selection`      | Domain 2         | 0–1                   |
| `Exposure Ascertainment`     | Domain 3         | 0–1                   |
| `Outcome Absent at Start`    | Domain 4         | 0–1                   |
| `Comparability (Age/Gender)` | Domain 5         | 0–2                   |
| `Comparability (Other)`      | Domain 6         | 0–2                   |
| `Outcome Assessment`         | Domain 7         | 0–1                   |
| `Follow-up Length`           | Domain 8         | 0–1                   |
| `Follow-up Adequacy`         | Domain 9         | 0–1                   |
| `Total Score`                | Sum of stars     | 0–9                   |
| `Overall RoB`                | Risk of bias     | Low / Moderate / High |

> 💡 *Tip:* Always include your raw NOS scoring table in supplementary materials for reproducibility.

---

## 🎨 Visualization Types

1. **Traffic-Light Bubble Plot** – Classic NOS traffic-light visualization.
2. **Domain Radar Chart** – Domain scores per study as radar polygons.
3. **Theme Radar Chart** – Theme-adapted radar chart.
4. **Domain Heatmap** – Color heatmap for domain-level bias.
5. **Item-Level Star Heatmap** – Item stars grouped into domain bands.
6. **Stacked Domain Stars** – Stacked domain stars for each study.
7. **Score Table** – Summary table of stars and overall risk.
8. **Risk Donut Chart** – Risk proportions per domain.
9. **Star Ratings Matrix** – Item-level star matrix ordered by total score.
10. **Total Score Lollipop** – Total NOS scores per study.
11. **Overall Risk Pie** – Overall risk-of-bias distribution.
12. **Stacked Area Risk Chart** – Risk distribution across domains.
13. **NOS Visualization Grid** – Item-level traffic-light grid with domain bands and totals.

Note: Radar Plots are only limited to 5 studies.

---

## NOS Scoring → Risk-of-Bias Conversion

| Total Stars | Interpretation         | Risk Category    |
| ----------- | ---------------------- | ---------------- |
| 7–9         | High-quality study     | **Low RoB**      |
| 4–6         | Moderate-quality study | **Moderate RoB** |
| 0–3         | Poor-quality study     | **High RoB**     |

> Conversion follows Newcastle–Ottawa Scale standards for cohort/case-control/cross-sectional designs.

---

## 🔧 Technical Details

* **Core Engine:** `matplotlib`, `seaborn`, `numpy`, `pandas`
* **Table Rendering:** `matplotlib.table`
* **Plot Layout Management:** `GridSpec`
* **Color Systems:** Custom mcolors, traffic-light mapping
* **Data Handling:** CSV/Excel file input with automatic parsing
* **Batch Plotting:** Parallel generation for multiple figure types
* **Export Quality:** 300 DPI (default), publication-ready vector output


---

###  Repository Structure

```
NOS-TLPlot-Package/
├── nos_tlplot/
│   ├── core.py            # Main plotting engine
│   ├── __init__.py        # Public API
│   └── __main__.py        # python -m nos_tlplot entry point
├── tests/                 # pytest suite
├── sample.csv             # Sample dataset
├── sample.xlsx            # Sample dataset (Excel)
├── pyproject.toml         # Package metadata
├── requirements.txt       # Pinned development environment
├── CITATION.cff           # Citation metadata
├── LICENSE                # Apache 2.0 License
└── README.md              # Project documentation
```

---

##  ⭐ Support

*  For usage questions, open a [Discussion](https://github.com/aurumz-rgb/NOS-TLPlot/discussions)
*  For bug reports or feature requests, open an [Issue](https://github.com/aurumz-rgb/NOS-TLPlot/issues)
*  Email: [mail](mailto:pteroisvolitans12@gmail.com)


---

##  Acknowledgment

I sincerely thank the **Journal of Open Research Software (JORS)** for providing a full publication waiver supporting this software.


---

##  🧩 Citation

NOS-TLPlot Software code is cited:

> **Sahu, V. (2025). NOS-TLPlot: Visualization Tool for Newcastle–Ottawa Scale in Meta-Analysis (v3.0.0). Zenodo.**
DOI: [10.5281/zenodo.17065214](https://doi.org/10.5281/zenodo.17065214)


NOS-TLPlot Software Metapaper is cited: **[PREFERRED]**

> **Sahu, V. (2026). NOS-TLPlot: A Specialized Python Tool for Visualizing Newcastle–Ottawa Scale Risk-of-Bias Assessments. *Journal of Open Research Software*, 14(1), 7.**
DOI: [10.5334/jors.635](https://doi.org/10.5334/jors.635)

```bibtex
@software{Sahu2025,
  author = {Sahu, Vihaan},
  title = {NOS-TLPlot: Visualization Tool for Newcastle–Ottawa Scale in Meta-Analysis (v3.0.0)},
  year = {2025},
  doi = {10.5281/zenodo.17065214},
  url = {https://doi.org/10.5281/zenodo.17065214},
  version = {3.0.0}
}

@article{Sahu2026,
  author = {Sahu, Vihaan},
  title = {NOS-TLPlot: A Specialized Python Tool for Visualizing Newcastle–Ottawa Scale Risk-of-Bias Assessments},
  journal = {Journal of Open Research Software},
  volume = {14},
  number = {1},
  pages = {7},
  year = {2026},
  doi = {10.5334/jors.635},
  url = {https://doi.org/10.5334/jors.635}
}
```

---

## Themes

NOS-TLPlot ships with four colour themes - `traffic_light` (default), `gray`, `ocean` and `sage` - selectable in the web app or via the optional theme argument on the command line.

| Theme | Low | Moderate | High |
| ----- | --- | -------- | ---- |
| `traffic_light` | `#2E7D32` | `#F9A825` | `#C62828` |
| `gray` | `#D6D6D6` | `#9E9E9E` | `#3C3C3C` |
| `ocean` | `#6BAED6` | `#2171B5` | `#08306B` |
| `sage` | `#63BF93` | `#5B6D80` | `#FF884D` |

![Example NOS plot in the ocean theme](https://raw.githubusercontent.com/aurumz-rgb/NOS-TLPlot/main/example/nos_plot_ocean.png)

![Example NOS plot in the sage theme](https://raw.githubusercontent.com/aurumz-rgb/NOS-TLPlot/main/example/nos_plot_sage.png)
