# Requirement Doc

This is a detailed document of what I noticed with my working with claude code that I need to optimize. This doc will involve a what to know during planning mode and what to do during execution/code writing mode.

## Planning

1. The user is only DONE planning when the command `/finished-planning` is triggered.
This command will then trigger the procedure of implementing what was planned during planning mode.
2. Making assumptions due to the ambiguity of the user's request is not sought after Claude should ask questions or make user select options whenever possible, removing any ambiguity.
3. Planning is the most crucial step in doing anything scientific. Engineering belongs to the realm of science, so planning is very crucial for writing code/algorithms as well.


## Code Implementation

During Code editing:
1. Writing README or any documentation should only be done if the user triggers the `/write-documentation` command. 
2. Using emoji is prohibited at all times, unless the user specificially requires the use of emoji.
3. Any bash/shell script should be written in the most simple form where args are specified as variables and a program takes that variable.
4. Shell scripts most times live inside the `scripts/` folder of the project's root directory
```
    ARG1="xx"
    ARG2="yy"
    uv run python main.py --arg1 "$ARG1" --arg2 "$ARG2"
```
5. Don't write all the code inside the project's root directory, try to at least organize them inside different folders as below.
```
project/
├── data/
│   ├── data_subfolder_1/
│   └── data_subfolder_2/
├── src/
│   ├── utils/
│   └── code_group_1/
├── scripts/
│
├── logs/
│  
└── docs/
    ├── manual/
    └── design/
```
6. Use loggers instead of `print` whenever possible.
## Code Execution

1. The use of `uv` is always present:
   1. any python code execution should start with `source .venv/bin/activate`
   2. any python package should be installed with either `uv add` or `uv pip install`
