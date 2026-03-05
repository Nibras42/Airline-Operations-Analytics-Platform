#### SER541: Exploratory Data Munging and Visualization
#### Title: Aircraft Type and Capacity Allocation Patterns in U.S. Domestic Airline Routes
#### author: Anonymous
#### date: 5th March, 2026

## Basic Questions
**Dataset Author(s):**  
U.S. Department of Transportation, Bureau of Transportation Statistics (BTS).
**Dataset Construction Date:**  
The T-100 Domestic Segment dataset is compiled continuously by the Bureau of Transportation Statistics using operational reports submitted by U.S. air carriers. The dataset used in this project was downloaded on January 28, 2026.
**Dataset Record Count:**  
The original dataset contains 376,272 records. After cleaning and filtering invalid entries such as zero-capacity flights, the processed dataset used in the analysis contains 342,025 records.
**Dataset Field Meanings:**
YEAR: year of operation  
MONTH: month of operation  
UNIQUE_CARRIER: airline carrier code  
UNIQUE_CARRIER_NAME: full airline name  
ORIGIN: origin airport code  
DEST: destination airport code  
AIRCRAFT_TYPE: aircraft model identifier used on the route  
DEPARTURES_PERFORMED: number of flights actually operated  
SEATS: total available seats offered across those flights  
PASSENGERS: total passengers transported  
LOAD_FACTOR: derived metric representing passenger utilization (PASSENGERS / SEATS)
**Dataset File Hash(es):**
MD5 hash of original dataset file: 5c87b5ba54f4b309258a1cf3252ef9c6

## Interpretable Records

### Record 1

**Raw Data**
YEAR: 2025  
MONTH: 8  
UNIQUE_CARRIER: 5V  
UNIQUE_CARRIER_NAME: Tatonduk Outfitters Limited d/b/a Everts Air Alaska and Everts Air Cargo  
ORIGIN: FAI  
DEST: RBY  
AIRCRAFT_TYPE: 421  
DEPARTURES_PERFORMED: 1  
SEATS: 1  
PASSENGERS: 1  
LOAD_FACTOR: 1.00

**Interpretation**
This record represents a small regional flight operated by Everts Air Alaska between Fairbanks (FAI) and Ruby (RBY) in Alaska. The flight carried one passenger on an aircraft with one available seat, resulting in a load factor of 1.0. This type of record is reasonable for small remote routes in Alaska where airlines often operate very small aircraft serving low passenger demand communities.

### Record 2

**Raw Data**

YEAR: 2025  
MONTH: 6  
UNIQUE_CARRIER: TJ  
UNIQUE_CARRIER_NAME: Tradewind Aviation  
ORIGIN: IAD  
DEST: HPN  
AIRCRAFT_TYPE: 479  
DEPARTURES_PERFORMED: 1  
SEATS: 8  
PASSENGERS: 3  
LOAD_FACTOR: 0.375

**Interpretation**
This record represents a flight operated by Tradewind Aviation between Washington Dulles (IAD) and Westchester County Airport (HPN). The flight had eight available seats but only transported three passengers, resulting in a load factor of 37.5%. This indicates relatively low seat utilization for that particular flight, which may occur on smaller charter-style operations or routes with fluctuating demand.

## Visualizations
### Visual 1 - Passengers vs Seats
This visualization shows a very strong linear relationship between the number of available seats and the number of passengers transported. Routes with higher seat capacity generally carry more passengers, which indicates that airlines tend to deploy larger aircraft on routes with higher demand.
### Visual 2 - Passengers vs Departures Performed
The scatter plot shows that passenger counts increase as the number of departures increases. This suggests that airlines respond to higher demand by scheduling more flights on popular routes, allowing passenger volumes to grow proportionally with service frequency.
### Visual 3 - Departures Performed vs Seats
The plot reveals several diagonal clusters that correspond to different aircraft capacities. These clusters likely represent different aircraft types where seat capacity is fixed but departures vary depending on route demand and airline scheduling decisions.
### Visual 4 - Passengers vs Load Factor
Most observations fall between load factor values of approximately 0.7 and 0.95, indicating that airlines typically operate flights with relatively high seat utilization. This reflects industry practices where airlines aim to maximize occupancy while still maintaining some flexibility for demand fluctuations.
### Visual 5 - Aircraft Type Distribution
The aircraft type histogram shows that a small number of aircraft models dominate domestic airline operations. This reflects the airline industry's reliance on standardized narrow-body aircraft families such as the Boeing 737 and Airbus A320 series, which are optimized for medium-distance domestic routes.

## Background Domain Knowledge
Airlines constantly make decisions about how to allocate aircraft and schedule flights across different routes. These decisions depend largely on passenger demand, route distance, airport constraints, and the types of aircraft available in the airline’s fleet. A central operational challenge is matching the number of seats offered on a route with the number of passengers who are likely to travel on that route. If too many seats are offered and demand is low, flights may operate with many empty seats, which reduces efficiency. On the other hand, if demand is high but capacity is limited, airlines may lose potential passengers or create overcrowded flights.
One commonly used metric in airline operations is the load factor, which measures how full a flight is relative to its total seat capacity. Load factor is calculated as the ratio of passengers transported to the number of seats available. Even though it does not directly measure profit, it is widely used as a practical indicator of how effectively capacity is being utilized. Commercial airlines typically aim to keep load factors relatively high while still maintaining enough flexibility in their schedules to respond to changes in demand.
Aircraft type also plays an important role in how airlines serve different routes. Larger aircraft are generally used on routes with higher passenger demand, while smaller aircraft are often deployed on regional or lower-demand routes. Choosing the appropriate aircraft type affects operational efficiency, fuel consumption, scheduling flexibility, and overall fleet utilization. Because of this, airlines frequently adjust both aircraft size and the number of departures to better match passenger demand across their network.
Publicly available aviation datasets provide useful information for studying these operational decisions. In the United States, the Bureau of Transportation Statistics collects airline operational data through the Form 41 reporting system. These datasets include information such as passengers transported, available seats, aircraft type, and number of departures for different flight segments. Although detailed financial data for individual routes is not publicly available, operational variables such as passenger counts, seat capacity, and load factor allow researchers to analyze how airlines deploy aircraft and capacity across their route networks.

## Dataset Generality
The dataset used in this project comes from the U.S. Bureau of Transportation Statistics (BTS) Form 41 reporting system, specifically the T-100 Domestic Segment dataset. This dataset contains operational information reported by U.S. air carriers for non-stop domestic flight segments. Key variables include the number of passengers transported, total available seats, aircraft type, and the number of departures performed. Since large U.S. airlines are required to report these statistics, the dataset provides a broad and reliable view of airline operations within the United States.
While the dataset focuses only on domestic routes operated by U.S. carriers, many of the operational relationships present in the data are not unique to the United States. Airlines in other countries also face similar challenges when deciding how frequently to operate flights and what aircraft types to assign to particular routes. Because of this, patterns observed in passenger demand, seat capacity, and flight frequency may reflect broader airline network planning strategies used throughout the industry.
At the same time, the dataset has certain limitations. It does not include detailed financial variables such as operating costs, ticket prices, or route-level profits. This means that profitability must be inferred indirectly using operational indicators such as load factor or passenger volumes. Additionally, since the dataset only covers U.S. domestic operations, the results may not fully represent airline behavior in international markets or under different regulatory conditions.

## Data Transformations
Before conducting the exploratory analysis, several preprocessing steps were applied to the raw dataset to ensure that the data was clean and suitable for analysis. The original CSV file was first loaded into a pandas DataFrame, and only the variables relevant to the project were selected. These included passengers transported, available seats, aircraft type, number of departures performed, and the calculated load factor.
Records containing invalid or missing values in key numerical fields were removed to prevent errors during analysis. In particular, rows with zero or missing seat capacity were filtered out because they would produce invalid load factor values. Data types for numerical columns were also verified and converted where necessary to ensure that calculations and visualizations could be performed correctly.
After cleaning the dataset, a processed version of the data was saved as a new CSV file within the data_processed directory. In addition, summary statistics and correlation matrices were generated to provide an overview of relationships between the main variables. These preprocessing steps help ensure that the dataset used for visualization and further analysis is consistent, interpretable, and free from obvious data quality issues.