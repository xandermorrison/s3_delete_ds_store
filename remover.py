import boto3
import sys

if len(sys.argv) < 2:
    print("Must give bucket name")
    sys.exit()

bucket_name = sys.argv[1]

client = boto3.client("s3")
paginator = client.get_paginator("list_objects_v2")
result = paginator.paginate(Bucket=bucket_name)

for page in result:
    if "Contents" in page:
        for key in page["Contents"]:
            key_string = key["Key"]
            if ".DS_Store" in key_string:
                print("Deleting: {}".format(key_string))
                client.delete_object(
                        Bucket=bucket_name,
                        Key=key_string)
