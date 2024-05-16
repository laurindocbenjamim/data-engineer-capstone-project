SELECT country, category, sum(amount) as totalsales FROM public."FactSales"
join public."DimCountry" on public."FactSales".countryid = public."DimCountry".countryid
join public."DimCategory" on public."FactSales".categoryid = public."DimCategory".categoryid
group by grouping sets(country,category)
order by country
limit 5