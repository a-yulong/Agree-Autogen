# Repository contents

The repository contains benchmark inputs, dataset preparation records, agent prompts, the generation pipeline, knowledge-base documents, the standalone validator, experiment runners, and recorded results.

`data/preparation/` contains the original construction scripts, candidate maps, screening tables, and 399-case quality checks. `examples/recorded_case003/` contains a recorded pipeline execution. `results/review_master/` contains the consolidated rubric scores.

Generation uses a model API. Validation uses JDK 17 and OSATE with AGREE. Configure the model endpoint, `JAVA_HOME`, and `OSATE_HOME` as shown in `README.md`.
