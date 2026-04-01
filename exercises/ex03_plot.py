import marimo

__generated_with = "0.22.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""
    # Exercise 3: Plotting Visualizations 📊

    **Plot Visuals!**

    **What you'll do:**

    - Create visualizations

    **Instructions:**

    - Complete each TODO section
    - Run cells to see your results
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 1: Your First Plot - Bar Chart
    """)
    return


@app.cell
def _():
    # TODO: Create a bar chart showing sales by category
    # Use plotly express (px.bar)
    # - x-axis: product_category
    # - y-axis: total sales
    # - Add a title
    # - Color the bars
    import polars as pl
    import plotly.express as px

    # Hint: Make sure category_sales is a valid dataframe first!
    category_sales = pl.read_json('../data/raw/sales.json')  # Replace with your actual data source
    category_sale = category_sales.group_by('product_category').agg(pl.col("total_amount").sum().alias("total_sales"))

    ex_fig1 = px.bar(
        category_sale,
        x='product_category',
        y='total_sales',
        title='Total Sales by Product Category',
        color = 'product_category'
    )

    # Uncomment when ready:
    ex_fig1.show()
    return category_sale, category_sales, pl, px


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2: Line Chart - Sales Over Time
    """)
    return


@app.cell
def _(category_sales, pl, px):
    # TODO: Create a line chart showing sales trends by month
    # Use px.line
    # - x-axis: month
    # - y-axis: total revenue
    # - Add markers to the line
    # - Add a title

    category_sales_months = category_sales.with_columns(
        pl.col("date").str.to_date("%Y-%m-%d")
    ).with_columns(
        pl.col("date").dt.month().alias("month")
    ).group_by('month').agg(pl.col('total_amount').sum().alias('total_revenue')).sort('month', descending=True)


    # line_graph_data = category_sales_months.group_by('month').agg(pl.col('total_amount').sum().alias('total_revenue'))

    ex_fig2 = px.line(
        category_sales_months,
        x = 'month',
        y = 'total_revenue',
        title="Total revenue by month",
        markers=True
    )

    # Uncomment when ready:
    ex_fig2.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 3: Scatter Plot - Exploring Relationships
    """)
    return


@app.cell
def _(pl, px):
    # TODO: Create a scatter plot showing the relationship between
    # attendance_rate (x-axis) and test_score (y-axis)
    # - Color points by grade_level
    # - Add a trendline (trendline="ols")
    # - Add appropriate title and labels
    school_data = pl.read_csv('../data/raw/students.csv')

    ex_fig3 = px.scatter(
        school_data,
        x = 'attendance_rate',
        y = 'test_score',
        color = 'grade_level',
        trendline = 'ols'
    )

    # Uncomment when ready:
    ex_fig3.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 4: Histogram - Distribution Analysis
    """)
    return


@app.cell
def _(category_sales, px):
    # TODO: Create a histogram of transaction amounts (total_amount)
    # - Use 30 bins
    # - Add a title
    # - Label the axes
    # - Try adding nbins=30 parameter

    ex_fig4 = px.histogram(
        category_sales,
        x="total_amount",
        title="Distribution of Transaction Amounts",
        labels={"total_amount": "Transaction Amount"},
        nbins=30,
    )

    # Uncomment when ready:
    ex_fig4.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 5: Advanced - Multiple Subplots
    """)
    return


@app.cell
def _(category_sale, category_sales, pl):
    # TODO: Create a dashboard with 2 subplots:
    # 1. Top plot: Bar chart of sales by category (reuse category_sales)
    # 2. Bottom plot: Bar chart of sales by region (reuse region_summary)

    # Hint: Use go.Figure() with make_subplots or add multiple traces
    # This is challenging - check the solution if you get stuck!

    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    region_summary = category_sales.group_by('region').agg(pl.col("total_amount").sum().alias("total_sales"))

    ex_fig5 = make_subplots(rows=2, cols=1, subplot_titles=["Sales by Category", "Sales by Region"])
    ex_fig5.add_trace(go.Bar(x=category_sale['product_category'], y=category_sale['total_sales']), row=1, col=1)
    ex_fig5.add_trace(go.Bar(x=region_summary['region'], y=region_summary['total_sales']), row=2, col=1)


    ex_fig5.update_layout(
        height=800,
        width =800,
        title_text="total sales by category and region",
        showlegend=False,
        title_font_size=24
    )
    # Uncomment when ready:
    ex_fig5.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🎉 Excellent Work!

    You've completed the plotting exercises!

    **What you practiced:**

    - ✅ Bar charts
    - ✅ Line charts
    - ✅ Scatter plots
    - ✅ Histograms
    - ✅ Advanced: Subplots
    - ✅ Multiple chart types (bar, line, scatter, histogram)
    - ✅ Combining data analysis with visualization

    **What's next?**

    - Try creating your own visualizations with the data!

    **Pro Tips:**

    - Plotly charts are interactive - hover, zoom, pan!
    - Always explore your data before plotting
    """)
    return


if __name__ == "__main__":
    app.run()
