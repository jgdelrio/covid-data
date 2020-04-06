import re
import dateutil
import numpy as np
import pandas as pd
from datetime import date, datetime, timedelta
from covid.sources import data_sources
from covid.config import DATA_FOLDER


is_date = re.compile(r'[\d]{1,2}/[\d]{1,2}/[\d]{1,4}')


def as_time_series(data):
    if 'Province/State' in data.columns:
        data.set_index('Province/State', inplace=True)

    counter = 0
    for d in data.columns:
        if isinstance(d, str):
            if is_date.match(d):
                break
            else:
                counter += 1
    #     print(f"Counter: {counter}")

    output = data.iloc[:, counter:].copy()
    if isinstance(output.columns[0], datetime):
        return output
    else:
        output.columns = [dateutil.parser.parse(d) for d in output.columns]
        return output


def get_total(df, column: str='total'):
    return pd.DataFrame({column: df.sum(axis=1)}, index=df.index)


def get_country(global_d, name: str='Spain'):
    output = {}
    as_array = []
    for key, entry in global_d.items():
        output[key] = get_total(as_time_series(entry[entry['Country/Region'] == name]).transpose())
        as_array.append((output[key], key))

    return pd.concat(as_array, axis=1), output


def load_global_data():
    global_d = {}
    for dat_src in data_sources['global']:
        global_d[dat_src['title']] = pd.read_csv(DATA_FOLDER.joinpath(f"{dat_src['output']}.{dat_src['type']}"))

    return global_d


global_data = load_global_data()
# country=df_glo_conf['Country/Region'].unique().tolist()


if __name__ == "__main__":
    print(global_data['Deaths'].head())
