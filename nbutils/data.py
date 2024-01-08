# Markus Enzweiler, markus.enzweiler@hs-esslingen.de

import os

from nbutils import exec as nb_exec


# To get around the problem of "Quota Exceeded" on the "official" CelebA
# download via torchvision (https://github.com/pytorch/vision/issues/1920),
# we use an alternative data source.
def download_celeba(dest_dir, on_colab, verbose):
    # Base URL for data
    data_url = "https://graal.ift.ulaval.ca/public/celeba/"

    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)

    # List of files to download
    celeba_files = [
        "img_align_celeba.zip",
        "list_attr_celeba.txt",
        "list_bbox_celeba.txt",
        "list_eval_partition.txt",
        "list_landmarks_align_celeba.txt",
        "list_landmarks_celeba.txt",
        "identity_CelebA.txt",
    ]

    # Download each file using wget with -nc option
    for file in celeba_files:
        file_url = data_url + file
        print(f"Downloading {file_url} ... ")
        # Run wget command
        if verbose:
            command = ["wget", "-nc", file_url, "-P", dest_dir]
        else:
            command = ["wget", "-nc", "-nv", file_url, "-P", dest_dir]
        nb_exec.executeCommand(command, on_colab)

    # Seems that we need to wait a bit here to make sure
    # that the files actually exist in Colab ... weird :(
    if on_colab:
        import time

        all_files_exist = False
        while not all_files_exist:
            # Assume all files exist until proven otherwise
            all_files_exist = True

            # Check each file
            for file in celeba_files:
                file_path = os.path.join(dest_dir, file)
                if not os.path.exists(file_path):
                    all_files_exist = False
                    break

            # Wait for a bit before checking again if not all files are found
            if not all_files_exist:
                time.sleep(5)  # wait for 5 seconds before checking again

    print("Download complete.")
