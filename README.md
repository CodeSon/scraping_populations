# Scraping_populations
Scraping country populations from a url and selecting specific tags with the scrapy framework

# Exploring scrapy shell and creating first spider
Created the country's spider to access the allowed domains;
https://www.worldometers.info/
as well as the starting urls
https://www.worldometers.info/world-population/population-by-country/

## Results from first spider
- List of countries retrieved
- 2022-07-14 09:57:57 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.worldometers.info/world-population/population-by-country/>
{'title': 'Countries in the world by population (2022)', 'countries': ['Honduras', 'United Arab Emirates', 'Djibouti', 'Saint Barthelemy', 'Seychelles', 'Antigua and Barbuda', 'Vietnam', 'Hungary', 'Tajikistan', 'Belarus', 'Austria', 'Fiji', 'DR Congo', 'Réunion', 'Papua New Guinea', 'Serbia', 'Comoros', 'Israel', 'Switzerland', 'Isle of Man', 'Turkey', 'Iran', 'Germany', 'Togo', 'Holy See', 'Sierra Leone', 'Guyana', 'Andorra', 'Bhutan', 'Hong Kong', 'Laos', 'Dominica', 'Paraguay', 'Thailand', 'Bulgaria', 'Libya', 'Solomon Islands', 'Lebanon', 'United Kingdom', 'Nicaragua', 'Cayman Islands', 'France', 'Kyrgyzstan', 'Macao', 'El Salvador', 'Montenegro', 'Luxembourg', 'Bermuda', 'Saint Helena', 'Italy', 'Turkmenistan', 'Tanzania', 'Western Sahara', 'South Africa', 'Marshall Islands', 'Suriname', 'Singapore', 'Saint Pierre & Miquelon', 'Denmark', 'Northern Mariana Islands', 'Greenland', 'Cabo Verde', 'Finland', 'American Samoa', 'Congo', 'Micronesia', 'Slovakia', 'Myanmar', 'Norway', 'Maldives', 'Kenya', 'Saint Kitts & Nevis', 'South Korea', 'Oman', 'State of Palestine', 'Costa Rica', 'Colombia', 'Liberia', 'Montserrat', 'Ireland', 'Faeroe Islands', 'Central African Republic', 'New Zealand', 'Spain', 'Mauritania', 'Uganda', 'Argentina', 'Malta', 'Algeria', 'Sudan', 'Brunei ', 'Ukraine', 'Panama', 'Sint Maarten', 'Kuwait', 'Croatia', 'Moldova', 'Iraq', 'Guadeloupe', 'Georgia', 'Belize', 'Bahamas', 'Monaco', 'Afghanistan', 'Turks and Caicos', 'Saint Martin', 'Liechtenstein', 'Poland', 'Canada', 'Martinique', 'Morocco', 'Eritrea', 'Saudi Arabia', 'Falkland Islands', 'Uruguay', 'Iceland', 'San Marino', 'Gibraltar', 'Uzbekistan', 'United States', 'Peru', 'Angola', 'Bosnia and Herzegovina', 'Mongolia', 'Malaysia', 'Mozambique', 'Ghana', 'Vanuatu', 'British Virgin Islands', 'French Guiana', 'Yemen', 'Armenia', 'Jamaica', 'Nepal', 'Qatar', 'Albania', 'Barbados', 'Puerto Rico', 'New Caledonia', 'Venezuela', 'French Polynesia', 'Madagascar', 'Indonesia', 'Mayotte', 'Lithuania', 'Cameroon', "Côte d'Ivoire", 'Caribbean Netherlands', 'North Korea', 'Australia', 'Namibia', 'Niger', 'Gambia', 'Taiwan', 'Botswana', 'Gabon', 'Pakistan', 'Sao Tome & Principe', 'Lesotho', 'Sri Lanka', 'Brazil', 'Burkina Faso', 'North Macedonia', 'Slovenia', 'Nigeria', 'Mali', 'Samoa', 'Guinea-Bissau', 'Romania', 'Malawi', 'Chile', 'Latvia', 'Kazakhstan', 'Zambia', 'Saint Lucia', 'Palau', 'Guatemala', 'Ecuador', 'Cook Islands', 'Syria', 'Channel Islands', 'Netherlands', 'Bahrain', 'Guam', 'Senegal', 'Cambodia', 'Bangladesh', 'Chad', 'Curaçao', 'Niue', 'Somalia', 'Anguilla', 'Zimbabwe', 'Russia', 'China', 'Equatorial Guinea', 'Trinidad and Tobago', 'Tokelau', 'Estonia', 'Timor-Leste', 'Guinea', 'Rwanda', 'Mexico', 'Mauritius', 'Japan', 'Benin', 'Cyprus', 'Kiribati', 'Burundi', 'Tunisia', 'Tuvalu', 'Bolivia', 'Eswatini', 'Belgium', 'Ethiopia', 'Haiti', 'Cuba', 'Grenada', 'Wallis & Futuna', 'South Sudan', 'St. Vincent & Grenadines', 'Philippines', 'Dominican Republic', 'Nauru', 'Czech Republic (Czechia)', 'Aruba', 'Tonga', 'U.S. Virgin Islands', 'Greece', 'Egypt', 'Jordan', 'Portugal', 'Azerbaijan', 'Sweden', 'India']}

## Stats from the shell
- 2022-07-14 09:57:57 [scrapy.core.engine] INFO: Closing spider (finished)
2022-07-14 09:57:57 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 499,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 18021,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 1,
 'downloader/response_status_count/404': 1,
 'elapsed_time_seconds': 0.816417,
 'finish_reason': 'finished',