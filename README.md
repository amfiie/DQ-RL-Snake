# DQ-RL-Snake
Deep Q Reinforcement Learning Snake game agent

## Prerequisites
- Python3
- venv/anaconda
- Unix (For windows users - use VSL)

## Setup
1. Clone this project
2. Go in to this folder and create a virtual environment:

    ### Unix
    ```
    cd DQ-RL-Snake
    python3 -m venv <environment name>
    ```

3. Go into virtual environment:

    ### Unix
    ```
    source <environment name>/bin/activate
    ```

4. Install requirements in the virtual environment:

    ### Unix
    ```
    pip install --upgrade pip && pip install -r requirements.txt
    ```

## Run

```
python3 main.py --speed=<speed of simulation>
```