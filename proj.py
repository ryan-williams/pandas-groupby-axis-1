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

    Assumes original DataFrame shape, suitable for calling like:
    ```
    df.groupby(lambda x:x, axis=1, level=0).apply(project))
    ```
    """
    df = df.T
    [top_level] = df.columns.get_level_values(0).drop_duplicates()
    d = df.loc[:, top_level]
    prv_ytd = d.prv_ytd
    cur_ytd = d.cur_ytd
    zero_mask = prv_ytd == 0
    prv_roy = d.prv_end - prv_ytd
    d.loc[ zero_mask, 'roy'] = (prv_roy + cur_ytd) * cur_roy_frac
    d.loc[~zero_mask, 'roy'] = prv_roy * (1 + cur_ytd_frac * (cur_ytd / prv_ytd - 1))
    d['roy'] = round(d.roy).astype(int)
    d['projected'] = cur_ytd + d.roy
    return d[['roy', 'projected']].T


# Compute projections
proj = df.T.groupby(lambda x: x, level=0).apply(project).T
print(proj)
proj.to_csv('proj.csv')
