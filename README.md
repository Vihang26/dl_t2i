# Description Logic for T2I Evaluations

Automated evaluation of text-to-image generative models using description logic.
The main T2I model to be evaluated is [Stable Diffusion V1.4](https://huggingface.co/CompVis/stable-diffusion-v1-4).

## Project Goals
| Estimated Duration | Task Allotted                                                                              |
|--------------------|--------------------------------------------------------------------------------------------|
|2 weeks             |Learning description logics                                                              |
|                    |Playing with Stable Diffusion (and understanding where it is failing)                    | 
|                    |Reading and analyzing the existing T2I evaluation strategies: DALL-Eval and HRS-Benchmark|
|2 weeks             |Defining the description logic rules (i.e., knowledge graph)                             |
|                    |Creating a small diverse set of prompts using automated strategies                       |
|                    |Evaluating several T2I models                                                            |
|3 weeks             |Scaling the description logic rules                                                      |
|                    |Performing automated evaluations of T2I models                                           |
|1 week              |Summarizing and report writing                                                           |

## Automating Evaluations
There are multiple evaluation methods. Evaluations can be automated using two ways: 
1. Creating a pipeline to generate a diverse set of prompts
2. Designing the evaluation procedure to check generated images

## Challenges
There are a few challenges associated with this task:
1. Bias within evaluation data (like, apple is always associated with red and green colors)
- Can we create better evaluation dataset?
- Other kinds of biases: apple is always evaluated on the basis of colors, but not sizes
Can Stable Diffusion generate big apple with the size of an elephant?
2. Hallucination: If we ask the model to generate “A” then it generates “A + B”.
- How to detect such hallucinations?

## Prompt Generation Methodology
Prompt generation will take the following format and expand on it to form more complicated prompts:
C = Color = {Red, Green, Black}
D = Fruit = {Banana, Apple}
F = Furniture = {Chair, Table}
R = Relation = {“on top of”, “and”}

### Level 1
C union D = {“red banana”, “black apple”}

### Level 2
R((C union D), F) = {“black apple on top of chair”}

### Level 3
R((C union D), (C union D)) = {“black apple and red banana”}


