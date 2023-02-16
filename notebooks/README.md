# silicon bring-up notebooks

## Install

```
python3 -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
python -m mpy_kernel_upydevice.install
```

## Run jupyter

```
jupyter notebook
```

## Create a new notebook

- Open `openmpw-bringup-template.ipynb` in Jupyter Notebook
- Click *File > Make a Copy...*
- Name the copy after your project, ex: `openmpw-bringup-mpw2-a5`

## Bring up your chip

- Run the cells of the notebooks
- Add more cells to test specific aspect if your design
- Send a pull request to https://github.com/efabless/caravel_board/ to share your notebooks with other OpenMPW participants.
