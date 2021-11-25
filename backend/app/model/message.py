from data_model.aws.s3 import S3
import os


class Message:

    def __init__(self, message_text, bucket=None, message_file_name=None):
        self.bucket = bucket or os.getenv("S3_BUCKET")
        self.message_file_name = message_file_name or os.getenv('MESSAGES FILE')
        self.message = message_text
        self.s3 = S3()

    def save(self):
        if self.s3.file_exists(self.bucket, self.messages_file_name):
            self.s3.download(self.bucket, self.messages_file_name, "messages.txt")
        with open("messages.txt", "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            file_object.write(self.message)
        self.s3.upload("messages.txt", self.bucket, self.messages_file_name)
