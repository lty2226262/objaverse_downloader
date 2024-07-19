import objaverse
import os
import json
import argparse

class ObjverseHelper:
    def __init__(self):
        pass

    def download_objects_by_tag(self, tag, max_objects=10000, download_folder="downloaded_objects"):
        """
        Downloads objects from Objverse by a specific tag.

        Parameters:
        - tag (str): The tag to search for.
        - max_objects (int): Maximum number of objects to download.
        - download_folder (str): Folder to save the downloaded objects.
        """
        uids = objaverse.load_uids()
        annotations = objaverse.load_annotations(uids)
        matched_uids = [uid for uid, content in annotations.items() if any(tag.lower() == t['name'].lower() for t in content["tags"])][:max_objects]

        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        objects = objaverse.load_objects(uids=matched_uids, download_processes=4)  # Adjust the number of processes based on your system

        # Save metadata to JSON
        with open(os.path.join(download_folder, f"{tag}_objects.json"), "w") as f:
            json.dump(objects, f)

        for uid, content in objects.items():
            obj_path = os.path.join(download_folder, f"{uid}.glb")
            os.symlink(os.path.realpath(content), obj_path)
        
        print(f"Downloaded {len(objects)} objects tagged with '{tag}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download objects by tag from Objverse.')
    parser.add_argument('--tag', type=str, default='car', help='Tag to search for.')
    parser.add_argument('--download_folder', type=str, default='downloaded_cars', help='Folder to save the downloaded objects.')

    args = parser.parse_args()
    
    obj_helper = ObjverseHelper() 
    obj_helper.download_objects_by_tag(args.tag, max_objects=10000, download_folder=args.download_folder)

