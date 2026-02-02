# Lab5-Mini-MapReduce-EMR
# Lab 5: Mini-MapReduce on Amazon EMR (WordCount Example)

This repository contains the code and documentation for the WordCount MapReduce job implemented using Hadoop Streaming with Python on Amazon EMR.

## Dataset Description
- **Source**: Preprocessed dump of Simple English Wikipedia from https://github.com/LGDoor/Dump-of-Simple-English-Wiki
- **File**: `corpus.tgz` (compressed), extracts to `corpus.txt`
- **Format**: Plain text, where each article starts with a title on the first line, followed by content lines until a blank line. Articles are separated by blank lines.
- **Size**: ~32 MB uncompressed (as observed in HDFS: 32,821,626 bytes)
- **Number of articles**: 50,441 articles (from repository description)
- **Content**: Full text content of Simple English Wikipedia (simplified English version of Wikipedia).
- **Usage in lab**: Uploaded to HDFS at `/user/hadoop/input/corpus.txt`. For experiments, duplicated to create larger input sizes.

## Mapper and Reducer Code
- `mapper.py`: Processes each line, extracts words (lowercased, alphanumeric), emits `<word, 1>`
- `reducer.py`: Aggregates counts for each word

Both scripts use Python 3 and are designed for Hadoop Streaming.

## Run Command (on EMR master node after SSH)
After uploading dataset to HDFS and making scripts executable:

```bash
# Clean previous output (if exists)
hdfs dfs -rm -r /user/hadoop/output/

# Submit the streaming job
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
  -input /user/hadoop/input/ \
  -output /user/hadoop/output/ \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py
