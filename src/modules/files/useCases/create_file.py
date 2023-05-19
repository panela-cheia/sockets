from modules.files.repositories.files_repository import FilesRepository
from modules.files.dtos.create_file_dto import CreateFileDTO

from shared.errors.errors import CustomError

from config.app_url import APP_URL

from providers.hash import hash

class CreateFileUseCase:
    def __init__(self,repository:FilesRepository) -> None:
        self.repository = repository

    async def execute(self,createFileDTO:CreateFileDTO):
        extension = createFileDTO.name[-4:]

        path = APP_URL + "/statics/" + createFileDTO.name

        if extension != ".png" and extension != ".jpg":
            raise CustomError("Extension is not permitted!")
        
        nameHashed = hash(value=createFileDTO.name,gensalt=4)

        finalName = nameHashed +  "-" + createFileDTO.name

        return await self.repository.create(finalName,path)