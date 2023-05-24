# nthu_recon_choose_point

## Installation

Install the dependencies 

```sh
cd nthu_recon_choose_point
pip install opencv_python
pip install sys
pip install numpy
modify path to image path
python choose_point.py
```

then u can click needed point, after 7 click, image will be shut down and give u a txt including coordinate

```sh
Add a write.py
If you are using meshlab.txt you can get 3D number splited by blank
for example:
you may record as:
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
then you can run write.py(please modify path), 
After that you can surprisingly find that you can get number just like this:
1,4,7,10,13,16,19
2,5,8,11,14,17,20
3,6,9,12,15,18,21
which fits exactly the format we want
```

| before | after |
|--------|-------|
|    ![bench_7.png](https://github.com/kstsunhj/nthu_recon_choose_point/blob/main/bench_7.png)    |    ![bench_7.png](https://github.com/kstsunhj/nthu_recon_choose_point/blob/main/Snipaste_2023-05-18_20-06-29.png)   |

