#!/bin/bash

echo "-------------------------- STARTS --------------------------"

# Ensure the user is logged in to Docker Hub
docker login || { echo "Failed to login to Docker Hub."; exit 1; }

# Dockerfile is at the same level as this script
DOCKERFILE_PATH="$(pwd)/src/scrapers/Dockerfile"

# Docker Hub username
# TODO: Change this to your Docker Hub username
DOCKERHUB_USERNAME="graphtylove"

# ------------------------ SCRAPERS IMAGES ------------------------
echo "-------------------------- SCRAPERS IMAGES --------------------------"
# Calculate total number of folders
TOTAL_FOLDERS=$(find ./src/scrapers -maxdepth 1 -type d | wc -l)
TOTAL_FOLDERS=$((TOTAL_FOLDERS-1))  # Subtract 1 to exclude the current directory (.)

# Initialize folder index counter
FOLDER_INDEX=0

# Loop over all directories in the current working directory
for DIR in src/scrapers/*/ ; do
    # Remove trailing slash from the directory name
    DIR_NAME="$(basename ${DIR%/})"
    
    # Increment the folder index counter
    FOLDER_INDEX=$((FOLDER_INDEX+1))

    # Print the current folder index and total number of folders
    echo "----------------------------------------"
    echo "Build and push image ${FOLDER_INDEX}/${TOTAL_FOLDERS} - ${DIR_NAME}"

    # Set image name based on the directory name
    IMAGE_NAME="${DOCKERHUB_USERNAME}/datatank_scraper_${DIR_NAME}"

    # Build the Docker image
    docker build -t "$IMAGE_NAME" -f "$DOCKERFILE_PATH" "$DIR" || { echo "Failed to build Docker image for $DIR_NAME."; exit 1; }

    # Push the Docker image to Docker Hub
    docker push "$IMAGE_NAME" || { echo "Failed to push Docker image for $DIR_NAME."; exit 1; }

    echo "Successfully built and pushed $IMAGE_NAME."
done

# ------------------------ PREPROCESSING IMAGE ------------------------
echo "-------------------------- PREPROCESSING IMAGE --------------------------"
# Set image name based on the directory name
IMAGE_NAME="${DOCKERHUB_USERNAME}/datatank_data_preprocessing"

# Build the Docker image
docker build -t "$IMAGE_NAME" -f "src/preprocessing/Dockerfile" "src/preprocessing" || { echo "Failed to build Docker image for $IMAGE_NAME"; exit 1; }

# Push the Docker image to Docker Hub
docker push "$IMAGE_NAME" || { echo "Failed to push Docker image for $IMAGE_NAME"; exit 1; }

echo "Successfully built and pushed $IMAGE_NAME."
echo "-------------------------- DONE --------------------------"