DlAL_CODES = [(86, 'China'), (91, 'India'), (1, 'United Status'), (62, 'Indonesia'), (55, 'Brazil'), (81, 'Jpan')]
country_code = {country: code for code, country in DlAL_CODES}
print(country_code)
country_code2 = {code: country.upper() for country, code in country_code.items() if code < 60}
print(country_code2)