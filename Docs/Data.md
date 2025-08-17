# Data Understanding

For this project, When i searched for data. These are what it lead me to : 

### Central Electricity Authority (CEA)

CEA is the offical indian authority for electricity generation, capacity and grid performance. It publishes plant-level and state-level data : generation (daily / monthly), installed capacity, plant load factors (PLF), outages, fuel mix (coal, gas, hydro, renewable) and grid frequency. Data formats are mostly Excel and PDF reports.

CEA is the primary source of data, which is accurate operational metrics. Which acts as the basis for energy mix calculation, supply-demand analysis and renewable penetration metrics.

As this is the primary data, this is feeded to Ember, MoSPI and State boards.

According to this reports,
- Daily Data
    - Daily Generation reports : 01, 02, 03, 04, 05, 17
    - Daily Coal report : for fuel availability and supply demand correlation
    - Outage Reports : 10, 10A, 11, 12, 13, 15
- Monthly data
    - Monthly Generation Report : for trend and sensonality analysis
    - Transmission & Installed Capacity Reports

The initial data consolidation process for the Powertrack project focuses on five key reports to build a robust data model from the ground up. This approach starts by cleaning the 01_All_India_Region_Wise_Power_generation_Overview file, which serves as a high-level summary of regional generation and capacity metrics. By then integrating the more granular data from three other critical reports, the project gains deep insights into grid performance and reliability. The 02 and 10 reports provide unit-level generation details and daily outage reasons, while the 12 report tracks long-term capacity issues. Finally, the 01_Daily_Coal_Report adds a vital layer of information on the fuel supply chain for thermal plants, completing the holistic view of the power sector.


[CEA data](https://npp.gov.in/publishedReports), 
[Link for CEA](https://cea.nic.in/?lang=en)

### Ember 

Ember is an independent, global energy think tank that focuses on using data and policy to accelerate the transition to clean energy. In context of Indian electricity, ember is an significant source of data and analysis, and its reports are frequently cited by media and policymakers.

Ember uses data from the CEA and own emission factors to produce carbon intensity, fuel share trends and transition speed metrics. Offers data in CSV/Excel with time-series trends.

Ember data enhances the CEA data with climate/emission context, supports world bank benchmarking for renewable share and can validate MoSPI trends for energy mix.

[Link for Ember](https://ember-energy.org/countries-and-regions/india/)

### MoSPI

MoSPI is Ministry of Statistics and programme implementation. Basically, it focuses on consumption side of the elctricity on the basis of different sector use. It publishes energy statistics yearbook with data since independence.

MoSPI shows long-term evolution of india's electricity demand and efficency and links electricty to GDP, population, industry growth.

CEA data tells you the supply and MoSPI tells you the demand, MoSPI enriches Ember and aligns with the World Bank.

[Link for MoSPI](https://mospi.gov.in/)

### World Bank

World Bank tracks electricty access, renewable share, per capita consumption, grid reliability across countries. data is standardized for global comparability.

Using the data, it puts indian in a global context. Useful for policy dashboards showing progress on UN SDGs.

World Bank helps us in benchmarking with MoSPI and CEA data available. World bank and ember works together use standardized metrics for comparision.

[Link for World Bank](https://www.worldbank.org/en/topic/energy)

### State Electricity Boards

State-level operations, such as : generation, load dispatches and outages. Often publishes real-time dashboards and daily PDFs. Captures regional reliability issues, renewable variability.

This data validated the CEA totals at a state level, Feeds dashboards for localized insights. Helps MoSPI refine state-level consumption figures.