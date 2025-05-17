from exa_py import Exa

exa = Exa('84adc682-ca8a-474d-8ea9-07bee42603ff')
query = input('Search here: ')

response = exa.search(
    query,
    num_results=10,
    type='keyword',
    include_domains=['www.tiktok.com'],
)

for result in response.results:
    print(f"Title: {result.title}")
    print(f"URL: {result.url}")
    print()
