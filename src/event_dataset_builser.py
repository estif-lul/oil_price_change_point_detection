import pandas as pd
import os

# Ensure output directory exists
output_dir = 'data'
os.makedirs(output_dir, exist_ok=True)

# Define major geopolitical and economic events affecting oil prices (2015–2025)
data = [
    ["Iran Nuclear Deal Implementation", "2016-01-16", "Policy", "Lifted sanctions on Iran, increasing global oil supply and lowering prices."],
    ["OPEC Production Cut Agreement", "2016-11-30", "Policy", "OPEC agreed to cut production, boosting oil prices globally."],
    ["US-China Trade War Begins", "2018-07-06", "Policy", "Trade tensions created global economic uncertainty, dampening oil demand and prices."],
    ["Drone Attack on Saudi Oil Facilities", "2019-09-14", "Conflict", "Temporarily disrupted 5% of global oil supply, causing price spike."],
    ["COVID-19 Pandemic Lockdowns", "2020-03-11", "Policy", "Global lockdowns led to historic drop in oil demand and prices."],
    ["Russia-Ukraine War Begins", "2022-02-24", "Conflict", "Triggered sanctions on Russian oil, disrupted supply chains, and spiked prices."],
    ["EU Ban on Russian Oil Imports", "2022-12-05", "Sanction", "Reduced Russian oil exports to Europe, tightening global supply."],
    ["US Strategic Petroleum Reserve Release", "2022-03-31", "Policy", "Released 180 million barrels to stabilize prices amid Ukraine war."],
    ["OPEC+ Voluntary Production Cuts", "2023-04-02", "Policy", "Saudi Arabia and others cut output to support prices amid demand concerns."],
    ["Israel-Iran Tensions Escalate", "2025-06-15", "Conflict", "Airstrikes and Strait of Hormuz threats caused Brent crude to spike 7–11%."],
    ["China Economic Slowdown", "2024-08-01", "Policy", "Reduced oil demand from world's largest importer, pressuring prices downward."],
    ["US Reimposes Sanctions on Venezuela", "2023-10-20", "Sanction", "Restricted Venezuelan oil exports, tightening supply in Latin America."],
    ["India Signs Long-Term Oil Deal with Russia", "2023-06-10", "Policy", "Shifted global trade flows, increasing Russian exports to Asia."],
    ["Houthi Attacks on Red Sea Shipping", "2024-01-05", "Conflict", "Threatened oil transport routes, raising geopolitical risk premiums."],
    ["Global Climate Agreement Targets Fossil Fuels", "2021-11-13", "Policy", "COP26 commitments pressured long-term oil demand outlook."],
    ["9/11 Terrorist Attacks", "2001-09-11", "Conflict", "Triggered global instability and fears of supply disruptions, causing oil price volatility."],
    ["U.S. Invasion of Iraq", "2003-03-20", "Conflict", "Disrupted oil production and exports from Iraq, contributing to rising oil prices."],
    ["Hurricane Katrina", "2005-08-29", "Conflict", "Damaged oil infrastructure in the Gulf of Mexico, leading to supply shortages and price spikes."],
    ["Global Financial Crisis", "2007-12-01", "Policy", "Reduced global demand for oil, causing a sharp decline in oil prices."],
    ["Russian-Georgian War", "2008-08-07", "Conflict", "Raised concerns over energy security in Europe, affecting oil market sentiment."],
    ["Oil Price Peak", "2008-07-01", "Policy", "Oil prices reached $145/barrel due to high demand and geopolitical tensions."],
    ["Arab Spring Begins", "2010-12-17", "Conflict", "Political unrest in oil-producing countries led to fears of supply disruptions."],
    ["Libyan Civil War", "2011-02-15", "Conflict", "Major oil production halted in Libya, tightening global supply."],
    ["U.S. Sanctions on Iran", "2012-01-01", "Sanction", "Restricted Iranian oil exports, reducing global supply and increasing prices."],
    ["Syrian Civil War Escalation", "2012-07-01", "Conflict", "Instability in the region raised concerns over oil transport routes and supply."],
    ["EU Sanctions on Russia", "2014-03-01", "Sanction", "Imposed due to Crimea annexation, affecting Russian oil exports and market dynamics."],
    ["OPEC Decision Not to Cut Production", "2014-11-27", "Policy", "Led to oversupply in the market, causing oil prices to plummet."],
    ["U.S. Shale Boom", "2010-01-01", "Policy", "Increased domestic oil production, contributing to global oversupply and price decline."],
    ["China's Economic Slowdown", "2015-01-01", "Policy", "Reduced demand growth for oil, contributing to falling prices."],
    ["Iran Nuclear Deal Framework", "2015-04-02", "Policy", "Raised expectations of increased Iranian oil exports, influencing market sentiment."],
    ["1973 Oil Embargo", "1973-10-17", "Policy", "OPEC imposed an oil embargo against nations supporting Israel in the Yom Kippur War, causing oil prices to quadruple."],
    ["1979 Iranian Revolution", "1979-01-01", "Conflict", "Political upheaval in Iran disrupted oil production, leading to a global oil supply shock and price surge."],
    ["1980 Iran-Iraq War", "1980-09-22", "Conflict", "War between two major oil producers led to significant supply disruptions and price volatility."],
    ["1986 Oil Price Collapse", "1986-01-01", "Policy", "Saudi Arabia increased production to regain market share, causing oil prices to plummet."],
    ["1990 Iraqi Invasion of Kuwait", "1990-08-02", "Conflict", "Iraq's invasion of Kuwait led to fears of supply shortages, driving oil prices sharply upward."],
    ["1978 Iranian Oil Strikes", "1978-10-01", "Conflict", "Strikes in Iran's oil sector reduced exports and contributed to rising global oil prices."],
    ["1983 OPEC Quota Agreement", "1983-03-01", "Policy", "OPEC agreed on production quotas to stabilize falling oil prices."],
    ["1985 US-Saudi Oil Agreement", "1985-06-01", "Policy", "Saudi Arabia aligned with US interests, increasing production and contributing to price declines."],
    ["1991 Gulf War", "1991-01-17", "Conflict", "Military conflict in the Persian Gulf region disrupted oil supplies and caused price spikes."],
    ["1974 US Oil Price Controls", "1974-01-01", "Policy", "US government imposed price controls to mitigate inflation from the oil embargo."],
    ["1980 US Sanctions on Iran", "1980-04-07", "Sanction", "US imposed sanctions on Iran following the hostage crisis, affecting oil trade flows."],
    ["1975 UK North Sea Oil Discovery", "1975-06-01", "Policy", "Discovery of North Sea oil reduced European dependence on Middle Eastern oil."],
    ["1998 Asian Financial Crisis", "1997-07-02", "Policy", "Economic downturn in Asia reduced oil demand, contributing to falling prices."],
    ["1973 Yom Kippur War", "1973-10-06", "Conflict", "Middle East conflict triggered the oil embargo and reshaped global energy politics."],
    ["1989 Exxon Valdez Oil Spill", "1989-03-24", "Policy", "Environmental disaster led to increased regulation and scrutiny of oil transport and production."],
    ["9/11 Terrorist Attacks", "2001-09-11", "Conflict", "Triggered fears of Middle East instability, leading to oil price volatility."],
    ["U.S. Invasion of Iraq", "2003-03-20", "Conflict", "Disrupted oil production and exports from Iraq, contributing to price increases."],
    ["Hurricane Katrina", "2005-08-29", "Conflict", "Damaged U.S. Gulf Coast oil infrastructure, causing supply disruptions and price spikes."],
    ["Global Financial Crisis", "2007-12-01", "Policy", "Reduced global demand for oil, leading to a sharp decline in prices."],
    ["Russian-Georgian War", "2008-08-07", "Conflict", "Raised concerns over energy transit routes in the Caucasus region."],
    ["Arab Spring Begins", "2010-12-17", "Conflict", "Political instability across oil-producing Arab nations led to price volatility."],
    ["Libyan Civil War", "2011-02-15", "Conflict", "Major disruption in Libyan oil exports, contributing to global supply concerns."],
    ["U.S. Sanctions on Iran", "2012-01-01", "Sanction", "Restricted Iranian oil exports, tightening global supply and raising prices."],
    ["EU Sanctions on Russia", "2014-03-17", "Sanction", "Imposed due to Crimea annexation, affecting Russian energy sector and oil flows."],
    ["OPEC Decision Not to Cut Production", "2014-11-27", "Policy", "Led to oversupply and a dramatic fall in oil prices."],
    ["China’s Economic Slowdown", "2015-01-01", "Policy", "Reduced demand growth from a major consumer, contributing to price declines."],
    ["U.S. Shale Boom", "2010-01-01", "Policy", "Increased domestic production, reducing import dependence and affecting global prices."],
    ["Peak Oil Theory Popularization", "2005-01-01", "Policy", "Speculative fears of declining production drove investment and price increases."],
    ["Iran Nuclear Deal Framework", "2015-04-02", "Policy", "Raised expectations of increased Iranian oil exports, influencing market sentiment."],
    ["Venezuelan Economic Crisis", "2014-01-01", "Policy", "Reduced oil output from Venezuela, affecting global supply."]
]

# Create DataFrame
columns = ["Event", "Start Date", "Type", "Impact Summary"]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
csv_path = os.path.join(output_dir, "oil_price_event_dataset.csv")
df.to_csv(csv_path, index=False)

print("Dataset saved to:", csv_path)
df.head()
