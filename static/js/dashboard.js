function createChart(id, type, labels, data, label = "") {
    new Chart(document.getElementById(id), {
        type: type,
        data: {
            labels: labels,
            datasets: [{ label: label, data: data }]
        }
    });
}

// Vendas por Mês
createChart("salesPerMonth", "bar", MONTHS, SALES_MONTH, "Vendas");

// Produtos mais vendidos
createChart("topProducts", "bar", TOP_PRODUCTS_LABELS, TOP_PRODUCTS_DATA, "Qtd");

// Categorias
createChart("topCategories", "doughnut", CATEGORY_LABELS, CATEGORY_DATA);

// Lucro x Custo
new Chart(document.getElementById("profitVsCost"), {
    type: "bar",
    data: {
        labels: MONTHS,
        datasets: [
            { label: "Custo", data: MONTHLY_COST },
            { label: "Lucro", data: MONTHLY_PROFIT }
        ]
    }
});

// Menor Estoque
createChart("lowestStock", "bar", LOW_STOCK_LABELS, LOW_STOCK_DATA, "Qtd");
