# Face_attribute_annotation_tool

This is a face attributes annotation tool.

It is written in Python and uses Qt for its frontend.

## Version 1:

It can be used to label the 40 face attributes used in [CelebA](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html).

### Requirements

Python==3.6.8

PyQt5==5.15.4

PySide2==5.15.2

numpy==1.19.5

### Usage

It is simply listing all 40 attributes on the right side. Once an image is selected by clicking "Open", you can annotate the attributes. If you done the work, you can click "Next" to continue the annotating work for the next image in this folder, or click "Prev" to double check the annotations. Of course, you can casually choose where to start and this project will save the annotation results simultaneously for you. However, if you close the window with some uncompleted annotations, a question will show up. If you click "Yes", they will be discarded.

### Demo
![Interface](https://github.com/SteveXWu/face_attribute_label_tool/blob/main/demo/interface.png)
### Python

This annotation tool could be launched by the following commend

```python
python attr_label.py
```

Also, you could use pyinstaller to package it as a .exe file on Windows system.

# Final goals

Final goals: 

1. Users can customize their interested face attributes 
2. This tool could automatically provide the results of some face attributes which have over 90% probability.
