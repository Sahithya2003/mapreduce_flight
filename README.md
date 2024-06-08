# MapReduce Program for Flight Data Analysis

This repository contains a MapReduce program written in Python for analyzing flight data over the past 10 years. The program is designed to run on the Hadoop framework. The MapReduce task includes finding the minimum flight occupancy by aggregating over all flights in a region and determining the frequency of maximum flight occupancy recorded during the past 10 years in the country.

## Installation and Setup

1. Install Hadoop on Linux by following the steps outlined in this [guide](https://medium.com/@abhikdey06/apache-hadoop-3-3-6-installation-on-ubuntu-22-04-14516bceec85).

2. Create a directory in Hadoop's file system for input data:
    ```bash
    hadoop fs -mkdir /input
    ```

3. Upload the flight data CSV file (`flight.csv`) to the Hadoop file system:
    ```bash
    hadoop fs -put flights.csv /input/flights.csv
    ```

4. Execute the MapReduce program using Hadoop Streaming:
    ```bash
    hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
        -file flight.py -mapper "python3 flight.py mapper" \
        -reducer "python3 flight.py reducer" \
        -input /input/flights.csv -output /output
    ```

5. View the output by displaying the contents of the result file:
    ```bash
    hadoop fs -cat /output/part-00000
    ```

Alternatively, you can check the Hadoop Web UI by accessing `your-ip-address:9870` in your web browser.
![image](https://github.com/Sahithya2003/mapreduce_flight/assets/92243343/73fa693b-275c-4178-b1d3-4e833e8099c0)

## Output Explanation

The output file (`part-00000`) will provide the following results:
- **Minimum Flight Occupancy**: Aggregated data over all flights in the region.
- **Frequency of Maximum Flight Occupancy**: Records the frequency of the highest recorded occupancy during the past 10 years in the country.

## File Structure

- `flight.py`: Contains the main MapReduce program.
- `OUTPUTpart-00000`: Includes the output.
- `flight.csv`: Sample flight data file.

## Note
Make sure to replace `your-ip-address` with the actual IP address of your Hadoop cluster's Namenode.
