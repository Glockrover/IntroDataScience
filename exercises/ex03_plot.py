import marimo

__generated_with = "0.19.11"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


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


@app.cell
def _():
    import polars as pl
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    return go, make_subplots, pl, px


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 1: Your First Plot - Bar Chart
    """)
    return


@app.cell
def _(pl, px):
    # Create a bar chart showing sales by category
    category_sales = pl.read_json("../data/raw/sales.json").group_by("product_category").agg([
        pl.col("total_amount").sum().alias("total_sales")
    ])

    ex_fig1 = px.bar(
        category_sales, 
        x="product_category", 
        y="total_sales", 
        title="Sales by Product Category", 
        color="product_category"
    )
    ex_fig1
    return (category_sales,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2: Line Chart - Sales Over Time
    """)
    return


@app.cell
def _(pl, px):
    # Create a line chart showing sales trends by month
    sales = pl.read_json("../data/raw/sales.json")
    monthly_sales = sales.with_columns([
        pl.col("date").str.strptime(pl.Date, "%Y-%m-%d").alias("date_parsed")
    ]).with_columns([
        pl.col("date_parsed").dt.month().alias("month")
    ]).group_by("month").agg([
        pl.col("total_amount").sum().alias("revenue")
    ]).sort("month")

    ex_fig2 = px.line(
        monthly_sales,
        x="month",
        y="revenue",
        title="Monthly Sales Trend",
        markers=True
    )
    ex_fig2
    return (sales,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 3: Scatter Plot - Exploring Relationships
    """)
    return


@app.cell
def _(pl, px):
    # Create a scatter plot
    students = pl.read_csv("../data/raw/students.csv")

    ex_fig3 = px.scatter(
        students,
        x="attendance_rate",
        y="test_score",
        title="Test Score vs Attendance Rate",
        labels={"attendance_rate": "Attendance (%)", "test_score": "Test Score"},
        color="grade_level"
    )
    ex_fig3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 4: Histogram - Distribution Analysis
    """)
    return


@app.cell
def _(px, sales):
    # Create a histogram
    ex_fig4 = px.histogram(
        sales,
        x="total_amount",
        title="Distribution of Transaction Amounts",
        labels={"total_amount": "Transaction Amount ($)"},
        nbins=30
    )
    ex_fig4
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 5: Advanced - Multiple Subplots
    """)
    return


@app.cell
def _(category_sales, go, make_subplots, pl, sales):
    # Create a dashboard with 2 subplots
    region_sales = sales.group_by("region").agg([
        pl.col("total_amount").sum().alias("total_sales")
    ])

    ex_fig5 = make_subplots(
        rows=2, cols=1,
        subplot_titles=("Sales by Category", "Sales by Region")
    )

    ex_fig5.add_trace(
        go.Bar(x=category_sales["product_category"], y=category_sales["total_sales"], name="Category"),
        row=1, col=1
    )

    ex_fig5.add_trace(
        go.Bar(x=region_sales["region"], y=region_sales["total_sales"], name="Region"),
        row=2, col=1
    )

    ex_fig5.update_layout(height=600, showlegend=False, title_text="Sales Dashboard")
    ex_fig5
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
