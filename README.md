# apache_beam_assignment

### Steps to Build  and Run Project
1. Clone GitHub repository  for Apache Beam pipelines. ( [https://github.com/prakher1992/weather_portal](https://github.com/prakher1992/apache_beam_assignment.git))

2. Go to the root directory by executing "cd apache_beam_assignment"

3. Install the required Python dependencies mentioned in the ‘requirements.txt’ file
```
pip install -r requirements.txt
```
4. Now execute the command to run the scripts.
   ```
   python pardo_pipeline.py
   python simple_pipeline.py
   ```
## Apache Beam
Apache Beam is a unified model for defining both batch and streaming data processing that can build portable Big data pipelines.
- [x] Portable, beam pipeline once created in any language can be able to run on any execution framework like a spark, flink, cloud dataflow, etc.
- [x] Beam is a programming model whereas Flink and Spark are execution engines.
- [x] Pipeline, encapsulate our entire data processing task from start to finish. This includes reading input data and transforming that data.

### Architecture of Apache Beam
![Picture1](https://github.com/prakher1992/apache_beam_assignment/assets/23658440/92ad0808-85e5-4727-a3c8-f345f70ac71e)
- [x] Beam or Runner API is the core of Apache Beam. If you want to run the Apache beam code in the spark execution engine, these beam or runner APIs will internally transfer the Apache beam to the spark code to run on the spark engine. Similarly for Flink and others.
- [x] Execution engines like a spark, flink where Apache code will actually run.

### Flow of Beam Programming Model:
<img width="503" alt="image" src="https://github.com/prakher1992/apache_beam_assignment/assets/23658440/314f39af-d374-401d-8228-97d46b4d2825">

- [x] Input: text file, Big query, Avro files, database, stream (Kafka, google pub/sub), etc.
- [x] Output: text file, database, Google storage bucket, stream (Kafka, google pub/sub), etc.
- [x] PCollection: A PCollection is a data set or data stream. The data that a pipeline process is part of a PCollection.
- [x] PTransform: A PTransform represents a data processing operation or a step in our pipeline. A transform is applied to zero or more PCollection objects and produces zero or more PCollection objects.

### Map, FlatMap, and Filter Transforms in Apache Beam
- [x] Map: Applies a simple 1-to-1 mapping function over each element in the collection.
- [x] FlatMap: Applies a simple 1-to-many mapping function over each element in the collection. The many elements are flattened into the resulting collection.
- [x] Filter: Given a predicate, filter out all elements that don’t satisfy that predicate. May also be used to filter based on an inequality with a given value based on the comparison ordering of the element.

### ParDo
- [x] ParDo is a Beam transform for generic parallel processing.
- [x] The ParDo processing paradigm is similar to the “Map” phase of a Map/Shuffle/Reduce-style algorithm. A ParDo transform considers each element in the input PCollection, performs some processing function (your user code) on that element, and emits zero, one, or multiple elements to an output PCollection.
- [x] ParDo is useful for a variety of common data processing operations, including:
- [x]	Filtering a data set. 
- [x]	Formatting or type-converting each element in a data set.
- [x]	Extracting parts of each element in a data set. 
- [x]	Performing computations on each element in a data set.
- [x]	When applying a ParDo transform, need to provide user code in the form of a DoFn object.

### DoFn
- [x]	DoFn is a Beam SDK class that defines a distributed processing function.
- [x]	The DoFn object that you pass to ParDo contains the processing logic that gets applied to the elements in the input collection. 



