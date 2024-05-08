import csv
import os

def get_disk_info():
    disk_info = []

    
    
    # Getting disk partitions information
    partitions = os.popen('df -h').readlines()
    
    for partition in partitions[1:]:
        partition = partition.split()
        partition_info = {}
        partition_info['filesystem'] = partition[0]
        partition_info['total_size'] = partition[1]
        partition_info['used'] = partition[2]
        partition_info['free'] = partition[3]
        partition_info['percentage'] = partition[4]
        partition_info['mountpoint'] = partition[5]
        
        disk_info.append(partition_info)
    
    return disk_info

def generate_disk_info_csv(file_path):
    disk_info = get_disk_info()
    
    # Writing disk information to CSV file
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['filesystem', 'total_size', 'used', 'free', 'percentage', 'mountpoint']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for partition_info in disk_info:
            writer.writerow(partition_info)

# Example usage
generate_disk_info_csv('disk_info.csv')
print("CSV file 'disk_info.csv' generated successfully.")

    