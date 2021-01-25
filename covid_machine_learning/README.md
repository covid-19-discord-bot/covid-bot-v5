# covid-machine-learning
Machine Learning scripts for the COVID-19 bot, both sync and async.

## Usage
Start by getting the latest CSV data from OWID and saving it as `data_sources/all_data.csv`

Now, call `process_data.process_country`, or `process_country.process_world` depending on your needs.

This makes a CSV file in `data_sources/`, with the ISO code or `world` prepended.

Call `ml_models.models.predict_model` with no args for the world, or with the ISO3 code for a country.
This will return the prediction, tuned to be as accurate as possible.
