import apache_beam as beam

p2 = beam.Pipeline()

grocery = (p2
           | "Read from Text" >> beam.io.ReadFromText("data/input.txt")
           | 'Filter regular' >> beam.Map(lambda record: record.upper())
           | 'Write to text' >> beam.io.WriteToText('output_data/output.txt')
           | beam.Map(print))
p2.run()