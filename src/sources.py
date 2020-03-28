

data_sources = {
    'sp': [
        {'url': 'https://covid19.isciii.es/resources/serie_historica_acumulados.csv',
         'type': 'csv',
         'desc': 'Cases by date and Region (Infected, Hospitalized, Intensive Care Unit & Deaths)',
         'source': 'Instituto de Salud Carlos III',
         'country': 'Spain',
         'output': 'sp-src-region'},
    ],
    'us': [
        {'url': 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv',
         'type': 'csv',
         'desc': 'Cases at County-level',
         'source': 'New York Times',
         'country': 'United States',
         'output': 'us-src-country'},
        {'url': 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv',
         'type': 'csv',
         'desc': 'Cases at State-level',
         'source': 'New York Times',
         'country': 'United States',
         'output': 'us-src-state'},
    ]
}


countries = data_sources.keys()
