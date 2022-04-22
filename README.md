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

It is simply listing all 40 attributes on the right side. Once an image is selected by clicking "Open", you can annotate the attributes. If you have done the work, you can click "Next" to continue the annotating work for the next image in this folder, or click "Prev" to double check the annotations. Of course, you can casually choose where to start and this project will save the annotation results simultaneously for you.

**The annotation files will be saved in your/opened/image/path/results/.**

### Demo
![Interface](https://github.com/SteveXWu/face_attribute_label_tool/blob/main/demo/interface.png)
### Python

This annotation tool could be launched by the following commend

```python
python attr_label.py
```

Also, you could directly download the App from

Windows: [attr_annotation_tool](https://drive.google.com/file/d/1TnRfiEiZDk_zDoL_GtqNpMCNfVZIpG8m/view?usp=sharing)

IOS: [attr_annotation_tool](https://drive.google.com/file/d/1D7iBEol89kmIzjD7Rd-ob5_r9oE3x43D/view?usp=sharing)

and launch the attr_label to start your labeling work.

### Packing

There are two UI forms could be chosen to pack:

[myUI_or.ui](https://github.com/SteveXWu/face_attribute_label_tool/blob/main/myUI_or.ui) has the same label sequence as the [CelebA](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html).

[myUI.ui](https://github.com/SteveXWu/face_attribute_label_tool/blob/main/myUI.ui) is the grouped version, where the attributes are grouped by the position. It is more convenient to annotate them, but the labels in the npy file are also in the same sequence as the [CelebA](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html).

*The current packed app is based on [myUI.ui](https://github.com/SteveXWu/face_attribute_label_tool/blob/main/myUI.ui).*

### TODO:

Make a convert button to collect the labels into one csv file.

# Final goals

Final goals: 

1. Users can customize their interested face attributes 
2. This tool could automatically provide the results of some face attributes which have over 90% probability.
