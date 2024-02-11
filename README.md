# Clearer Views for Cancer Research: Upgrading Chromosome Analysis
This contains the code for our chromosome segmentation tool. The notebook files were for
our personal testing and early implemntations.

## Directory

| File      | Description |
| ----------- | ----------- |
| config.ini      | Configuration file to set parameters       |
| environment.yml   | File to create the environment        |



| Folder      | Description |
| ----------- | ----------- |
| sample      | Folder containing sample images to use with our project       |
| src   | Contains our Python scripts        |

## Installation
To get started, run the following code to create the environment.

```
git clone 
cd ecDNA-Capstone
conda env create -f environment.yml
conda activate cnn-cap
```

## Image Specifications
Input folder will only read .tif files

## Tasks
### `normalize_images`
Normalize images based on a percentile and combine images that are separated into r/g/b channels. Not needed to be used if the photos are already combined.

Set parameters in config.yaml under `Normalize`:

````
folder_path : path to folder containing images
````

#### Output

1. **norm folder** - folder containing normalized images

### `find_boxes`
Manual annotation tool for finding bounding boxes in cell images.

Set parameters in config.yaml under `Find`:

````
folder_path : path to folder containing images
````

#### Output

1. **output/time txt file** - text file containing the coordinates of the located bounding boxes in the image

### `parse_boxes`
Uses output of coordinates from `find_boxes` to generate cell parsed cell images.

Set parameters in config.yaml under `Boxes`:

````
folder_path : path to folder containing images
coords_path: path to text file containing coordinates
````

#### Output

1. **cropped images folder** - folder containing the image crops using the input folder and coordinates
