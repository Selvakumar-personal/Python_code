from googleapiclient.discovery import build

# Inputs
PROJECT_ID = "forward-camera-446712-c7"  # Replace with your GCP project ID
ZONE = "us-central1-a"          # Default zone
DISK_NAME = "selva-test-jan19"     # Name for the new disk
DISK_SIZE_GB = 10               # Size in GB

# Initialize the Compute Engine client
compute = build("compute", "v1")

# Define the disk configuration
disk_body = {
    "name": DISK_NAME,
    "sizeGb": DISK_SIZE_GB,
    "type": f"zones/{ZONE}/diskTypes/pd-standard"  # Standard persistent disk
}

# Create the disk
request = compute.disks().insert(project=PROJECT_ID, zone=ZONE, body=disk_body)
response = request.execute()

print(f"Disk '{DISK_NAME}' created successfully in zone '{ZONE}'.")
