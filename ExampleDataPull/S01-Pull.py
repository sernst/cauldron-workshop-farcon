import cauldron as cd
import pandas as pd
import requests
import io
import string


url_prefix = 'https://s3-us-west-2.amazonaws.com/cauldron-workshop/data'


data_frames = []

for character in string.ascii_lowercase:
    response = requests.get('{}/{}.csv'.format(url_prefix, character))
    data = response.text
    buffer = io.StringIO(data)
    data_frames.append(pd.read_csv(buffer))


df: pd.DataFrame = pd.concat(data_frames)
df = df.sort_values(by='user_id')

cd.display.table(df.head(100))

cd.shared.df = df
