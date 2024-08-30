import os
import hashlib
from uuid import uuid4

from fastapi import HTTPException, status


class FileService:
    def __init__(self):
        pass

    def checksum(self, content: bytes, client_checksum_key: str):
        checksum_key = hashlib.md5(content).hexdigest()
        return checksum_key == client_checksum_key

    def upload(
        self,
        content: bytes,
        file_name_extension: str,
        client_checksum_key: str,
    ):
        if self.checksum(content, client_checksum_key) is False:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Checksum failed",
            )

        file_name = str(uuid4())
        file_path = os.path.join(
            "storage", f"{file_name}.{file_name_extension}"
        )

        with open(file_path, "wb") as f:
            f.write(content)

        return file_name
