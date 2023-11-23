from django.core.management.base import BaseCommand
import pandas as pd

from forex.models import Currency

class Command(BaseCommand):
    help = 'Your custom command description'

    def handle(self, *args, **options):
        url_link = 'https://tradingeconomics.com/currencies?base=usd'
        # url_link = 'https://finance.yahoo.com/currencies/'
        import requests
        r = requests.get(url_link)
        r = requests.get(url_link,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

        df = pd.read_html(f'{r.text}')[0]
        df = df[['Crosses', 'Price', 'Day']]
        df = df.to_dict()

        # print(len(df['Crosses']))
        for i in range(len(df['Crosses'])):
            # print(df['Crosses'][i][3:], end='\t\n')
            # print(df['Price'][i], end='\t')
            # print(df['Day'][i], end='\n')

            name = df['Crosses'][i][3:]
            rate = df['Price'][i]

            try:
                cash = Currency.objects.get(name = name)
                cash.name = name
                cash.rate = rate
                cash.save()
            except:
                cash = Currency()
                cash.name = name
                cash.rate = rate
                cash.save()

        self.stdout.write(self.style.SUCCESS('Command executed successfully'))
