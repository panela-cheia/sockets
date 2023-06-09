from modules.files.repositories.files_repository import FilesRepository
from modules.files.dtos.create_file_dto import CreateFileDTO

from shared.errors.errors import CustomError

from config.app_url import APP_URL

from providers.uuid import generate

class CreateFileUseCase:
    def __init__(self,repository:FilesRepository) -> None:
        self.repository = repository

    async def execute(self,createFileDTO:CreateFileDTO):
        extension = createFileDTO.name[-4:]

        if extension != ".png" and extension != ".jpg":
            raise CustomError("Extension is not permitted!")

        finalName = generate() +  "-" + createFileDTO.name

        path = APP_URL + "/statics/" + finalName

        response = await self.repository.create(name=finalName,path=path)

        return { "id":response["id"],path:response["path"] }