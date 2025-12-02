# Strava Bulk Export to MySQL

## Overview

This project provides a pipeline to **import bulk Strava activity exports** into a **MySQL relational database** for easy querying, analysis, and integration with other tools. It is designed for athletes, data enthusiasts, and developers who want to store and analyze their Strava data locally.

***

## Features

*   **Bulk Import**: Handles Strava ZIP exports containing multiple activity files.
*   **Data Parsing**: Supports `.fit` and `.gpx` formats.
*   **Relational Schema**: Normalized MySQL schema for activities, segments, and metrics.

***

## Requirements

*   **Python**: 3.10+
*   **MySQL**: 8.0+

Install dependencies:

```bash
pip install -r requirements.txt
```

***

## Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/<YOURUSERNAME>/CS3200_Strava_Secretary.git
    cd CS3200_Strava_Secretary
    ```

2.  **Configure MySQL connection**:
    Create a `.env` file:
    ```env
    MYSQL_HOST=hostname/ip
    MYSQL_USER=username
    MYSQL_PASSWORD=yourpassword
    MYSQL_DATABASE=dbname
    ```

***

## Usage

1.  **Place your Strava export ZIPs** in the `data/` folder.
2.  **Run through the cells in the Jupyter Notebooks, starting with Step1**:
3.  **Verify data in MySQL**:


***

## Roadmap

*   ✅ Initial bulk import
*   ✅ Support for `.fit`, `.gpx`
*   ⬜ Add support for incremental updates and `.tcx`
*   ⬜ Visualization dashboard

***

## Contributing

Pull requests are welcome! Please open an issue first to discuss major changes.

***

## License

MIT License.
