import apache_beam as beam
import re
from stop_words import get_stop_words

class WordExtractingDoFn(beam.DoFn):
  def process(self, element):
    return re.findall(r'[\w\']+', element)

class SplitRow(beam.DoFn):
  def process(self, element):
    return [element.split(',')]

def format_result(word, count):
    return f"{word},{count}"


with beam.Pipeline() as p:
  input_data = (p
                | "read from text" >> beam.io.ReadFromText("data/sample.txt"))

  counts = (
          input_data
          | 'Split' >> beam.ParDo(WordExtractingDoFn())
          | 'PairWithOne' >> beam.Map(lambda x: (x, 1))
          | 'GroupAndSum' >> beam.CombinePerKey(sum))

  format_count = counts | 'Format' >> beam.MapTuple(format_result)

  filter_stop_words = (format_count
                | "filtering the data with stop words" >> beam.Filter(lambda record: record[0] not in get_stop_words('english')))

  filter_stop_words | 'Write_filter' >> beam.io.WriteToText("output_data/filter_count_output.txt")
  format_count | 'Write_Non_filter' >> beam.io.WriteToText("output_data/nonfilter_count_output.txt")


