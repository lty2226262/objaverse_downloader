# Download Objverse Objects

This script allows you to download objects from Objverse by a specific tag. It's designed to be flexible, allowing you to specify the tag and the maximum number of objects to download, as well as the download folder.

## Requirements

- Python 3.x
- `objaverse` package installed by `pip install objaverse`

## Usage

To use the script, navigate to the directory containing `download_objverse_objects.py` and run the following command in your terminal:

```bash
python download_objaverse_objects.py --tag <TAG> --download_folder <DOWNLOAD_FOLDER>
```

For example,
```bash
python download_objaverse_objects.py --tag car --download_folder './downloaded_cars'
