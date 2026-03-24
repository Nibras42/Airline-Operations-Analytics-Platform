#### SER541: Revised Project Proposal  
#### Title: Aircraft Type and Capacity Allocation Patterns in U.S. Domestic Airline Routes  
#### Author: Nibras Dsouza  
#### Date: 22nd March 2026  

**Keywords:** Airline operations, Load factor modeling, Aircraft capacity allocation  

## Description  
This project analyzes U.S. domestic airline operational data to study how aircraft type and capacity are deployed across routes with varying demand characteristics. Using the Bureau of Transportation Statistics (BTS) T-100 Domestic Segment dataset, the focus is on non-stop domestic flight segments and the relationships between passengers transported, available seats, departure frequency, and aircraft type. Load factor is used as a proxy for route-level operational efficiency and profitability. The project aims to identify patterns in how airlines balance demand and capacity, and to develop a predictive model that explains and estimates load factor using operational variables.

## Research Objectives  

**RO1:** To identify and describe patterns in airline capacity deployment and demand using exploratory visualizations of passengers, seats, departures, and aircraft types across routes.  

**RO2:** To develop a regression model that predicts load factor based on operational features such as seats, departures performed, and aircraft type.  

**RO3:** To evaluate and defend the predictive model by assessing its performance, consistency, and ability to generalize across different routes and aircraft categories.  

**RO4:** To interpret the model results to understand how operational decisions, such as aircraft size and flight frequency, influence route-level efficiency and demand utilization.  

## Preregistration  

**Target Feature:**  
LOAD_FACTOR  

**Input Features:**  
SEATS, DEPARTURES_PERFORMED, AIRCRAFT_TYPE  

**Key Features Selected:**  
A = SEATS  
B = DEPARTURES_PERFORMED  
C = AIRCRAFT_TYPE  

### Single Feature Hypotheses  

**SEATS → LOAD_FACTOR:** Increasing seat capacity without proportional demand will decrease load factor due to overcapacity.  
**DEPARTURES_PERFORMED -> LOAD_FACTOR:** Increasing flight frequency on the same route will reduce load factor if demand is fixed, as passengers are distributed across more flights.  
**AIRCRAFT_TYPE -> LOAD_FACTOR:** Larger aircraft types may exhibit lower load factors on low-demand routes but higher efficiency on high-demand routes due to better capacity utilization.  

### Pairwise Feature Hypotheses  

**SEATS & DEPARTURES_PERFORMED:** High seat capacity combined with high frequency is expected to reduce load factor due to supply exceeding demand.  
**DEPARTURES_PERFORMED & AIRCRAFT_TYPE:** Smaller aircraft used with higher frequency may maintain higher load factors compared to large aircraft used frequently.  
**SEATS & AIRCRAFT_TYPE:** Larger aircraft types with higher seating capacity may only achieve high load factors on routes with sufficient demand, otherwise leading to underutilization.  

## Intellectual Merit  
This project contributes new knowledge by empirically analyzing how airlines allocate aircraft capacity across routes with varying demand levels using publicly available operational data. While airline network planning is widely studied, route-level efficiency patterns are not directly observable due to the absence of public profitability data. By modeling load factor as a proxy for operational efficiency, this study enables data-driven insights into airline decision-making without relying on proprietary financial data. The integration of predictive modeling and exploratory analysis provides a deeper understanding of capacity allocation strategies and their impact on efficiency.

## Data Sourcing  
The dataset used in this project is the U.S. Bureau of Transportation Statistics (BTS) T-100 Domestic Segment dataset, which provides monthly records of non-stop flight operations by U.S. carriers. It includes information such as passengers, available seats, departures performed, and aircraft type. The dataset includes recent data (2024–2025), ensuring relevance to current airline operations. Data is downloaded from the BTS website and processed locally using a reproducible pipeline that filters relevant fields, removes invalid entries, and computes derived features such as load factor.

## Background Knowledge  

1. Holloway, S. (2008). *Straight and Level: Practical Airline Economics*.  
2. Belobaba, P., Odoni, A., & Barnhart, C. (2015). *The Global Airline Industry*.  
3. Vasigh, B., Fleming, K., & Tacker, T. (2018). *Introduction to Air Transport Economics*.  

## Related Work  

1. Belobaba, P. (1989). Airline seat inventory control models.  
2. Coldren, G. et al. (2003). Modeling airline itinerary choices.  
3. Barnhart, C. & Cohn, A. (2004). Airline schedule planning.  
4. Wei, W. & Hansen, M. (2007). Aircraft size and profitability.  
5. Abdelghany, K. & Abdelghany, A. (2009). Airline modeling applications.  
6. Smith, B. et al. (1992). Yield management at American Airlines.  
