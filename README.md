# Technical Assessment
This software is a Python REST API that serves PNG and JSON XYZ map tiles from cached COG and GPKG data sources.  It is a prototype that is part of a technical assessment to demonstrate competency in HTTP API design, geoscientific programming, and data engineering.

## Requirements
- git >= 2.30.1
- libspatialindex >= 1.9.3
- Python >= 3.9.6

## Installation, Tests, and Running the Development Server
1. Clone this GitHub repository:
```
git clone git@github.com:asonnenschein/technical-assessment.git
```

2. Create a Python >= 3.9.6 virtual environment:
```
python3 -m venv venv
```

3. Activate Python >= 3.9.6 virtual environment:
```
. venv/bin/activate
```

4. Install project and dependencies into virtual environment.  These commands should be run in the root level of the project:
```
pip install .
pip install -r requirements.txt
```

5. Run feature tests to confirm that the software is installed correctly.  This command should be run in the root level of the project:
```
pytest tests/*
```

5. Run development server.  This command should be run in the root level of the project:
```
python run.py
```

## Notes
- This application is a prototype, or proof of concept.  It is not intended to run in a production environment as is.  As such, it does not currently do any application specific logging - adding DEBUG/ERROR/INFO logging would be a logical next step.
- Source COG and GPKG data assets exceed GitHub's file size limit of 100MB, and are therefore not included in this repository.
- Python software standards are enforced via `black` utility.  Type hints are included wherever possible across the software.
- PNG and JSON XYZ tiles are generated dynamically, on-the-fly, when invoked via REST API service controller.  These data are generated from source COG and GPKG files that are cached in-memory in the Python server upon startup.  This allows API views to easily access the already cached in-memory source data files without having to read the data from disk on the file system every time a service controller is requested, thereby reducing I/O bound complexity of the process.  Simplicity of this performance optimization comes at the expense of durability - it is not a persistent cache, and can put a strain on failover and undermine high availability (because I/O bound complexity is moved to server startup).  In a production environment, it would make a lot more sense to make source data available via persistent cache that is decoupled from the core Python server.  This would remove I/O bound complexity from the REST API, and improve consistency across horizontally scaled application servers by being a single source of truth for source data files.
- All service controllers in this application resolve to views that execute complex geospatial processes, which add CPU bound complexity.  Rigorous performance testing and profiling of these algorithms should be conducted to identify potential bottlenecks.  Results of performance testing and profiling will help inform whether or not it is safe to go to production with the existing synchronous execution pattern, or if it makes more sense to refactor CPU bound complexity into an asynchronous execution pattern that can operate more efficiently within each thread.
- Geospatial algorithms currently live in their respective REST API views, and are not unit tested but are accounted for (at a high level of testing) via the included feature tests.  A good next step in the development of this software would be to break those algorithms out into their own methods/objects/module which would better encapsulate them and separate concerns, and be easier to unit test.