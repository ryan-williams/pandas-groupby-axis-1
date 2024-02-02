import pandas as pd

# Load input DataFrame
url = 'ytds.csv'
df = pd.read_csv(url, header=[0, 1], index_col=0)

# Compute year-to-date (YTD), rest-of-year (ROY) fractions:
to_dt = pd.to_datetime
now = to_dt('now')
cur_year_start = to_dt(f'{now.year}')
nxt_year_start = to_dt(f'{now.year + 1}')
cur_ytd_frac = (now - cur_year_start) / (nxt_year_start - cur_year_start)
cur_roy_frac = 1 - cur_ytd_frac


def project(df):
    """Compute current year-end projection.

    Assumes transposed DataFrame shape, suitable for calling like:
    ```
    df.groupby(lambda x:x, level=0).apply(project))
    ```
    Transposes all operations from `project` (e.g. `df[k]` → `df.loc[k]`)
    """
    [top_level] = df.index.get_level_values(0).drop_duplicates()
    d = df.loc[top_level]
    prv_ytd = d.loc['prv_ytd']
    cur_ytd = d.loc['cur_ytd']
    zero_mask = prv_ytd == 0
    prv_roy = d.loc['prv_end'] - prv_ytd
    d.loc['roy',  zero_mask] = (prv_roy + cur_ytd) * cur_roy_frac
    d.loc['roy', ~zero_mask] = prv_roy * (1 + cur_ytd_frac * (cur_ytd / prv_ytd - 1))
    d.loc['roy'] = round(d.loc['roy'])
    d.loc['projected'] = cur_ytd + d.loc['roy']
    return d.loc[['roy', 'projected']].astype(int)  # casting d.loc['roy'] above doesn't work, for some reason


# Compute projections
proj = df.T.groupby(lambda x: x, level=0).apply(project).T
print(proj)
proj.to_csv('proj.csv')
