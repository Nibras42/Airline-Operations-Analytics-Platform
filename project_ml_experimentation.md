#### SER541: Machine Learning Experimentation  
#### Title: Aircraft Type and Capacity Allocation Patterns in U.S. Domestic Airline Routes  
#### Author: Anonymous 
#### Date: April 2026  

---

## Selected Records  

Three records from the test dataset were selected to analyze model predictions:

1. SEATS=2084, DEPARTURES_PERFORMED=11, AIRCRAFT_TYPE=699, LOAD_FACTOR=0.8191  
2. SEATS=13585, DEPARTURES_PERFORMED=95, AIRCRAFT_TYPE=612, LOAD_FACTOR=0.7278  
3. SEATS=5434, DEPARTURES_PERFORMED=38, AIRCRAFT_TYPE=612, LOAD_FACTOR=0.8438  

---

## Prediction Explanation  

The model predicts load factor based on the balance between capacity (SEATS), flight frequency (DEPARTURES_PERFORMED), and aircraft type.  

- The first and third records show relatively high load factors, indicating efficient capacity utilization. These routes likely match supply with demand effectively.  
- The second record has a lower load factor despite having very high seat capacity and frequency. This suggests that capacity exceeds demand, leading to reduced efficiency.  

This aligns with the expectation that higher capacity and frequency do not always lead to higher utilization.

---

## Feature Variation Analysis  

### SEATS  

Increasing SEATS while keeping other variables constant tends to decrease load factor. This is because larger aircraft introduce more capacity, which may not be fully utilized if demand does not scale proportionally.  

### DEPARTURES_PERFORMED  

Increasing DEPARTURES_PERFORMED tends to decrease load factor when demand is fixed. More frequent flights distribute passengers across multiple departures, reducing utilization per flight.  

### AIRCRAFT_TYPE  

Different aircraft types correspond to different capacity levels. Larger aircraft types are more efficient on high-demand routes but may lead to underutilization on lower-demand routes.  

---

## Pairwise Feature Interaction  

### SEATS & DEPARTURES_PERFORMED  

When both seat capacity and frequency are high, load factor tends to decrease significantly. This reflects over-supply conditions where available capacity exceeds demand.  

### DEPARTURES_PERFORMED & AIRCRAFT_TYPE  

Smaller aircraft operated at higher frequency may maintain higher load factors compared to large aircraft used frequently. This suggests that airlines may optimize efficiency by matching aircraft size with route demand.  

### SEATS & AIRCRAFT_TYPE  

Aircraft type directly influences seat capacity. Larger aircraft increase total capacity, but without sufficient demand, this leads to lower load factor. High load factors are achieved when aircraft size aligns with demand characteristics.  

---

## Summary  

The experimentation confirms that load factor is strongly influenced by the relationship between capacity and demand. The model captures both linear and non-linear effects, showing that increasing capacity or frequency without corresponding demand reduces efficiency. These observations support the hypotheses defined in the preregistration section and demonstrate meaningful relationships between operational variables.