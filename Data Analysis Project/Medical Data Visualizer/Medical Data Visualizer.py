import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('/workspace/boilerplate-medical-data-visualizer/medical_examination.csv')

# 2
df['overweight'] = df.apply(lambda row: 1 if (row['weight'] / ((row['height'] / 100) ** 2)) > 25 else 0, axis=1)

# 3
df['cholesterol'] = df.apply(lambda row: 0 if row['cholesterol'] == 1 else 1, axis=1)
df['gluc'] = df.apply(lambda row: 0 if row['gluc'] == 1 else 1, axis=1)


# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars=['cardio'],
                     value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # 6
    df_cat = df_cat.rename(columns={"value": "value"})

    # 7
    chart = sns.catplot(
        data=df_cat,
        x='variable',
        hue='value',
        col='cardio',
        kind='count',
    )

    # 8
    chart.set_axis_labels('variable', 'total')
    fig = chart.fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
        ]

    # 12
    corr = df_heat.corr().round(1)

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(10, 8))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', linewidths=0.5, ax=ax)

    # 16
    fig.savefig('heatmap.png')
    return fig
