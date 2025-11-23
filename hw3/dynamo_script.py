import boto3
from botocore.exceptions import ClientError


REGION_NAME = "us-east-1" 
BUCKET_NAME = "anj-cli-bucket-002"  
TABLE_NAME = "TestTable"             

def list_s3_objects(bucket_name: str) -> None:
    """
    List all files in the given S3 bucket.
    """
    s3 = boto3.client("s3")

    print(f"Attempting to list files in bucket: {bucket_name}")

    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
    except ClientError as e:
        print("Error listing S3 objects:", e)
        return

    contents = response.get("Contents")

    if not contents:
        print("Bucket is empty or does not exist.")
        return

    print(f"Found {len(contents)} file(s):")
    for obj in contents:
        key = obj["Key"]
        size = obj["Size"]
        print(f" - {key} (Size: {size} bytes)")


def create_dynamodb_table(table_name: str) -> None:
    """
    Create a DynamoDB table with a simple primary key 'id' (string).
    If the table already exists, skip creation.
    """
    dynamodb = boto3.client("dynamodb", region_name=REGION_NAME)

    #  if table already exists
    existing_tables = dynamodb.list_tables().get("TableNames", [])
    if table_name in existing_tables:
        print(f"Table '{table_name}' already exists. Skipping creation.")
        return

    print(f"Creating DynamoDB table '{table_name}'...")

    try:
        dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    "AttributeName": "id",
                    "KeyType": "HASH",  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    "AttributeName": "id",
                    "AttributeType": "S",  # String
                }
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5,
            },
        )

        # Wait until the table is active
        waiter = dynamodb.get_waiter("table_exists")
        waiter.wait(TableName=table_name)

        print(f"Table '{table_name}' created successfully!")

    except ClientError as e:
        print("Error creating DynamoDB table:", e)


def insert_item_into_table(table_name: str) -> None:
    """
    Insert a single item into the DynamoDB table.
    """
    dynamodb_resource = boto3.resource("dynamodb", region_name=REGION_NAME)
    table = dynamodb_resource.Table(table_name)

    item = {
        "id": "1",
        "Description": "Sample item inserted by Boto3 script",
        "Status": "ACTIVE",
    }

    print(f"Inserting item into table '{table_name}'...")

    try:
        response = table.put_item(
            Item=item,
            ReturnConsumedCapacity="TOTAL",
        )
        print("Item inserted successfully!")

        consumed_capacity = response.get("ConsumedCapacity")
        if consumed_capacity:
            print("Consumed capacity:", consumed_capacity)

    except ClientError as e:
        print("Error inserting item into DynamoDB table:", e)


def main():
    print("AWS clients initialized successfully")

    # 1. List S3 objects
    list_s3_objects(BUCKET_NAME)

    # 2. Create DynamoDB table
    create_dynamodb_table(TABLE_NAME)

    # 3. Insert an item into the table
    insert_item_into_table(TABLE_NAME)


if __name__ == "__main__":
    main()
