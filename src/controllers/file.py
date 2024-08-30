from fastapi import APIRouter, Request, UploadFile, status
from fastapi.responses import JSONResponse

from src.services.file import FileService

router = APIRouter(prefix="/files")
file_service = FileService()


@router.post("/upload")
def upload(request: Request, file: UploadFile):
    content = file.file.read()
    file_name_extension = file.filename.split(".")[-1]
    client_checksum_key = request.headers.get("client-checksum-key")
    print(client_checksum_key)

    file_name = file_service.upload(
        content, file_name_extension, client_checksum_key
    )

    return JSONResponse(
        content={"file_name": file_name}, status_code=status.HTTP_200_OK
    )
