

data_sources = {
    'global': [
        {'url': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
         'type': 'csv',
         'desc': 'Global confirmed cases',
         'source': 'Johns Hopkins CSSE',
         'country': 'World',
         'title': 'Confirmed',
         'output': 'global-covid-confirmed', 'isClean': True},
        {'url': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv',
         'type': 'csv',
         'desc': 'Global deaths',
         'source': 'Johns Hopkins CSSE',
         'country': 'World',
         'title': 'Deaths',
         'output': 'global-covid-deaths', 'isClean': True},
        {'url': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv',
         'type': 'csv',
         'desc': 'Global recovered cases',
         'source': 'Johns Hopkins CSSE',
         'country': 'World',
         'title': 'Recovered',
         'output': 'global-covid-recovered', 'isClean': True},
    ],
    'sp': [
        {'url': 'https://covid19.isciii.es/resources/serie_historica_acumulados.csv',
         'type': 'csv',
         'desc': 'Cases by date and Region (Infected, Hospitalized, Intensive Care Unit & Deaths)',
         'source': 'Instituto de Salud Carlos III',
         'country': 'Spain',
         'output': 'sp-covid-region', 'isClean': False},
    ],
    'us': [
        {'url': 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv',
         'type': 'csv',
         'desc': 'Cases at County-level',
         'source': 'New York Times',
         'country': 'United States',
         'output': 'us-covid-counties', 'isClean': True},
        {'url': 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv',
         'type': 'csv',
         'desc': 'Cases at State-level',
         'source': 'New York Times',
         'country': 'United States',
         'output': 'us-covid-states', 'isClean': True},
    ]
}


countries = data_sources.keys()
