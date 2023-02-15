import boto3
from botocore.exceptions import ClientError
from fastapi import UploadFile

from settings import aws

s3 = boto3.client(
    "s3",
    aws_access_key_id=aws.aws_access_key_id,
    aws_secret_access_key=aws.aws_secret_access_key,
)


def save_image_file(file: UploadFile) -> str:
    file_key = f"images/{file.filename}"

    try:
        s3.upload_fileobj(file.file, aws.bucket_name, file_key)

    except ClientError:
        return None
    return f"https://{aws.bucket_name}.s3.amazonaws.com/{file_key}"


def generate_presigned_url(object_key: str) -> str:
    try:
        url = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": aws.bucket_name, "Key": object_key},
            ExpiresIn=600,
            HttpMethod="GET",
        )

    except ClientError:
        return None
    return url
