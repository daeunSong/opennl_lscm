# Least Squares Conformal Mapping (LSCM)

This repository is an archive for a simple demo program for LSCM from [OpenNL](http://alice.loria.fr/index.php/software/4-library/23-opennl.html) (Open Numerical Library). 


1. Build and Compile
```sh
cd src
g++ main.cpp OpenNL_psm.c -o LSCM -ldl
```

2. Run
```sh
./LSCM input_file.obj <output_file.obj> <spectral=true|false>
```
It will generate an obj file with texture coordinate (uv coordinate), indicated as **vt**. 

3. Plot the result
```sh
python3 -i plot_test.py
```
