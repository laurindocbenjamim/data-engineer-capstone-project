CREATE MATERIALIZED VIEW total_sales_per_country AS
SELECT country, sum(amount) as totalsales FROM public."FactSales"
join public."DimCountry" on public."FactSales".countryid = public."DimCountry".countryid
group by grouping sets(country)
order by country;
