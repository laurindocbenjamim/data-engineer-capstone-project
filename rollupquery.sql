SELECT year,country, avg(amount) as salesAverage FROM public."FactSales"
join public."DimCountry" on public."FactSales".countryid = public."DimCountry".countryid
join public."DimDate" on public."FactSales".dateid = public."DimDate".dateid
group by rollup (year,country)
order by year
limit 5