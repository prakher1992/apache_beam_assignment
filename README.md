# apache_beam_assignment

## Apache Beam
Apache Beam is a unified model for defining both batch and streaming data processing that can build portable Big data pipelines.
- [x] Portable, beam pipeline once created in any language can be able to run on any execution framework like a spark, flink, cloud dataflow, etc.
- [x] Beam is a programming model whereas Flink and Spark are execution engines.
- [x] Pipeline, encapsulate our entire data processing task from start to finish. This includes reading input data and transforming that data.
## Architecture of Apache Beam
![Picture1](https://github.com/prakher1992/apache_beam_assignment/assets/23658440/92ad0808-85e5-4727-a3c8-f345f70ac71e)
- [x] Beam or Runner API is the core of Apache Beam. If you want to run the Apache beam code in the spark execution engine, these beam or runner APIs will internally transfer the Apache beam to the spark code to run on the spark engine. Similarly for Flink and others.
- [x] Execution engines like a spark, flink where Apache code will actually run.

