import pandas as pd
import matplotlib.pyplot as plt


DATA_SRC = "./data/product.csv"

dtypes = dict(
    short_name="string", source="string", price="float", created_at="datetime64[ns]"
)


def run_report():
    df = pd.read_csv(DATA_SRC, names=dtypes.keys()).astype(dtypes)
    df["created_date"] = df.created_at.dt.date

    fig, ax = plt.subplots(
        nrows=len(df.short_name.unique()),
        figsize=(8, len(df.short_name.unique()) * 4),
        squeeze=False,
    )
    for i, product_name in enumerate(sorted(df.short_name.unique())):
        plt_df = (
            df[df.short_name == product_name]
            .groupby(["created_date", "source"])
            .mean(numeric_only=True)
            .reset_index()
        )
        plt_df = plt_df.pivot(index="created_date", columns="source", values="price")
        plt_df.plot(ax=ax[i][0], title=product_name, rot=30)
        ax[i][0].set_xlabel("Price date")
        # handles, labels = ax[i][0].get_legend_handles_labels()
        # ax[i][0].legend(handles=handles[1:], labels=labels[1:])
    fig.tight_layout()
    plt.savefig("index.svg", format="svg")
    print("Report generated successfully")


if __name__ == "__main__":
    run_report()
